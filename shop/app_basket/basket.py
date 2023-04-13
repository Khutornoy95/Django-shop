from django.conf import settings


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, count=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'id': product_id,
                                     'category': product.category.pk,
                                     'price': float(product.price),
                                     'count': 0,
                                     'date': str(product.date),
                                     'title': product.title,
                                     'description': product.description,
                                     'href': product.href(),
                                     'freeDelivery': product.freeDelivery,
                                     'images': product.images,
                                     'tags': product.tags,
                                     'reviews': len(product.reviews.all()),
                                     'rating': float(product.rating)
                                     }
        self.cart[product_id]['count'] += count
        total = product.price * self.cart[product_id]['count']
        self.cart[product_id]['price'] = float(total)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product, count=0):
        product_id = str(product.id)
        if product_id in self.cart:
            if count:
                self.cart[product_id]['count'] -= count
                total = product.price * self.cart[product_id]['count']
                self.cart[product_id]['price'] = float(total)
            else:
                del self.cart[product_id]
            self.save()

    # def __iter__(self):
    #     product_ids = self.cart.keys()
    #     products = Product.objects.filter(id__in=product_ids)
    #     for product in products:
    #         self.cart[str(product.id)]['product'] = product
    #     for item in self.cart.values():
    #         item['price'] = Decimal(item['price'])
    #         item['total_price'] = item['price'] * item['count']
    #         yield item

    # def __len__(self):
    #     return sum(item['count'] for item in self.cart.values())
    #
    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['count'] for item in
    #                self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
