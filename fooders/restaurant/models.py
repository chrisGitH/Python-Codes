from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    logo = models.ImageField(upload_to='restaurant_images')
    food_category = models.ForeignKey(FoodCategory)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    google_location_lat = models.FloatField()
    google_location_long = models.FloatField()
    restaurant = models.ForeignKey(Restaurant)

    def __unicode__(self):
        return self.name
