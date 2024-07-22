password = "Rajshri$123"
password_length = len(password)

if len(password) < 6:
    criteria = "Weak"
elif len(password) <= 10:
    criteria = "Medium"
elif len(password) > 10:
    criteria = "Strong"

print("The criteria of your password is:", criteria)
