a = "Single String"
b = """MultiLine String
Multiline String
"""

print(a)
print(a[1])
print(a[7:])

# Format String
print(f"Value of a is: {a}")
# print("Value of a is: %s" % a)
# print("Value of a is: {}".format(a))

# Transform String
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("S", "M"))
print(a.split(" "))
print(a.join(" "))
print(a.capitalize())