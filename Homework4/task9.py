"""
Task 9 — Music Festival Ticket Analyzer (No dicts, No functions) 🎤

Constraints: lists + loops + conditions + strings + numbers only (NO dicts, NO def).

Scenario:
  Entrance logs are noisy strings with three data points:
    - Ticket ID starting with 'T' + digits (e.g., T123)
    - Age (e.g., age=21, AGE:17)
    - Zone name containing 'zone' (zoneA, ZONE_B, ZONE_C)

Example logs:
  logs = [
    "id:T123 age=21 zoneA",
    "noise T045 AGE=17 ZONE_B",
    "ticket T222 age:35 zoneA",
    "id:T045 age=17 zoneB (duplicate)",
    "bad line missing fields",
    "T555 age=12 ZONE_C",
  ]

Requirements:
  1) Extract for each line:
     - ticket id (string starting with 'T' + digits)
     - age (int)
     - zone label ('A', 'B', 'C') derived from zone token (case-insensitive)
     Ignore lines missing any of these three fields.

  2) Compute and print:
     - Valid tickets count
     - Minors (<18) count
     - Average age (1 decimal)
     - Zone counts as: A=?, B=?, C=?
     - Duplicates list (IDs that appear more than once)

Practice: string normalization, token scanning, counters, averages, duplicate detection

OUTPUT EXAMPLE
--------------
Valid tickets: 5
Minors: 2
Average age: 21.2
Zone counts: A=2, B=2, C=1
Duplicates: T045
"""

logs = [
    "id:T123 age=21 zoneA",
    "noise T045 AGE=17 ZONE_B",
    "ticket T222 age:35 zoneA",
    "id:T045 age=17 zoneB (duplicate)",
    "bad line missing fields",
    "T555 age=12 ZONE_C",
]

print("(Starter) Logs loaded:", len(logs))
# TODO: parse each line, extract id/age/zone using loops over tokens
# TODO: compute metrics with lists and counters only (no dicts, no def)
ticket = []
for sq_br in range(len(logs)):
    ticket.append([])
n = 0
for data in logs:
    data = data.split()
    for inf in data:
        if "T" in inf:
            ticket[n].append(inf[-4:])
        if "age" in inf.lower():
            ticket[n].append(inf[-2:])
        if "zone" in inf.lower():
            ticket[n].append(inf[-1])
    n += 1

dub_v = []
for c, data_t in enumerate(ticket):
   for dub, filtr in enumerate(ticket):
       if data_t == filtr and c != dub:
           ticket.pop(dub)
           dub_v.append(filtr[0])
   if len(data_t):
       ticket.pop(c)
v_t = 0
av_age = []
zoneA_count = 0
zoneB_count = 0
zoneC_count = 0
minors = 0
for count in ticket:
   for t_inf in count:
       if "T" in t_inf:
           v_t += 1
       if t_inf.isdigit():
           av_age.append(int(t_inf))
           if int(t_inf) < 18:
               minors += 1
       elif t_inf.isalpha():
           if "A" in t_inf:
               zoneA_count += 1
           elif "B" in t_inf:
               zoneB_count += 1
           elif "C" in t_inf:
               zoneC_count += 1
av_age = sum(av_age) / len(av_age)
print("Tickets:", len(ticket))
print("Minors:", minors)
print(f"Average age: {av_age:.1f}")
print(f"Zone counts: A={zoneA_count} B={zoneB_count} C={zoneC_count}")
print(f"Duplicates: ", end='')
for d in dub_v:
    print(d, end=' ')





