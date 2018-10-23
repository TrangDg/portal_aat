import terms_update

logging.basicConfig(level=os.environ.get('LOG_LEVEL').upper())

terms_update.update(filename="aat_update.csv", 
					url = "http://aat-web-services-staging.getty.edu/aat/")



