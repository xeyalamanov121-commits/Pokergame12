# =====================================================================
# FILE: lobby.py
# Otaqların yaradılması, lobby snapshot-ları, table broadcast helpers
# =====================================================================
from collections import OrderedDict

from constants import STAKE_TIERS
from room import GameRoom


# Qlobal vəziyyət (bütün modullar bunu paylaşır)
rooms        = OrderedDict()   # room_id -> GameRoom
lobby_users  = {}              # sid -> {'name', 'avatar'}


def init_lobby_rooms():
    """Hər tier üçün 2 otaq pre-create edirik."""
    for (tid, tname, sb, bb, buyin, minp, maxp) in STAKE_TIERS:
        for i in range(1, 3):
            rid = f"{tid.upper()}-{i:02d}"
            rooms[rid] = GameRoom(rid, tid, tname, sb, bb, buyin, minp, maxp)


def lobby_snapshot():
    return {
        'online': len(lobby_users) + sum(
            len(r.players) + len(r.spectators) for r in rooms.values()
        ),
        'tiers':  [{'id': t[0], 'name': t[1]} for t in STAKE_TIERS],
        'rooms':  [{
            'id':           r.room_id,
            'tier':         r.tier_id,
            'tier_name':    r.tier_name,
            'sb':           r.SB,
            'bb':           r.BB,
            'buy_in':       r.buy_in,
...
