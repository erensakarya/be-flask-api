from flask_restx import Namespace
from apis.python_list_endpoints.views.add_order import AddOrderService, add_orders_parser
from apis.python_list_endpoints.views.delete_order import DeleteOrderService, delete_order_parser
from apis.python_list_endpoints.views.get_all_orders import GetAllOrdersService
from apis.python_list_endpoints.views.get_order import GetOrderService, get_order_parser
from apis.python_list_endpoints.views.update_order import UpdateOrderService, UpdateOrderStatusService, \
    update_orders_parser


def load_endpoint(ns, name, class_, parser_=None):
    (ns.route(f"/{name}"))(class_)
    (ns.doc(parser=parser_))
    return ns


python_list_ns = Namespace('python_list')

python_list_ns = load_endpoint(
    python_list_ns, name='add_order', class_=AddOrderService,
    parser_=add_orders_parser
)

python_list_ns = load_endpoint(
    python_list_ns, name='delete_order', class_=DeleteOrderService,
    parser_=delete_order_parser
)

python_list_ns = load_endpoint(
    python_list_ns, name='orders', class_=GetAllOrdersService
)

python_list_ns = load_endpoint(
    python_list_ns, name='order', class_=GetOrderService,
    parser_=get_order_parser
)

python_list_ns = load_endpoint(
    python_list_ns, name='update_order', class_=UpdateOrderService,
    parser_=update_orders_parser
)

python_list_ns = load_endpoint(
    python_list_ns, name='update_orders_status', class_=UpdateOrderStatusService,
    parser_=update_orders_parser
)
