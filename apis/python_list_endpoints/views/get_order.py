from flask import jsonify
from flask_restx import Namespace, Resource, reqparse
from data.orders_list import orders_list
from services.order_name_check_service import is_order_name_valid


get_order_mini_namespace = Namespace(name="get_order")

get_order_parser = reqparse.RequestParser()
get_order_parser.add_argument('order_name', required=False, type=str, default="test")


@get_order_mini_namespace.route("/")
class GetOrderService(Resource):
    @get_order_mini_namespace.expect(get_order_parser)
    def get(self):
        """
        Get if your order exists!
        :return:
        """
        args = get_order_parser.parse_args()
        order_name = args['order_name']
        try:
            is_order_name_valid(order_name)
            orders_name_list = [order["name"] for order in orders_list]
            if order_name in orders_name_list:
                _index = orders_name_list.index(order_name)
                return jsonify(orders_list[_index])
            else:
                message = {"message": f"There is no {order_name} order in the orders list!"}
                return jsonify(message)
        except Exception as e:
            raise e
