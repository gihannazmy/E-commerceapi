# 🛍️ E-commerce API

A Django REST API for managing an e-commerce platform with product listings, order management, and user authentication.

---
## 🚀 Features

- ✅ User registration and authentication  
- ✅ Product catalog management  
- ✅ Shopping cart and order placement  

---
## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:**  SQLite
 **Authentication:** Token-based (DRF AuthToken)  

## ⚙️ Setup Instructions

```
git clone https://github.com/gihannazmy/E-commerceapi.git
cd E-commerceapi
python -m venv venv
source venv/bin/activate    
# On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
🧪 API Endpoints
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/login/	Login and receive token
GET	/api/products/	Retrieve product list
POST	/api/order/new/	Create new order
GET	/api/orders/	List user orders
📬 Contact
Name: Gihan Atef Nazmy

Email: gihanelsayed187@gmail.com

LinkedIn: [(https://www.linkedin.com/in/gihanatef/)]
Last updated: 29 April 2025


