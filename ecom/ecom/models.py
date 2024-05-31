from django.db import models

class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    password=models.CharField( max_length=255)
    # shipping_address=models.TextField()
    # billing_address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    default_shipping_address=models.ForeignKey(
        "Shipping_Address",
        on_delete=models.DO_NOTHING,
        null=True,
        related_query_name='user_info')

    def __str__(self) -> str:
        return self.name
    

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    zip_code=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    #should we create a Address class abstract or should we create a seperate Table for that
    class Meta:
        abstract=True

class Shipping_Address(Address):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shipping_address"
    )