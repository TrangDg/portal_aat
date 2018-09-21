import urllib.request
import json
import csv

def main():
	f = open("aat_spreadsheet_test.csv", "r")
	r = csv.reader(f)

	next(r) #Skip header

	for row in r:
		aat_id = row[1]
		urlData = "http://aat-web-services-staging.getty.edu/aat/" + aat_id + ".json"

		try:
			webUrl = urllib.request.urlopen(urlData)
		except: 
			print ("URL is not found", aat_id)
			continue

		data = webUrl.read()

		theJSON = json.loads(data)
		thisDict = theJSON["identified_by"]

		termSet = set()
		for i in thisDict:
			termSet.add(i["value"])

		all_the_terms = []
		for x in termSet:
			theList = (aat_id,x)
			all_the_terms.append(theList)
			# yield (theList)

		return all_the_terms
		

termList = main()

def aatUpdate():
	f = open("aat_update.csv", "w")
	w = csv.writer(f)

	w.writerow(["Portal term", "AAT ID"])
	w.writerows(termList)

	f.close()

aatUpdate()



