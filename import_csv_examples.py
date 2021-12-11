import csv
import random

file = open("cyber_security_terms.csv")
csv_reader = csv.reader(file)

# Note: Data is read from a 'csv' file and generates a 'data' object 
# in the form of a "list of lists" (ex. table with rows of lists).
data = []
for row in csv_reader:
    data.append(row)

# GLOBAL VARIABLES
rowCount = len(data)
answerOptionsCount = 4
dataIndexList = list(range(0, rowCount-1))
searchIndex = -1

print()

print()
print("Number of rows in data: ", rowCount)

print()
searchTerm = "IP Address"
searchIndex = -1
for row in data:
    searchIndex += 1
    if searchTerm in row: # Find first instance of search criteria
        searchResults = str(row)
        break
print("Search results (term = '" + searchTerm + "'): " + searchResults)

print()
print("Search index: " + str(searchIndex))

print()
print("Cell value ('Term'): '" + data[searchIndex][0] + "'")
print("Cell value ('Definition'): '" + data[searchIndex][1] + "'")

print()
# answerOptionsList = random.choices(dataIndexList, k = answerOptionsCount) # allows for duplicates
answerOptionsList = random.sample(dataIndexList, answerOptionsCount) # does not allow for duplicates
print("Random answer (index) list: " + str(answerOptionsList))

print()
