import functools

# 1.1.1 print hello world
#Method 1
print'Hello World'

#Method 2
s = 'Hello World'
print s

# 1.1.2 print hello world in new line
#Method 1
print'Hello \n World'

#Method 2: using for loop
for each_word in s.split():
    print each_word

#Method 3: using comprehensive
s= [each_word for each_word in s.split()]
print s

#Method 4: using lambda
word = lambda s: [each_word for each_word in s.split()]
print word('Hello World, Here I go')

#1.1.3: print hello world using tab
#Method 1
print('Hello \t World')

#Method 2
new = "Hello\tWorld"
print([splits for splits in new.split("\t")])

#Method 3
word = lambda s:[each_word for each_word in s.split("\t")]
print word ('Hello\tWorld')

#1.1.4 and 1.1.5
def input_variable():
    i = input("Enter a variable")
    print type(i)

#1.1.6 a,b,c
def inputvariable():
    while(True):
        inVar = input('Enter a variable (enter 0 to exit): ')
        if (inVar==0):
            break
        if (isinstance(inVar, int) or isinstance(inVar,float)):
            print 'The inputted number is a number'
            if(inVar > 64.0 and inVar < 65.0):
                print 'The inputted number is between 64 and 65'

            elif (inVar < 65):
                print 'The inputted number is less than 65'
            else:
                print'The inputted number is greater than 64'

        elif (isinstance(inVar, str)):
            print 'The inputted value is a string'

        else:
            print 'The inputted value is neither a number not a string'

# 1.1.7
def triangleArea():
    base = input('Enter the base of the triangle: ')
    height = input('Enter the height of the triangle: ')

    if (base < 0 or height < 0):
        print('You have entered negative values for either base:{0} or height:{1} or both. Exit the code.'.format(base, height))
        exit(0)
    elif(isinstance(base, (int, float)) and isinstance(height, (int, float))):
        print 'The area of the triangle is {}'.format(base * height)
    else:
        print ('You have entered invalid values for either base:{0} or height:{1} or both. Please enter either an integer or a float. Exit the code.'.format(base, height))

# 1.1.8

def triangleArea1():
    base = float(raw_input('Enter the base of the triangle: '))
    height = float(raw_input('Enter the height of the triangle: '))

    if (base < 0.0 or height < 0.0):
        print('You have entered negative values for either base:{0} or height:{1} or both. Exit the code.'.format(base, height))
        exit(0)
    else:
        print 'The area of the triangle is {}'.format(base * height)


#1.2.1
def mean2():
    my_list = []
    i = int(input('Number of elements?: '))
    l = 0
    while ( l < i and i!='s'):
        my_list.append(raw_input ('Enter the element {0} (s terminates the program): ').format(l+1))
        l = l+1
    print my_list
    sum = 0
    for i in my_list:
        sum = sum + eval(i)
        #print sum
    mean = sum / (len(my_list)*1.0)
    print 'Mean is: {}'.format(mean)

#1.2.2a
def inputlst2():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr
    l = 0
    for i in inputarr:
        while (l < 2):
            print inputarr[l]
            l = l+1
#1.2.2b
def inputlst3():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    inputarr.reverse()
    print inputarr
    l = 0
    for i in inputarr:
        while (l < 2):
            print inputarr[l]
            l = l+1
#1.2.2c
def inputlst4():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr[:9]

#1.2.2d
def inputlst4a():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr[1:]



#1.2.2e
def inputlst5():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr[2:7]

#1.2.2f
def inputlst6():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))

    inputarr.append(raw_input('Enter another number to append to the list: '))
    print inputarr

#1.2.2g
def inputlst7():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    inputarr.extend(list(map(int, raw_input('Enter 5 numbers separated by comma: ').split(','))))
    print inputarr
