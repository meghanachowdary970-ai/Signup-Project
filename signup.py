
def signup(username, password):
    if username == "":
        return "Username is required"

    if len(password) < 6:
        return "Password must be at least 6 characters"

    return "Signup successful"

print(signup("Meghana", "123456"))
print(signup("", "123456"))
print(signup("Meghana", "123"))
