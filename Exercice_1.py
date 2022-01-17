# -*- coding: utf-8 -*-
"""

EXERCICES PYTHON PROGRAMMING

Created on Sat Jan 15 10:04:36 2022

@author: LN
"""

# Exercice 1 : Using a WHILE loop, find a way to create a very simple authentification script
# ###########################################################################################

password = '1234'

essai = input("Entrer le mot de passe")
while essai != str(password):
    essai = input("Mot de passe erroné : Entrer le mot de passe")
print("Bravo ! Tu as trouvé le mot de passe")

# Exercice 2 : Create functions 
# #############################

# Declare a function that returns the square root of a number. We'll call it sqrt().

def sqrt (x) : 
    return x ** 0.5

# Execute the function to compute the square root of 25 and print the result:

print(sqrt(25))

# Exercice 3 : Calculate interests
# ################################

# How much do you get for your savings ?

# So let's create a function that will allow us to know how much money a user will have in total after a certain number of years.

# The user should be able to call the function which will then ask for :
    # The total amount he wishes to place
    # The number of years he wants to invest his money for
    # The rate of interest to which he is entitled

def interest(amount, years, rate): 
    interests = 0
    A = amount
    if A > 0  and years > 0 and rate > 0 :
        if rate <= 1 :
            try :
                for i in range(years):
                    interests += A * rate
                    A += A * rate
                print("Your final amount will be {:4.2f}".format(A))
                print("Your total earn interest will be {:4.2f}".format(interests))
                print("The total amount of money you will have after you deposit {:4.2f} at the end of {:4.2f} years will be {:4.2f} €".format(amount, years, A))
            
            except ValueError: # happens if the user types something other than numbers.
                print('Please recall you need to enter numbers.')
        else : 
            print("Please recall to enter rate as a value between 0 and 1 and not a %.")
    else : 
        print("Please recall you need to enter positive numbers.")

interest(1000,10,0.1)

# Exercice 2 : Mathematically Oriented Programming
# ################################################

# Mathematics, in general, we don't like to do it. 
# Especially when it involves repeating operations, over and over again. 
# Let's be real lazy and create a class that will do the operations we want for us.

# 1. Create a class to be called "math."
# _This class will have no internal attributes, so you don't need to define an init() _

class math():

# 2. Create a method that will compute the square root of any number.
    def square(self):
        return self ** 0.5

# 3. Create a method that will calculate the average of any list of numbers.
    def average(self):
        if not isinstance(self, list):
            raise TypeError("L'objet doit être une liste'")
        else: 
            return sum(self) / len(self)

# 4. Create a method to find out if a number is even or odd.
    def odd(self):
        if self % 2 == 0 : 
            print("Even")
        else : 
            print("Odd")
            
# 5. Finally, create a method that will give the total sum of a list of numbers.
    def sum(self):
        return sum(self)

# Exercice 3 : Imputer 
# ####################

# 1. Create a class that we will call Imputer.
# To simplify the exercise, we will only deal with lists for the moment. 

class Imputer():

# 2. Our class will take an attribute that we will call list.
    def __init__(self, liste): 
        self.liste = liste

# 3. Create an avg() function that will first remove the missing value and then replace it with the average of the list.
    def avg(self): 
        index = 0
        sansNA = [x for x in self.liste if x != None]
        Moyenne = sum(sansNA)/len(sansNA)
        for i in self.liste :
            if i == None :
                self.liste[index] =  Moyenne
            index += 1
        # ou 
        # self.liste = [Moyenne if x is None else x for x in self.liste]
                
# 4. With a median ?
    def med(self): 
        index = 0
        sansNA = [x for x in self.liste if x != None]
        l = sorted(sansNA)
        l_len = len(l)
        if l_len < 1:
            mediane = None
        elif l_len % 2 == 0 :
            mediane = (l[int((l_len-1)/2)] + l[int((l_len+1)/2)]) /2
        else:
            mediane = l[int((l_len-1)/2)]
        for i in self.liste :
            if i == None :
                self.liste[index] = mediane 
            index += 1

# Exercice 4 : Manipulate data types
# ##################################

# LISTES : 

#Here is a list ["Hello", "I", “Michel”, “am”]

# 1. Store this list in a variable we will call my_list

my_list = ["Hello", "I", "Michel", "am"]

# 2. Make a loop so that the console returns each of the items in the list
    
for i in my_list : 
    print(i)

# Here's a list of ages: [12, 16, 34, 58, 9].

# 1. Store this age list in a variable that we'll call age

age = [12, 16, 34, 58, 9]

# 2. We would like this list to be arranged in ascending order, how do we do that?

age.sort()
print(age)

# DICTIONARIES

# We told you that dictionaries are very useful with APIs, so let's try to use the Star Wars API.

import requests
request = requests.get("https://swapi.dev/api/people/1/")
dic = request.json()

# This will make it possible to call the Star Wars API to store it on a dictionary format in a variable called dic.

# 1. See what's in the dictionary via a loop

for item in dic.items() :
    print(item)

# 2. We'd like to make a nice phrase to describe the character like this:

print("{} is {} cm tall and weighs {} kg. He was born in {}".format(dic['name'], dic['height'], dic['mass'], dic['birth_year']))

# 3. import new character

request = requests.get("https://swapi.dev/api/people/5/")
dic = request.json()

# 4. Re-run your code, do you see a problem? Try to fix it.

for item in dic.items() :
    print(item)
if dic['gender'] == 'female':
    print("{} is {} cm tall and weighs {} kg. She was born in {}".format(dic['name'], dic['height'], dic['mass'], dic['birth_year']))
else :
    print("{} is {} cm tall and weighs {} kg. He was born in {}".format(dic['name'], dic['height'], dic['mass'], dic['birth_year']))

# SLICEs

kilometres_travelled = [50, 10, 100, 25, 1000, 21, 12,30]

# 1. Using a loop, calculate the total average of all the users' trips
total = 0
for i in kilometres_travelled :
    total += i

Average = total / len(kilometres_travelled)
print("On average, users travelled {} km to get to work.".format(Average))

# This average is not really representative because it is higher than most of the values in the list. 
# Indeed, the distances are all <= 100kms, except one which is worth 1000kms.
# This value is what is called an outlier, which probably corresponds to an erroneous entry 
# (it seems unlikely that someone would travel 1000kms every morning to work).

# To get a more representative average of the sample, this outlier could be removed from the list before calculating the average.
# 2. Change the variable kilometers_travelled to have a more representative average

New_mean = sum([x for x in kilometres_travelled if x < 1000]) / len([x for x in kilometres_travelled if x < 1000])
index = 0
for i in kilometres_travelled : 
    if i > 100 :
        kilometres_travelled[index] = New_mean
    index += 1
 print(kilometres_travelled)           
