from flask import Flask
from config import Config
from routes.rutas import customer_bp, product_bp

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(customer_bp)
    app.register_blueprint(product_bp)
    
    return app