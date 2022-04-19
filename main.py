width=35
currency = "BYN"
shop_name = "shop #32"

#receipt([(name, price, count), ...])
def receipt (purchases):
    total = 0

    items = [
        shop_name.center(width),
        currency.rjust(width)
     ]

    for name, price ,count in purchases:
        total += price*count

        all_price = str(round(price*count, 2))

        msg = f'{name}'.ljust(width-len(all_price), ' ')
        msg += all_price

        if type(count) is int and count >= 2:
            msg += f'\n   {count} x {price}'
        elif type(count) is float:
            msg += f'\n   {count} kg x {price}'

        items.append(msg)
    total = str(round(total, 2))
    items.append("\nTOTAL:".ljust(width-len(total)+1) + total)

    return '\n'.join(items)

ITEMS = [
    ("Banane", 1.15, 0.227),
    ("Branza", 2.72, 1),
    ("Ridichi", 0.89, 1),
    ("Ceapa", 0.79, 1),
    ("Ciuperci", 0.99, 1),
    ("Usturoi", 1.19, 1),
    ("Crab", 4.99, 1),
    ("Iaurt Grecesc", 1.99, 1),
    ("Suc de portocale", 1.45, 2),
    ("Cafea bio", 2.99, 1),
    ("Biscuiti", 0.59, 2),
    ("Ciocolata",0.85, 2),
    ("Acadele de ciocolata", 1.29, 1),
    ("CD", 3.99, 1),
]

print(receipt(ITEMS))