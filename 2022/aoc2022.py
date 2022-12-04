# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:54:32 2022

@author: cjlit
"""
import os
os.chdir('C:/Users/cjlit/OneDrive/Documents/AOC/2022/')
def getdata(day):
    filepath = 'inputs/day'+ str(day) + '.txt'
    f = open(filepath)
    dat = f.readlines()
    f.close()
    return dat
def day1func(dat):
    maxv = [0,0,0]
    current = 0
    for i in dat:
        if(i == "\n"):
            current = 0
        else:
            n = int(i.replace("\n", ""))
            current += n
            if current > maxv[0]:
                maxv[0] = current
            elif current > maxv[1]:
                maxv[1] = current
            elif current > maxv[2]:
                maxv[2] = current
    return(maxv)

def day2inp():
    filepath = 'inputs/day2.txt'
    f = open(filepath)
    dat = f.readlines()
    f.close()
    return(dat)

def day2func(dat):
    # A + X = Rock 1, B + Y = Paper 2, C+Z = Scissors
    wins = ['A Y', 'B Z', 'C X']
    draws = ['A X', 'B Y', 'C Z']
    score = 0
    for i in dat:
        j = i.replace('\n', '')
        if j in wins:
            score += 6
        elif j in draws:
            score += 3
        if j[2] == 'X':
            score += 1
        elif j[2] == 'Y':
            score += 2
        elif j[2] == 'Z':
            score += 3
            
    return score
            
def day2func2(dat):
    # X lose, y draw, z win
    score = 0
    for i in dat:
        j = i.replace('\n', '')
        if j[2] == 'X':
            score += 0
            if j[0] == 'A':
                score += 3 # scissors
            elif j[0] == 'B':
                score += 1
            elif j[0] == 'C':
                score += 2
        elif j[2] == 'Y':
            score += 3
            if j[0] == 'A':
                score += 1
            elif j[0] == 'B':
                score += 2
            elif j[0] == 'C':
                score += 3   
        elif j[2] == 'Z':
            score += 6
            if j[0] == 'A':
                score += 2
            elif j[0] == 'B':
                score += 3
            elif j[0] == 'C':
                score += 1
                
    return score
            
def day3func(dat):
    tot = 0
    for i in dat:
        j = i.replace('\n', '')
        v = int(len(j)/2)
        f = j[:v]
        l = j[v:]
        if len(f) != len(l):
            print('Wrong')
        for x in ''.join(set(f)):
            if x in l:
                if(ord(x)>=97):
                    print(x + ' ' + str(ord(x) - 96))
                    tot += ord(x)-96 # make lower case priority start 1
                else:
                    print(x + ' ' + str(ord(x)-38))
                    tot += ord(x) - 38 # make upper case priority start 27
    return tot

def day3func2(dat):
    tot = 0
    for g in range(int(len(dat)/3)):
        
        sub = [dat[3*g].replace('\n',''),
               dat[(3*g)+1].replace('\n',''), 
               dat[(3*g) + 2].replace('\n','')]
        sets=[set(sub[0]),
              set(sub[1]),
              set(sub[2])
              ]
        res=sets[0].intersection(sets[1]).intersection(sets[2])
        x = ''.join(set(res))
        if(ord(x)>=97):
            tot += ord(x)-96 # make lower case priority start 1
        else:
            tot += ord(x) - 38 # make upper case priority start 27
    print(tot)
    
def day4func(dat):
    counter = 0
    counter2 = 0
    for j in dat:
        r=j.replace('\n', '')
        l = r.split(',')
        one = l[0].split('-')
        two = l[1].split('-')
        if int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
            #print('TRUE: ' + l[0] +':' + l[1] + ': r1')
            counter += 1
        elif int(two[0]) >= int(one[0]) and int(two[1]) <= int(one[1]):
            #print('TRUE: ' + l[0] +': '+ l[1] + ': r2')
            counter += 1
        #else:
            #print('FALSE: ' + l[0] +': '+ l[1])
            
        if int(one[0]) >= int(two[0]) and int(one[0]) <= int(two[1]):
            counter2 +=1
            print('TRUE 1:' +one[0] + ', '+ two[0] + '-'+two[1])
        elif int(one[1]) >= int(two[0]) and int(one[1]) <= int(two[1]):
            counter2 += 1
            print('TRUE 2:' +one[1] + ', ' +two[0] + '-'+two[1])
        elif int(two[1]) >= int(one[0]) and int(two[1]) <= int(one[1]):
            counter2 += 1
            print('TRUE 3:' +two[1] + ', ' +one[0] + '-'+one[1])
        elif int(two[0]) >= int(one[0]) and int(two[0]) <= int(one[1]):
            counter2 += 1
            print('TRUE 4:' +two[0] + ', ' +one[0] + '-'+one[1])
        else:
            print('FALSE: ' + l[0] + ': ' + l[1])
            
    print(counter2)