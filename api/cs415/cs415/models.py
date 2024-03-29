from django.db import models


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    quantity = models.IntegerField()
    package = models.ForeignKey('Package', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cart'

    def __str__(self):
        return f'{self.quantity}'

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Orders'

    def __str__(self):
        return f'{self.order_date}'
    
class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    base_price = models.IntegerField()
    max_photos = models.IntegerField()
    package_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Package'

    def __str__(self):
        return f'{self.package_name}'
    
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    type = models.ForeignKey('Paymenttype', models.DO_NOTHING)
    payment_amount = models.IntegerField()
    payment_status = models.CharField(max_length=30, blank=True, null=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Payment'

    def __str__(self):
        return f'{self.payment_amount} {self.payment_status}'

class Paymenttype(models.Model):
    type_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PaymentType'

    def __str__(self):
        return f'{self.payment_type}'

class Useraccount(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    pass_word = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.BigIntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserAccount'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Userprofile(models.Model):
    user_profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Useraccount, models.DO_NOTHING)
    profile_picture = models.CharField(max_length=50, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserProfile'

    def __str__(self):
        return f'{self.profile_picture}'

