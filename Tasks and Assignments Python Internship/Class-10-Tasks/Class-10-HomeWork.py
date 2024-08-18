# PROBLEM 1 -> # Create a simple function that access a dictionary & return his age.

person = {
    "name": "Neo",
    "age": 21,
    "email": "neo@gmail.com"
}

def return_age(dic):
    print(dic.get("age"))

return_age(person)

# PROBLEM 2 -> # Convert the function into a lambda function

return_age = lambda dic: dic.get("age")
print(return_age(person))

# PROBLEM 3 -> # Make a list with same shape dictionary at least 5 element and each of them call your function.
