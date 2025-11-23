"""Task 4 — Countdown Timer with Text Alerts

Goal: Combine loops, timing, and conditional logic in functions.

Write a function:

import time

def countdown(start, step, alert_every):
    ...

It should:

    Print numbers from start down to 0 with pauses of 0.5 seconds (time.sleep(0.5)).
    Every alert_every seconds, print a message like "N seconds left!".
    If there is no alert_every in the function call, use a default value of 5.
    At the end, print "Time’s up!".
"""
import time

def countdown(start, step=1, alert_every=5):
    count = 0
    while start != 0:
        time.sleep(0.5)
        if count % alert_every == 0 and count != 0:
            print(f"{start} seconds left!")
            start -= step
            count += 1
            continue
        print(f"{start}")
        count += 1
        start -= step
    print("Time’s up!")
countdown(10)
