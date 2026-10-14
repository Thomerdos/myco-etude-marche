import re
for n in ("index", "02", "05"):
    s = open(f"{n}.html", encoding="utf-8").read()
    s = re.sub(r'/myco-etude-marche/assets/css/style\.css\?v=[0-9a-f]+', 'fixed.css', s)
    open(f"fixed-{n}.html", "w", encoding="utf-8").write(s)
