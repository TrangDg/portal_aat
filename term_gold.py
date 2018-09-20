import urllib.request
import json

def printResults(data):
	theJSON = json.loads(data)

	label = theJSON.get("label")
	print ("The concept is: " + label)

	print ("Other terms are:")
	for i in theJSON["identified_by"]:
		alt_term = i["value"]
		print (alt_term)






def main():
	urlData = "http://aat-web-services-staging.getty.edu/aat/300011021.json"

	webUrl = urllib.request.urlopen(urlData)
	
	data = webUrl.read()
	printResults(data)

main()