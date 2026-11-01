#import 
import random

battery_level = 100.0
for step in range(1, 11):


    #step 3: 
    reduce_battery= random.uniform(1.5, 3.5)
    battery_level -= reduce_battery

    #step 4:
    print(f"Waypoint {step}: Battery = {battery_level:.2f}%")
    if battery_level < 80:
        print(f"[CAUTION] Battery level is low:{battery_level:.2f}%")

    if battery_level < 75:
        print(f"[WARNING] Battery level is critical: {battery_level:.2f}%")
        break