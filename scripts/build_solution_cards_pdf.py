from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas


OUTPUT_PATH = Path("output/pdf/terminus-solution-cards-paysage.pdf")
PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

FONT_REGULAR = "ArialTerminus"
FONT_BOLD = "ArialTerminusBold"
FONT_CODE = "ConsolasTerminus"

COLORS = {
    "bg": colors.HexColor("#F5F0E7"),
    "ink": colors.HexColor("#18232F"),
    "muted": colors.HexColor("#596674"),
    "line": colors.HexColor("#C9D4DD"),
    "shadow": colors.HexColor("#DDE5EC"),
    "blue": colors.HexColor("#254E70"),
    "green": colors.HexColor("#2F6F55"),
    "orange": colors.HexColor("#CC741F"),
    "gold": colors.HexColor("#BD9119"),
    "red": colors.HexColor("#B8483D"),
    "soft_blue": colors.HexColor("#EAF2F8"),
    "soft_green": colors.HexColor("#ECF6F0"),
    "soft_orange": colors.HexColor("#FCF1E4"),
    "soft_gold": colors.HexColor("#FBF4DF"),
    "soft_red": colors.HexColor("#F9E8E5"),
    "white": colors.white,
}


CARDS = {
    "start": {
        "title": "Départ",
        "lines": ["ls", "cat Palourde"],
        "x": 20,
        "y": 396,
        "w": 96,
        "h": 82,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
    },
    "forest": {
        "title": "BoisDesLutins",
        "lines": ["ls", "cat RentreChezToi"],
        "x": 132,
        "y": 396,
        "w": 108,
        "h": 82,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    "academy": {
        "title": "AcadémieDesBots",
        "lines": [
            "ls",
            "cd Cours",
            "cat Professeur",
            "cd ../SalleDEntrainement",
            "ls",
            "mv Pilier* ~/",
        ],
        "x": 254,
        "y": 382,
        "w": 148,
        "h": 96,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    "prairie": {
        "title": "Prairie",
        "lines": ["ls", "cat Poney"],
        "x": 416,
        "y": 396,
        "w": 100,
        "h": 82,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    "mountains": {
        "title": "Montagnes",
        "lines": ["ls", "cat VieilHomme", "cat Manuscrit"],
        "x": 530,
        "y": 396,
        "w": 110,
        "h": 82,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    "cave": {
        "title": "Cave et Portail",
        "lines": [
            "ls",
            "cd SombreCorridor",
            "cd Cellier",
            "ls",
            "mv Rocher PetitRenfoncement",
            "cd Tunnel",
            "ls",
            "cd ChambreDePierre",
            "cd Portail",
            "ls",
        ],
        "x": 664,
        "y": 282,
        "w": 158,
        "h": 196,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
    },
    "hub": {
        "title": "PlaceDuVillage",
        "lines": [
            "hub principal",
            "faire chaque branche",
            "puis revenir ici",
        ],
        "x": 328,
        "y": 242,
        "w": 184,
        "h": 88,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
    },
    "market": {
        "title": "PlaceDuMarché",
        "lines": [
            "ls",
            "cat SacÀDos",
            "unzip SacÀDos.zip",
            "cat Vendeur -> mkdir",
            "cat Vendeur -> rm",
        ],
        "x": 28,
        "y": 276,
        "w": 190,
        "h": 94,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
        "side": "left",
        "anchor_y": 323,
        "return_cmd": "cd ..",
        "go_cmd": "cd PlaceDuMarché",
    },
    "shop": {
        "title": "BoutiqueArtisanale",
        "lines": [
            "ls",
            "cat Artisane",
            "touch rouage",
            "cp rouage rouage1",
            "cp rouage rouage2",
            "cp rouage rouage3",
            "cp rouage rouage4",
            "cp rouage rouage5",
        ],
        "x": 28,
        "y": 156,
        "w": 190,
        "h": 106,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
        "side": "left",
        "anchor_y": 209,
        "return_cmd": "cd ..",
        "go_cmd": "cd BoutiqueArtisanale",
    },
    "library": {
        "title": "Bibliothèque",
        "lines": [
            "ls",
            "./IntrigantLevier",
            "cd PièceSecrète",
            "cat Grep",
        ],
        "x": 624,
        "y": 276,
        "w": 190,
        "h": 94,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
        "side": "right",
        "anchor_y": 323,
        "return_cmd": "cd ../..",
        "go_cmd": "cd Bibliothèque",
    },
    "rocky": {
        "title": "CheminEnPierres",
        "lines": ["ls", "rm ÉnormeRocher"],
        "x": 624,
        "y": 164,
        "w": 190,
        "h": 78,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
        "side": "right",
        "anchor_y": 203,
        "return_cmd": "cd ..",
        "go_cmd": "cd CheminEnPierres",
    },
    "bridge": {
        "title": "PontCassé et Clairière",
        "lines": [
            "ls",
            "touch Planche",
            "cd Clairière",
            "ls",
            "mkdir Maison",
        ],
        "x": 188,
        "y": 26,
        "w": 150,
        "h": 112,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
    },
    "trolls": {
        "title": "CheminInquiétant",
        "lines": [
            "rm RoncesTordues",
            "cd CaveDesTrolls",
            "ls",
            "rm TrollMoche",
            "mv Cage/EnfantKidnapé .",
            "cd Toboggan",
        ],
        "x": 406,
        "y": 26,
        "w": 168,
        "h": 112,
        "fill": COLORS["soft_red"],
        "stroke": COLORS["red"],
    },
    "final": {
        "title": "FichiersNoyau -> Paradis",
        "lines": [
            "ls",
            "cat Prospectus",
            "cat Instructions",
            "cd PlusDeFichiersNoyau",
            "grep pass *.txt",
            "mot de passe : IHTFP",
            "cd ..",
            "sudo cat Certificat",
            "cd Paradis",
            "ls",
        ],
        "x": 620,
        "y": 18,
        "w": 202,
        "h": 128,
        "fill": COLORS["soft_gold"],
        "stroke": COLORS["gold"],
    },
}


TOP_LINKS = [
    ("start", "forest", "cd BoisDesLutins"),
    ("forest", "academy", "cd AcadémieDesBots"),
    ("academy", "prairie", "cd ~/Prairie"),
    ("prairie", "mountains", "cd Montagnes"),
    ("mountains", "cave", "cd Cave"),
]


def register_fonts():
    pdfmetrics.registerFont(TTFont(FONT_REGULAR, "C:/Windows/Fonts/arial.ttf"))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, "C:/Windows/Fonts/arialbd.ttf"))
    pdfmetrics.registerFont(TTFont(FONT_CODE, "C:/Windows/Fonts/consola.ttf"))


def make_styles():
    return {
        "title": ParagraphStyle(
            "title",
            fontName=FONT_BOLD,
            fontSize=21,
            leading=25,
            textColor=colors.white,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            fontName=FONT_REGULAR,
            fontSize=9.4,
            leading=11.4,
            textColor=colors.white,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            fontName=FONT_BOLD,
            fontSize=10.9,
            leading=13.2,
            textColor=colors.white,
        ),
        "code": ParagraphStyle(
            "code",
            fontName=FONT_CODE,
            fontSize=6.8,
            leading=7.8,
            textColor=COLORS["ink"],
        ),
        "small": ParagraphStyle(
            "small",
            fontName=FONT_REGULAR,
            fontSize=8.0,
            leading=9.6,
            textColor=COLORS["muted"],
        ),
        "label": ParagraphStyle(
            "label",
            fontName=FONT_CODE,
            fontSize=7.0,
            leading=8.0,
            alignment=1,
            textColor=COLORS["muted"],
        ),
    }


def draw_paragraph(pdf, text, style, x, top_y, width):
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, top_y - height)
    return height


def draw_panel(pdf, x, y, width, height, fill, stroke, radius=18, line_width=1.2):
    pdf.setFillColor(COLORS["shadow"])
    pdf.roundRect(x + 3, y - 3, width, height, radius, fill=1, stroke=0)
    pdf.setFillColor(fill)
    pdf.setStrokeColor(stroke)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_card(pdf, styles, card):
    draw_panel(pdf, card["x"], card["y"], card["w"], card["h"], card["fill"], card["stroke"])
    pdf.setFillColor(card["stroke"])
    pdf.roundRect(card["x"], card["y"] + card["h"] - 28, card["w"], 28, 18, fill=1, stroke=0)
    draw_paragraph(pdf, card["title"], styles["card_title"], card["x"] + 11, card["y"] + card["h"] - 5, card["w"] - 22)
    top = card["y"] + card["h"] - 39
    for index, line in enumerate(card["lines"]):
        draw_paragraph(pdf, line, styles["code"], card["x"] + 11, top - index * 8.2, card["w"] - 22)


def draw_arrow_head(pdf, start, end):
    sx, sy = start
    ex, ey = end
    dx = ex - sx
    dy = ey - sy
    length = max((dx * dx + dy * dy) ** 0.5, 1)
    ux = dx / length
    uy = dy / length
    size = 5.6
    px = ex - ux * 8
    py = ey - uy * 8
    left_x = px - uy * size
    left_y = py + ux * size
    right_x = px + uy * size
    right_y = py - ux * size
    pdf.line(ex, ey, left_x, left_y)
    pdf.line(ex, ey, right_x, right_y)


def draw_poly_arrow(pdf, points, stroke=None, width=1.6):
    pdf.setStrokeColor(stroke or COLORS["line"])
    pdf.setLineWidth(width)
    for start, end in zip(points, points[1:]):
        pdf.line(start[0], start[1], end[0], end[1])
    draw_arrow_head(pdf, points[-2], points[-1])


def label_width(text):
    return min(max(54, int(len(text) * 4.7 + 18)), 118)


def draw_label_box(pdf, styles, text, center_x, center_y, width=None):
    box_width = width or label_width(text)
    box_height = 16
    x = center_x - box_width / 2
    y = center_y - box_height / 2
    pdf.setFillColor(COLORS["white"])
    pdf.setStrokeColor(COLORS["line"])
    pdf.setLineWidth(0.9)
    pdf.roundRect(x, y, box_width, box_height, 7, fill=1, stroke=1)
    draw_paragraph(pdf, text, styles["label"], x + 5, y + box_height - 1, box_width - 10)


def right_center(card):
    return (card["x"] + card["w"], card["y"] + card["h"] / 2)


def left_center(card):
    return (card["x"], card["y"] + card["h"] / 2)


def top_center(card):
    return (card["x"] + card["w"] / 2, card["y"] + card["h"])


def bottom_center(card):
    return (card["x"] + card["w"] / 2, card["y"])


def draw_top_link(pdf, styles, left_card, right_card, text):
    start = right_center(left_card)
    end = left_center(right_card)
    y = (start[1] + end[1]) / 2
    draw_poly_arrow(pdf, [(start[0], y), (end[0], y)])
    label_y = max(left_card["y"] + left_card["h"], right_card["y"] + right_card["h"]) + 12
    draw_label_box(pdf, styles, text, (start[0] + end[0]) / 2, label_y)


def draw_parallel_branch_link(pdf, styles, hub_card, branch_card):
    branch_mid_x = branch_card["x"] + branch_card["w"] if branch_card["side"] == "left" else branch_card["x"]
    hub_mid_x = hub_card["x"] if branch_card["side"] == "left" else hub_card["x"] + hub_card["w"]
    y = branch_card["anchor_y"]
    out_y = y + 7
    back_y = y - 7

    if branch_card["side"] == "left":
        draw_poly_arrow(pdf, [(hub_mid_x, out_y), (branch_mid_x, out_y)])
        draw_poly_arrow(pdf, [(branch_mid_x, back_y), (hub_mid_x, back_y)])
    else:
        draw_poly_arrow(pdf, [(hub_mid_x, out_y), (branch_mid_x, out_y)])
        draw_poly_arrow(pdf, [(branch_mid_x, back_y), (hub_mid_x, back_y)])

    mid_x = (hub_mid_x + branch_mid_x) / 2
    draw_label_box(pdf, styles, branch_card["go_cmd"], mid_x, out_y + 14)
    draw_label_box(pdf, styles, branch_card["return_cmd"], mid_x, back_y - 14, width=64 if branch_card["return_cmd"] == "cd .." else 76)


def build_pdf():
    register_fonts()
    styles = make_styles()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    pdf = canvas.Canvas(str(OUTPUT_PATH), pagesize=landscape(A4))
    pdf.setTitle("Terminus - solution cards paysage")
    pdf.setAuthor("Codex")

    pdf.setFillColor(COLORS["bg"])
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    pdf.setFillColor(COLORS["blue"])
    pdf.rect(0, PAGE_HEIGHT - 64, PAGE_WIDTH, 64, fill=1, stroke=0)
    pdf.setFillColor(COLORS["gold"])
    pdf.rect(0, PAGE_HEIGHT - 68, PAGE_WIDTH, 4, fill=1, stroke=0)

    draw_paragraph(pdf, "Terminus - solution en cards", styles["title"], 24, PAGE_HEIGHT - 12, 420)
    draw_paragraph(
        pdf,
        "Toutes les flèches affichent la vraie commande pour avancer ou revenir.",
        styles["subtitle"],
        24,
        PAGE_HEIGHT - 37,
        470,
    )
    draw_label_box(pdf, styles, "haut = aller", 707, PAGE_HEIGHT - 28, 86)
    draw_label_box(pdf, styles, "bas = retour", 793, PAGE_HEIGHT - 28, 90)

    for card in CARDS.values():
        draw_card(pdf, styles, card)

    for left_key, right_key, text in TOP_LINKS:
        draw_top_link(pdf, styles, CARDS[left_key], CARDS[right_key], text)

    draw_poly_arrow(
        pdf,
        [
            left_center(CARDS["cave"]),
            (596, 386),
            (558, 356),
            (486, CARDS["hub"]["y"] + CARDS["hub"]["h"]),
        ],
    )
    draw_label_box(pdf, styles, "cd PlaceDuVillage", 606, 401, 94)

    draw_parallel_branch_link(pdf, styles, CARDS["hub"], CARDS["market"])
    draw_parallel_branch_link(pdf, styles, CARDS["hub"], CARDS["shop"])
    draw_parallel_branch_link(pdf, styles, CARDS["hub"], CARDS["library"])
    draw_parallel_branch_link(pdf, styles, CARDS["hub"], CARDS["rocky"])

    bridge_top = top_center(CARDS["bridge"])
    hub_bottom = bottom_center(CARDS["hub"])
    draw_poly_arrow(pdf, [(hub_bottom[0], hub_bottom[1]), bridge_top])
    draw_label_box(pdf, styles, "cd PontCassé", 344, 182, 78)

    draw_poly_arrow(pdf, [right_center(CARDS["bridge"]), (338, 148), (406, 148), left_center(CARDS["trolls"])])
    draw_label_box(pdf, styles, "cd CheminInquiétant", 372, 156, 108)

    draw_poly_arrow(pdf, [right_center(CARDS["trolls"]), (574, 148), (620, 148), left_center(CARDS["final"])])
    draw_label_box(pdf, styles, "cd FichiersNoyau", 597, 156, 92)

    pdf.setFont(FONT_REGULAR, 8.0)
    pdf.setFillColor(COLORS["muted"])
    pdf.drawString(24, 12, "Version revérifiée sur le build local : sans chemin inventé.")

    pdf.save()
    print(f"written {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
