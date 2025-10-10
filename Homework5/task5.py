"""
✈️ TASK 5 — Airport Codes Translator
Topic: dict lookup + iteration

Airports: {"KBP":"Kyiv", "LHR":"London", "JFK":"New York"}
Flights:  ["KBP", "JFK", "LHR", "CDG"]
Print the city for each flight code; if code not in dict — print "Unknown".

"""
# Starter:
airports = {"KBP":"Kyiv", "LHR":"London", "JFK":"New York"}
flights = ["KBP", "JFK", "LHR", "CDG"]
# TODO: print city for each code using .get
for item in flights:
    print(item, airports.get(item, "Unknown"))