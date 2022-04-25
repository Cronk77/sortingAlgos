#Note: Sorting string values will not be case senstive in all sorting algorithms
#Note: Sorting alphanumeric values in combination will sort the numbers first and numbers will
#      be sorted based on values of characters left to right not value of literal number,
#      although if all numbers are handed to the sorting algorithms then it sorts them by literal
#      number values

import numpy as np
import datetime as dt
import re
from numpy import random
from os.path import exists


#Main___________________________________________________________________________________________________
def main():
    #Menu() call
    menu()

#Menu___________________________________________________________________________________________________
def menu():
    menuOptions = {
        1: 'Random Integers',
        2: 'Sorting Algorithm comparison based on .txt file given with Time Cost analysis',
        3: 'Sort .txt file alphanumericly into \'outputSorted.txt\' file',
        4: 'Sort content of file alphanumerically to \'outputSortedAndCounted.txt\' file with counted words',
        5: 'Exit'
    }

    while(True):
        printMenu(menuOptions)
        option = ''
        try:
            option = int(input('Please select an option: '))

        except:
            print('Incorrect option inputed, please enter a valid number...')

        if option == 1:
            option1()
                  
        elif option == 2:
            option2()

        elif option == 3:
            option3()

        elif option == 4:
            option4()

        elif option == 5:
            print('\nThank you for using SortingAlgos!!!!!!\n')
            exit()

        else:
            print('Invalid option, Enter an number a number between 1 and 5.')
            
    
#Printing the menu______________________________________________________________________________________       
def printMenu(options):
    for key in options.keys():
        print(key, '--', options[key])

#Option 1: Random Integars______________________________________________________________________________
def option1():
    x = int(input("Enter a integer that is the number of random integers (0-100) that will be sorted: "))
    arr = np.random.randint(100, size=(x))

    print(arr)
    
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    
    aMerge = dt.datetime.now()
    merge_sort(arr1)
    bMerge = dt.datetime.now()
    cMerge = bMerge - aMerge
    secondsMerge = cMerge.total_seconds()
    print('\nMerge Sort time cost is: ', secondsMerge, ' seconds')
    #print(arr1)

    aQuick = dt.datetime.now()
    quickSort(arr2)
    bQuick = dt.datetime.now()
    cQuick = bQuick - aQuick
    secondsQuick = cQuick.total_seconds()
    print('Quick Sort time cost is: ', secondsQuick, ' seconds')
    #print(arr2)

    aBubble = dt.datetime.now()
    bubbleSort(arr3)
    bBubble = dt.datetime.now()
    cBubble = bBubble - aBubble
    secondsBubble = cBubble.total_seconds()
    print('Bubble Sort time cost is: ', secondsBubble, ' seconds')
    #print(arr3)

    aInsertion = dt.datetime.now()
    insertionSort(arr4)
    bInsertion = dt.datetime.now()
    cInsertion = bInsertion - aInsertion
    secondsInsertion = cInsertion.total_seconds()
    print('Insertion Sort time cost is: ', secondsInsertion, ' seconds')
    #print(arr4)

    aSelection = dt.datetime.now()
    selectionSort(arr5)
    bSelection = dt.datetime.now()
    cSelection = bSelection - aSelection
    secondsSelection = cSelection.total_seconds()
    print('Selection Sort time cost is: ', secondsSelection, ' seconds')
    #print(arr5)

    print('\nThe sorted list is:\n', arr1,'\n\n')

    


#Option 2: Sorting Algos comparison and time cost_______________________________________________________
def option2():
    list1 = readFile()

    if len(list1) < 1000:
        print(list1)
    
    list2 = list1.copy()
    list3 = list1.copy()
    list4 = list1.copy()
    list5 = list1.copy()
    list6 = list1.copy()
    
    aMerge = dt.datetime.now()
    merge_sort(list2)
    bMerge = dt.datetime.now()
    cMerge = bMerge - aMerge
    secondsMerge = cMerge.total_seconds()
    print('\nMerge Sort time cost is: ', secondsMerge, ' seconds')
    #print(list2)
    
    aQuick = dt.datetime.now()
    quickSort(list3)
    bQuick = dt.datetime.now()
    cQuick = bQuick - aQuick
    secondsQuick = cQuick.total_seconds()
    print('Quick Sort time cost is: ', secondsQuick, ' seconds')
    #print(list3)
    
    
    
    aBubble = dt.datetime.now()
    bubbleSort(list4)
    bBubble = dt.datetime.now()
    cBubble = bBubble - aBubble
    secondsBubble = cBubble.total_seconds()
    print('Bubble Sort time cost is: ', secondsBubble, ' seconds')
    #print(list4)
    

    
    aInsertion = dt.datetime.now()
    insertionSort(list5)
    bInsertion = dt.datetime.now()
    cInsertion = bInsertion - aInsertion
    secondsInsertion = cInsertion.total_seconds()
    print('Insertion Sort time cost is: ', secondsInsertion, ' seconds')
    #print(list5)
    

    aSelection = dt.datetime.now()
    selectionSort(list6)
    bSelection = dt.datetime.now()
    cSelection = bSelection - aSelection
    secondsSelection = cSelection.total_seconds()
    print('Selection Sort time cost is: ', secondsSelection, ' seconds\n')
    #print(list6)

    if len(list2) < 1000:
        print(list2, '\n')

