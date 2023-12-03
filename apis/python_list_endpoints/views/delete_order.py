from flask import jsonify
from flask_restx import Namespace, reqparse, Resource
from data.orders_list import orders_list
from services.order_name_check_service import is_order_name_valid


delete_order_mini_namespace = Namespace(name="delete_order")

delete_order_parser = reqparse.RequestParser()
delete_order_parser.add_argument("order_name", required=True, type=str)


@delete_order_mini_namespace.route("/")
class DeleteOrderService(Resource):
    @delete_order_mini_namespace.expect(delete_order_parser)
    def delete(self):
        """
        Delete your order if exists!
        :return:
        """
        args = delete_order_parser.parse_args()
        order_name = args['order_name']
        is_order_name_valid(order_name)
        orders_name_list = [order["name"] for order in orders_list]
        if order_name in orders_name_list:
            _index = orders_name_list.index(order_name)
            orders_list.pop(_index)
            return jsonify(orders_list)
        else:
            message = {"message": f"There is no {order_name} order in the orders list!"}
            return jsonify(message)
