job_roles = ['manager', 'team lead', 'staff']

role_name = input("Eneter the Job Role: ").lower()
years_of_experience = int(input("Eneter Years of Experience: "))

if role_name in job_roles:
    if role_name == job_roles[0] and years_of_experience > 5:
        print("Eligible for Special Benefit.")
    elif role_name == job_roles[1] and 1 <= years_of_experience <= 5:
        print("Eligible for Special Benefit.")
    elif role_name == job_roles[2] and years_of_experience > 7:
        print("Eligible for Special Benefit.")
    else:
        print("Not eligible for Special Benefit.")
else:
    print("There is no such Job Roles.")


