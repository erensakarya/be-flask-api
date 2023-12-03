from flask import jsonify, current_app
from flask_restx import Namespace, Resource


get_all_orders_from_mongodb_mini_namespace = Namespace(name="orders")


@get_all_orders_from_mongodb_mini_namespace.route("/")
class GetAllOrdersFromMongodbService(Resource):
    def get(self):
        """
        Get all orders from mongodb!
        :return:
        """
        all_orders_list = current_app.config.mongodb_service.get_all_orders()
        return jsonify(all_orders_list)
