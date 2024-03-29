from django.contrib import admin
from .models import Cart, Orders, Package, Payment, Paymenttype, Useraccount, Userprofile

admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Package)
admin.site.register(Payment)
admin.site.register(Paymenttype)
admin.site.register(Useraccount)
admin.site.register(Userprofile)

