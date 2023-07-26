import os
import requests 
import json
from datetime import datetime
import sqlite3
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torontodata.settings')
django.setup()

from basicmap.models import WashroomData


def store_geojson():
    # To hit our API, you'll be making requests to:
    base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
    
    # Datasets are called "packages". Each package can contain many "resources"
    # To retrieve the metadata for this package and its resources, use the package name in this page's URL:
    
    url = base_url + "/api/3/action/package_show"
    params = {"id": "washroom-facilities"}
    package = requests.get(url, params=params).json()

    for idx, resource in enumerate(package["result"]["resources"]):
        if resource["datastore_active"]:
            url = base_url + "/datastore/dump/" + resource["id"]
            resource_dump_data = requests.get(url).text

            # To selectively pull records and attribute-level metadata:
            url = base_url + "/api/3/action/datastore_search"
            p = {'id': resource['id'], 'limit': 500 }
            resource_search_data = requests.get(url, params = p).json()["result"]
            for i, record in enumerate(resource_search_data['records']):
                datapoint = WashroomData(
                    geojson = record,
                    date_updated = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    parent_id = record['id'],
                    opendata_id = record['_id'],
                    asset_id = record['asset_id'],
                    alternative_name = record['alternative_name'],
                    washroom_type = record['type'],
                    accessible = record['accessible'],
                    hours = record['hours'],
                    location_details = record['location_details'],
                    url = record['url'],
                    address = record['address'],
                    geometry = record['geometry'],
                )
                datapoint.save()
                print('Storing record:')
                print(datapoint.opendata_id, datapoint.asset_id)
                # break

        # break

if __name__ == '__main__':
    store_geojson()
    
    