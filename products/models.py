from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='products/categories', default=None, null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta: 
        verbose_name = '1. Category'



class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = '2. Subcategory'

class Type(models.Model):
    subcategory= models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)


    # def __str__(self):
    #     return self.title

    def __str__(self):
        return f'{self.subcategory.category}-{self.subcategory}-{self.title}'

    class Meta: 
        verbose_name = '3. Type'

class Brand(models.Model):
     title = models.CharField(max_length=255)
     caption = models.CharField(max_length=255)

     def __str__(self):
         return self.title

     class Meta: 
        verbose_name = '4. Brand'

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    price = models.FloatField()
    stock = models.IntegerField()
    discount = models.FloatField(default=0)
    status= models.BooleanField()
    details = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank = True)
    specification = models.TextField(null=True, blank= True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = '5. Product'
