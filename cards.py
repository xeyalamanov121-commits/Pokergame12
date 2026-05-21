# =====================================================================
# FILE: cards.py
# Kart dəstəsinin yaradılması və 5 kartlıq əllərin qiymətləndirilməsi
# =====================================================================
from itertools import combinations
from collections import Counter

from constants import SUITS, RANKS, RANK_VAL, HAND_NAMES  # noqa: F401


def make_deck():
    """52 kartlıq standart dəstə qaytarır."""
    return [
        {'rank': r, 'suit': s, 'red': s in ['♥', '♦']}
        for s in SUITS for r in RANKS
    ]


def _rv(c):
    return RANK_VAL[c['rank']]


def evaluate_5(cards):
    """5 kartlıq əlin qiymətləndirilməsi.
    Qaytarır: (category, [kicker-lər]) — böyüklük tuple müqayisəsi ilə işləyir.
    """
    vals = sorted([_rv(c) for c in cards], reverse=True)
    suits = [c['suit'] for c in cards]
    is_flush = len(set(suits)) == 1
    is_straight = (vals == list(range(vals[0], vals[0] - 5, -1)))

    # Wheel straight: A-2-3-4-5
    if not is_straight and vals[0] == 14 and vals[1:] == [5, 4, 3, 2]:
        is_straight = True
        vals = [5, 4, 3, 2, ...

