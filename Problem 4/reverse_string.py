"""
Complete the following python code to reverse the string entered by the user.

Name: Xiao Xinhai
Lab Time: February 15th
"""

def reverse_string():
    # YOUR CODE HERE
    
    
    while True:
        text_line = str(input())
        string = ""
        if text_line == "d":
            break
        elif text_line == "done" :
            break
        elif text_line == "Done":
            break
        string = text_line[::-1]
        print(string)

if __name__ == "__main__":
    reverse_string()