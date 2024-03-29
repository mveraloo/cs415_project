import datetime 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import Cart, Orders, Package, Payment, Paymenttype, Useraccount, Userprofile
from cs415.serializers import CartSerializer, OrdersSerializer, PackageSerializer, PaymentSerializer, PaymenttypeSerializer, UseraccountSerializer, UserprofileSerializer


class CartAPIView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response({'carts': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)


class OrdersAPIView(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response({'orders': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        

class PackageAPIView(APIView):
    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response({'packages': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)

class PaymentAPIView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response({'payments': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)
        

class PaymenttypeAPIView(APIView):
    def get(self, request):
        paymenttypes = Paymenttype.objects.all()
        serializer = PaymenttypeSerializer(paymenttypes, many=True)
        return Response({'paymenttypes': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = PaymenttypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)


class UseraccountAPIView(APIView):
    def get(self, request):
        useraccounts = Useraccount.objects.all()
        serializer = UseraccountSerializer(useraccounts, many=True)
        return Response({'useraccounts': serializer.data})
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.datetime.now())
        request.data['is_active'] = 1
        serializer = UseraccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)


class UserprofileAPIView(APIView):
    def get(self, request):
        userprofile = Userprofile.objects.all()
        serializer = UserprofileSerializer(userprofile, many=True)
        return Response({'userprofile': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = UserprofileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("pass_word")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)
        
        check_user = Useraccount.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        check_pass = Useraccount.objects.filter(email = email, pass_word=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = Useraccount.objects.get(email = email, pass_word=password)
        if user is not None:
            # jwt_token = JWTAuthentication.create_jwt(user)
            # data = {
            #     'token': jwt_token
            # }
            return Response({'success': True,
                             'user_id': user.user_id},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)
    
class GetSingleUserProfileAPIView(APIView):
    def get(self, request, id):
            user_data = {}
            userprofile = Userprofile.objects.get(pk=id)
            userprofile_serializer = UserprofileSerializer(userprofile)
            user_data.update({"userprofile": userprofile_serializer.data})
            
            # Retrieve related Useraccount
            useraccount_serializer = UseraccountSerializer(userprofile.user)
            user_data.update({"account": useraccount_serializer.data})

            # Retrieve related Cart
            cart = Cart.objects.filter(user_id=userprofile.user_id).first()  # Assuming one cart per user
            if cart:
                cart_serializer = CartSerializer(cart)
                user_data.update({"cart": cart_serializer.data})
                
                # Retrieve related Orders through the cart
                orders = Orders.objects.filter(cart=cart)
                orders_serializer = OrdersSerializer(orders, many=True)
                user_data.update({"orders": orders_serializer.data})
    
            
            return Response(user_data)
    
class GetSingleOrderAPIView(APIView):
    def get(self, request, id):
        order_data = {}
        # Retrieve the order by its primary key
        order = Orders.objects.get(pk=id)
        order_serializer = OrdersSerializer(order)
        order_data.update({"orders": order_serializer.data})
        cart = order.cart
        cart = order.cart
        if cart:
            # Retrieve the package associated with the cart
            package_serializer = PackageSerializer(cart.package)
            order_data.update({"package": package_serializer.data})
            
            # Retrieve the payment associated with the order
            payment = Payment.objects.filter(order_id=order.order_id).first()
            if payment:
                payment_serializer = PaymentSerializer(payment)
                order_data.update({"payment": payment_serializer.data})
                
                # Retrieve the payment type associated with the payment
                payment_type = payment.type
                if payment_type:
                    payment_type_serializer = PaymenttypeSerializer(payment_type)
                    order_data.update({"payment_type": payment_type_serializer.data})
        return Response(order_data)
    