from smarthouse.domain import SmartHouse, Device, Actuator, Sensor, Measurement 
from datetime import date


DEMO_HOUSE = SmartHouse()

# Building house structure

# FLOORS
ground_floor = DEMO_HOUSE.register_floor(1)
second_floor = DEMO_HOUSE.register_floor(2)

# ROOMS ON GROUND FLOOR
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
livingRoom_kitchen = DEMO_HOUSE.register_room(ground_floor, 39.75, "Living Room/Kitchen")
bathroom1 = DEMO_HOUSE.register_room(ground_floor, 6.3, "Bathroom 1")
guestRoom1 = DEMO_HOUSE.register_room(ground_floor, 8, "Guest Room 1")
garage = DEMO_HOUSE.register_room(ground_floor, 19, "Garage")

# DEVICES ON GROUND FLOOR
smart_lock = Actuator("4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "Smart Lock", "MythicalTech", "Guardian Lock 7000")
electricity_meter = Sensor("a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "Electricity Meter", "MysticEnergy Innovations", "Volt Watch Elite") 
motion_sensor = Sensor("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5","Motion Sensor","NebulaGuard Innovations","MoveZ Detect 69")
heat_pump = Actuator("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "Heat Pump", "ElysianTech", "Thermo Smart 6000")
co2_sensor = Sensor("8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "CO2 sensor", "ElysianTech", "Smoke Warden 1000")
humidity_sensor = Sensor("3d87e5c0-8716-4b0b-9c67-087eaaed7b45", "Humidity Sensor", "AetherCorp", "Aqua Alert 800")
smart_oven1 = Actuator("8d4e4c98-21a9-4d1e-bf18-523285ad90f6", "Smart Oven", "AetherCorp", "Pheonix HEAT 333")
automatic_garage_door = Actuator("9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "Automatic Garage Door", "MythicalTech", "Guardian Lock 9000")

# REGISTERING DEVICES GROUND FLOOR
DEMO_HOUSE.register_device(entrance, smart_lock)
DEMO_HOUSE.register_device(entrance, electricity_meter)
DEMO_HOUSE.register_device(livingRoom_kitchen, motion_sensor)
DEMO_HOUSE.register_device(livingRoom_kitchen, heat_pump)
DEMO_HOUSE.register_device(livingRoom_kitchen, co2_sensor)
DEMO_HOUSE.register_device(bathroom1, humidity_sensor)
DEMO_HOUSE.register_device(guestRoom1, smart_oven1)
DEMO_HOUSE.register_device(garage, automatic_garage_door)


# ROOMS ON SECOND FLOOR
office = DEMO_HOUSE.register_room(second_floor, 11.75, "Office")
bathroom2 = DEMO_HOUSE.register_room(second_floor, 9.25, "Bathroom 2")
guestRoom2 = DEMO_HOUSE.register_room(second_floor, 8, "Guest Room 2")
hallway = DEMO_HOUSE.register_room(second_floor, 10, "Hallway")
guestRoom3 = DEMO_HOUSE.register_room(second_floor, 10, "Guest Room 3")
dressingRoom = DEMO_HOUSE.register_room(second_floor, 4, "Dressing Room")
masterBedroom = DEMO_HOUSE.register_room(second_floor, 17, "Master Bedroom")

# DEVICES ON SECOND FLOOR
smart_plug = Actuator("1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79", "Smart Plug", "MysticEnergy Innovations", "FlowState X")
dehumidifier = Actuator("9e5b8274-4e77-4e4e-80d2-b40d648ea02a", "Dehumidifier", "ArcaneTech Solutions", "Hydra Dry 8000")
lightbulp = Actuator("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Light Bulp", "Elysian Tech", "Lumina Glow 4000")
air_quality_sensor = Sensor("7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "Air Quality Sensor", "CelestialSense Technologies", "AeroGuard Pro")
temperature_sensor = Sensor("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "Temperature Sensor", "AetherCorp", "SmartTemp 42")
smart_oven2 = Actuator("c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1", "Smart Oven", "IgnisTech Solutions", "Ember Heat 3000")

# REGISTERING DEVICES SECOND FLOOR
DEMO_HOUSE.register_device(office, smart_plug)
DEMO_HOUSE.register_device(bathroom2, dehumidifier)
DEMO_HOUSE.register_device(guestRoom2, lightbulp)
DEMO_HOUSE.register_device(guestRoom3, air_quality_sensor)
DEMO_HOUSE.register_device(masterBedroom, temperature_sensor)
DEMO_HOUSE.register_device(masterBedroom, smart_oven2)
