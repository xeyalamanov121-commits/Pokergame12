# =====================================================================
# FILE: events.py
# Socket.IO event handler-ləri: connect / disconnect / lobby / join /
# leave / player_action / chat
# =====================================================================
from constants import AVATARS
from lobby import (
    rooms, lobby_users,
    lobby_snapshot, table_snapshot,
    broadcast_lobby, broadcast_table_update, broadcast_result,
)


# ──────────────────────────────────────────────────────────
# avto-start callback (lobby.py-də referans alınır)
# ──────────────────────────────────────────────────────────
def auto_start_room(room):
    """Min oyunçu varsa raundu başlat və hamıya bildiriş göndər."""
    from server import sio  # late import: server-də qurulan instance
    if room.phase != 'waiting':
        return
    if len(room.players) < room.min_players:
        return

    sb_sid, bb_sid = room.start_round()  # noqa: F841
    state = room.get_state()

    # Aktiv oyunçulara öz hand-ı ilə
    for ps in room.players:
        hand = room.players[ps]['hand']
        your_turn = bool(room.to_act and room.to_act[0] == ps)
        sio.emit('round_started', {
            'hand':       hand,
            'state':      state,
            'players':    room.public_players(reveal_sids=[ps]),
            'sb':         room.SB,
            'bb':         room.BB,
            'your_turn':  your_turn,
...

