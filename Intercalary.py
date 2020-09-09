'''         QUESTION:

Intercalary:

An Intercalary year is a year with one extra day. Can you write a program to check if a year is Intercalary or not?

Input Format : The first line of input contains an integer t--the number of test case.
Then the next t lines consist of a year.

Input Constraints : 1<=year<=10^9

Output Format : Print "Yes" if it's Intercalary, Otherwise "No"

Sample Input :
1
2019

Sample Output :
No





















HINTS:

1 - Not all years divisible by 4 are leap years.

2 - If the year is divisible by 4 and it is not divisible by 100, it is a leap year.

3 - If a year is divisible by 100. then is a leap year only if it is evenly divisible by 400.

'''


















































# ANSWER:

for i in range(int(input())):
  year = int(input())
  
  if (year%4==0 and (year%100!=0 or year%400==0)):
    print("Yes")
  else:
    print("No")
  
  
  
