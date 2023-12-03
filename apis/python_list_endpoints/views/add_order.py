from flask import jsonify
from flask_restx import Namespace, Resource, reqparse
from data.orders_list import orders_list
from services.order_name_check_service import is_order_name_valid


add_order_mini_namespace = Namespace(name="add_order")

add_orders_parser = reqparse.RequestParser()
add_orders_parser.add_argument('order_name', required=False, type=str, default="test")


@add_order_mini_namespace.route("/")
class AddOrderService(Resource):
    @add_order_mini_namespace.expect(add_orders_parser)
    def post(self):
        """
        Add a new order to the end of the list!
        :return:
        """
        args = add_orders_parser.parse_args()
        order_name = args['order_name']
        order_name = is_order_name_valid(order_name)
        orders_name_list = [order["name"] for order in orders_list]
        if order_name not in orders_name_list:
            orders_list.append({"name": f"{order_name}", "status": "being_prepared"})
            return jsonify(orders_list)
        else:
            return jsonify({"message": f"You already ordered a {order_name}, please wait!"})
