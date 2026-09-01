

product_price = float(input("Ingrese el precio del producto: "))
if product_price >= 100:
    discount = product_price * 0.10
else:
    discount = product_price * 0.02
discounted_price = product_price - discount
print(f"El precio del producto con descuento es: {discounted_price}")