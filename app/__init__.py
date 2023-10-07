from flask import Flask
from flasgger import Swagger

from flask import Flask
from flasgger import Swagger

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "JordanGpt",
        "description": """ 
        This is a simple API to access Jordan's resume and role descriptions. You can also ask JordanGpt, a GPT-3 model, and chatbot.
        ### Steps to Use the API:
        1. **Endpoint Selection**: Navigate to the desired endpoint using the left sidebar.
        2. **Parameters**: Fill in any required parameters in the provided fields.
        3. **Execute**: Click the "Try it out" button and then "Execute" to see the API in action.
        4. **Response**: Review the response returned by the API in the "Responses" section.
        5. **Further Queries**: Navigate to other endpoints or adjust parameters as needed and repeat.
        6. **Authentication**: If required, obtain an API key or token.

        For any issues or feedback, please contact [jordaneisenman@gmail.com](mailto:support@example.com).
        """,
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "firebase_auth": {
            "type": "apiKey",
            "description": "Firebase ID token",
            "name": "Authorization",
            "in": "header"
        }
    }
}

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app, template=SWAGGER_TEMPLATE)

    from .routes import app_blueprint
    app.register_blueprint(app_blueprint)

    return app
