# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:36:40 2022

@author: khool
"""
"""Given the names and grades for each student in a class of  students, store 
them in a nested list and print the name(s) of any student(s) having the second
lowest grade. Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line"""
"""Constraints: 2 <= N <= 5.
There will always be one or more students having the second lowest grade"""

final_list = [] #nested list of names and scores
for number in range(int(input('enter N: '))): #number of students
    inner_list = [] #initial list
    name = input('enter a name: ') #enter name
    score = float(input('enter a score: ')) #enter score
    inner_list.append(name) #append name
    inner_list.append(score) #append score
    final_list.append(inner_list)#create a nested list to look like [[],[]]
    
score_list_1 = [inner_list_1[1] for inner_list_1 in final_list] 
#print(score_list_1) #create a list for scores

#score_list = []
#for score_1 in range(len(final_list)):
    #score_list.append(final_list[score_1][1])
#print(score_list) #alternative way to create a list for scores

min_score = min(score_list_1) #minimum score 
nxt_min_score_list = [nxt_score for nxt_score in score_list_1 if nxt_score != min_score]
#print(nxt_min_score_list)

nxt_min_score = min(nxt_min_score_list) #next minimum score
nxt_score_student_list = [student[0] for student in final_list if nxt_min_score == student[1]]
#print(nxt_score_student_list) #create a list for student list for next minimum score

nxt_score_student_list = sorted(nxt_score_student_list) #sorted alphabetically

for student_s in nxt_score_student_list:
    print(student_s)