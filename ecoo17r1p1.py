# trip_cost = 수학여행 비용 , student = 학생수 y = 학년
y =[12,10,7,5]

trip_cost = int(input())
trip_cost = 50 < c < 50000

student = int(input())
student = 4 < n < 2000

proportions = input().split()

for i in range(len(proportions)):
   proportions[i] = float(proportions[i])

students_per_year = []

for proportion in proportions:
   students = int(student * proportion)
   students_per_year.append(student)

counted = sum(students_per_year)
uncounted = student - counted
most = max(students_per_year)
where = students_per_year.index(most)
students_per_year[where] = students_per_year[where] + uncounted

total_raised = 0
for i in range(len(students_per_year)):
   total_raised = total_raised + students_per_year[i] * y[i]

if toal_raised /2 < trip_cost:
   print('Yes')
else:
   print('No')
