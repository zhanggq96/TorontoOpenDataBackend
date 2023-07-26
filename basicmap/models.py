from django.db import models

# Create your models here.

class WashroomData(models.Model):
    geojson = models.TextField()
    date_updated = models.TextField()
    
    opendata_id = models.TextField(primary_key=True)
    parent_id = models.TextField()
    asset_id = models.TextField()
    alternative_name = models.TextField()
    washroom_type = models.TextField()
    accessible = models.TextField() 
    hours = models.TextField()
    location_details = models.TextField()
    url = models.TextField()
    address = models.TextField()
    geometry = models.TextField()
    
    def __str__(self):
        return f'{self.opendata_id}/{self.parent_id}: {self.alternative_name}'
