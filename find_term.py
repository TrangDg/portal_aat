import urllib.request
import json

def printResults(data):
	# Load json data
	theJSON = json.loads(data) 


	thisDict = theJSON["identified_by"] 
	termList = [] # Initial term list with duplicates

	for i in thisDict:
		termList.append(i["value"]) #Pulling and putting terms in the list
		

	newList = [] # New list without duplicates

	# Funcion to assign terms to new list without duplicates
	for val in termList:
		if val not in newList:
			newList.append(val)

	# newList.sort() # Sort by alphabetical order

	for i in newList:
		print (i)


def main():
	urlData = "http://aat-web-services-staging.getty.edu/aat/300011021.json"

	webUrl = urllib.request.urlopen(urlData)
	
	data = webUrl.read()
	printResults(data)

main()
