user = {
    "name": "Alice",
    "age": 28,
    "skills": ["Python", "SQL"]
}

# print(user)

# print(user["name"])

# user["location"] = "New York"
# user["name"] = "Bob"

# print(user)

for key, value in user.items():
    print(f"{key} -> {value}")