#Option 3: Sort File into an output .txt file__________________________________________________________
def option3():
    outputFile = './outputSorted.txt'

    list1 = readFile()
    merge_sort(list1)
    writeFile(list1, outputFile)

    print('\nThe file outputSorted.txt has the file items in alphanumeric order\n')

#Option 4: Sort given file into output file with word count____________________________________________
def option4():
    outputFile = 'outputSortedAndCounted.txt'

    list1 = readFile()
    merge_sort(list1)

    words = []
    countList = []

    #checks to see how many of the same word, regaurdless of case, there are, and puts
    #   every unique word in words, and has its corresponding count within countList
    #   at the same index as that unique word. Words is also sorted.
    for i in list1:
        check = False
        for j in words:
            if j.lower() == i.lower():
                check = True
        if check == False:
            wordCount = 0
            for k in list1:
                if k.lower() == i.lower():
                    wordCount = wordCount + 1
            words.append(i)
            countList.append(str(wordCount))

    #print(words)
    #print(countList)

    #combine the unique words and their counts together into another list
    combinedWordAndCount = []
    for c in range(0, len(words)):
        temp = words[c] + ' : ' + countList[c]
        combinedWordAndCount.append(temp)

    #print(combinedWordAndCount)
    writeFile(combinedWordAndCount, outputFile)

    print('\nThe file outputSortedAndCounted.txt has the file items in alphanumeric order and has each unique word counted\n')

    numTotalWords = len(list1)

    numUniqueWords = len(words)

    print('The total number of words in the file: ', numTotalWords)
    print('The total number of unique words in the file: ', numUniqueWords, '\n')
    
        
#Read file and input into a list_______________________________________________________________________
def readFile():
    list1 = []
    path = input('Please enter the path of the file you\'d like to read from: ')

    existsBool = exists(path)
    while existsBool == False:
        path = input('Incorrect path of input file, please enter correct path: ')
        existsBool = exists(path)
        
    with open(path, 'r') as f:
        for line in f:
            for word in line.split():
                filteredWord = re.sub(r'[^\w\s]', '',word)#used regex to filter out
                                                          #   the characters that do not belong in words
                list1.append(filteredWord)
    return list1

#write to file from list________________________________________________________________________________
def writeFile(list1, outputFile):
    path = open(outputFile, 'w')
    for i in list1:
        path.write(i + '\n')
    path.close()
    
#Merge Sort Algo_________________________________________________________________________________________
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2].copy()#all elements up to half the length of the arr(slicing array)
        right_arr = arr[len(arr)//2:].copy()# all elements from half the lengthof the array to end of arr
        
        #recurisive step
        merge_sort(left_arr)
        merge_sort(right_arr)

        #implimentation of the merge
        i = 0 #left arr index
        j = 0 #right arr index
        k = 0 # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if isinstance(left_arr[i], np.int64) == True:# if data type is int
                #print(type(left_arr[i]))# checks the Type thats being passed in
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
            else:# if data type is string
                if left_arr[i].lower() <= right_arr[j].lower():
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
                
 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr

#Quick Sort_______________________________________________________________________________________________
def quickSort(arr):
    arrLength = len(arr)

    if arrLength < 2:
        return arr

    curr_pos = 0

    for i in range(1, arrLength):
        if isinstance(arr[i], np.int64) == True:# if data type is int
            if arr[i] <= arr[0]:
                curr_pos += 1
                temp = arr[i]
                arr[i] = arr[curr_pos]
                arr[curr_pos] = temp

                
        else:# if data type is string
            if arr[i].lower() <= arr[0].lower():
                curr_pos += 1
                temp = arr[i]
                arr[i] = arr[curr_pos]
                arr[curr_pos] = temp

            
    temp = arr[0]
    arr[0] = arr[curr_pos]
    arr[curr_pos] = temp

    left_arr = quickSort(arr[0:curr_pos])
    right_arr = quickSort(arr[curr_pos+1: arrLength])

    arr = left_arr + [arr[curr_pos]] + right_arr

    return arr

#Bubble Sort______________________________________________________________________________________________
def bubbleSort(arr):
    arrLength = len(arr)

    for i in range(arrLength-1):
        for j in range(0, arrLength-i-1):
            if isinstance(arr[j], np.int64) == True:# if data type is int
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
            else:# if data type is string
                if arr[j].lower() > arr[j+1].lower():
                    arr[j], arr[j+1] = arr[j+1] , arr[j]

    return arr
            

#Insertion Sort___________________________________________________________________________________________
def insertionSort(arr):
    arrLength = len(arr)
    for i in range(1, arrLength):
        temp = arr[i]
        j = i - 1
        if isinstance(arr[j], np.int64) == True:# if data type is int
            while j >= 0  and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        else:# if data type is string
            while j >= 0  and temp.lower() < arr[j].lower():
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = temp

    return arr

#Selection Sort___________________________________________________________________________________________
def selectionSort(arr):
    arrLength = len(arr)

    for i in range(arrLength):
        minIndex = i
        for j in range(i+1, arrLength):
            if isinstance(arr[j], np.int64) == True:# if data type is int
                if arr[minIndex] > arr[j]:
                    minIndex = j
            else:# if data type is string
                if arr[minIndex].lower() > arr[j]:
                    minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr

##########################################################################################################
if __name__ == "__main__":
    main()
                      

