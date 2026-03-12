

class Measurement:
    """
    Denne klassen representerer en måling tatt av en sensor (inneholder når målingen ble tatt, verdien og enheten). 
    En måling kan for eksempel være en temperaturmåling som ble tatt 2024-06-01 kl. 12:00, med verdien 21.5 og enheten "°C".
    """

    def __init__(self, timestamp, value, unit):                 # Konstruktøren (tar inn tidspunkt og dato for målingen, verdien og enheten)
        self.timestamp = timestamp                              # Tidspunkt og dato (f.eks. "2024-06-01 12:00")
        self.value = value                                      # Måleverdien (f.eks. 21.5)
        self.unit = unit                                        # Enheten for måleverdien (f.eks. "°C")




class Floor:
    """
    Denne klassen representerer et gulv i huset (inneholder gulvets nivå og hvilke rom som er registrert på det).
    """
    def __init__(self, level):                                  # Konstruktøren (tar inn etasje, f.eks. 0 for kjeller, 1 for første etasje)
        self.level = level                                      # Etasjenivå 
        self.rooms = []                                         # Liste over rom som er registrert på denne etasjen

    def add_room(self, room):                                   # Metode for å legge til et rom på etasjen
        self.rooms.append(room)                                 # Legger til rommet i listen i konstruktøren

    def get_area(self):                                         # Metoden beregner total areal for etasjen ved å summere arealet til hvert rom på etasjen   
        return sum(room.area for room in self.rooms)            # Returnerer total areal for etasjen, som er summen av arealet til hvert rom i listen self.rooms




class Room:
    """
    Denne klassen representerer et rom i huset (inneholder rommets areal, navn og hvilke enheter som er registrert i det).
    """
    def __init__(self, area, room_name):                        # Konstruktøren (tar inn areal og romnavn)
        self.area = area                                        # Areal i kvadratmeter  
        self.room_name = room_name                              # Navn på rommet ("Stue", "Kjøkken", etc.)
        self.devices = []                                       # Liste over enheter (devices) som er i rommet

    def add_device(self, device):                               # Metode for å legge til en enhet i rommet
        self.devices.append(device)                             # Legger til enheten i listen i konstruktøren




class Device:
    """
    Denne klassen representerer en smart enhet i huset, og fungerer som en superklasse for både sensorer og aktuatorer.
    """
    def __init__(self, id, supplier, model_name, device_type):  # Konstruktøren (tar inn id, leverandør, modellnavn og type enhet)
        self.id = id                                            # Unik identifikator for enheten
        self.supplier = supplier                                # Leverandør av enheten
        self.model_name = model_name                            # Modellnavn for enheten    
        self.device_type = device_type                          # Type enhet ("temperatursensor", "lysbryter", etc.)
        self.room = None                                        # Rommet enheten er registrert i (utgangspunkt: None)

    def is_sensor(self):                                        # Enheten er ikke en sensor
        return False

    def is_actuator(self):                                      # Enheten er ikke en aktuator     
        return False




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

    def last_measurement(self):                                 # Metode for å hente siste måling fra sensoren
        if self.measurements:                                   # Sjekker om det finnes noen målinger i listen
            return self.measurements[-1]                        # Returnerer siste måling fra listen
        return None                                             # Returnerer None hvis det ikke finnes noen målinger




class Actuator(Device):
    """
    Denne klassen representerer en aktuator-enhet i huset, arver fra Device-klassen
    """
    def __init__(self, id, device_type, supplier, model_name):  # Konstruktøren
        super().__init__(id, supplier, model_name, device_type) # Kaller konstruktøren til Device-klassen for å initialisere felles attributter
        self.state = False                                      # Aktuatoren starter i av-tilstand (False)
        self.target_value = None                                # Aktuatoren har ingen målverdi ved oppstart

    def is_actuator(self):                                      # Metode for å sjekke om enheten er en aktuator
        return True                         

    def turn_on(self, value=None):                              # Metode for å slå på aktuatoren, med mulighet for å spesifisere en målverdi
        self.state = True                                       # Skrur på aktuatoren
        if value is not None:                                   # Hvis en målverdi er spesifisert,
            self.target_value = value                           # Lagre målverdien i target_value-attributtet

    def turn_off(self):                                         # Metode for å slå av aktuatoren
        self.state = False                                      # Skrur av aktuatoren

    def is_active(self):                                        # Metode for å sjekke om aktuatoren er aktiv (på)
        return self.state                                       # Returnerer True hvis aktuatoren er på, ellers False

    def change_target_value(self, new_value):                   # Metode for å endre verdi til en påskrudd actuator
        if self.state:
            self.target_value = new_value






class SmartHouse:
    def __init__ (self):
        self.floors = []                                     # Liste med etasjer
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):
        for floor in self.floors:                           #Sjekker om etasjen allerede eksisterer i huset
            if floor.level == level:
                return floor

        new_floor = Floor(level)                            #Hvis etasjen ikke eksisterer, opprettes en ny etasje
        self.floors.append(new_floor)

        return new_floor                                    #Returnerer den nye etasjen som beskrevet i oppgaven

        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """

    def register_room(self, floor, room_size, room_name = None):
        new_room = Room(room_size, room_name)               #Lager et nytt rom med gitte navn og areal

        if floor in self.floors:                            #Sjekker om etasjen til rommet eksisterer og legger det til
            floor.add_room(new_room)
        else:
            self.register_floor(floor).add_room(new_room)   #Hvis etasjen ikke eksisterer, opprettes den og rommet legges til

        return new_room
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """


    def get_floors(self):
        return sorted(self.floors, key=lambda f: f.level)   #Returnerer alle rom sortert i stigende rekkefølge
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """


    def get_rooms(self):
        rooms = []                                          #Lager en liste for å putte alle rom i huset i
        for floor in self.floors:                           #Itererer over alle etasjer 
            rooms.extend(floor.rooms)                       #Legger rommene til i listen
        return rooms                                        #Returnerer listen med rom
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """


    def get_area(self):
        return sum(floor.get_area() for floor in self.floors) #Summerer arealet til alle etasjer
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        for floor in self.floors:                           #Itererer over alle etasjer
            if room in floor.rooms:                         #Sjekker om rommet eksisterer i huset
                room.add_device(device)                      #Legger til enheten i rommet
                device.room = room                           #Registrerer rommet i enhetens attributt
                return device
        """
        This methods registers a given device in a given room.
        """

    
    def get_device_by_id(self, device_id):
        for floor in self.floors:                           #Itererer over alle etasjer
            for room in floor.rooms:                        #Itererer over alle rom i etasjen
                for device in room.devices:                 #Itererer over alle enheter i rommet
                    if device.id == device_id:              #Sjekker om enhetens id matcher den gitte id-en
                        return device                       #Returnerer enheten hvis den finnes
        return None                                        #Returnerer None hvis enheten ikke finnes i huset
        """
        This method retrieves a device object via its id.
        """
    
    def get_devices(self):
        devices = []                                      #Lager en liste for å putte alle enheter i huset i
        for floor in self.floors:                           #Itererer over alle etasjer
            for room in floor.rooms:                        #Itererer over alle rom i etasjen
                devices.extend(room.devices)               #Legger enhetene til i listen
        return devices                                     #Returnerer listen med enheter
        """
        This method returns a list of all registered devices in the house.
        The resulting list has no particular order.
        """