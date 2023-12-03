import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_restx import Api
from apis import mongodb_ns, python_list_ns
from services import init_services
from home_page import home_page_blueprint


def load_environment():
    try:
        # dotenv_path = pathlib.Path(os.path.dirname(__file__), '.env')
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        if not load_dotenv(dotenv_path):
            raise FileNotFoundError(f"The .env file was not found at {dotenv_path}!")
    except Exception as e:
        raise e


def create_app(mode):
    load_environment()
    app = Flask(__name__)

    app.register_blueprint(home_page_blueprint)

    api = Api(app, doc='/doc/')

    api.add_namespace(mongodb_ns)
    api.add_namespace(python_list_ns)

    app = init_services(app, mode)

    if mode != "development":
        @app.before_request
        def check_host():
            if request.headers.get('token') != os.environ.get('API_TOKEN'):
                return jsonify({'error': 'Access denied'}), 403

    return app


if __name__ == '__main__':
    create_app(mode="development").run()
    # create_app(mode="docker_single").run()
    # create_app(mode="docker_cluster").run()
