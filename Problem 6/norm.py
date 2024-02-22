"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:Xiao Xinhai
Lab Time:Februrary 15th
"""

def norm():


 num_values = int(input())
 value_list = []

 for _ in range(0,num_values):
     value = float(input())
     value_list.append(value)
 max_value = max(value_list)
 for value in value_list:
     change_value = value / max_value
     print(f'{change_value:.2f}')

    # Write your code here

if __name__ == "__main__":
    norm()