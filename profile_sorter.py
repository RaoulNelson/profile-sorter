# Uses a bubble sort algorithm to sort user profiles by calories in ascending order
def bubbleSort(profiles):
    n = len(profiles)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if profiles[j]["Calories"] > profiles[j + 1]["Calories"]:
                profiles[j], profiles[j + 1] = profiles[j + 1], profiles[j]

# Requests input of the number of user profiles
numProfiles = int(input("Enter the number of user profiles: "))

# Requests information regarding each user profile
user_profiles = []
for i in range(numProfiles):
    name = input("\nEnter name: ")
    age = int(input("Enter age: "))
    calories = int(input("Enter daily calorie intake: "))
    user_profile = {
        "Name": name,
        "Age": age,
        "Calories": calories
    }
    user_profiles.append(user_profile)

# Shows the unsorted profiles
# Used for debugging
"""
print("\nUnsorted User Profiles:")
for profile in user_profiles:
    print(profile)
"""
# Sorts profiles using bubble sort
bubbleSort(user_profiles)

# Displays the sorted user profiles
print("\nSorted User Profiles:")
for profile in user_profiles:
    print(profile)