from flask import jsonify, current_app
from flask_restx import Namespace, Resource, reqparse
from services.order_name_check_service import is_order_name_valid


get_order_from_mongodb_mini_namespace = Namespace(name="order")

get_order_from_mongodb_parser = reqparse.RequestParser()
get_order_from_mongodb_parser.add_argument('order_name', required=False, type=str, default="test")


@get_order_from_mongodb_mini_namespace.route("/")
class GetOrderFromMongodbService(Resource):
    @get_order_from_mongodb_mini_namespace.expect(get_order_from_mongodb_parser)
    def get(self):
        """
        Get if your order exists!
        :return:
        """
        args = get_order_from_mongodb_parser.parse_args()
        order_name = args['order_name']
        is_order_name_valid(order_name)
        order_dict = current_app.config.mongodb_service.get_specific_order_if_exists(order_name)
        if not order_dict:
            return jsonify({"message": f"There is no {order_name} order in the orders list!"})
        else:
            return jsonify(order_dict[0])
