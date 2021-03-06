'''       QUESTION:

Speed Dating:

A nationwide speed dating event is organised on 14th of February every year. Let’s say ‘N’ men and ‘M’ women attended the speed dating event in the year 2019. 
Each person attending the event will be given a special token. On each successful meet, the token has to be exchanged with the other person.  
A prize is given for one among the lucky participants, who has got their own token back. 
Since it is a onetime opportunity it’s made sure that each men and women meet each other once. 
Your task is to find out how many times the tokens are being exchanged in total.

Input Format : The input contains two integer values N and M
N is the number of Men and M is the number of Women

Input Constraints : 1<= N,M <=10^9

Output Format : One single number - Total number of token exchanges

Sample Input :
8776 7974

Sample Output :
69979824















HINTS:

1 - Try to relate the problem with permutation.

2 - The problem is to find the possibilities while Choosing N men on one side and M women at another side.

3 - The answer is to just multiply the two integers. The proper formula is nP1*mP1.

'''





















































# ANSWER:

n,m=map(int,input().split())
x = n * m
print(x)
