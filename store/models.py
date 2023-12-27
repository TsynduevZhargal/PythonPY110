from django.db import models

DATABASE = {'1': {'name': 'Болгарский перец',
                  'discount': 30,
                  'price_before': 300.00,
                  'price_after': 210.00,
                  'description': 'Сочный и яркий, он добавит красок и вкуса в ваши блюда.',
                  'rating': 4.9,
                  'review': 250,
                  'sold_value': 600,
                  'weight_in_stock': 500,
                  'category': 'Овощи',
                  'id': 1,
                  'url': 'store/images/product-1.jpg',
                  'html': 'bell_pepper'
                  },
            '2': {'name': 'Клубника',
                  'discount': None,
                  'price_before': 500.00,
                  'price_after': 500.00,
                  'description': 'Сладкая и ароматная клубника, полная витаминов, чтобы сделать ваш день ярче.',
                  'rating': 5.0,
                  'review': 200,
                  'sold_value': 700,
                  'weight_in_stock': 400,
                  'category': 'Фрукты',
                  'id': 2,
                  'url': 'store/images/product-2.jpg',
                  'html': 'strawberry'
                  },
            '3': {'name': 'Стручковая фасоль',
                  'discount': None,
                  'price_before': 250.00,
                  'price_after': 250.00,
                  'description': 'Зеленая натуральность и богатство белка для вашей здоровой диеты.',
                  'rating': 5.0,
                  'review': 100,
                  'sold_value': 500,
                  'weight_in_stock': 600,
                  'category': 'Овощи',
                  'id': 3,
                  'url': 'store/images/product-3.jpg',
                  'html': 'green_beans'
                  },
            '4': {'name': 'Краснокочанная капуста',
                  'discount': None,
                  'price_before': 90.00,
                  'price_after': 90.00,
                  'description': 'Удивите своих гостей экзотическим вкусом и цветом ваших блюд.',
                  'rating': 4.7,
                  'review': 30,
                  'sold_value': 50,
                  'weight_in_stock': 300,
                  'category': 'Овощи',
                  'id': 4,
                  'url': 'store/images/product-4.jpg',
                  'html': 'purple_cabbage'
                  },
            '5': {'name': 'Помидоры',
                  'discount': 25,
                  'price_before': 240.00,
                  'price_after': 180.00,
                  'description': 'Свежие и сочные помидоры для идеальных салатов и соусов.',
                  'rating': 4.9,
                  'review': 350,
                  'sold_value': 700,
                  'weight_in_stock': 300,
                  'category': 'Овощи',
                  'id': 5,
                  'url': 'store/images/product-5.jpg',
                  'html': 'tomatoes'
                  },
            '6': {'name': 'Брокколи',
                  'discount': None,
                  'price_before': 320.00,
                  'price_after': 320.00,
                  'description': 'Здоровье в каждом кусочке, чтобы укрепить вашу иммунную систему.',
                  'rating': 4.9,
                  'review': 150,
                  'sold_value': 250,
                  'weight_in_stock': 300,
                  'category': 'Овощи',
                  'id': 6,
                  'url': 'store/images/product-6.jpg',
                  'html': 'broccoli'
                  },
            '7': {'name': 'Морковь',
                  'discount': None,
                  'price_before': 50.00,
                  'price_after': 50.00,
                  'description': 'Красота и здоровье для ваших глаз и кожи в каждой моркови.',
                  'rating': 4.8,
                  'review': 220,
                  'sold_value': 800,
                  'weight_in_stock': 900,
                  'category': 'Овощи',
                  'id': 7,
                  'url': 'store/images/product-7.jpg',
                  'html': 'carrots'
                  },
            '8': {'name': 'Фруктовый сок',
                  'discount': None,
                  'price_before': 120.00,
                  'price_after': 120.00,
                  'description': 'Натуральная свежесть и энергия в каждом глотке.',
                  'rating': 4.9,
                  'review': 300,
                  'sold_value': 800,
                  'weight_in_stock': 1200,
                  'category': 'Соки',
                  'id': 8,
                  'url': 'store/images/product-8.jpg',
                  'html': 'fruit_juice'
                  },
            '9': {'name': 'Лук',
                  'discount': 20,
                  'price_before': 40.00,
                  'price_after': 32.00,
                  'description': 'Придайте особый аромат и вкус вашим блюдам с нашим свежим луком.',
                  'rating': 4.6,
                  'review': 80,
                  'sold_value': 170,
                  'weight_in_stock': 350,
                  'category': 'Овощи',
                  'id': 9,
                  'url': 'store/images/product-9.jpg',
                  'html': 'onion'
                  },
            '10': {'name': 'Яблоки',
                   'discount': None,
                   'price_before': 130.00,
                   'price_after': 130.00,
                   'description': 'Сочные и сладкие яблоки - идеальная закуска для здорового перекуса.',
                   'rating': 4.7,
                   'review': 30,
                   'sold_value': 70,
                   'weight_in_stock': 200,
                   'category': 'Фрукты',
                   'id': 10,
                   'url': 'store/images/product-10.jpg',
                   'html': 'apple'
                   },
            '11': {'name': 'Чеснок',
                   'discount': None,
                   'price_before': 150.00,
                   'price_after': 150.00,
                   'description': 'Секрет вкусных блюд и поддержания здоровья вашего сердца.',
                   'rating': 4.9,
                   'review': 150,
                   'sold_value': 400,
                   'weight_in_stock': 1000,
                   'category': 'Овощи',
                   'id': 11,
                   'url': 'store/images/product-11.jpg',
                   'html': 'garlic'
                   },
            '12': {'name': 'Перец Чили',
                   'discount': None,
                   'price_before': 400.00,
                   'price_after': 400.00,
                   'description': 'Острая страсть для тех, кто ищет приключения на своей тарелке.',
                   'rating': 5.0,
                   'review': 40,
                   'sold_value': 300,
                   'weight_in_stock': 50,
                   'category': 'Овощи',
                   'id': 12,
                   'url': 'store/images/product-12.jpg',
                   'html': 'chilli'
                   },
            }
