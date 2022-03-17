from django import template
register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product,cart):
    print(cart)
    keys=cart.keys()
    # print(keys)
    print(product,cart) 
    for id in keys:
        if id!="null":
        # print(type(id),type(product.Sno))
            if int(id)==int(product.Sno):
                return True

    return False


@register.filter(name="cart_quantity")
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


@register.filter(name='price_total')
def price_total(product  , cart):
    return product.Price * cart_quantity(product , cart)


@register.filter(name='multiply')
def multiply(num1, num2):
    return num1*num2

@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)

    return sum