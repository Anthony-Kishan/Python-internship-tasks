"""
Print this to the terminal:
His name is xyz. He is 30 years of old. His email address is 'xyz@gmail.com'.
Is he married ? True. He has 5 years of experience.
"""
# Dictionary
person1 = {
    "name" : "xyz",
    "age" : 30,
    "email" : "xyz@gmail.com",
    "marital_status" : True,
    "experience" : 5,
    "languages" : ["Bangla", "English", "Hindi"]
}

# Creating & Printing the Bio
print(f"His name is {person1.get('name')}. He is {person1.get('age')} years of old. His email address is {person1.get('email')}.\nIs he married? {person1.get('marital_status')}. He has {person1.get('experience')} years of experience. {person1.get('languages')[2]}")

print("=======================================================================================================")

# List of Dictionaries
persons = [
    {"name":"xyz", "age":30, "email":"xyz@gmail.com", "marital_status":True, "experience":5},
    {"name":"abc", "age":28, "email":"abc@gmail.com", "marital_status":True, "experience":4},
    {"name":"def", "age":29, "email":"def@gmail.com", "marital_status":False, "experience":3}
]
# Accessing the values
print(persons[2].get("name"), persons[2].get("experience"))

# Printing the Bio
print(f"His name is {persons[1].get('name')}. He is {persons[1].get('age')} years of old. His email address is {persons[1].get('email')}.\nIs he married? {persons[1].get('marital_status')}. He has {persons[1].get('experience')} years of experience.")