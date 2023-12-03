from flask import jsonify
from flask_restx import Namespace, Resource
from data.orders_list import orders_list

get_all_orders_mini_namespace = Namespace(name="orders")


@get_all_orders_mini_namespace.route("/")
class GetAllOrdersService(Resource):
    def get(self):
        """
        Get all orders in present!
        :return:
        """
        return jsonify(orders_list)