#1.2.2h
def inputlst8():
    inputarr = []
    while (len(inputarr) < 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    inputarr.insert(3, 1234)
    print inputarr
#1.2.2i
def inputlst9():
    inputarr = []
    while (len(inputarr) < 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    modifyn = int(raw_input('Enter the element you wish to modify:'))
    inputarr.pop(modifyn)
    insern = int(raw_input('Enter the number you wish to replace the above element by: '))
    inputarr.insert(modifyn, insern)
    print inputarr
#1.2.2j
def inputlst10():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr[::-1]# an index which is a multiple of -1 so -1*0 = 0, -1*1 = -1 and so on in the reverse order!
#1.2.2k
def inputlst11():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr[::2]
#1.2.2l
def inputlst12():
    inputarr= []
    while (len(inputarr)< 10):
        inputarr.append(raw_input('Enter the element {0} : '.format(len(inputarr)+1)))
    print inputarr[::-2]


#1.2.3, 1.2.4 ,1.2.5,1.2.6
evens = lambda lst: filter(lambda num: num%2==0, lst)
odds = lambda lst: filter(lambda num: num%2==1, lst)
# 1.2.3
#print evens(range(1000))
# 1.2.4
#print odds(range(1000))
# 1.2.5
#print (evens(range(1000)) + odds(range(1000)))
# 1.2.6
lstoddeven = (evens(range(1000)) + odds(range(1000)))
lstoddeven.reverse()
#print lstoddeven


# 1.2.7a
squarelst = [i**2 for i in range(100)]
finallst = lambda squarelst: filter(lambda num:num>1000, squarelst)
#print(finallst(squarelst))

# 1.2.7b
squarelst1 = [i**2 for i in range(100) if i**2  > 1000]
evenlst =  lambda squarelst1: filter(lambda num: num%2==0, squarelst1)
#print(evenlst(squarelst1))


#1.2.8
players = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']
injuredPlayers = ['A', 'B']
noninjuredplayers= [i for i in players if i not in injuredPlayers]

# 1.2.9a
names = ['A', 'B']
ages = [1,19]
nameagelst = [(name, age) for name, age in zip(names, ages)]

#1.2.9b
# Using zip is better than other methods.
nameagelst1 = [(name, age) for name, age in zip(names, ages) if age >=18]
#without zip (using for loop)
nameandage = [(name, age) for name in names for age in ages if age >=18]
#without zip (using dict)
dict = {names [i]:ages[i] for i in range(len(names)) if ages[i] >=18}
dictlist = []
for key, value in dict.iteritems():
    temp = (key, value)
    dictlist.append(temp)

# 1.2.10a
def divisionbyten(lst):
    divbyten = lambda num: num%10==0
    is_ten = []
    for num in lst:
        if divbyten(num):
            is_ten.append(num)
    return is_ten
#divisionbyten(range(10000000))

# 1.2.10b
divisionbyten1 = lambda lst: filter(lambda num: num%10==0, lst)
#divisionbyten1(range(10000000))

# delta time
import time
t1 = time.clock()
result = divisionbyten(range(10000000))
t2 = time.clock()
deltatime = t2-t1

t1 = time.clock()
result = divisionbyten1(range(10000000))
t2 = time.clock()
deltatime1 = t2 - t1

print 'For loop runtime: {} sec'.format(deltatime)
print 'Comprehension  runtime: {} sec'.format(deltatime1)
print 'Comprehension is {} sec faster than the for loop'.format(deltatime - deltatime1)

# 1.2.11
listoflist = [['A', 'B'], ['C', 'D']]
flattenedlist = [num for list in listoflist for num in list]
#print flattenedlist

# 1.3.1
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Method 1 using comprehension
weekd = [i for i in enumerate(weekdays)]
print weekd

#Method 2 using lambda
weekd1 = lambda weekdays: [(value, weekdays[value]) for value in range(len(weekdays))]
print weekd1(weekdays)

# 1.3.2 fibonacci sequence
from functools import reduce

def fibonnaci(count):
    sequence = (0,1)
    for i in range(2, count):
        sequence += (reduce(lambda x,y: x+y,sequence[-2:]),)
    return sequence[:count]
print fibonnaci(10)

#1.3.3 : Mean
my_list = [1,4,5,10,12]
def funaverage(my_list):
    #sum = reduce((lambda x, y: x + y), my_list)
    average = sum(my_list) / (len(my_list)) # average = sum(my_list)/ len(my_list)*1.0
    return average


# 1.3.4, 1.3.5 : Variance  with degree of freedom as 0 and 1

def funvar(average, my_list, degoffree = 1):
    var = []
    var = [(average - i)**2 for i in my_list]
    print sum(var)/(len(my_list)- degoffree)*1.0


# variance with degree of freedom as user input (and not as keyword argument)

def funvar1(average, my_list):
    degoffree = int(input('Degree of freedom?: '))
    var = []
    var = [(average - i)**2 for i in my_list]
    print sum(var)/(len(my_list)- degoffree)*1.0



# 1.3.6: Mean with args as tuples

def argsMean(*args):
    indx = [index for value, index in enumerate(args)]
    #lambda args: [index for value, index in enumerate(args)]
    #print(type(indx([1,2,3,4])))
    sum = reduce((lambda x, y: x + y), indx)
    average = sum / (len(indx)*1.0)
    print(average)

# 1.3.6:  Mean with list as *args
def argsMeanlst(*args):
    lst = [1.3, 4.5, 6.7, 11.2, 100, 987.6]
    indx = lambda lst: [(lst[value]) for value in range(len(lst))]
    sum = reduce((lambda x, y: x + y), indx(lst))
    average1 = sum / (len(indx(lst))*1.0)
    print(average1)


#1.3.7: kwargs
def kwargsa(name = None, age=None, **kwargs):
    if name:
        print(name)
    if age:  # if age is not None
        print(age)
    print(kwargs.get('State'))  # kwarg is a dictionary
    print(kwargs.get('Height'))
    print(kwargs.get('Weight'))

# 1.3.8
# Method 1: using dict.values()
def kwargsd(name=None, age=None, **kwargs):
    if name:
        print(name)
    if age:  # if age is not None
        print(age)
    print(kwargs.values())

# Method 2: using iteiterator, dict.iteritems()
def kwargsd1(name=None, age=None, **kwargs):
    if name:
        print(name)
    if age:  # if age is not None
        print(age)

    dictlist = []
    for key, value in kwargs.iteritems():
        dictlist.append(value)
    print dictlist


# 1.4.1
from random import randint

def randlist():
    myrandlist = []
    i = 0
    while (i < 10000000):
        myrandlist.append((randint(100,10001)))
        i = i+1

    miniMortgages = lambda myrandlist: filter(lambda x: x < 200, myrandlist)
    mini= miniMortgages(myrandlist)

    print mini

    standardMortgages = lambda myrandlist: filter(lambda x: 200<=x<=467, myrandlist)
    stan = standardMortgages(myrandlist)
    print stan

    jumboMortgages = lambda myrandlist: filter(lambda x: x > 467, myrandlist)
    jumbo = jumboMortgages(myrandlist)
    print jumbo

    # Verify using all
    testmini = lambda mini: 'Mini Mortgage is accurate' if all([x < 200 for x in mini])==True else 'Mini Mortgage is inaccurate'
    print testmini(mini)

    teststandard = lambda stan:'Standard Mortgage is accurate' if all([200<=x <= 467 for x in stan])==True else 'Standard Mortgage is inaccurate'
    print teststandard(stan)

    testjumbo = lambda jumbo:'Jumbo Mortgage is accurate' if all([x > 467 for x in jumbo])==True else 'Jumbo Mortgage is inaccurate'
    print testjumbo(jumbo)


    # verify using any
    testmini1 = lambda mini: 'Mini Mortgage is inaccurate' if any([x >= 200 for x in mini])==True  else 'Mini Mortgage is accurate'
    print testmini1(mini)

    teststandard1 = lambda stan: 'Standard Mortgage is inaccurate' if any([200>x>467 for x in stan])==True else 'Standard Mortgage is accurate'
    print teststandard1(stan)

    testjumbo1 = lambda jumbo:'Jumbo Mortgage is inaccurate' if any([x <= 467 for x in jumbo])==True else 'Jumbo Mortgage is accurate'
    print testjumbo1(jumbo)

    #1.4.2
    if len(myrandlist) == len(mini) + len(stan) + len(jumbo):
        print 'Length of the full list {0} is equal to the sum of the lengths of the three mortgages: {1}+{2}+{3}'.format(
            len(myrandlist), len(mini), len(stan), len(jumbo))
    else:
        print 'Length of the full list {0} is not equal to the sum of the lengths of the three mortgages: {1}+{2}+{3}'.format(
            len(myrandlist), len(mini), len(stan), len(jumbo))


    #1.4.3
    summini = functools.reduce((lambda x, y: x + y), mini)
    print summini
    sumstan = functools.reduce((lambda x, y: x + y), stan)
    print sumstan
    sumjumbo = functools.reduce((lambda x, y: x + y), jumbo)
    print sumjumbo

    #method 1
    totalmort = (lambda x, y, z: x + y + z)(summini,sumstan,sumjumbo)
    print 'Total mortgage amount is: {}'.format(totalmort)

    #method 2
    totalmort = summini+sumstan+sumjumbo
    print totalmort

    #is_max = lambda lst: max(lst)
    #is_min = lambda lst: min(lst)

    # 1.4.4 : Find min/ max of each mortgage type
    minimin= lambda mini: min(mini)
    print minimin(mini)
    minimax = lambda mini: max(mini)
    print minimax(mini)

    stanmin = lambda stan: min(stan)
    print stanmin(stan)
    stanmax = lambda stan: max(stan)
    print stanmax(stan)

    jumbomin = lambda jumbo: min(jumbo)
    print jumbomin(jumbo)
    jumbomax = lambda jumbo: max(jumbo)
    print jumbomax(jumbo)



#1.4.5: Illustrate abs
def meanabs2():
    my_list = []
    i = int(input('Enter the number of values: '))
    l = 0
    while ( l < i and i!='s'):
        my_list.append(raw_input ('Element {0} is (s will terminate the program): '.format((len(l)+1))))
        l = l+1
    print my_list
    sum = 0.0
    # replace this code with lambda reduce
    for i in my_list:
        sum = sum + abs(eval(i))
        print sum
    mean = sum / len(my_list)
    print 'Mean is: {}'.format(mean)


# 1.5 dicts and sets

#1.5.1
players = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'D')
injuredPlayers = ('A', 'B')

noninjuredplayers1= [i for i in players if i not in injuredPlayers]
print set(noninjuredplayers1)

# Benefits: Elements of set are unique and hashable (immutable)

#1.5.2

us = set(['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George', 'Kenneth', 'Steven', 'Edward', 'Brian'])
uk = set(['John', 'William', 'Thomas', 'George', 'James', 'Robert', 'Charles', 'Henry', 'Joseph', 'David', 'Richard', 'Frederick', 'Arthur', 'Edward', 'Albert', 'Alfred', 'Michael', 'Peter', 'Walter', 'Ernest'])

# 1.5.2a : Print the first element in us and uk
for i in us:
    print i
    break
#
for i in uk:
    print i
    break


# 1.5.2b and 1.5.2c
print us.difference(uk)
print uk.difference(us)


def randset():
    myrandset = set()
    i = 0
    while (i < 10000):
        myrandset.add((randint(100,10001)))
        i = i+1
    print myrandset
#1.5.3
def randsetterm():
    myrandset = set()
    i = 0
    while (i < 10000):
        myrandset.add((randint(100,10001)))
        i = i+1
    print myrandset
#1.5.4a
    myrandsetterm = set([10,15,30])
    for j in range(5, 10, 5):
        myrandsetterm.add(j)
    print myrandsetterm
#1.5.4b
    myrandsetterm.remove(15)
    print myrandsetterm
#1.5.4c
    # use discard to remove items ; this does not give the error message if the element isn't found in the set
    myrandsetterm.discard(45)
    print myrandsetterm



# 1.5.5

import collections
def createdict1():

    country = ['UK', 'US', 'IND', 'UK']
    population = [100, 200, 300, 100]

    dict = {country [i]:population[i] for i in range(len(country))}

    enter = raw_input('Enter country name (0 will terminate the program):')
    while (enter!= '0'):
        for index, item in enumerate(country):
            if (item == enter):
                print ('Country {0} has population {1}').format(enter,dict[enter])
                exit(0)


        if (item!=enter):

            print dict

            country.append(raw_input('Unknown country.Please enter the country name:'))
            population.append(input('Enter the population:'))
            dict = {country[i]: population[i] for i in range(len(country))}

            # sort on key: country
            sortkey = collections.OrderedDict(sorted(dict.items(), key=lambda t: t[0]))

            for index in sortkey:
                print 'Country {0} has population  {1}'.format(index, dict[index])

            # sort on value: population with largest first
            sortvalue = collections.OrderedDict(sorted(dict.items(), key = lambda t: t[1], reverse = True))

            for index, value in sortvalue.items():
                print 'Country {0} has population  {1}'.format(index, value)

            exit(0)


#1.5.6

#Method 1 using Counter and most_common
from collections import Counter
my_list = [1,2,2,3, 4,5 ,6,7,7,7,7,7,8,9,9,9,9,9,9,9,9,9,9,9]
# count the items in the list using Counter
mydict = collections.Counter(my_list)
# use most_common to print the mode
for index, value in mydict.most_common(1):
    print 'Mode is {0} with count {1} '.format(index, value)

# Method 2 using Counter and sorted
from collections import Counter
my_list = [1,2,2,3, 4,5 ,6,7,7,7,7,7,8,9,9,9,9,9,9,9,9,9,9,9]
# count the items in the list using Counter
mydict = collections.Counter(my_list)
# sort the dictionary with max count at the top
sortvalue = collections.OrderedDict(sorted(mydict.items(), key = lambda t: t[1], reverse = True))
#print the index corresponding to max count
for index, value in sortvalue.items():
    print 'Mode is: {0}'.format(index)
    break


#1.5.7 and 1.5.8
def randlistext():
    myrandlist = []
    randnum= 100
    i = 0
    while (i < randnum):
        myrandlist.append((randint(100,10001)))
        i = i+1

    miniMortgages = lambda myrandlist: filter(lambda x: x < 200, myrandlist)
    mini= miniMortgages(myrandlist)

    standardMortgages = lambda myrandlist: filter(lambda x: 200<=x<=467, myrandlist)
    stan = standardMortgages(myrandlist)

    jumboMortgages = lambda myrandlist: filter(lambda x: x > 467, myrandlist)
    jumbo = jumboMortgages(myrandlist)

    # create a string of unique ID's
    import string
    import random
    mystring = []
    i = 0
    while (i < randnum):
        lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(6)]
        str = "".join(lst)
        mystring.append(str)
        i = i + 1
    mastermortgage = [mini, stan, jumbo]

    # flatten the mastermortgage and add the unique key to each of the items
    mastermortgageflatten = [list for sublist in mastermortgage for list in sublist]

    # create a dictionary with unique strings
    dict = {mystring[i]: mastermortgageflatten[i] for i in range(len(mastermortgageflatten))}

    mini2= filter(lambda v: v < 200, dict.iteritems())
    stan2= filter(lambda v: 200<= v <=467, dict.iteritems())
    jumbo2 = filter(lambda v: v > 467, dict.iteritems())

    # modify jumbo2: Does the original dict change?
    jumbo2[0]= ('Oomegf', 3439)
    # the original dict will not change on modifying one of the values in jumbo

    # the original dict will not change on modifying one of the values in mini. MiniMortagage list will obviously change.
    mini2.append(('Oxnmgf', 39))


