"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name:
Lab Time:
"""

def inc_5():
    one = int(input())
    two = int(input())
    if two < one:
        print("Second integer can't be less than the first.")
    else:
     string = ""
     for i in range(one, two + 1, 5):
          string = string + str(i) +" "
        

     print(string)
        
    # Write your code here
    



if __name__ == '__main__':
    inc_5()