from flask import jsonify, current_app
from flask_restx import Namespace, Resource, reqparse
from services.order_name_check_service import is_order_name_valid


update_order_to_mongodb_mini_namespace = Namespace(name="update")

update_order_to_mongodb_parser = reqparse.RequestParser()
update_order_to_mongodb_parser.add_argument('order_name', required=False, type=str, default="test")
update_order_to_mongodb_parser.add_argument('order_name_new', required=False, type=str)
update_order_to_mongodb_parser.add_argument('status', required=False, type=str)


@update_order_to_mongodb_mini_namespace.route("/order")
class UpdateOrderNameFromMongodbService(Resource):
    @update_order_to_mongodb_mini_namespace.expect(update_order_to_mongodb_parser)
    def put(self):
        """
        Update your order if exists!
        :return:
        """
        args = update_order_to_mongodb_parser.parse_args()
        order_name = args['order_name']
        order_name_new = args['order_name_new']
        order_name = is_order_name_valid(order_name)
        order_name_new = is_order_name_valid(order_name_new)
        response = current_app.config.mongodb_service.update_order_name(order_name, order_name_new)
        return jsonify(response)


@update_order_to_mongodb_mini_namespace.route("/status")
class UpdateOrderStatusFromMongodbService(Resource):
    @update_order_to_mongodb_mini_namespace.expect(update_order_to_mongodb_parser)
    def put(self):
        """
        Update your orders status if exists!
        :return:
        """
        args = update_order_to_mongodb_parser.parse_args()
        order_name = args['order_name']
        status = args['status']
        order_name = is_order_name_valid(order_name)
        response = current_app.config.mongodb_service.update_order_status(order_name, status)
        return jsonify(response)
