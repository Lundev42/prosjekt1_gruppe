class Measurement:
    """
    Denne klassen representerer en måling tatt av en sensor (inneholder når målingen ble tatt, verdien og enheten). 
    En måling kan for eksempel være en temperaturmåling som ble tatt 2024-06-01 kl. 12:00, med verdien 21.5 og enheten "°C".
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit




class Floor:
    """
    Denne klassen representerer et gulv i huset (inneholder gulvets nivå og hvilke rom som er registrert på det).
    """
    def __init__(self, level):
        self.level = level
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_area(self):
        return sum(room.area for room in self.rooms)




class Room:
    """
    Denne klassen representerer et rom i huset (inneholder rommets areal, navn og hvilke enheter som er registrert i det).
    """
    def __init__(self, area, room_name):
        self.area = area
        self.room_name = room_name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)




class Device:
    """
    Denne klassen representerer en smart enhet i huset, og fungerer som en superklasse for både sensorer og aktuatorer.
    """
    def __init__(self, id, supplier, model_name, device_type):
        self.id = id
        self.supplier = supplier
        self.model_name = model_name
        self.device_type = device_type
        self.room = None

    def is_sensor(self):
        return False

    def is_actuator(self):
        return False

    def get_info(self):
        return {
            "id": self.id,
            "device_type": self.device_type,
            "supplier": self.supplier,
            "model_name": self.model_name,
        }




class Sensor(Device):                                           
    """
    Denne klassen representerer en sensor-enhet i huset, arver fra Device-klassen
    """
    def __init__(self, id, device_type, supplier, model_name):  # Konstruktøren
        super().__init__(id, supplier, model_name, device_type) # Kaller konstruktøren til Device-klassen for å initialisere felles attributter
        self.measurements = []                                  # Tom liste for å lagre målinger som er tatt av sensoren

    def add_measurement(self, measurement):                     # Metode for å legge til en måling i sensoren
        self.measurements.append(measurement)                   # Legger til målingen i listen

    def is_sensor(self):                                        # Metode for å sjekke om enheten er en sensor
        return True

    def last_measurement(self):                         # Metode for å hente siste måling fra sensoren
        if self.measurements:                           # Sjekker om det finnes noen målinger i listen
            return self.measurements[-1]                # Returnerer siste måling fra listen
        return None                                     # Returnerer None hvis det ikke finnes noen målinger




class Actuator(Device):
    """
    Denne klassen representerer en aktuator-enhet i huset, arver fra Device-klassen
    """
    def __init__(self, id, device_type, supplier, model_name):  # Konstruktøren
        super().__init__(id, supplier, model_name, device_type) # Kaller konstruktøren til Device-klassen for å initialisere felles attributter
        self.state = False                  # Aktuatoren starter i av-tilstand (False)
        self.target_value = None            # Aktuatoren har ingen målverdi ved oppstart

    def is_actuator(self):                  # Metode for å sjekke om enheten er en aktuator
        return True                         

    def turn_on(self, value=None):          # Metode for å slå på aktuatoren, med mulighet for å spesifisere en målverdi
        self.state = True                   # Skrur på aktuatoren
        if value is not None:               # Hvis en målverdi er spesifisert,
            self.target_value = value       # Lagre målverdien i target_value-attributtet

    def turn_off(self):                     # Metode for å slå av aktuatoren
        self.state = False                  # Skrur av aktuatoren

    def is_active(self):                    # Metode for å sjekke om aktuatoren er aktiv (på)
        return self.state                   # Returnerer True hvis aktuatoren er på, ellers False
        




class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        pass


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        pass


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        pass


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        pass

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        pass

