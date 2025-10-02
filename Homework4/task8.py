"""
Task 8 — Movie Ratings Dashboard 📊

Requirements:
  - ratings = [4, 5, 3, 2, 5, 4, 5, 3, 4]
  - Use a loop to compute:
      * Average rating (1 decimal)
      * Count of 5-star reviews
  - Print both results on separate lines

Practice: loop aggregation, counting, formatting

OUTPUT EXAMPLE
--------------
Average rating: 3.9
Number of 5-star reviews: 3
"""

ratings = [4, 5, 3, 2, 5, 4, 5, 3, 4]
print("(Starter) Ratings:", ratings)
# TODO: compute average and number of 5-star reviews using loops only
b = 0
for rating in ratings:
    b += rating
av = b / len(ratings)
print(f"Average rating: {av:.1f}")
fivestar = 0
for rating in ratings:
    if rating == 5:
        fivestar += 1
print(f"Number of 5-star reviews: {fivestar}")
