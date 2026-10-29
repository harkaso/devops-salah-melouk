from collections.abc import Sequence

TAX_RATE = 0.09

def average(prices: Sequence[int|float]) -> float:
    if not prices:
        return 0
    return sum(prices) / len(prices)

def total(prices: Sequence[int|float]) -> float:
    """Cart total, taxes included."""
    return round(sum(prices) * (1+ TAX_RATE), 2)

def apply_discount(prices: Sequence[int|float], percent: int) -> Sequence[int|float]:
    return [price * (1 - percent/100) for price in prices]

def count(prices: Sequence[int|float]) -> int:
    return len(prices)
