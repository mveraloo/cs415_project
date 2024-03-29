from rest_framework import serializers
from cs415.models import Cart, Orders, Package, Payment, Paymenttype, Useraccount, Userprofile

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymenttypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymenttype
        fields = '__all__'

class UseraccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraccount
        fields = '__all__'

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'



