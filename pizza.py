def make_pizza(size,*topping):
    print(f"你訂了{size}的披薩")
    for toppings in topping:
        print(f"加了以下配料{toppings}")