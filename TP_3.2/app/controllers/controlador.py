from flask import jsonify
from flask import request
from database import DatabaseConnection

class CustomerController:
    @classmethod
    def create_customer(self):
        query = "INSERT TO sales.customers (first_name, last_name, email, phone, street, city, state, zip_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        params = request.args.get('first_name',''), request.args.get('last_name',''),request.args.get('email',''), request.args.get('phone',''), request.args.get('street',''), request.args.get('city',''), request.args.get('state',''), request.args.get('zip_code','')
        DatabaseConnection.execute_query(query, params)
        return jsonify({"msg": "Cliente creado con éxito"}, 201)
        
    @classmethod
    def get_customer(customer_id):
        query = "SELECT * FROM sales.customers WHERE customer_id = %s;"
        params = customer_id
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return jsonify({
                "id": result [0],
                "nombre": result[1],
                "apellido": result[2],
                "email": result[3],
                "telefono":result[4],
                "calle": result[5],
                "ciudad": result[6],
                "estado": result[7],
                "código postal": result[8]
            }), 200
        else:
            return jsonify({"msg":"No se encontró el cliente"}),404

    @classmethod
    def get_customers(self):
        query = "SELECT * FROM sales.customers WHERE customers.state LIKE %s;"
        params = request.args.get('buscar','')
        results = DatabaseConnection.fetch_all(query, params)
        customers = []
        total = 0
        for result in results:
            customers.append ({
                "id": result [0],
                "nombre": result[1],
                "apellido": result[2],
                "email": result[3],
                "telefono":result[4],
                "calle": result[5],
                "ciudad": result[6],
                "estado": result[7],
                "código postal": result[8]
            }),
            total += 1
        return jsonify(f'{customers} El total de clientes obtenidos es:{total}', 200)
     
    @classmethod   
    def update_customer(self,customer_id):
        query = "UPDATE sales.customers SET last_update = %s WHERE customers.customer_id = %s;"
        params = request.args.get('last_update', ''), customer_id
        DatabaseConnection.execute_query(query, params)
        return jsonify({"msg": "Datos del cliente actualizados con éxito"}, 200)

    @classmethod
    def delete_customer(self,customer_id):
        query = "DELETE FROM sales.customers WHERE customers.customer_id = %s;"
        params = customer_id,
        DatabaseConnection.execute_query(query, params)
        return jsonify({"msg": "Cliente eliminado con éxito"}, 204)
    
class ProductController:
    
    @classmethod
    def register_product(self):
        query = "INSERT TO production.products (product_name,brand_id, category_id, model_year, list_price) VALUES (%s, %s, %s, %s, %s)"
        params = request.args.get('product_name',''), request.arg.get('brand_id',''), request.arg.get('category_id',''), request.arg.get('model_year',''), request.arg.get('list_price','')
        DatabaseConnection.execute_query(query, params)
        return jsonify({"msg": "Cliente creado con éxito"}, 201)
    
    @classmethod
    def get_product(self, product_id):
        query = "SELECT products.product_id, products.product_name, products.model_year, products.list_price, brands.*, categories.* FROM ((products INNER JOIN brands ON products.brand_id = brands.brand_id) INNER JOIN categories ON products.category_id = categories.category_id) WHERE products.product_id"
        params = product_id
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return jsonify({
                "product_id": result [0],
                "product_name": result [1],
                "model_year": result [2],
                "list_price": result [3],
                "brand":{
                    "brand_id": result [4],
                    "brand_name": result [5]
                },
                "category": {
                    "category_id": result[6],
                    "category_name": result[7]
                },
                }),200
        else:
            return jsonify({"msg":"No se encontró el producto"}),404
    
    @classmethod
    def get_products(self):
        query = "SELECT products.product_id, products.product_name, products.model_year, products.list_price, brands.*, categories.* FROM ((products INNER JOIN brands ON products.brand_id = brands.brand_id) INNER JOIN categories ON products.category_id = categories.category_id) WHERE products.category_id LIKE %s"
        params= request.args.get('buscar','')
        results = DatabaseConnection.fetch_all(query, params)
        products= []
        total= 0
        for result in results:
            products.append({
                "product_id": result [0],
                "product_name": result [1],
                "model_year": result [2],
                "list_price": result [3],
                "brand":{
                    "brand_id": result [4],
                    "brand_name": result [5]
                },
                "category": {
                    "category_id": result[6],
                    "category_name": result[7]
                },
                }),
            total += 1
        return jsonify(f'{products}El total de productos obtenidos es {total}', 200)
            
    @classmethod
    def update_product(self, product_id):
        query = "UPDATE production.products SET last_update = %s WHERE products.product_id = %s;"
        params= request.args.get('last_update', ''), product_id
        DatabaseConnection.execute_query(query, params)
        return jsonify({"msg": "Datos del producto actualizados con éxito"}, 200)
    
    @classmethod
    def delete_product(self, product_id):
        query = "DELETE FROM production.products WHERE products.product_id = %s;"
        params = product_id,
        DatabaseConnection.execute_query(query, params)
        return jsonify({"msg": "Producto eliminado con éxito"}, 204)