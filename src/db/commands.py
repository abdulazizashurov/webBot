from asgiref.sync import sync_to_async

from base.models import Product


@sync_to_async
def getProductById(productId):
    try:
        product = Product.objects.get(id=productId)
        return product
    except:
        return None