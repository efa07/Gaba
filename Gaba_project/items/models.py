from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_img/',blank=True,null=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price  = models.FloatField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items_img/',blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "items"
        unique_together = ('name', 'category')