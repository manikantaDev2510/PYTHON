# # Calculation

# a = int(input("Enter the values: "))
# b = int(input("Enter the values: "))

# print(f"Addition of {a},{b} {a+b}")
# print(f"Subtraction of {a},{b} {a-b}")
# print(f"Multiplication of {a},{b} {a*b}")
# print(f"Division of {a},{b} {a/b}")
# print(f"Modulus of {a},{b} {a%b}")
# print(f"Power of {a},{b} {a**b}")


# # Reversing
# string = input("Enter the String: ")
# print(string[::-1])

# # Palindrome checker
# word = input("Enter the String: ")

# if (word == word[::-1]):
#     print("Give Word is Palindrome")
# else:
#     print("Give Word is Not Palindrome")


# Email Checking
email = input("Enter your Email: ")

if email.split("@")[0] != "" and "@" in email and email.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")
