password="BACd1*abc"
if not any(char.isupper() for char in password):
    print("Not valid")
elif len(password)<8:
    print("Not valid")
elif not any(char.islower() for char in password):
    print("Not valid")
elif not any(char.isdigit() for char in password):
    print("Not valid.")
elif not any(char in "@#$%^&*=+-_" for char in password):
    print("Not valid.")
else:
    print("Valid password")
