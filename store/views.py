from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ


def products_view(request):
    if request.method == "GET":
        id_ = request.GET.get("id")
        if id_:
            if id_ in DATABASE:
                return JsonResponse(DATABASE[id_],
                                    json_dumps_params={"indent": 4,
                                                       "ensure_ascii": False}
                                    )
            else:
                return HttpResponseNotFound("Данного продукта нет в базе данных")

        return JsonResponse(DATABASE, json_dumps_params={"indent": 4,
                                                         "ensure_ascii": False}
                            )


def products_page_view(request, page):
    if request.method == "GET":
        for data in DATABASE.values():
            if data['html'] == page:
                with open(f'store/products/{page}.html', encoding="utf-8") as f:
                    data_page = f.read()
                return HttpResponse(data_page)

        return HttpResponse(status=404)