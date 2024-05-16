from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    #logo = models.ImageField(upload_to= 'caminho/do/diretorio/') needs to be implemetad
    institutional_email = models.EmailField(max_length=50)
    personal_page_link = models.URLField(max_length=200)
    # subcategory_key = models.ForeingKey(Subcategory,  on_delete=models.CASCADE)
    # has to be implemented after subcategory model been created
