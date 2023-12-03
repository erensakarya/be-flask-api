import string


def is_order_name_valid(order_name):
    if order_name is None or order_name.strip(" ") == "":
        raise ValueError("order_names can not be empty!")
    elif any(p in order_name for p in string.punctuation.replace("_", "")):
        raise ValueError("order_names can not contain punctuation characters!")
    else:
        return order_name
