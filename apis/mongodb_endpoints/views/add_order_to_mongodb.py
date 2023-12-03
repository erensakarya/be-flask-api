from flask import jsonify, current_app
from flask_restx import Namespace, Resource, reqparse
from services.order_name_check_service import is_order_name_valid


add_order_to_mongodb_mini_namespace = Namespace(name="add_order", description="add a new order to mongodb")

add_order_to_mongodb_parser = reqparse.RequestParser()
add_order_to_mongodb_parser.add_argument("order_name", required=False, type=str, default="test")


@add_order_to_mongodb_mini_namespace.route("/")
class AddOrderToMongodbService(Resource):
    @add_order_to_mongodb_mini_namespace.expect(add_order_to_mongodb_parser)
    def post(self):
        """
        Add a new order if doesn't exist!
        :return:
        """
        args = add_order_to_mongodb_parser.parse_args()
        order_name = args['order_name']
        order_name = is_order_name_valid(order_name)
        response = current_app.config.mongodb_service.add_order(order_name)
        return jsonify(response)

