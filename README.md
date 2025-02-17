# E-commerce Store

This is a fully functional e-commerce store built using:
- **Frontend:** HTML, CSS, JavaScript, HTMX, Alpine.js
- **Backend:** Django
- **Payment Gateway:** Paystack

## 🚀 Features
### User Features
- Sign up and log in
- Add items to the cart
- Like products and leave reviews
- View order history in the "Orders" section
- Update cart (increase quantity or remove items)
- Checkout with a form to input address and redirect to Paystack for payment

### 🔧 Admin Features
- Access Django's admin panel
- Manage products (add images, descriptions, and other details)
- Manage users
- Update order statuses (e.g., pending, shipped, completed)

## 🛠 Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <project-directory>
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```
If you encounter issues with `psycopg2`, install necessary dependencies:
```sh
sudo apt install libpq-dev
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root and define the following variables:
```sh
MAILGUN_API_KEY=<your-mailgun-api-key>
JWT_KEY=<your-jwt-secret-key>
DEBUG=0
ALLOWED_HOSTS=127.0.0.1,localhost
AWS_ACCESS_KEY_ID=<your-aws-access-key>
AWS_SECRET_ACCESS_KEY=<your-aws-secret-key>
DB_NAME=<your-database-name>
DB_USER=<your-database-user>
DB_PASSWORD=<your-database-password>
DB_HOST=<your-database-host>
DB_PORT=5432
TEST_DB_NAME=<your-test-database-name>
PAYSTACK_SECRET_KEY=<your-paystack-secret-key>
HOST=localhost:8000
AWS_BUCKET_NAME=<your-aws-bucket-name>
ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```
> **🔹 Note:** The database engine is **PostgreSQL**, which is why the port is set to `5432`. If needed, you can modify this in the settings and change the port accordingly.
> 
> **🔹 Note:** `HOST` refers to the domain at which the site is hosted.
>
> **🔹 Note:** `ALLOWED_ORIGINS` is used for CORS (Cross-Origin Resource Sharing) configuration.
>
> **🔹 Note:** To use AWS S3 for storing media and static files, you need to set up AWS buckets and configure them accordingly.

### 4. Run Migrations
```sh
python manage.py makemigrations account
python manage.py makemigrations store
python manage.py migrate store
python manage.py migrate account
python manage.py migrate
```

### 5. Run the Development Server
```sh
python manage.py runserver
```

### 6. 📂 Static and Media Files (Production Only)
When `DEBUG=False`, static and media files are served from AWS S3. Run the following command to collect static files:
```sh
python manage.py collectstatic
```
> **Note:** In development, Django serves static and media files automatically.

## 🎯 Usage
- Access the website at `http://localhost:8000`
- Use Django admin panel at `http://localhost:8000/admin` to manage products, orders, and users

## 📜 License
This project is licensed under the MIT License.

---
### ✨ Author
Praise Josiah

