"""
Homework 1:
✈️ Synchronized Arrival: F-16 and Eurofighter Typhoon

📘 Scenario:
Two fighter jets — the F-16 Fighting Falcon and the Eurofighter Typhoon — are flying to the same
destination and must arrive at the exact same time. The F-16 is slower, so it takes off first at 10:00.
Both aircraft fly the same distance, but at different speeds and fuel consumption rates.

All input data in an `INIT DATA` section below is given in imperial units:
Distance: miles
Speed: mph
Fuel consumption: gallons per hour

Your tasks:
0. Read about Python's triple quotes, used for the text - https://realpython.com/ref/glossary/triple-quoted-string/
1. Convert all values from an `INIT DATA` section below into metric units (kilometers, km/h, liters/hour).
2. Calculate the flight time for each aircraft, expressed in full hours and minutes.
   Read about convertion to integer - https://www.w3schools.com/python/ref_func_int.asp
3. Determine the departure time of the Typhoon so it arrives at the same time as the F-16.
4. Calculate how much fuel was used by each aircraft.
5. Print all results in a formatted table.
6. Use input() to enter the distance value from a keyboard - https://www.w3schools.com/python/python_user_input.asp

Formatted table example

----------------------------------------------------------------------------------------------------------
| Aircraft               | Distance (km)  | Speed (km/h)   |  Flight Time  | Departure   | Fuel Used (L) |
----------------------------------------------------------------------------------------------------------
| F-16 Fighting Falcon   |         1932.0 |          929.0 |  2 h  4 min   | 10:00       |       23646.4 |
| Eurofighter Typhoon    |         1932.0 |         1853.1 |  1 h  2 min   | 10:00       |        9088.1 |
----------------------------------------------------------------------------------------------------------


"""

# Conversion constants
MILE_TO_KM = 1.61
GALLON_TO_LITER = 3.79

# INIT DATA
#task6
# Distance in miles
distance_miles = input("Type the distance in miles: ")
if not distance_miles :
    distance_miles = 1200
    print(f"Distance in miles = {distance_miles}(default)")
else:
    distance_miles = int(distance_miles)
    print(f"Distance in miles = {distance_miles}")

# F-16 data
speed_mph_f16 = 577
fuel_gph_f16 = 3000

# Typhoon data
speed_mph_typhoon = 1151
fuel_gph_typhoon = 2300

# YOUR CODE
# task 1
distance_kilometers = distance_miles * MILE_TO_KM
# f-16 into km/h and liters/h
speed_kmph_f16 = speed_mph_f16 * MILE_TO_KM
fuel_lph_f16 = fuel_gph_f16 * GALLON_TO_LITER
# typhoon into km/h and liters/h
speed_kmph_typhoon = speed_mph_typhoon * MILE_TO_KM
fuel_lph_typhoon = fuel_gph_typhoon * GALLON_TO_LITER

# task 2

# f-16
time_f16_hour = int(distance_kilometers / speed_kmph_f16)
time_f16_minute = int((distance_kilometers / speed_kmph_f16)*60)

# typhoon
time_typhoon_hour = int(distance_kilometers / speed_kmph_typhoon)
time_typhoon_minute = int((distance_kilometers / speed_kmph_typhoon)*60)

# task 3
f16_departure_time_hour = 10
f16_departure_time_minute = 0
typhoon_departure_time_hour = f16_departure_time_hour + (time_f16_minute - time_typhoon_minute)//60
typhoon_departure_time_minute = f16_departure_time_minute + (time_f16_minute - time_typhoon_minute)%60


# task 4
# f-16
f16_used_fuel = (distance_kilometers / speed_kmph_f16) * fuel_lph_f16
# typhoon
typhoon_used_fuel = (distance_kilometers / speed_kmph_typhoon) * fuel_lph_typhoon
# task 5
a = "-"
x = a * 106
print(x)
print("| Aircraft               | Distance (km)  |  Speed (km/h)  |  Flight Time  |  Departure  | Fuel Used (L) |")
print(x)
print(f"| F-16 Fighting Falcon   |{distance_kilometers:>16.1f}|{speed_kmph_f16:>16.1f}|{time_f16_hour:>5} h{time_f16_minute%60:>3} min |       {f16_departure_time_hour%24:02d}:{f16_departure_time_minute%60:02d} |{f16_used_fuel:>15.1f}|")
print(f"| Eurofighter Typhoon    |{distance_kilometers:>16.1f}|{speed_kmph_typhoon:>16.1f}|{time_typhoon_hour:>5} h{time_typhoon_minute%60:>3} min |       {typhoon_departure_time_hour%24:02d}:{typhoon_departure_time_minute%60:02d} |{typhoon_used_fuel:>15.1f}|")
print(x)