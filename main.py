import scraper
import pandas as pd
import boto3

start_page = 1
number_of_page = 1

collections = scraper.main(start_page, number_of_page)

collection_dictionaries = list(map(lambda collection: collection.to_dict(), collections))
collections_df = pd.DataFrame(collection_dictionaries)
collections_df.head()
collections_df.to_csv('csvs/Collections.csv')




