import os
import filecmp
import csv
#from dateutil.relativedelta import *
#Gives Error "No module named 'dateutil'"
from datetime import date


def getData(file):
        inFile = open(file, 'r')
        topLine = inFile.readline()
        readLines = inFile.readlines()
        topList = topLine.split(',')
        newList = []
        inFile.close()

        for x in readLines[0:]:
                d = {}
                split = x.split(',')
                d[topList[0]] = split[0]
                d[topList[1]] = split[1]
                d[topList[2]] = split[2]
                d[topList[3]] = split[3]
                d[topList[4].strip()] = split[4].strip()

                if d not in newList:
                        newList.append(d)

        return newList

def mySort(data,col):
        sortedList = sorted(data, key = lambda x: x[col])

        for y in range(1):
                current = sortedList[y]
                return(current["First"] + " " + current["Last"])

def classSizes(data):
        classList = []

        seniorCount = 0
        juniorCount = 0
        sophomoreCount = 0
        freshmanCount = 0

        for x in data:
                if x["Class"] == "Senior":
                        seniorCount += 1
                if x["Class"] == "Junior":
                        juniorCount += 1
                if x["Class"] == "Sophomore":
                        sophomoreCount += 1
                if x["Class"] == "Freshman":
                        freshmanCount += 1

        classList.append(("Senior", seniorCount))
        classList.append(("Junior", juniorCount))
        classList.append(("Sophomore", sophomoreCount))
        classList.append(("Freshman", freshmanCount))

        return(sorted(classList, key=lambda x: x[1], reverse = True))

def findMonth(a):
        d = {}

        for x in a:
                if x['DOB'].split('/')[0] in d:
                        d[x['DOB'].split('/')[0]] += 1

                elif x['DOB'].split('/')[0] not in d:
                        d[x['DOB'].split('/')[0]] = 1

        d_sorted = sorted(d.items(), key=lambda x: x[1], reverse = True)

        return(int(d_sorted[0][0]))
                        
def mySortPrint(a,col,fileName):
        outFile = open(str(fileName),"w")
        
        x = sorted(a, key = lambda x: x[str(col)])
        
        for name in x:
                first = name["First"]
                last = name["Last"]
                email = name["Email"]
                outFile.write(first + "," + last + "," + email + "\n")
        outFile.close()

def findAge(a):
        current_year = int(2018)
        total_ages = 0
        num_of_people = 0
        
        for x in a:
                num_of_people+=1
                dob = x["DOB"]
                dob_split = dob.split('/')
                dob_year= dob_split[2]
                age = int(current_year - int(dob_year))
                total_ages+= age
                
        return(int(total_ages/num_of_people))

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
