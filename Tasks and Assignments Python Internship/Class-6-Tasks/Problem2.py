midterm_score = input("Enter Mid Term Exam Score: ").lower()
final_score = input("Enter Final Exam Score: ").lower()
extra_curricular = input("Enter Extra Curricular Status: ").lower()

grade = 'false'

if (midterm_score and final_score in ['a','b','c','d']) and (extra_curricular in ['high','moderate','none']):
    # print("entered 1st if statement")
    if midterm_score == 'a' and final_score == 'a' and extra_curricular == 'high':
        grade = 'A'
        is_graduate = True
    elif (midterm_score in ['a','b']) and (final_score in ['a','b']) and (extra_curricular in ['high','moderate']):
        grade = 'B'
        is_graduate = True
    elif (midterm_score in ['c','d']) and (final_score in ['c','d']) and (extra_curricular == 'moderate'):
        grade = 'C'
        is_graduate = False
    elif (midterm_score == 'd') and (final_score == 'd') and (extra_curricular == 'none'):
        grade = 'D'
        is_graduate = False
else:
    print("Invalid Input.")

if (grade in ['A','B']) and (extra_curricular in ['high','moderate']):
    print("The Student is Graduated.")
else:
    print("The Student does not meet the above criteria.")