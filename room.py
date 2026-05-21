# =====================================================================
# FILE: room.py
# Bir poker masasının tam state-i + bütün hərəkət məntiqi
# =====================================================================
import random
import time
from collections import OrderedDict

import eventlet
import socketio as _sio_lib  # noqa: F401  (sio referansı events-də import olur)

from constants import TURN_TIMEOUT, AUTOSTART_WAIT, HAND_NAMES
from cards import make_deck, best_hand_score


class GameRoom:
    def __init__(self, room_id, tier_id, tier_name,
                 sb, bb, buy_in, min_p, max_p):
        self.room_id     = room_id
        self.tier_id     = tier_id
        self.tier_name   = tier_name
        self.SB          = sb
        self.BB          = bb
        self.buy_in      = buy_in
        self.min_players = min_p
        self.max_players = max_p

        self.players     = OrderedDict()   # sid -> player dict
        self.spectators  = set()
        self.phase       = 'waiting'
        self.deck        = []
        self.community   = []
        self.pot         = 0
        self.current_bet = 0
        self.dealer_idx  = 0
        self.to_act      = []
        self.round_num   = 0
        self.sb_sid      = None
        self.bb_sid      = None
        self.last_raise  = bb

        self.turn_...
