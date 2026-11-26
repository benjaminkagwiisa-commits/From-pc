# Benjamin Kagwiisa

import random
import math

# collect user input
callsign = input("Enter spacecraft callsign: ")

# seed random number generator
random.seed(callsign)

# generate mission parameters
fuel = random.randrange(1, 101)
crew = random.randrange(2, 9)
signal = random.randrange(1, 21)

# calculate mission statistics
range_km = math.pow(fuel, 2)
oxygen_days = math.floor(fuel / crew)
boost = math.ceil(signal * 1.5)

# calculate mission ID
mission_id = fuel + crew + signal

# display mission profile
print(f"=== Mission Profile: {callsign} ===")
print(f"Fuel Level:       {fuel}%")
print(f"Crew Size:        {crew}")
print(f"Signal Strength:  {signal}")
print(f"Mission Range:    {range_km} km")
print(f"Oxygen Supply:    {oxygen_days} days")
print(f"Transmission Boost: {boost}")
print(f"Mission ID (decimal): {mission_id}")
