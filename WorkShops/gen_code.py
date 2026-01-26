import random

def generate_password():
    """
    This Function Generate a Random Password.
    """
    length = int(input("Enter The Length You Want:"))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = " "
    for _ in range(length):   # "_" => ignore the index ,"i" not important and make it random .
        password += random.choice(characters)
        
    return f"The Generated Password is:{password}"
        
generate_password()