percent = None
sum = 0
for i in range(5):
    grade = float(input('Enter your grade - '))
    sum+=grade

percent = sum/5

print(percent)

if percent >= 90:
    print('Grade A')
elif percent < 90 and percent >= 80:
    print('Grade B')
elif percent < 80 and percent >= 65:
    print('Grade C')
elif percent < 65 and percent >= 50:
    print('Grade D')
else:
    print('Grade F')
