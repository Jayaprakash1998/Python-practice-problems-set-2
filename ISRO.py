'''        QUESTION:

ISRO:

ISRO scientists have to generate a series of numbers and encode it so that nobody could understand. The encoded series is generated with 2 numbers 1 and 9. 
Now help the scientist to generate the series .And print the series upto n.

Input Format : Single Integer N

Input Constraints : 1<=N<=1000

Output Format : List of encoded numbers within N

Sample Input :
10

Sample Output :
1
9
11
19
91
99
111
119
191
199




















HINTS:

1 - Assign 1 for 0s and 9 for 1s. But, in the binary representation of numbers, 3(11) is followed by 4(100) where in our case, 000 is missing.

2 - To avoid the case mentioned in the previous hint, start from 2(10) and while converting each number, neglect the 1 at the starting.

3 - Isn't it similar to the binary representation of numbers?

'''











































# ANSWER:

n = int(input())

for i in range(2, n+2):
  res = bin(i)[3:]
  res = list(res)
  for i in range(len(res)):
    if (res[i]=='0'):
      res[i]='1'
    else:
      res[i]='9' 
      
  res = ''.join(res) 
  print(res)



