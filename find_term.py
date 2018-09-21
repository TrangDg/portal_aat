import urllib.request
import json

def printResults(data):
	# Load json data
	theJSON = json.loads(data) 

	thisDict = theJSON["identified_by"] 
	
	termSet = set()
	for i in thisDict:
		termSet.add(i["value"]) 

	for x in termSet:
		print (x)


def main():
	urlData = "http://aat-web-services-staging.getty.edu/aat/" + "300011021" + ".json"

	webUrl = urllib.request.urlopen(urlData)
	
	data = webUrl.read()
	printResults(data)

main()
