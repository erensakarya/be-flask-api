from flask_restx import Namespace
from apis.mongodb_endpoints.views.add_order_to_mongodb import AddOrderToMongodbService, add_order_to_mongodb_parser
from apis.mongodb_endpoints.views.delete_order_from_mongodb import DeleteOrderFromMongodbService, delete_order_from_mongodb_parser
from apis.mongodb_endpoints.views.get_all_orders_from_mongodb import GetAllOrdersFromMongodbService
from apis.mongodb_endpoints.views.get_order_from_mongodb import GetOrderFromMongodbService, get_order_from_mongodb_parser
from apis.mongodb_endpoints.views.update_order_from_mongodb import UpdateOrderNameFromMongodbService, UpdateOrderStatusFromMongodbService, update_order_to_mongodb_parser


def load_endpoint(ns, name, class_, parser_=None):
    (ns.route(f"/{name}"))(class_)
    (ns.doc(parser=parser_))
    return ns


mongodb_ns = Namespace('mongodb')

mongodb_ns = load_endpoint(
    mongodb_ns, name='add_order', class_=AddOrderToMongodbService,
    parser_=add_order_to_mongodb_parser
)

mongodb_ns = load_endpoint(
    mongodb_ns, name='delete_order', class_=DeleteOrderFromMongodbService,
    parser_=delete_order_from_mongodb_parser
)

mongodb_ns = load_endpoint(
    mongodb_ns, name='orders', class_=GetAllOrdersFromMongodbService
)

mongodb_ns = load_endpoint(
    mongodb_ns, name='order', class_=GetOrderFromMongodbService,
    parser_=get_order_from_mongodb_parser
)

mongodb_ns = load_endpoint(
    mongodb_ns, name='update_order', class_=UpdateOrderNameFromMongodbService,
    parser_=update_order_to_mongodb_parser
)

mongodb_ns = load_endpoint(
    mongodb_ns, name='update_orders_status', class_=UpdateOrderStatusFromMongodbService,
    parser_=update_order_to_mongodb_parser
)
