from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount= models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

# Run migrations
# python manage.py makemigrations
# python manage.py migrate