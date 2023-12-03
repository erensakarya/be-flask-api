from flask_restx import Api
from apis.mongodb_endpoints import mongodb_ns
from apis.python_list_endpoints import python_list_ns


api = Api(
    title='Super Flask App Example',
    version='1.0',
    description='A Flask Rest App Example works with MongoDB!'
)


api.add_namespace(mongodb_ns)
api.add_namespace(python_list_ns)
