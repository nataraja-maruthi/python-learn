age = input("Enter the age\n")

print("Age is ", age)

decade = int(age) // 10
remainder = int(age) % 10

print("Age is ", int(decade))
print("Age is ", remainder)

print("you are " + str(decade) + " decades and " + str(remainder) + " days old")