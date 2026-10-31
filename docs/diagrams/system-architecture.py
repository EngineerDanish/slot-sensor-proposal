"""Source for system-architecture.svg and system-architecture.png.

Run:  python3 system-architecture.py
Writes the SVG next to this file, then renders the PNG (about 2000 px wide)
with Playwright/Chromium. Hand-placed layout; edit coordinates below.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
W, H = 1400, 1010

INK = "#1f2933"
LINE = "#34495e"
MUTED = "#52606d"
FONT = "Inter, Arial, Helvetica, sans-serif"

out = []


def add(s):
    out.append(s)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=19, weight="normal", anchor="start", fill=INK, style="normal"):
    add(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" fill="{fill}" font-style="{style}">{esc(s)}</text>')


def box(x, y, w, h, lines, fill="#ffffff", dashed=False, title_size=20, size=17, gap=23, bold=1):
    """Rounded box with a bold first line and lighter following lines, centred."""
    dash = ' stroke-dasharray="9 6"' if dashed else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
        f'stroke="{LINE}" stroke-width="2"{dash}/>')
    n = len(lines)
    total = title_size + (n - 1) * gap
    cy = y + h / 2 - total / 2 + title_size * 0.8
    for i, ln in enumerate(lines):
        if i < bold:
            text(x + w / 2, cy, ln, size=title_size, weight="600", anchor="middle")
            cy += gap + 2 if i == bold - 1 else title_size + 4
        else:
            italic = "italic" if ln.startswith("(optional") else "normal"
            text(x + w / 2, cy, ln, size=size, anchor="middle", fill=MUTED, style=italic)
            cy += gap


def path(d, dashed=False, arrow_end=True, arrow_start=False, width=2.2):
    dash = ' stroke-dasharray="9 6"' if dashed else ""
    me = ' marker-end="url(#arr)"' if arrow_end else ""
    ms = ' marker-start="url(#arrs)"' if arrow_start else ""
    add(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="{width}"{dash}{me}{ms}/>')


# ---------------------------------------------------------------- header
add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
    f'font-family="{FONT}">')
add('<defs>'
    f'<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker>'
    f'<marker id="arrs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
    f'<path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker>'
    '</defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fbfaf7"/>')

text(30, 48, "16-slot sensing unit: system overview", size=30, weight="700")
text(30, 80, "Every place or remove event reaches the web dashboard over LoRaWAN "
     "and nearby phones over Bluetooth", size=19, fill=MUTED)

# column headers
for x, label in ((30, "THE UNIT (AT THE SITE)"), (780, "RADIO AND PHONE"), (1130, "ONLINE SERVICE")):
    text(x, 122, label, size=15, weight="700", fill=MUTED)
add(f'<line x1="30" y1="131" x2="1390" y2="131" stroke="#d3d8de" stroke-width="1.5"/>')

# ---------------------------------------------------------------- electronics bay
add(f'<rect x="30" y="145" width="570" height="455" rx="14" fill="#edf1f5" stroke="{LINE}" stroke-width="2.5"/>')
text(48, 176, "Sealed electronics bay", size=22, weight="700")
text(48, 200, "weatherproof box with breather vent", size=16, fill=MUTED)

box(45, 218, 270, 155, ["Replaceable lithium", "battery", "two 18650-class cells or",
                         "one D-size primary cell,", "with pulse buffer"], size=16, gap=22, bold=2)
box(375, 255, 210, 80, ["Low-power", "regulator"], size=20, gap=24, title_size=20)
box(45, 420, 270, 140, ["Switch reader", "16-input expander,", "wakes the radio", "on any change"])
box(375, 420, 210, 140, ["Radio module", "Bluetooth and", "LoRaWAN in one"])

# power
path("M315,295 L373,295")
text(345, 285, "power", size=15, anchor="middle", fill=MUTED)
path("M480,335 L480,418")
path("M400,335 L400,395 L180,395 L180,418")
# reader to radio
path("M315,490 L373,490")

# external LoRa antenna: stub out of the bay and a mast
add(f'<path d="M585,450 L640,450 L640,395" fill="none" stroke="{LINE}" stroke-width="2.5"/>')
add(f'<path d="M628,378 L640,395 L652,378 M640,378 L640,395" fill="none" stroke="{LINE}" stroke-width="2.5"/>')
text(610, 474, "External", size=16, fill=MUTED)
text(610, 494, "LoRa antenna", size=16, fill=MUTED)

# ---------------------------------------------------------------- slot body
path("M180,688 L180,562")
text(195, 640, "sealed switch cable", size=16, fill=MUTED)

add(f'<rect x="30" y="690" width="570" height="120" rx="14" fill="#f3efe6" stroke="{LINE}" stroke-width="2.5"/>')
text(48, 720, "Slot body, 24 inches long", size=22, weight="700")
sec_w = 132
for i in range(4):
    sx = 45 + i * (sec_w + 7)
    add(f'<rect x="{sx}" y="734" width="{sec_w}" height="62" rx="6" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>')
    for j in range(4):
        cx = sx + 15 + j * 29
        add(f'<rect x="{cx}" y="744" width="18" height="18" rx="3" fill="#ffffff" stroke="{LINE}" stroke-width="2"/>')
        add(f'<circle cx="{cx + 9}" cy="753" r="4" fill="{LINE}"/>')
    text(sx + sec_w / 2, 786, "6 in section", size=14, anchor="middle", fill=MUTED)
text(30, 840, "Four 6 inch sections with 4 switches each:", size=17, fill=INK)
text(30, 864, "16 sealed switches in total, one per slot", size=17, fill=INK)

# ---------------------------------------------------------------- LoRaWAN path
# main radio link to public hotspot
path("M646,395 L778,395")
text(705, 362, "LoRaWAN", size=16, anchor="middle", fill=MUTED)
text(705, 382, "radio link", size=16, anchor="middle", fill=MUTED)
box(780, 340, 260, 110, ["Helium hotspot", "public network,", "coverage at the site"])

# optional client-owned gateway, branch from the radio link
path("M740,397 L740,580 L778,580", dashed=True)
box(780, 515, 260, 130, ["Client-owned gateway", "at the site, instead of", "public hotspots", "(optional)"],
    dashed=True)

box(1130, 340, 260, 110, ["LoRaWAN", "network server"])
path("M1040,395 L1128,395")
text(1085, 384, "internet", size=15, anchor="middle", fill=MUTED)
path("M1040,580 L1085,580 L1085,430 L1128,430", dashed=True)

# hosting region
add(f'<rect x="1110" y="490" width="280" height="410" rx="14" fill="#f4f6f8" stroke="{LINE}" '
    f'stroke-width="2" stroke-dasharray="9 6"/>')
box(1130, 510, 245, 100, ["Backend and", "database"], size=20, gap=24, title_size=20)
box(1130, 680, 245, 120, ["Web dashboard", "users log in", "from a browser"])
path("M1252,450 L1252,508")
path("M1252,610 L1252,678")
text(1252, 840, "Live hosting and", size=17, anchor="middle", fill=MUTED, style="italic")
text(1252, 862, "monitoring service", size=17, anchor="middle", fill=MUTED, style="italic")
text(1252, 884, "(optional)", size=17, anchor="middle", fill=MUTED, style="italic")

# ---------------------------------------------------------------- Bluetooth path
path("M585,525 L700,525 L700,800 L778,800")
text(780, 690, "Bluetooth broadcast,", size=16, fill=MUTED)
text(780, 711, "encrypted so only the", size=16, fill=MUTED)
text(780, 732, "client's app can read it", size=16, fill=MUTED)
box(780, 750, 260, 110, ["Mobile app", "on the client's phone"])

# optional firmware update over Bluetooth from the app
path("M778,840 L670,840 L670,550 L587,550", dashed=True)
text(780, 890, "Firmware update over", size=16, fill=MUTED, style="italic")
text(780, 911, "Bluetooth from the app", size=16, fill=MUTED, style="italic")
text(780, 932, "(optional)", size=16, fill=MUTED, style="italic")

# ---------------------------------------------------------------- legend
lx, ly = 30, 940
add(f'<rect x="{lx}" y="{ly - 30}" width="570" height="62" rx="10" fill="#ffffff" stroke="#c4cbd3" stroke-width="1.5"/>')
text(lx + 18, ly + 7, "Legend", size=16, weight="700")
path(f"M{lx + 100},{ly} L{lx + 160},{ly}")
text(lx + 172, ly + 6, "included", size=16)
path(f"M{lx + 275},{ly} L{lx + 335},{ly}", dashed=True)
text(lx + 347, ly + 6, "optional, offered separately", size=16)

add("</svg>")

svg = "\n".join(out) + "\n"
assert chr(0x2014) not in svg  # no long dash anywhere
svg_path = HERE / "system-architecture.svg"
svg_path.write_text(svg, encoding="utf-8")

# ---------------------------------------------------------------- PNG
from playwright.sync_api import sync_playwright  # noqa: E402

scale = 2000 / W
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=scale)
    pg.goto(svg_path.as_uri())
    pg.screenshot(path=str(HERE / "system-architecture.png"), clip={"x": 0, "y": 0, "width": W, "height": H})
    b.close()
print("wrote", svg_path, "and PNG")
