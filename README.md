# Toronto Open Data Backend

Backend for open data visualization. The backend serves the API for the frontend at the endpoint /api/.
Link: http://35.183.91.143/ (currently no domain name)
Frontend Repository: https://github.com/zhanggq96/TorontoOpenData

## Information

This project uses a Django backend and a React frontend to visualize geographical data provided by the city of toronto. Leaflet is used to generate the map. Currently, only the [washroom facilities](https://open.toronto.ca/dataset/washroom-facilities/) dataset is supported with plans to expand in the future.

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
                                43.7119805089016,
                                -79.4461230209045
                            ]
                        }
                    },
                    "date_updated":"14/07/2023 10:02:17"
                }
            },
        ]
    }
