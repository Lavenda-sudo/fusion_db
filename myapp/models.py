from django.db import models
import uuid

def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]  # jane.png -> png
    newfilename = f'{uuid.uuid4()}.{ext}'
    return f'products/{newfilename}'
CATEGORIES = [
    ('Food', 'Food Category'),
    ('Drinks', 'Drinks Category'),
    ('Cleaning', 'Cleaning Category'),
    ('Hardware', 'Hardware Category'),

]
class Products(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount= models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices =CATEGORIES)
    pic = models.ImageField(upload_to=gen_unique_path, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

# Run migrations
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# Love 37020227