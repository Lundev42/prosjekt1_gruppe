class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit



# Ferdig floor class
class Floor:
    """
    This class represents a floor in the house.
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
    This class represents a room in the house.
    """
    def __init__(self, area, name):
        self.area = area
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)




class Device:
    """
    This class represents a smart device in the house.
    """
    def __init__(self, id, supplier, model_name, device_type):
        self.id = id
        self.supplier = supplier
        self.model_name = model_name
        self.device_type = device_type

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
    This class represents a sensor device in the house.
    """
    def __init__(self, id, device_type, supplier, model_name):
        super().__init__(id, supplier, model_name, device_type)
        self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)




class Actuator(Device):
    """
    This class represents an actuator device in the house.
    """
    def __init__(self, id, device_type, supplier, model_name):
        super().__init__(id, supplier, model_name, device_type)

    def set_state(self, state):
        self.state = state
        




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

