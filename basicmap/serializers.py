import ast
import json
from rest_framework import serializers

from .models import WashroomData

class WashroomDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashroomData
        fields = ('opendata_id', 'geojson', 'date_updated',)

    def to_representation(self, instance):
        # print('[serializers.to_representation]') 
        # print(type(instance)) <class 'basicmap.models.Washroomdata'

        representation = super().to_representation(instance)

        try:
            representation['geojson'] = ast.literal_eval(representation['geojson'])
            representation['geojson']['geometry'] = \
                ast.literal_eval(representation['geojson']['geometry'])
            # Flip to keep consistent with leaflet representation
            representation['geojson']['geometry']['coordinates'][0], representation['geojson']['geometry']['coordinates'][1] = \
    	        representation['geojson']['geometry']['coordinates'][1], representation['geojson']['geometry']['coordinates'][0]
        except SyntaxError as e:
            print('Error decoding into Python dict:')
            print(e)
            print(representation['geojson'])

        return representation

