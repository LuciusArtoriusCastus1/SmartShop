from math import ceil


def filter_rate(products, rate_list):
    products = list(filter(lambda x: x.average_rate is not None, products))
    return list(filter(lambda x: str(ceil(x.average_rate)) in rate_list, products))


def order_rate(products):
    rate_list = [i for i in products if i.average_rate is not None]
    none_list = [i for i in products if i.average_rate is None]
    rate_list = list(sorted(rate_list, key=lambda x: x.average_rate, reverse=True))
    return rate_list + none_list
