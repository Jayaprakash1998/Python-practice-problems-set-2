'''       QUESTION:

Weirdvita - Coding Contest:

A group of students was separated into two batches A and B to attend a coding contest. For ‘A’ batch, a program that has been completed is represented with 1. 
For the ‘B’ batch, 0 represents the completed program.

Let's assume all the students completed the given program so the winning team is calculated in a weird way. 
Students are sitting in a row and they are already shuffled. 
The co-ordinator passes a sheet with all the student names in an order the same as their sitting position. 
As mentioned above they fill the sheet with one character either '0' or '1', it is based on their team.

If there are at least 7 students of some team marked one after another the same character in the sheet, then they are the winning team. 
For example, 00100110111111101, then Batch A is the winner.

If any team win the contest print "Some team has Won" or print "No Team Won"

Input Format : The first input line contains a non-empty string consisting of characters "0" and "1", which represents students.

Input Constraints : The length of the string does not exceed 100 characters. There's at least one student from each team present on the contest.

Output Format : Print "Some Team Has Won", Otherwise print "No Team Won"

Sample Input :
1000000001

Sample Output :
Some Team Has Won





















# HINTS:

1 - It has all to do with implementation.

2 - Use a temporary variable to track consecutive characters.

3 - If the current character is the same as the previous, increment the counter variable. If the count is >= 7, then the answer is Yes. No, otherwise.

'''









































# ANSWER:

x = input()
if "0000000" in x or "1111111" in x:
  print("Some Team Has Won")
else:
  print("No Team Won")








