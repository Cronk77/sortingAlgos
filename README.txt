Motivation: It has been a while since I touched python and in order to refresh on syntax and usability of python i decided to create this program. I also wanted to test the abilites of well know sorting algorithms in python with regaurds to how much data it can take and the time cost involved for each algorithm. I was also intrested in being able to take a text file and strip the contents, sort it, and find out data about that file such as how many words they used or how many unique words each has. Potentially I could take a book and find out the words they used and how many of each word there were.

Future add ons: Add an option for a .txt file filled with Create a GUI; Handle some stress testing and exceptions; Import some panda and do some statistical analysis of data mining on the conent of the .txt files;

How to Run: This program is a python console program. To use this program you will need to ensure you have python3 and pip3 installed on the machine you're using. Go the the directory where this program is held. To run: python3 SortingAlgos.py This will display a menu option 1-5.

option 1: The console will prompt the user to enter in the number of random integars they want to see sorted by the 5 diffrent algorithms and the time cost involved in them. These algorithms include Merge Sort, Quick Sort, Bubble Sort, Insertion Sort, and Selection Sort. The contents of the array of random numbers will be printed to the screen and once merged, the sorted version will also be printed to the screen.

option 2: The console will prompt the user to enter a path to a .txt file to be read in. The contents of the .txt file will then be stripped into a list and sorted based on the 5 sorting algorithms, as well as the time cost of each involved.

option 3: The console will prompt the user to enter a path to a .txt file to be read in. The contents will be sorted and sent to a file called outputSorted.txt located in the same direcetory as the SortingAlgos.py file.

option 4: The console will prompt the user to enter a path to a .txt file to be read in. The contents of the file will be sorted. The program will then strip the unique words out of the file and the number of each unique words and print those together in a file called outputSortedAndCounted.txt. The Console will the print out how many total words were in the original file and the number of unique words.

option 5: The program will end with a departing message.

Note: The sorting is done in a non case senstive instance. Note: Sorting alphanumeric values in combination will sort the numbers first and numbers will be sorted based on values of characters left to right not value of literal number, although if all numbers are handed to the sorting algorithms then it sorts them by literal number values.
