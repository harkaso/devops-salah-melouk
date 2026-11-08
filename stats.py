def most_exepensive(prices):
    """Price of the most expensive item in the list, None for an empty cart."""
    if not prices:
        return None
    return max(prices)