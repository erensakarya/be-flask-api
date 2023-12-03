from flask import jsonify
from flask_restx import Namespace, Resource, reqparse
from data.orders_list import orders_list
from services.order_name_check_service import is_order_name_valid


update_order_mini_namespace = Namespace(name="update_order")

update_orders_parser = reqparse.RequestParser()
update_orders_parser.add_argument('order_name', required=False, type=str, default="test")
update_orders_parser.add_argument('order_name_new', required=False, type=str)
update_orders_parser.add_argument('status', required=False, type=str)


@update_order_mini_namespace.route("/order")
class UpdateOrderService(Resource):
    @update_order_mini_namespace.expect(update_orders_parser)
    def put(self):
        """
        Update your order if exists!
        :return:
        """
        args = update_orders_parser.parse_args()
        order_name = args['order_name']
        order_name_new = args['order_name_new']
        order_name = is_order_name_valid(order_name)
        order_name_new = is_order_name_valid(order_name_new)
        orders_name_list = [order["name"] for order in orders_list]
        if order_name not in orders_name_list:
            return jsonify({"message": f"You didn't order a {order_name}, so you can't change it!"})
        else:
            _index = orders_name_list.index(order_name)
            orders_list[_index]["name"] = order_name_new
            return jsonify({"message": f"Your {order_name} order is changed with a {order_name_new} order!"})


@update_order_mini_namespace.route("/status")
class UpdateOrderStatusService(Resource):
    @update_order_mini_namespace.expect(update_orders_parser)
    def put(self):
        """
        Update status of the order!
        :return:
        """
        args = update_orders_parser.parse_args()
        order_name = args['order_name']
        order_name = is_order_name_valid(order_name)
        status = args['status']
        orders_name_list = [order["name"] for order in orders_list]
        if order_name in orders_name_list:
            _index = orders_name_list.index(order_name)
            orders_list[_index]["status"] = status
            return jsonify(orders_list)
        else:
            return jsonify({"message": f"You didn't order a {order_name}, so you can't change its status!"})


