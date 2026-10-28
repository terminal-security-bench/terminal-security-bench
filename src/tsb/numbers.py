"""Exact ratios and their percentages, rounded half up as the paper prints them.

A rate is kept as a `Fraction` so that a value that lies exactly on a rounding boundary is rounded
the same way every time. In floating point, 204/320 becomes 63.74999999999999 and prints as 63.7,
while the paper prints the exact value 63.75 as 63.8.
"""
from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction


def ratio(num: int, den: int) -> Fraction | None:
    return Fraction(num, den) if den else None


def mean(values) -> Fraction | None:
    values = list(values)
    return sum(values, Fraction(0)) / len(values) if values else None


def pct(x: Fraction | None, digits: int = 1) -> str:
    """`x` as a percentage with `digits` decimals, rounded half up; `-` when undefined."""
    if x is None:
        return "-"
    exact = Decimal(x.numerator * 100) / Decimal(x.denominator)
    return str(exact.quantize(Decimal(1).scaleb(-digits), rounding=ROUND_HALF_UP))
