# =====================================================================
# FILE: constants.py
# Stake tier-ləri, avatarlar, kart konstantları, tayming dəyərləri
# =====================================================================

# (id, ad, sb, bb, buy_in, min_players, max_players)
STAKE_TIERS = [
    ('micro', 'Micro · 0.20/0.40', 0.20, 0.40,    20, 4, 6),
    ('low',   'Low · 1/2',         1,    2,      100, 4, 6),
    ('mid',   'Mid · 5/10',        5,    10,     500, 4, 6),
    ('high',  'High · 25/50',      25,   50,    2500, 4, 6),
    ('vip',   'VIP · 100/200',     100,  200,  10000, 4, 6),
    ('elite', 'Elite · 500/1000',  500,  1000, 50000, 4, 6),
]

AVATARS = ['🦁', '🐯', '🐺', '🦊', '🐻', '🐼',
           '🐸', '🦅', '🐲', '🦄', '👑', '🎭']

TURN_TIMEOUT   = 30   # saniyə: oyunçunun növbə vaxtı
AUTOSTART_WAIT = 10   # saniy...
