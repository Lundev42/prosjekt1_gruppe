import sqlite3

from typing import Optional
from smarthouse.domain import Measurement, Room, Sensor, Actuator, SmartHouse, Floor


class SmartHouseRepository:
    """
    Provides the functionality to persist and load a _SmartHouse_ object 
    in a SQLite database.
    """

    def __init__(self, file: str) -> None:
        self.file = file
        self.conn = sqlite3.connect(file, check_same_thread=False)

    def __del__(self):
        self.conn.close()

    def cursor(self) -> sqlite3.Cursor:
        """
        Provides a _raw_ SQLite cursor to interact with the database.
        When calling this method to obtain a cursors, you have to 
        rememeber calling `commit/rollback` and `close` yourself when
        you are done with issuing SQL commands.
        """
        return self.conn.cursor()

    def reconnect(self):
        self.conn.close()
        self.conn = sqlite3.connect(self.file)

    def load_smarthouse_deep(self):
        """
        This method retrives the complete single instance of the _SmartHouse_ 
        object stored in this database. The retrieval yields a _deep_ copy, i.e.
        all referenced objects within the object structure (e.g. floors, rooms, devices) 
        are retrieved as well. 
        """

        cur = self.cursor()
        cur.execute("""                     
            SELECT *
            FROM rooms;
        """)
        rooms_data = cur.fetchall()

        h = SmartHouse()
        room_cache = {}

        for row in rooms_data:
            room_id, floor, area, name = row[0], row[1], row[2], row[3]
            new_room = h.register_room(floor, area, name)
            new_room.id = room_id
            room_cache[room_id] = new_room

        cur.execute("""SELECT * FROM devices;""")
        devices_data = cur.fetchall()

        for row in devices_data:
            room_db_id = row[1]
            new_room = room_cache.get(room_db_id)

            if row[3] == 'actuator':
                new_device = Actuator(row[0], row[2], row[4], row[5])
                cur2 = self.cursor()
                cur2.execute(""" 
                    SELECT state FROM actuators WHERE id = ?
                """, (row[0],))
                state_row = cur2.fetchone()
                if state_row and state_row[0] == 1:
                    new_device.turn_on()
            else:
                new_device = Sensor(row[0], row[2], row[4], row[5])

            if new_room:
                h.register_device(new_room, new_device)

        cur.close()

        return h

    def get_latest_reading(self, sensor) -> Optional[Measurement]:

        cur = self.cursor()  # Henter connection til databasen
        cur.execute(""" SELECT * FROM Measurements WHERE device = ? ORDER BY ts DESC LIMIT 1; """,
                    (sensor.id,))  # SQL-spørring for å hente siste måling for en sensor
        row = cur.fetchone()  # Henter data fra connection
        cur.close()  # Lukker connection til databasen
        if row is None:
            return None
        """
        Retrieves the most recent sensor reading for the given sensor if available.
        Returns None if the given object has no sensor readings.
        """

        return Measurement(row[1], row[0], row[2], row[3])

    def update_actuator_state(self, actuator):
        """
        Saves the state of the given actuator in the database. 
        """
        cur = self.cursor()                 # Oppretter en connection med databasen
        cur.execute("""
            CREATE TABLE IF NOT EXISTS actuators (
            id TEXT PRIMARY KEY,
            kind TEXT NOT NULL,
            supplier TEXT,
            product TEXT,
            state INTEGER NOT NULL DEFAULT 0
        );
        """)                                # Oppretter en ny tabell som heter actuators med kolonnene: id,
        # kind, supplier, product og state.
        # "IF NOT EXISTS" gjør at den opprettes kun èn gang

        cur.execute("""
            INSERT OR IGNORE INTO actuators (id, kind, supplier, product)
            SELECT id, kind, supplier, product
            FROM devices
            WHERE category = 'actuator';
        """)                                # Markerer alle aktuatorer i device-tabellen og legger til informasjonen
        # i den nye tabellen "actuators".

        # "OR IGNORE" håndterer tilfeller hvor aktuatoren allerede eksisterer i
        # tabellen, slik at man unngår duplikasjoner

        if actuator.is_active():            # Dersom aktuatoren man jobber med/kaller på er aktiv, endres state til 1
            cur.execute("""
                UPDATE actuators
                SET state = 1
                WHERE id = ?;
        """, (actuator.id,))
        else:                               # Dersom aktuatoren man jobber med/kaller på ikke er aktiv, endres state til 0
            cur.execute("""
                UPDATE actuators
                SET state = 0
                WHERE id = ?;
        """, (actuator.id,))

        self.conn.commit()
        cur.close()

       

    # statistics

    def calc_avg_temperatures_in_room(self, room, from_date: Optional[str] = None, until_date: Optional[str] = None) -> dict:
        """Calculates the average temperatures in the given room for the given time range by
        fetching all available temperature sensor data (either from a dedicated temperature sensor 
        or from an actuator, which includes a temperature sensor like a heat pump) from the devices 
        located in that room, filtering the measurement by given time range.
        The latter is provided by two strings, each containing a date in the ISO 8601 format.
        If one argument is empty, it means that the upper and/or lower bound of the time range are unbounded.
        The result should be a dictionary where the keys are strings representing dates (iso format) and 
        the values are floating point numbers containing the average temperature that day.
        """
        
        cur = self.cursor()
        conditions = ["d.room = ?", "m.unit = '°C'"]
        parametres = [room.id]

        if from_date:
            conditions.append("DATE(m.ts) >= ?")
            parametres.append(from_date)
        if until_date:
            conditions.append("DATE(m.ts) <= ?")
            parametres.append(until_date)
        where = " AND ".join(conditions)

                      
        cur.execute(f"""
                    SELECT DATE(m.ts), AVG(m.value)
                    FROM measurements m
                    JOIN devices d ON m.device = d.id
                    WHERE {where}
                    GROUP BY DATE(m.ts)
                    ORDER BY DATE(m.ts);
        """, parametres)

        rows = cur.fetchall()
        cur.close()

        
        

        return {day: avg for day, avg in rows}
       

    def calc_hours_with_humidity_above(self, room, date: str) -> list:
        """
        This function determines during which hours of the given day
        there were more than three measurements in that hour having a humidity measurement that is above
        the average recorded humidity in that room at that particular time.
        The result is a (possibly empty) list of number representing hours [0-23].
        """

        cur = self.cursor()
        cur.execute("""
                    SELECT AVG(m.value)
                    FROM measurements m
                    JOIN devices d ON m.device = d.id
                    WHERE room = ? AND DATE(m.ts) = ? and m.unit = '%' 

        """, (room.id, date))

        average_hum = cur.fetchone()[0]
        if average_hum is None:
            return []

        cur.execute("""
                    SELECT strftime('%H', m.ts) as hour
                    FROM measurements m
                    JOIN devices d ON m.device = d.id
                    WHERE d.room = ? AND DATE(m.ts) = ? and m.unit = '%' AND m.value > ?
                    GROUP BY hour
                    HAVING COUNT(*) > 3
                    ORDER BY hour 

        """, (room.id, date, average_hum))

        row = cur.fetchall()
        cur.close()
        hours = [int(row[0]) for row in row]


        return hours
                     
       
