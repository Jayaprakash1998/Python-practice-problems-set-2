'''           QUESTION:

Weird City:

You are stuck in a weird city. The city is called weird because calculations are approached differently. The subtraction means mod, addition means Power in the city. 
There is an airplane that was hidden behind a number of complicated tree roots numbered from 1. You have to find that airplane to return back to your place. 
You sought help from a person in that city. He gave you two numbers n and m. And told you to perform m-(2+n). Write a program to find the correct answer.

Input Format : The first line contains a single integer n
The second line contains a single integer m

Input Constraints : 1<=n,m<=10^8

Output Format : Output a single integer

Sample Input :
4
42

Sample Output :
10

















HINTS:

1 - See that the value of N is larger. We can't handle numbers that big in size.

2 - Modular arithmetics have the property that the result will be always in the range. For example, if M does not exceed 10 in any case, For n=1,2,3 you can do the process. 
    For bigger values, you can simply print M.
    
3 - If N<27, perform the operation. Beyond that, you can simply print M as 2^27 is greater than 10^8.

'''



















































# ANSWER:

n = int(input())
m = int(input())
x = m%(2**n)
print(x)
