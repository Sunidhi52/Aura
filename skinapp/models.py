from django.db import models

class NormalSkin(models.Model):
    facewash_name = models.CharField(max_length=200)
    face_image = models.URLField(max_length=500, blank=True, null=True)
    face_link = models.URLField(max_length=500,default='default_value')
    moisturizer_name = models.CharField(max_length=200)
    moisturizer_image = models.URLField(max_length=500, blank=True, null=True)
    moisturizer_link = models.URLField(max_length=500,default='default_value')
    serum_name = models.CharField(max_length=200)
    serum_image = models.URLField(max_length=500, blank=True, null=True)
    serum_link = models.URLField(max_length=500,default='default_value')
    sunscreen_name = models.CharField(max_length=200)
    sunscreen_image = models.URLField(max_length=500, blank=True, null=True)  # Image link field
    sunscreen_link = models.URLField(max_length=500,default='default_value')

    def __str__(self):
        return f"Normal Skin: {self.facewash_name}, {self.moisturizer_name}, {self.serum_name}, {self.sunscreen_name}"


class OilySkin(models.Model):
    facewash_name = models.CharField(max_length=200)
    face_image = models.URLField(max_length=500, blank=True, null=True)
    face_link = models.URLField(max_length=500,default='default_value')
    moisturizer_name = models.CharField(max_length=200)
    moisturizer_image = models.URLField(max_length=500, blank=True, null=True)
    moisturizer_link = models.URLField(max_length=500,default='default_value')
    serum_name = models.CharField(max_length=200)
    serum_image = models.URLField(max_length=500, blank=True, null=True)
    serum_link = models.URLField(max_length=500,default='default_value')
    sunscreen_name = models.CharField(max_length=200)
    sunscreen_image = models.URLField(max_length=500, blank=True, null=True)  # Image link field
    sunscreen_link = models.URLField(max_length=500,default='default_value')

    def __str__(self):
        return f"Oily Skin: {self.facewash_name}, {self.moisturizer_name}, {self.serum_name}, {self.sunscreen_name}"


class DrySkin(models.Model):
    facewash_name = models.CharField(max_length=200)
    face_image = models.URLField(max_length=500, blank=True, null=True)
    face_link = models.URLField(max_length=500,default='default_value')
    moisturizer_name = models.CharField(max_length=200)
    moisturizer_image = models.URLField(max_length=500, blank=True, null=True)
    moisturizer_link = models.URLField(max_length=500,default='default_value')
    serum_name = models.CharField(max_length=200)
    serum_image = models.URLField(max_length=500, blank=True, null=True)
    serum_link = models.URLField(max_length=500,default='default_value')
    sunscreen_name = models.CharField(max_length=200)
    sunscreen_image = models.URLField(max_length=500, blank=True, null=True)  # Image link field
    sunscreen_link = models.URLField(max_length=500,default='default_value')

    def __str__(self):
        return f"Dry Skin: {self.facewash_name}, {self.moisturizer_name}, {self.serum_name}, {self.sunscreen_name}"


class CombinationSkin(models.Model):
    facewash_name = models.CharField(max_length=200)
    face_image = models.URLField(max_length=500, blank=True, null=True)
    face_link = models.URLField(max_length=500,default='default_value')
    moisturizer_name = models.CharField(max_length=200)
    moisturizer_image = models.URLField(max_length=500, blank=True, null=True)
    moisturizer_link = models.URLField(max_length=500,default='default_value')
    serum_name = models.CharField(max_length=200)
    serum_image = models.URLField(max_length=500, blank=True, null=True)
    serum_link = models.URLField(max_length=500,default='default_value')
    sunscreen_name = models.CharField(max_length=200)
    sunscreen_image = models.URLField(max_length=500, blank=True, null=True)  # Image link field
    sunscreen_link = models.URLField(max_length=500,default='default_value')

    def __str__(self):
        return f"Combination Skin: {self.facewash_name}, {self.moisturizer_name}, {self.serum_name}, {self.sunscreen_name}"
    
from django.db import models

class Recommendations(models.Model):
    product_name = models.CharField(max_length=255)
    product_image_url = models.URLField(max_length=500)
    purchase_link = models.URLField(max_length=500)

    def __str__(self):
        return self.product_name
    

class body_Recommendations(models.Model):
    product_name = models.CharField(max_length=255)
    product_image_url = models.URLField(max_length=500)
    purchase_link = models.URLField(max_length=500)

    def _str_(self):
        return self.product_name
    
class HealthcareRecommendations(models.Model):
    product_name = models.CharField(max_length=255)
    product_image_url = models.URLField(max_length=500)
    purchase_link = models.URLField(max_length=500)

def __str__(self):
        return self.product_name