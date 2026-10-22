TAX_RATE = 0.19

def average(prices: list[int|float]) -> float:
    return sum(prices) / len(prices)

def total(prices: list[int|float]) -> float:
    """Cart total, taxes included."""
    return round(sum(prices) * (1+ TAX_RATE), 2)

def apply_discount(prices: list[int|float], percent: int) -> list[int|float]:
    return [price * (1 - percent/100) for price in prices]
