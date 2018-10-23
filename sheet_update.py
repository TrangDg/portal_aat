import requests
import csv
import logging
import os 


logging.basicConfig(level=os.environ.get('LOG_LEVEL', 'INFO').upper())
	

def read():
	f = open("aat_update.csv", "r")
	r = csv.reader(f)

	next(r) #Skip header
	
	
	id_list = [] #create a list of AAT ID
	all_the_terms = []
	
	for row in r:
		aat_id = row[1]
		# Condition to check whether id has already existed
		# If not, add id to the id_list and run the rest
		if aat_id not in id_list:
			id_list.append(aat_id)  
			url = "http://aat-web-services-staging.getty.edu/aat/" + aat_id + ".json"

			try:
				webUrl = requests.get(url, timeout=1)
				logging.info("URL works")
			except: 
				# print ("URL is not found:", aat_id)
				logging.warning("CANNOT open URL: %s", aat_id)
				continue

			data = webUrl.json()
			
			termSet = set()
			for i in data["identified_by"]:
				termSet.add(i["value"])

			
			for x in termSet:
				theList = (x,aat_id)
				all_the_terms.append(theList)

	return all_the_terms
		

termList = read()

def aatUpdate():
	f = open("aat_update.csv", "w", encoding='utf-8')
	w = csv.writer(f)
	w.writerow(["Portal term", "AAT ID"])
	
	w.writerows(termList)

	f.close()

aatUpdate()



