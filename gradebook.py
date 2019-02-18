# create initial subject and grade lists
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# add a class with its grade to the right lists
subjects.append("computer science")
grades.append(100)

# combine the lists into a human readable gradebook
gradebook = list(zip(subjects, grades))

# append an additional class to the gradebook
gradebook.append(("visual arts", 93))

# create last semesters gradebook
subjects1 = ["physics1", "calculus1", "poetry1", "history1", "comp sci1", "gym"]
grades1 = [83, 84, 85, 86, 87, 88]
last_sem_gradebook = list(zip(subjects1, grades1))

# combine the 2 semesters into a single gradebook
full_gradebook = last_sem_gradebook + gradebook

# print out full gradebook
print(full_gradebook)

# print(list(subjects))
# print(list(grades))
# print(gradebook)
