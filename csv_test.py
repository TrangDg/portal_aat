import urllib.request
import json
import csv

# def update_sheet(aList):
# 	f = open("update_aat.csv", "w")
# 	w = csv.writer(f)

# 	w.writerow(["Portal term", "AAT ID"])
# 	w.writerow(alist)



def printResults(data, aat_id):
	# Load json data
	theJSON = json.loads(data) 

	thisDict = theJSON["identified_by"] 
	
	termSet = set()
	for i in thisDict:
		termSet.add(i["value"]) 

	
	for x in termSet:
		theList = [aat_id]
		theList.insert(0, x)
		print (theList)



def main():
	f = open("aat_spreadsheet_test.csv", "r")
	r = csv.reader(f)

	next(r) #Skip header

	for row in r:
		aat_id = row[1]
		urlData = "http://aat-web-services-staging.getty.edu/aat/" + aat_id + ".json"

		try:
			webUrl = urllib.request.urlopen(urlData)
			data = webUrl.read()
			printResults(data, aat_id)


			# f = open("update_aat_sheet.csv", "w", newline = "")
			# header = ["Portal term", "AAT ID"]
			# w = csv.DictWriter(f, fieldnames = header)
			# w.writeheader()
			# w.writerow({"Portal term": printResults(data), "AAT ID": str(aat_id)})
		except: 
			print ("URL is not found")

main()