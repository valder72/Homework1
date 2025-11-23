"""
Task 3 — Prime Analyzer

Goal: Create and reuse helper functions to solve a bigger logic problem.

Write:

    is_prime(n) — returns True if n is prime.
    list_primes(start, end) — returns a list of all primes between start and end.

Ask the user for the range and:

    Show the primes,
    Count them,
    Print the average distance between consecutive primes.

Example:

Range: 10–50
Primes: 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
Count: 11
Average gap: 3.6
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def list_primes(start, end):
    return [n for n in range(start, end) if is_prime(n)]

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
primes = list_primes(start, end)
print(f"Range: {start}-{end}")
if not primes:
    print("No primes in this range.")
else:
    print(f"Primes: {", ".join([str(s) for s in primes])}")
    print(f"Count: {len(primes)}")
c = primes[0]
gap = 0
for i in primes:
    if c == i:
        continue
    gap += abs(c - i)
    c = i
print(f"Average gap: {gap/(len(primes)-1)}")