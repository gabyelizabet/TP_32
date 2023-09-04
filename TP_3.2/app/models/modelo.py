class Customer:
    def __init__ (self , customer_id = None, first_name = None , last_name =None , email= None, phone =None, street=None, city=None, state=None, zip_code=None ):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.phone = phone
        self.street= street
        self.city= city
        self.state= state
        self.zip_code= zip_code


class Product:
    def __init__(self, product_id = None, product_name = None, brand_id= None, category_id = None, model_year = None, list_price = None):
        self.product_id = product_id
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price
    
class Brand:
    def __init__(self, brand_id=None, brand_name= None):
        self.brand_id = brand_id
        self.brand_name = brand_name

class Category:
    def __init__(self, category_id = None, category_name= None):
        self.category_id = category_id
        self.category_name = category_name
