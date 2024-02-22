"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name:Xiao Xinhai
Lab Time:February 15th
"""

def brute_eq():

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())

    for x in range (-10, 11, 1):
        for y in range (-10, 11, 1):
            if a * x + b * y == c and d * x + e * y == f:
                print("x = %d , y = %d"%(x, y))
                return

    print("There is no solution found")

    
if __name__ == "__main__":
    brute_eq()