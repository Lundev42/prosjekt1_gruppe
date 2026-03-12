from datetime import date

from smarthouse.domain import Actuator, Device, Sensor, SmartHouse, Measurement

DEMO_HOUSE = SmartHouse()

# Building house structure
#ground_floor = DEMO_HOUSE.register_floor(1)
#entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices

# Floors
ground_floor = DEMO_HOUSE.register_floor(1)
second_floor = DEMO_HOUSE.register_floor(2)

# Ground floor rooms
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
bathroom = DEMO_HOUSE.register_room(ground_floor, 15.0, "Bathroom")
storage = DEMO_HOUSE.register_room(ground_floor, 8.0, "Storage")
laundry = DEMO_HOUSE.register_room(ground_floor, 9.0, "Laundry")
office = DEMO_HOUSE.register_room(ground_floor, 10.0, "Office")
guest_room = DEMO_HOUSE.register_room(ground_floor, 12.0, "Guest Room")

#second floor rooms
living_room = DEMO_HOUSE.register_room(second_floor, 35.0, "Living Room")
kitchen = DEMO_HOUSE.register_room(second_floor, 25.0, "Kitchen")
bedroom1 = DEMO_HOUSE.register_room(second_floor, 10.0, "Bedroom 1")
bedroom2 = DEMO_HOUSE.register_room(second_floor, 7.0, "Bedroom 2")
dresser = DEMO_HOUSE.register_room(second_floor, 6.0, "Dressing Room") 
hallway = DEMO_HOUSE.register_room(second_floor, 6.05, "Hallway")

# Devices
lightbulb = Actuator("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Light Bulp", "Elysian Tech", "Lumina Glow 4000")
heatpump= Actuator("5e13cabc-5c58-4bb3-82a2-3039e4480a6d","Heat Pump","Nordic Climate Systems","FrostFlow X")
motion_sesnsor = Sensor("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5","Motion Sensor","NebulaGuard Innovations","MoveZ Detect 69")
temperature_sensor = Sensor("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e","Temperature Sensor","ArcticSense","ThermoTrack Mini")

lightbulb1 = Actuator("66d2656c-9cf3-4180-9037-5da68d98fbfb", "Light Bulp1", "Elysian Tech", "Lumina Glow 4000")
lightbulb2 = Actuator("fe49598c-83b9-4460-9961-890acae53113", "Light Bulp2", "Elysian Tech", "Lumina Glow 4000")
heatpump1= Actuator("9eb2e230-2c41-4954-8ea5-661b73ae7082","Heat Pump1","Nordic Climate Systems","FrostFlow X")
heatpump2= Actuator("6d1bfcda-ea92-405a-b376-a53c984b357f","Heat Pump2","Nordic Climate Systems","FrostFlow X")
motion_sesnsor1 = Sensor("587462a3-91bf-44bf-b69e-89366308feea","Motion Sensor1","NebulaGuard Innovations","MoveZ Detect 69")
temperature_sensor1 = Sensor("f175d858-b6f1-4079-a810-1387473206f2","Temperature Sensor1","ArcticSense","ThermoTrack Mini")
heatpump3= Actuator("acc01b98-2c1d-48a4-89f2-107c102221df","Heat Pump3","Nordic Climate Systems","FrostFlow X")
lightbulb3= Actuator("6af8343d-bb6b-471f-be5a-659fc781ce4c","Light Bulp3","Elysian Tech","Lumina Glow 4000")
motion_sesnsor3 = Sensor("cfd3f745-0ad3-4177-b359-3bdbefc56fd5","Motion Sensor3","NebulaGuard Innovations","MoveZ Detect 69")
temperature_sensor3 = Sensor("b3eaa51f-0542-489a-b0eb-5364ff6ed91e","Temperature Sensor3","ArcticSense","ThermoTrack Mini")

measurement = Measurement(date.today(), value=22.5, unit="°C")
temperature_sensor.add_measurement(measurement)

DEMO_HOUSE.register_device(living_room, temperature_sensor)  
DEMO_HOUSE.register_device(living_room, motion_sesnsor) 
DEMO_HOUSE.register_device(hallway,lightbulb) 
DEMO_HOUSE.register_device(bedroom1, heatpump1)
DEMO_HOUSE.register_device(bedroom2, lightbulb1)
DEMO_HOUSE.register_device(bedroom2, heatpump2)
DEMO_HOUSE.register_device(office, motion_sesnsor1)
DEMO_HOUSE.register_device(office, temperature_sensor1)
DEMO_HOUSE.register_device(living_room, lightbulb2)
DEMO_HOUSE.register_device(kitchen, heatpump3)
DEMO_HOUSE.register_device(guest_room, motion_sesnsor3)
DEMO_HOUSE.register_device(guest_room, temperature_sensor3)
DEMO_HOUSE.register_device(kitchen, lightbulb3)

DEMO_HOUSE.register_device(kitchen, heatpump)  