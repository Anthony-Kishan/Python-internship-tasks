"""
Write a list which contains 5 players of Bangladesh Cricket Board
Write another list which contains only 5 booleans (each data represent each player is retired or not)
Write another list which contains 5 numbers (each number's are player age)

Input: user's name , user's age , user is reteired 

Decision , Shakib is a player and retired or his age is below 40

Output: True / False
30July , 2024
"""

# Assigning lists of players name, retirement status, and ages
player_name = ["shakib al hasan", "tamim iqbal", "gholam nousher", "mushfiqur rahim", "gazi ashraf"]
is_player_retired = [False, False, True, False, True]
player_age = [37, 35, 59, 37, 63]

# Taking user input values
name = input("Enter Player's Name: ").lower()
age = int(input("Enter Player's Age: "))
status = input("Enter Player's Retirement Status: ").lower()

# Checking if the player name is in the list and finding the name index in list
name_in_list = name in player_name
name_index = player_name.index(name)

# Checking if the player is retired or not by the index number and the boolean value
retired = status == "is retired" and is_player_retired[name_index] == True
not_retired = status == "is not retired" and is_player_retired[name_index] == False

# Checking if the player's age is below 40 or not with the index number
age_below_40 = age and player_age[name_index] < 40
age_above_40 = age and player_age[name_index] >= 40

final_result = (name_in_list and (age_below_40 and not_retired)) or (name_in_list and (age_above_40 and retired))

print(final_result)
