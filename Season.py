# Seasons stored in a tuple
seasons = ("Winter", "Spring", "Summer", "Autumn")

# Ask user for month number
month = int(input("Enter month number 1-12: "))

# Determine season
if month in (12, 1, 2):
    season = seasons[0]   # Winter
elif month in (3, 4, 5):
    season = seasons[1]   # Spring
elif month in (6, 7, 8):
    season = seasons[2]   # Summer
elif month in (9, 10, 11):
    season = seasons[3]   # Autumn
else:
    season = "Invalid month!"

print("Season:", season)
