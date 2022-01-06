# Imports
import random
import string

# Random chars
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Input length of the password
length = int(input("Length of the password: "))

# Shuffle characters
random.shuffle(characters)

# Creating password
password = []
for i in range(length):
    password.append(random.choice(characters))

# Print Password
print("".join(password))
