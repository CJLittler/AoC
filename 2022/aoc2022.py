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
    dat = f.read().splitlines()
    f.close()
    return dat
def day1func(dat):
    maxv = [0,0,0]
    current = 0
    for i in dat:
        if(i == ""):
            current = 0
        else:
            n = int(i)
            current += n
            if current > maxv[0]:
                maxv[0] = current
            elif current > maxv[1]:
                maxv[1] = current
            elif current > maxv[2]:
                maxv[2] = current
    return(maxv)


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
        j = i
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
    for j in dat:
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
    for r in dat:
        l = r.split(',')
        one = l[0].split('-')
        two = l[1].split('-')
        if int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
            counter += 1
        elif int(two[0]) >= int(one[0]) and int(two[1]) <= int(one[1]):
            counter += 1
        #else:
            #print('FALSE: ' + l[0] +': '+ l[1])
            
        if int(one[0]) >= int(two[0]) and int(one[0]) <= int(two[1]):
            counter2 +=1
        elif int(one[1]) >= int(two[0]) and int(one[1]) <= int(two[1]):
            counter2 += 1
        elif int(two[1]) >= int(one[0]) and int(two[1]) <= int(one[1]):
            counter2 += 1
        elif int(two[0]) >= int(one[0]) and int(two[0]) <= int(one[1]):
            counter2 += 1
        #else:
        #    print('FALSE: ' + l[0] + ': ' + l[1])
            
    print([counter,counter2])
    
def day5func(dat,part):
    start=dat[0:8]    
    inst=dat[10:]
    locs = [1,5,9,13,17,21,25,29,33]
    rows=[]
    for j in locs:
        nr = [item[j] for item in start]
        #print(nr)
        newrow=list(filter(lambda x: x != ' ', nr))
        newrow.reverse()
        #print(newrow)
        rows.append(newrow)
        
    def move(rows, rcol, ct, ncol,part):

        moving=rows[rcol][-ct:]
        if part == 1:
           moving.reverse()
        rows[rcol]=rows[rcol][:-ct]
        [rows[ncol].append(x) for x in moving]
        
        return rows
    for i in inst:
        i.replace('\n', '')
        irow = i.split(' ')
        rows = move(rows, int(irow[3])-1, int(irow[1]), int(irow[5])-1,part)
    return [x[-1] for x in rows]
        
def day6func(dat,part):
    if part == 1:
        size = 4
    elif part == 2:
        size = 14
    def find(data,x,size):
        y=0
        if len(set(data[x:x+size])) == size:
            y=x
        if y != 0:
            return y + size # size for hitting end of line
    def checkvalid(n):
        if n > 0:
            return True
        else:
            return False
    out = [int(find(dat[0],x,size) or -1) for x in range(len(dat[0])-size)]
    v = list(filter(checkvalid, out))
    return min(v)

def day7func(dat, part):
    def increment(allpaths, path, amount):
        # Function that loops path within current directory to add the size
        for p in range(len(path)):
            allpaths[''.join(path[0:p+1])] += amount
        return allpaths
    
    path= []
    allpaths = {}
    size = 0
    for row in dat:
        if row[0:7] == '$ cd ..':
            path = path[:-1]
        elif row[0:6] == '$ cd /':
            path = []
        elif row[0:4] == '$ cd':
            path.append(row[5:])
            #print(path)
        elif row[0:3] == 'dir':
            allpaths[''.join(path)+row[4:]]=0
        elif row[0:1] not in ['$', 'd']:
            amt = row.split(' ')[0]
            #print(amt + ''.join(path))
            allpaths = increment(allpaths, path, int(amt))
            size += int(amt)
    tot = 0
    print(size)
    targetrem = size - 40000000
    rem=size
    for x in allpaths.values():
        if x < 100000 and part == 1:
            tot += x
        if x > targetrem and part == 2:
           rem = min(rem,x)
            
    if part == 1:
        rvalue = tot
    elif part == 2:
        rvalue = rem
    return rvalue
    
    