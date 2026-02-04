from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    
    from app.routes import jobs
    app.register_blueprint(jobs.bp)
    
    return app
