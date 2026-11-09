from bisect import bisect_left


def suggested_products(products, search_word):
    products = sorted(products)
    out = []
    prefix = ""
    start = 0
    for char in search_word:
        prefix += char
        start = bisect_left(products, prefix, start)   # first product >= prefix
        out.append([p for p in products[start:start + 3] if p.startswith(prefix)])
    return out
