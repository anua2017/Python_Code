import time
from Assignment1functions.myLists import mean2,inputlst2, inputlst3, inputlst4, inputlst4a, inputlst5, inputlst6, inputlst7, inputlst8, inputlst9, inputlst10, inputlst11, inputlst12
from Assignment1functions.myLists import evens, odds, finallst, squarelst
from Assignment1functions.myLists import evenlst, squarelst1, noninjuredplayers, nameagelst, nameagelst1, nameandage, dictlist, divisionbyten, divisionbyten1, deltatime, deltatime1, flattenedlist
from Assignment1functions.myLists import argsMean, funaverage, funvar, funvar1, argsMeanlst, kwargsa, kwargsd, kwargsd1
from random import randint
from Assignment1functions.myLists import randlist, meanabs2, noninjuredplayers, us, uk, randset, randsetterm, createdict1

#randlis, miniMortgages, myrandlist, standardMortgages, jumboMortgages, testmini, teststandard, testjumbo
# miniMortgages1

def main():
    #1.2.1a, 1.2.1b
    mean2()

    #1.2.2a,1.2.2b,1.2.2c,1.2.2d,1.2.2e,1.2.2f,1.2.2g,1.2.2h,1.2.2i,1.2.2j,1.2.2k,1.2.2l
    #inputlst2()
    #inputlst3()
    #inputlst4()
    #inputlst4a()
    #inputlst5()
    #inputlst6()
    #inputlst7()
    #inputlst8()
    #inputlst9()
    #inputlst10()
    #inputlst11()
    #inputlst12()

    # 1.2.3
    #print evens(range(1000))
    #1.2.4
    #print odds(range(1000))
    #1.2.5
    #print (evens(range(1000)) + odds(range(1000)))

    # check that the combined list of odds and evens contains odd and even numbers
    #lstoddeven = (evens(range(1000)) + odds(range(1000)))
    #for i in lstoddeven:
        #print i == 1
    #1.2.6
    #lstoddeven = (evens(range(1000)) + odds(range(1000)))
    #lstoddeven.reverse()
    # check that the combined list of odds and evens contains odd and even numbers
    #print lstoddeven
    #for i in lstoddeven:
        #print i == 4

    #1.2.7a
    # print(finallst(squarelst))
    #1.2.7b
    #print(evenlst(squarelst1))
    #print(finallst1(squarelst))

    #1.2.8
    #print(noninjuredplayers)

    # 1.2.9a, 1.2.9b
    #print nameagelst
    #print nameagelst1
    #print dictlist
    #print type(dictlist)# list

    # 1.2.10a, 1.2.10b
    #divisionbyten(range(10000000))
    #divisionbyten1(range(10000000))


    #1.2.11
    #print flattenedlist

    #1.3.1
    #print weekd
    #print weekd1(weekdays)

    # 1.3.3
    #my_list = [1, 4, 5, 10, 12]
    #funaverage(my_list)
    #print(average)

    #1.3.4, 1.3.5
    #funvar(funaverage(my_list), my_list, 0)
    #funvar(funaverage(my_list), my_list)
    #funvar1(funaverage(my_list), my_list)

    # 1.3.6
    #argsMean(1.3,4.5, 6.7, 11.2, 100, 987.6)
    #lst = [1.3,4.5, 6.7, 11.2, 100, 987.6]
    #argsMeanlst(lst)

    # 1.3.7
    #kwargsa('C', State='MT', Height = 171, Weight = 80, hairColor = 'Black')
    #kwargsa('C', 12, Height = 171, Weight = 80, hairColor = 'Black')
    #kwargsa(State='MT', Height=171, Weight=80, hairColor='Black')
    #1.3.8
    #kwargsd(State='MT', Height=171, Weight=80, hairColor='Black')
    #kwargsd1(State='MT', Height=171, Weight=80, hairColor='Black')


    # 1.4
    # 1,2,3,4

    #1.4.1
    #randlist()
    # 1.4.5
    #meanabs2()

    #1.5.1
    #print set(noninjuredplayers1)

    #1.5.4
    #randsetterm()

    #1.5.5
    #createdict1()

    #1.5.6
    #randlistext()

if __name__ == "__main__":
    import sys
    main()
