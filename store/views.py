
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE


def products_view(request):
    if request.method == "GET":
        return JsonResponse(DATABASE,
                            json_dumps_params={"indent": 4,
                                               "ensure_ascii": False}
                            )# Вернуть JsonResponse с объектом DATABASE и параметрами отступов и кодировок,


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ

# def products_view(request):
#     if request.method == "GET":
#         id_ = request.GET.get("id")
#         id = DATABASE
#         return JsonResponse(id)



# Ваша реализация