# 1.5.8

    # keys
    print mystring

    # mortgages
    mynewmortgage = []
    randnum = 100
    i = 0
    while (i < randnum):
        mynewmortgage.append((randint(100000, 1000000)))
        i = i + 1

    #rates
    myrandsetrate = []
    for j in range(1, 11, 2):
        myrandsetrate.append(j)
        myrandsetratenew = (myrandsetrate)*20


    # terms are in myrandsetterm
    myrandsetterm = []
    for j in range(1,randnum+1, 1):
        myrandsetterm.append(j)


    # create dictionary with mortgage, rate and term
    dictnew = {mystring[i]: (mynewmortgage[i], myrandsetratenew[i], myrandsetterm[i]) for i in range(len(mynewmortgage))}

    # sort the list by amount in a descending order
    from operator import itemgetter
    sorteddictnew = sorted(dictnew.iteritems(), key=itemgetter(1), reverse= True)

    # WAR(amount/sum(amount))* rate
    summortgage = functools.reduce((lambda x, y: x + y), mynewmortgage)
    war= [(float(value[0] * value[2])/float(summortgage))for key, value in dictnew.iteritems()]

    #WAM amount/sum(amount))* term
    wam= [(float(value[0] * value[1])/float(summortgage))for key, value in dictnew.iteritems()]

    value0list = [value[0] for key, value in dictnew.iteritems()]
    print value0list[0]
    value1list = [value[1] for key, value in dictnew.iteritems()]
    print len(value1list)
    value2list = [value[2] for key, value in dictnew.iteritems()]
    print len(value2list)
    print len(dictnew)

    # new dicionary using the term as key and a list of amount and rate as tuples for easch Term Key.
    dictnew1 = {value1list[i]: (value0list[i], value2list[i]) for i in range(len(dictnew))}
    print dictnew1


