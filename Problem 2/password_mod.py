"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:Xiao Xinhai
Lab Time:February 15th
"""
# * i becomes 1
# * a becomes @
# * m becomes M
# * B becomes 8
# * s becomes $
def password_mod():
    word = input()
    password = ''
    for i in range (0, len(word), 1):
        if word[i] == 'i':
            password += '1'
        elif word[i] == 'a':
            password += '@'
        elif word[i] == 'm':
            password += 'M'
        elif word[i] == 'B':
            password += '8'
        elif word[i] == 's':
            password += '$'
        else:
            password += word[i]
    password += '!'
    print (password)
    # Type your code here.

if __name__ == "__main__":
    password_mod()