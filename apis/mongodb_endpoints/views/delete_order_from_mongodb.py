from flask import jsonify, current_app
from flask_restx import Namespace, reqparse, Resource
from services.order_name_check_service import is_order_name_valid


delete_order_from_mongodb_mini_namespace = Namespace(name="delete_order")

delete_order_from_mongodb_parser = reqparse.RequestParser()
delete_order_from_mongodb_parser.add_argument("order_name", required=True, type=str)


@delete_order_from_mongodb_mini_namespace.route("/")
class DeleteOrderFromMongodbService(Resource):
    @delete_order_from_mongodb_mini_namespace.expect(delete_order_from_mongodb_parser)
    def delete(self):
        """
        Delete your order from mongodb if exists!
        :return:
        """
        args = delete_order_from_mongodb_parser.parse_args()
        order_name = args['order_name']
        order_name = is_order_name_valid(order_name)
        response = current_app.config.mongodb_service.delete_order(order_name)
        return jsonify(response)
