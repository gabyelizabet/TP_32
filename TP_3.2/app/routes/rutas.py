from flask import Blueprint
from controllers.controlador import CustomerController, ProductController

customer_bp = Blueprint ('customer_bp', __name__)

customer_bp.route('/customers', methods=['POST'])(CustomerController.create_customer)
customer_bp.route('/customers/<int:customer_id>', methods = ['GET'])(CustomerController.get_customer)
customer_bp.route('/customers', methods=['GET'])(CustomerController.get_customers)
customer_bp.route('/customers/update/<int:customer_id>', methods = ['PUT'])(CustomerController.update_customer)
customer_bp.route('/customers/delete/<int:customer_id>', methods = ['DELETE'])(CustomerController.delete_customer)


product_bp = Blueprint ('product_bp',__name__)

product_bp.route('/products', methods=['POST'])(ProductController.register_product)
product_bp.route('/products/<int:product_id>', methods = ['GET'])(ProductController.get_product)
product_bp.route('/products', methods=['GET'])(ProductController.get_products)
product_bp.route('/products/update/<int:product_id>', methods = ['PUT'])(ProductController.update_product)
product_bp.route('/products/delete/<int:product_id>', methods = ['DELETE'])(ProductController.delete_product)