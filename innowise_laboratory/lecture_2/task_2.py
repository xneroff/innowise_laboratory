def generate_profile(age):
    if  0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

user_name = input("Enter your name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []

while True:
    hobby = input("Enter your hobby or 'stop' to finish: ")
    if hobby == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {
    "name": user_name,
    "age": current_age,
    "birth_year": birth_year,
    "life_stage": life_stage,
    "hobbies": hobbies
}

print("---|")
print(f"Profile Summary:"
      f"\nName: {user_profile['name']}"
      f"\nAge: {user_profile['age']}"
      f"\nLife Stage: {user_profile['life_stage']}")
if len(user_profile["hobbies"]) == 0:
    print("You didn't have any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile["hobbies"]:
        print(f"- {hobby}")