# Project 2: Age in Seconds
# Convert Age (years) to seconds

print("=" * 35)
print("AGE IN SECONDS CALCULATOR")
print("=" * 35)

#Ask for age
age_years = input("How old are you(in years)?")

# Convert from string to integer (whole number)
age_years = int(age_years)

# calculate seconds
# 1 year = 365 days (ignoring leap years)
# 1 day = 24 hours 
# 1 hour = 3600 seconds
seconds_in_year = 365 * 24 * 3600
age_seconds = age_years * seconds_in_year

#Display result
print(f"\nYou are approximately {age_seconds:,} seconds old!")
print(f"(Based on {age_years} year * 365 days/year)")

# Bonus: Calculate for a specific number of years
print("\n---BONUS---")
years_to_check = 10
seconds_10_years = years_to_check * seconds_in_year
print(f"At age {years_to_check}, you'd be {seconds_10_years:,} seconds old.")