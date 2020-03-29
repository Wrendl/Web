from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    j_p = [p.to_json() for p in products]
    return JsonResponse(j_p, safe=False)


def product_id(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')
    return JsonResponse(product.to_json())


def categories_list(request):
    categories = Category.objects.all()
    j_c = [c.to_json() for c in categories]
    return JsonResponse(j_c, safe=False)


def category_id(request, cat_id):
    try:
        category = Category.objects.get(id=cat_id)
    except Category.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}!!!</h2>')
    return JsonResponse(category.to_json())


def products_by_cat(request, cat_id):
    products = Product.objects.all()
    j_p = [p.to_json() for p in products]
    p = []
    for i in j_p:
        if i['category_id'] == cat_id:
            p.append(i.copy())
    if not p:
        return HttpResponse(f'<h2>Product DoesNotExist!!!</h2>')
    return JsonResponse(p, safe=False)
    #try:
    #    category = Category.objects.get(id=cat_id)
    #except Product.DoesNotExist as e:
    #    return HttpResponse(f'<h2>{e}!!!</h2>')
    #products = category.product_set.all()
    #j_p = [p.to_json() for p in products]
    #return JsonResponse(j_p, safe=False)
