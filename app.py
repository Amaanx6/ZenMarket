from flask import Flask, render_template, url_for

app = Flask(__name__)

# Mock Product Data
products = [
    {"name": "Smartphone", "price": "$299.99", "description": "Latest smartphone with amazing features.", "image": "smartphone.jpg"},
    {"name": "Laptop", "price": "$899.99", "description": "High-performance laptop for work and play.", "image": "laptop.jpg"},
    {"name": "T-shirt", "price": "$19.99", "description": "Comfortable cotton t-shirt in various sizes.", "image": "tshirt.jpg"},
    {"name": "Headphones", "price": "$49.99", "description": "Wireless headphones with great sound quality.", "image": "headphones.jpg"},
    {"name": "Camera", "price": "$499.99", "description": "High-resolution camera for photography lovers.", "image": "camera.jpg"},
    {"name": "Smartwatch", "price": "$199.99", "description": "Stylish smartwatch with fitness tracking features.", "image": "smartwatch.jpg"},
    {"name": "Tablet", "price": "$299.99", "description": "Lightweight tablet for entertainment and work.", "image": "tablet.jpg"},
    {"name": "Speakers", "price": "$149.99", "description": "Portable Bluetooth speakers with rich sound.", "image": "speakers.jpg"},
    {"name": "Car Kit", "price": "$59.99", "description": "Car kit for hands-free calling and navigation.", "image": "car_kit.jpg"},
    {"name": "Charger", "price": "$15.99", "description": "Fast charging USB charger for devices.", "image": "charger.jpg"},
]

# Routes
@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<product_name>')
def product_detail(product_name):
    product = next((item for item in products if item["name"].lower() == product_name.lower()), None)
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/account')
def my_account():
    return render_template('my_account.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
