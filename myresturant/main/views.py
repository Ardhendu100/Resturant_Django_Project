from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import FoodItem,Category,Customer,Order
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.hashers import make_password,check_password

def homepage(request):
    print("You are",request.user.get_username())
    return render(request,'home.html')

def menupage(request):
    cart = request.session.get('cart')
    # print(cart)
    if not cart:
        request.session['cart'] = {}
    allItems=None
    # request.session.get('cart').clear()
    categories=Category.get_all_categories();
    categoryID=request.GET.get('category')
    if categoryID:
        allItems=FoodItem.get_all_foodItems_by_categoryid(categoryID)
    else:
        allItems=FoodItem.get_all_foodItems();
    data={}
    data['allItems']=allItems
    data['categories']=categories
    return render(request,'main/menuPage.html',data)

def post_product(request):
    #print("You are",request.session.get('email'))
    product=request.POST.get('product')
    cart=request.session.get('cart')  #here cart return a dictionary
    if cart:   
        quantity=cart.get(product)
        # print(quantity)
        if quantity:
            cart[product]=quantity+1

        else:
            cart[product]=1

    else:
        cart={}
        cart[product]=1
    request.session['cart']=cart
    # print('cart',request.session['cart'])
    return redirect(menupage)


#remove item from cart 

def remove_item(request):
    product=request.POST.get('product')
    cart=request.session.get('cart')
    if cart:   
        quantity=cart.get(product)
        if quantity:
            if quantity<=1:
                cart.pop(product)
            else:
                cart[product]=quantity-1

    else:
        cart={}
        cart[product]=1
    request.session['cart']=cart
    # print('cart',request.session['cart'])


    return redirect(menupage)



#Cart section start
def cart(request):
    
    if cart:
        ids=list(request.session.get('cart').keys())
        products=FoodItem.get_foodItems_by_id(ids)
        # print(products)
        
        return render(request,'main/cart.html',{'products' : products})
    else:
        return HttpResponse("404- Not found")

def cart_quantity(product,cart):
    # del cart["null"]
    keys=cart.keys()
    # print(keys)
    # print(product,cart) 
    for id in keys:
        if id!="null":
        # print(type(id),type(product.Sno))
            if int(id)==int(product.Sno):
                return cart.get(id)

    return 0
# Check Out
def check_out(request):
    full_name=request.POST.get('full_name')
    address=request.POST.get('address')
    landmark=request.POST.get('landmark')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    cart=request.session.get('cart')
    products=FoodItem.get_foodItems_by_id(list(cart.keys()))
    customer=request.user.id
    # print(address,landmark,phone,email,customer,cart,products)
    for product in products:
            # print(cart.get(str(product.Sno)))
            order = Order(customer=User(id=customer),
                          full_name=full_name,
                          product=product,
                          price=product.Price,
                          address=address,
                          landmark=landmark,
                          phone=phone,
                          email=email,
                          quantity=cart.get(str(product.Sno)))
            if customer:
                order.save()
            else:
                messages.error(request, "Please Login to checkout your product")
                return redirect(customerLogin)
    request.session['cart'] = {}
    return redirect('cart')


#Orders section start
def orders(request):
    customer=request.user.id
    orders=Order.get_orders_by_customer(customer)
    # print(orders)
    return render(request,'main/orders.html',{'orders':orders})




#Return Searched Value
def about(request):
    return render(request,'main/about.html',)

# def post_product(request):
#     product=request.POST.get('product')
#     print(product)
#     return redirect(menupage)

# Signup section work start
# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'main/signup.html')
#     else:
#         first_name=request.POST.get('firstname')
#         last_name=request.POST.get('lastname')
#         phone=request.POST.get('phone')
#         email=request.POST.get('email')
#         password=request.POST.get('password')  
  
#         #validation
#         value={
#             'first_name':first_name,
#              'last_name':last_name,
#              'phone': phone,
#              'email':email
#         }
#         if len(first_name)<3:
#             messages.error(request, "Enter a valid first name")
#             return render(request, 'main/signup.html', {'values':value})
#         elif len(last_name)<3:
#             messages.error(request, "Enter a valid last name")
#             return render(request, 'main/signup.html', {'values':value})
#         elif len(phone)!=10:
#             messages.error(request, "Enter a valid phone number")
#             return render(request, 'main/signup.html', {'values':value})
#         elif len(password)<6:
#             messages.error(request, "Your password must be 6 character long. Enter a valid password")
#             return render(request, 'main/signup.html', {'values':value})

#         # Unique Email id
#         elif Customer.objects.filter(email=email):
#             messages.error(request, "Email already registered")
#             return render(request, 'main/signup.html', {'values':value})
#         #saving
#         else:
#             customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
#             customer.password=make_password(customer.password)
#             customer.save()
#             messages.success(request, "Your account has been sucessfully created.")
#             return render(request, 'main/signup.html', {'values':value})


#Login section work start
# def customerLogin(request):
#     if request.method == 'GET':
#         return render(request, 'main/login.html')
#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         value={
#             'email':email
#         }
#         customer=Customer.objects.get(email=email)
#         if customer:
#             flag=check_password(password, customer.password)
#             if flag:
#                 request.session['customer_id']=customer.id
#                 request.session['email']=customer.email
#                 login(request,customer)
#                 messages.success(request, "Sucessfully Logged In")
#                 return redirect('homepage')
#             else:
#                 messages.error(request, "Invalid email id or password")
#                 return render(request, 'main/login.html',{'values':value})

#         else:
#             messages.error(request, "Invalid email id or password")
#             return render(request, 'main/login.html')
#         return render(request, 'main/login.html',{'values':value})




def customerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        # print(user)     

        if user is not None:
            login(request,user)
            print('created')
            messages.success(request, f"Successfully logged in {username}")

            return redirect('homepage')
    

        else:
            # print('invalid')
            messages.error(request, "Invalid username or password")
            return render(request,'main/login.html')
    return render(request,'main/login.html')
def signup(request):
    if request.method == 'GET':
        return render(request, 'main/signup.html')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
         #validation
        value={
           'first_name':first_name,
           'last_name':last_name,
           'username':username,
            'email':email
        }
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return render(request,'main/signup.html',{'values':value})
            else:
                user=User.objects.create(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.set_password(password1)
                user.save()
                messages.success(request, "Your account has been sucessfully created")
                return redirect('homepage')
            
        else:
            messages.error(request, "Password didin't match")
            return redirect('main/signup.html')






# Log out user
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('homepage')