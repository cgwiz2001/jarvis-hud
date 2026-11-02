#!/usr/bin/env python3
"""Write a salted PBKDF2-SHA256 hash of $JARVIS_HUD_PIN into index.html. Never prints the PIN."""
import os, re, sys, base64, hashlib, pathlib
pin = os.environ.get("JARVIS_HUD_PIN", "")
if not pin: sys.exit("JARVIS_HUD_PIN is not set")
it = 600000; salt = os.urandom(16)
h = hashlib.pbkdf2_hmac("sha256", pin.encode(), salt, it, 32)
p = pathlib.Path(__file__).resolve().parent.parent / "index.html"
s = p.read_text()
new = 'const PIN={salt:"%s",iter:%d,hash:"%s"};' % (base64.b64encode(salt).decode(), it, base64.b64encode(h).decode())
s2, n = re.subn(r'const PIN=\{[^}]*\};', new, s)
assert n == 1
p.write_text(s2); print("PIN hash written (value not shown)")
