import requests
import csv
import logging
import os 

def update(filename, url):
	

	f = open(filename, "r")
	rdr = csv.reader(f)

	next(rdr) #Skip header
	
	
	id_list = [] #create a list of AAT ID
	all_the_terms = []
	
	# Processing API and extracting alternate terms
	for row in rdr:
		aat_id = row[1]
		# Check whether id has already existed
		# if not, add id to the id_list and run the rest
		if aat_id not in id_list:
			id_list.append(aat_id)  
			uri = url+aat_id+".json"

			try:
				rq = requests.get(uri, timeout=1)
				logging.info("Processing AAT_ID: %s", aat_id)
			except: 
				logging.warning("CANNOT load API for AAT_ID: %s", aat_id)
				continue

			data = rq.json()
			
			termSet = set()
			for i in data["identified_by"]:
				termSet.add(i["value"])

			
			for x in termSet:
				r = (x,aat_id)
				all_the_terms.append(r)

	# Write csv file 
	fn = open(filename, "w", encoding='utf-8-sig')
	w = csv.writer(fn)
	w.writerow(["Portal term", "AAT ID"])
	
	w.writerows(all_the_terms)

	fn.close()
	




