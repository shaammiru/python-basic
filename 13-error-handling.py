# Error Handling is the process of catching errors and handling them gracefully.
x = 0
try:
  print(10 / x)
except ZeroDivisionError:
  print("Can't divide by zero!")
except:
  print("Something went wrong!")
else:
  print("Divide success!")
finally:
  print("This will always execute.")

# Raise an exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero!")