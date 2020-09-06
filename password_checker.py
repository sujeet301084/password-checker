# user input for user name 
user_name = input('username: ')
# user pasword
pass_word = input('password: ')
# create a variable to check for the password length
pass_length = len(pass_word)
# create a variable pass_hidden to hide the password when it is printed
pass_hidden = pass_length * '*'
print(f'Hello {user_name} your password is {pass_hidden} and is {pass_length} characters long')