print("-------------Grade Statistics-------")

# Input grads
grade1 = float(input("Enter grads 1:  "))
grade2 = float(input("Enter grads 2:  "))
grade3 = float(input("Enter grads 3:  "))

# Store grades in a list
grade = [grade1, grade2 , grade3 ]

#Calculate total and average
total_grades = sum(grade)
average_grade = total_grades/len(grades)

#Find highest and lowest
highest_grade = max(grade)
lowest_grade = min(grade)
#Display results
print("/n-----Results------")
print("Entered grades:" , grades)
print("Total points:" , total_grades)
print("Average grade:", round(average_grade, 2))
print("Highest grade:" , highest_grade)
print("Lowest grade:" , lowest_grade)

