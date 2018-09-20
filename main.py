import urllib.request

def main():

	urlData = "http://aat-web-services-staging.getty.edu/aat/300011021.json"

	webUrl = urllib.request.urlopen(urlData)
	print ("result code: " + str(webUrl.getcode()))

main()
