# PerfectMatch: A Simple Marriage Matchmaker

# Sample database of potential matches
profiles = [
    {"name": "Riya", "age": 25, "gender": "Female", "hobbies": ["reading", "traveling"]},
    {"name": "Raj", "age": 27, "gender": "Male", "hobbies": ["sports", "movies"]},
    {"name": "Priya", "age": 23, "gender": "Female", "hobbies": ["music", "cooking"]},
    {"name": "Aman", "age": 26, "gender": "Male", "hobbies": ["traveling", "fitness"]},
    {"name": "Neha", "age": 24, "gender": "Female", "hobbies": ["art", "dance"]},
]

def find_match(user_profile):
    best_match = None
    highest_score = 0

    for profile in profiles:
        # Skip profiles of the same gender
        if profile["gender"] == user_profile["gender"]:
            continue

        # Calculate match score based on hobbies
        common_hobbies = set(user_profile["hobbies"]).intersection(set(profile["hobbies"]))
        score = len(common_hobbies)

        # Update the best match if this profile has a higher score
        if score > highest_score:
            highest_score = score
            best_match = profile

    return best_match, highest_score

# Input from the user
print("Welcome to PerfectMatch!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ").capitalize()
hobbies = input("Enter your hobbies (comma-separated): ").lower().split(", ")

user_profile = {
    "name": name,
    "age": age,
    "gender": gender,
    "hobbies": hobbies,
}

# Find the best match
match, score = find_match(user_profile)

if match:
    print(f"\nCongratulations, {user_profile['name']}! We found a match for you:")
    print(f"Name: {match['name']}, Age: {match['age']}, Hobbies: {', '.join(match['hobbies'])}")
    print(f"Compatibility Score: {score}")
else:
    print("\nSorry, no suitable match was found. Try again later!")

