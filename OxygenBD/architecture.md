oxygen/
 ├── manage.py
 │
 ├── oxygen/                 # основной конфиг проекта
 │    ├── __init__.py
 │    ├── settings.py
 │    ├── urls.py
 │    ├── asgi.py
 │    └── wsgi.py
 │
 ├── users/
 ├── shops/
 ├── catalog/
 ├── cart/
 ├── orders/
 ├── reviews/
 │
 ├── templates/              # HTML
 │    ├── base.html
 │    ├── includes/
 │    │    ├── header.html
 │    │    └── navbar.html
 │    │
 │    ├── users/
 │    │    ├── login.html
 │    │    ├── register.html
 │    │    └── profile.html
 │    │
 │    ├── shops/
 │    │    ├── shop_list.html
 │    │    └── shop_detail.html
 │    │
 │    ├── catalog/
 │    │    ├── product_list.html
 │    │    └── product_detail.html
 │    │
 │    ├── cart/
 │    │    └── cart_detail.html
 │    │
 │    ├── orders/
 │    │    └── order_detail.html
 │    │
 │    └── reviews/
 │         └── review_create.html
 │
 ├── static/                 # CSS / JS / изображения
 │    ├── global/
 │    │    └── base.css
 │    │
 │    ├── users/
 │    │    └── styles/
 │    │         ├── login.css
 │    │         ├── register.css
 │    │         └── profile.css
 │    │
 │    ├── shops/
 │    │    └── styles/
 │    │         └── shop.css
 │    │
 │    ├── catalog/
 │    │    └── styles/
 │    │         ├── product_list.css
 │    │         └── product_detail.css
 │    │
 │    ├── cart/
 │    │    └── styles/
 │    │         └── cart.css
 │    │
 │    ├── orders/
 │    │    └── styles/
 │    │         └── order.css
 │    │
 │    └── reviews/
 │         └── styles/
 │              └── review.css
 │
 ├── media/                  # загружаемые файлы (картинки)
 │
 ├── requirements.txt
 └── .env