student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
max_value = None
for max in student_scores:
    if (max_value is None or max > max_value):
        max_value = max
print(max_value)


# Alternate solution
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)
