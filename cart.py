TAX_RATE = 0.19

def average(prices: list[int|float]) -> float:
    if not prices:
        return 0
    return sum(prices) / len(prices)

def total(prices: list[int|float]) -> float:
    """Cart total, taxes included."""
    return round(sum(prices) * (1+ TAX_RATE), 2)
