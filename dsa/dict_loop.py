students = {'Taiye': 'Dayo', 'Mercy': 'Theo', 'Lords': 'Nkem', 'Sweetie': 'Abdullahi'}

for first_name, last_name in students.items():
    print(f'{first_name} -> {last_name}')

print()

for student in students:
    print(f'{student}: {students[student]}')
