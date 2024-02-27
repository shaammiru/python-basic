# Else after For
numbers = [1, 2, 3, 4, 5]

for num in numbers:
  if num == 6:
    print("Angka ditemukan! Program berhenti!")
    break
else:
  print("Angka tidak ditemukan.")

# Else after While
num = 0
while num < 5:
  print("Nilai num adalah: ", num)
  num += 1
else:
  print("Loop selesai.")

# List Comprehension
numbers = [1, 2, 3, 4]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)