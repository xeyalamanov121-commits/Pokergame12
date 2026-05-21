# =====================================================================
# FILE: server.py
# Entry point: Socket.IO + eventlet WSGI + static fayl xidməti
# Çalışdırmaq: python server.py   (PORT env dəstəklənir, default 8080)
# =====================================================================
import os
import mimetypes

import eventlet
eventlet.monkey_patch()                  # MUST be before any other I/O

import eventlet.wsgi                     # noqa: E402
import socketio                          # noqa: E402

from constants import STAKE_TIERS        # noqa: E402
from lobby import init_lobby_rooms, rooms  # noqa: E402
from events import register_events       # noqa: E402


# ──────────────────────────────────────────────────────────
# Socket.IO server (events.py bu instance-a register edir)
# ──────────────────────────────────────────────────────────
sio = socketio.Server(cors_allowed_origins="*", async_mode='eventlet')
register_events(sio)


# ──────────────────────────────────────────────────────────
# Static fayl serveri (HTML / CSS / JS)
# ──────────────────────────────────────────────────────────
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')


def static_app(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    if path == '/health':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'ok']

    if path in ('/', '/index.html'):
        rel = 'index.html'
    else:
        rel = path.lstrip('/')

    file_path = os.path.normpath(os.path.join(STATIC_DIR, rel))
    if not file_path.startswith(STATIC_DIR) or not os.path.isfile(file_path):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']

    ctype, _ = mimetypes.guess_type(file_path)
    ctype = ctype or 'application/octet-stream'
    with open(file_path, 'rb') as f:
        data = f.read()
    start_response('200 OK', [
        ('Content-Type', ctype + '; charset=utf-8'),
        ('Content-Length', str(len(data))),
    ])
    return [data]


app = socketio.WSGIApp(sio, static_app)


# ──────────────────────────────────────────────────────────
# ENTRY POINT
# ──────────────────────────────────────────────────────────
if __name__ == '__main__':
    init_lobby_rooms()
    port = int(os.environ.get('PORT', 8080))
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('  TEXAS HOLD\'EM POKER — Premium Edition')
    print(f'  Port: {port}')
    print(f'  Tiers...')
