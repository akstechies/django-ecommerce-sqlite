from django.db import models
import uuid
import os
from user_cart.models import CartItem

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def product_image_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = str(uuid.uuid4())
    return f"product_images/{unique_id}.{extension}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=product_image_upload_path)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
    def delete_image(self):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
            self.image.delete(save=False)

    def delete_old_image(self, old_image):
        if os.path.isfile(old_image):
            os.remove(old_image)
