# Toronto Open Data Backend

This project uses a React frontend and Django backend to visualize geographical data provided by the city of Toronto. The backend serves the API for the frontend at the endpoint /api/. <br>

Works on Chrome and Firefox desktop.

- Website Link: [http://35.183.91.143/](http://35.183.91.143/) (currently no domain name)
- Frontend Repository: [https://github.com/zhanggq96/TorontoOpenData](https://github.com/zhanggq96/TorontoOpenData)
- Backend Repository: [https://github.com/zhanggq96/TorontoOpenDataBackend](https://github.com/zhanggq96/TorontoOpenDataBackend)
- Toronto Open Data Site: [https://www.toronto.ca/city-government/data-research-maps/open-data/](https://www.toronto.ca/city-government/data-research-maps/open-data/)


## Information

The site is hosted on an instance of Amazon Lightsail. Data is fetched from Toronto's open data api to populate an SQLite database, with plans to migrate to MongoDB in the future as the latest version of Amazon Linux (July 2023) does not support MongoDB. See the frontend repository for information about the frontend.

Currently, only the [washroom facilities](https://open.toronto.ca/dataset/washroom-facilities/) dataset is supported.

## Backend Dependencies

<ul>
  <li>Django==3.2.18</li>
  <li>djangorestframework==3.14.0</li>
  <li>django-cors-headers==4.1.0</li>
  <li>requests</li>
</ul> 

## API format for Map Data

The main portion of this API follows the API provided by the City of Toronto. Example of format using one facility:

    {
        "data": [
            {
                "type": "WashroomData",
                "id": "1",
                "attributes":{
                    "opendata_id":"1",
                    "geojson":{
                        "_id": 1,
                        "id": 774,
                        "asset_id": 80165,
                        "location": "Wenderly Park",
                        "alternative_name": "Wenderly Park Baseball Diamond Bottle Filling Station",
                        "type": "Bottle Filling Station",
                        "accessible": "",
                        "hours": "None",
                        "location_details": "Located north of the baseball diamond along the pathway.",
                        "url":"https://www.toronto.ca/data/parks/prd/facilities/complex/774/index.html",
                        "address": "89 Wenderly Dr",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                43.7119805089016, # Lat
                                -79.4461230209045 # Long
                            ]
                        }
                    },
                    "date_updated":"14/07/2023 10:02:17"
                }
            },
        ]
    }
