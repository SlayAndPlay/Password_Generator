import random
import string

while True:
    
    while True:
        pass_length = input("Enter length of password required: ")
        if pass_length == "":
            print("Cannot be left blank!")
        else:
            try:
                int(pass_length)
            except:
                print("Invalid entry")
                continue
            else:
                break
    
    special_chars = input("Which special characters are allowed? [Hit enter if no exclusions exist]. ")
    
    if special_chars == "":
        special_chars = "!@#$%&"

    pass_components = [string.ascii_letters, string.digits, special_chars]

    chars = []

    for components in pass_components:
        for item in components:
            chars.append(item)
            
    def generate_password():
        password = []
        for i in range(int(pass_length)):
            rchar = random.choice(chars)
            password.append(rchar)
        return "".join(password)
    print("Generated password is: " + generate_password()) 
    break   