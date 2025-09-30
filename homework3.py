r"""
Advanced Password Quality Meter — Strings Only

GOAL
----
Read a username and a password and classify the password.

INPUT with input() function
-----
Line 1: username
Line 2: password

MANDATORY RULES (all must pass or print EXACTLY "REJECT"):
  R1) length: 10..64 characters inclusive
  R2) contains at least one digit
  R3) contains at least one lowercase letter
  R4) contains at least one uppercase letter
  R5) contains at least one special from: ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \ |
  R6) no spaces or tabs
  R7) must start with a LETTER (A–Z or a–z)
  R8) must NOT contain the username (case-insensitive)
  R9) must NOT contain the reversed username (case-insensitive)
  R10) must NOT contain these weak substrings (case-insensitive):
       "password", "qwerty", "12345", "admin", "god"

CLASSIFICATION (only if all R1..R10 pass):
  Score the following extras (each +1):
    E1) ends with a digit OR a special
    E2) contains BOTH '-' and '_' somewhere
    E3) contains at least one of '@' or '#'
    E4) contains at least two categories among {digit, upper, lower, special} at
        the BEGINNING 4 chars (first four chars contain at least two categories)
  Total extras: 0..4
  LABEL:
    0-1 -> OK
    2-3 -> STRONG
    4   -> ELITE

OUTPUT
------
If any mandatory rule fails: print
  REJECT

Else print
  RESULT: <OK|STRONG|ELITE> (len=<n>, d=<0/1>, lo=<0/1>, up=<0/1>, sp=<0/1>)

NOTES / HINTS
-------------
- You may use: len, in, not in, strip, lower, upper, replace, startswith/endswith,
  slicing (e.g., s[:4], s[::-1]), comparisons, boolean ops, f-strings.
"""

usr_log = input("login: ")
password = input("password: ")
if not 10 <= len(password) <= 64:
  print("REJECT")
  print("Your password must contain from 10 to 64 characters inclusive")
  exit()
i = 0
while i < len(password):
    if password[i].isdigit():
      i = 0
      break
    elif i == (len(password) - 1):
        print("REJECT")
        print("Your password must contain at least one digit")
        exit()
    else:
        i+=1

while i < len(password):
    if password[i].islower():
        i = 0
        break
    elif i == (len(password) - 1):
        print("REJECT")
        print("Your password must contain at least one lowercase letter")
        exit()
    else:
        i+=1

while i < len(password):
    if password[i].isupper():
        i = 0
        break
    elif i == (len(password) - 1):
        print("REJECT")
        print("Your password must contain at least one uppercase letter")
        exit()
    else:
        i+=1

special_s = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '?', '/', '\\', '|' ]

while i < len(password):
    if password[i] in special_s:
        i = 0
        break
    elif i == (len(password) - 1):
        print("REJECT")
        print(r"Your password must contain at least one special from: ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . ? / \ |")
        exit()
    else:
        i+=1

while i < len(password):
    if password[i] == " " or password[i] == "\t":
        print("REJECT")
        print("Your password must not contain spaces or tabs")
        exit()
    elif i == (len(password) - 1):
        i = 0
        break
    else:
        i += 1

if not password[0].isalpha():
    print("REJECT")
    print("Your password must start with a LETTER (A–Z or a–z)")
    exit()
elif usr_log.lower() in password.lower():
    print("REJECT")
    print("Your password must not contain your username")
    exit()
elif usr_log[::-1].lower() in password.lower():
    print("REJECT")
    print("Your password must not contain your username")
    exit()

weak_pswd = ["password", "qwerty", "12345", "admin", "god"]
while i < 5:
    if weak_pswd[i] in password.lower():
        print("REJECT")
        print('Your password must NOT contain these weak substrings (case-insensitive): "password", "qwerty", "12345", "admin", "god" ')
        exit()
    elif i == 5:
        i = 0
        break
    else:
        i+=1

score = 0
if password[-1].isdigit() or password[-1] == special_s:
    score +=1
if "-" in password and "_" in password:
    score +=1
if "@" in password or "#" in password:
    score +=1
special_s_bool = False
di_bool = False
up_bool = False
lo_bool = False
while i < 4:
    if password[i] in special_s:
        special_s_bool = True
    elif password[i].isdigit():
        di_bool = True
    elif password[i].isupper():
        up_bool = True
    elif password[i].islower():
        lo_bool = True

    i += 1
if special_s_bool and (di_bool or up_bool or lo_bool):
    score +=1
if di_bool and (special_s_bool or up_bool or lo_bool):
    score +=1
if up_bool and (di_bool or special_s_bool or lo_bool):
    score +=1
if lo_bool and (di_bool or special_s_bool or up_bool):
    score +=1
di = 0
lo = 0
up = 0
sp = 0
for i in password:
    if i in special_s:
        sp+=1
    if i.islower():
        lo+=1
    if i.isupper():
        up+=1
    if i.isdigit():
        di+=1
ok = ""
strong = ""
elite = ""
if 0 <= score <= 1:
    ok = "OK"
if 2 <= score <= 3:
    strong = "STRONG"
if score == 4:
    elite = "ELITE"
print(f"RESULT: {ok}{strong}{elite} (len={len(password)} d={di}/{len(password)} lo={lo}/{len(password)} up={up}/{len(password)} sp={sp}/{len(password)})")