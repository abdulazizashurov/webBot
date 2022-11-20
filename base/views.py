from django.shortcuts import render

from base.models import Product


def homePage(request):
    products = Product.objects.all()
    return render(request, template_name="base.html", context={"products": products})
