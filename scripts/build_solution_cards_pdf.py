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
    "bg": colors.HexColor("#F6F1E8"),
    "ink": colors.HexColor("#17212B"),
    "muted": colors.HexColor("#5D6975"),
    "line": colors.HexColor("#C8D2DD"),
    "blue": colors.HexColor("#234E70"),
    "green": colors.HexColor("#2D6A4F"),
    "orange": colors.HexColor("#C96B1F"),
    "gold": colors.HexColor("#B88A1B"),
    "red": colors.HexColor("#B44338"),
    "soft_blue": colors.HexColor("#EAF2F8"),
    "soft_green": colors.HexColor("#EBF6EF"),
    "soft_orange": colors.HexColor("#FCF1E5"),
    "soft_gold": colors.HexColor("#FBF3DE"),
    "soft_red": colors.HexColor("#F9E8E5"),
}


MAIN_CARDS = [
    {
        "title": "Départ",
        "lines": [
            "ls",
            "cat Palourde",
            "cd BoisDesLutins",
        ],
        "x": 20,
        "y": 392,
        "w": 96,
        "h": 78,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
    },
    {
        "title": "BoisDesLutins",
        "lines": [
            "cat RentreChezToi",
            "cd AcadémieDesBots/Cours",
        ],
        "x": 132,
        "y": 392,
        "w": 112,
        "h": 78,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "Académie",
        "lines": [
            "cat Professeur",
            "cd ../SalleDEntrainement",
            "mv Pilier* ~/",
        ],
        "x": 260,
        "y": 380,
        "w": 136,
        "h": 90,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "Prairie",
        "lines": [
            "cd ~/Prairie",
            "cat Poney",
        ],
        "x": 412,
        "y": 392,
        "w": 102,
        "h": 78,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "Montagnes",
        "lines": [
            "cd Montagnes",
            "cat VieilHomme",
            "cat Manuscrit",
        ],
        "x": 530,
        "y": 392,
        "w": 112,
        "h": 78,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "Cave -> Portail",
        "lines": [
            "cd Cave/SombreCorridor/Cellier",
            "mv Rocher PetitRenfoncement",
            "cd .../PlaceDuVillage",
        ],
        "x": 658,
        "y": 380,
        "w": 164,
        "h": 90,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
    },
]


HUB_CARD = {
    "title": "PlaceDuVillage",
    "lines": [
            "hub principal",
            "tu pars en branche",
            "puis tu reviens ici",
    ],
    "x": 334,
    "y": 234,
    "w": 174,
    "h": 84,
    "fill": COLORS["soft_blue"],
    "stroke": COLORS["blue"],
}


BRANCH_CARDS = [
    {
        "title": "Marché",
        "lines": [
            "cd PlaceDuMarché",
            "cat SacÀDos",
            "unzip SacÀDos.zip",
            "acheter mkdir puis rm",
        ],
        "x": 50,
        "y": 252,
        "w": 190,
        "h": 80,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
        "anchor_y": 292,
        "side": "left",
    },
    {
        "title": "Boutique",
        "lines": [
            "cd ../BoutiqueArtisanale",
            "cat Artisane",
            "touch rouage",
            "cp rouage rouage1 ... rouage5",
        ],
        "x": 50,
        "y": 148,
        "w": 190,
        "h": 88,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
        "anchor_y": 192,
        "side": "left",
    },
    {
        "title": "Bibliothèque",
        "lines": [
            "cd ../Bibliothèque",
            "./IntrigantLevier",
            "cd PièceSecrète",
            "cat Grep",
        ],
        "x": 602,
        "y": 252,
        "w": 190,
        "h": 80,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
        "anchor_y": 292,
        "side": "right",
    },
    {
        "title": "CheminEnPierres",
        "lines": [
            "cd ../../CheminEnPierres",
            "rm ÉnormeRocher",
            "option : Ferme",
        ],
        "x": 602,
        "y": 156,
        "w": 190,
        "h": 72,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
        "anchor_y": 192,
        "side": "right",
    },
]


BOTTOM_CARDS = [
    {
        "title": "PontCassé -> Clairière",
        "lines": [
            "cd ../PontCassé",
            "touch Planche",
            "cd Clairière",
            "mkdir Maison",
        ],
        "x": 238,
        "y": 42,
        "w": 168,
        "h": 92,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
    },
    {
        "title": "CaveDesTrolls",
        "lines": [
            "cd CheminInquiétant",
            "rm RoncesTordues",
            "cd CaveDesTrolls",
            "rm TrollMoche",
            "mv Cage/EnfantKidnapé .",
        ],
        "x": 432,
        "y": 30,
        "w": 180,
        "h": 104,
        "fill": COLORS["soft_red"],
        "stroke": COLORS["red"],
    },
    {
        "title": "Finale",
        "lines": [
            "cd Toboggan -> cd FichiersNoyau",
            "cat Prospectus -> cat Instructions",
            "cd PlusDeFichiersNoyau -> grep pass *.txt",
            "Mot de passe : IHTFP",
            "sudo cat Certificat -> cd Paradis -> ls",
        ],
        "x": 638,
        "y": 22,
        "w": 184,
        "h": 112,
        "fill": COLORS["soft_gold"],
        "stroke": COLORS["gold"],
    },
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
            fontSize=22,
            leading=26,
            textColor=colors.white,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            fontName=FONT_REGULAR,
            fontSize=10.2,
            leading=12.8,
            textColor=colors.white,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            fontName=FONT_BOLD,
            fontSize=11.3,
            leading=13.6,
            textColor=colors.white,
        ),
        "code": ParagraphStyle(
            "code",
            fontName=FONT_CODE,
            fontSize=7.4,
            leading=8.7,
            textColor=COLORS["ink"],
        ),
        "small": ParagraphStyle(
            "small",
            fontName=FONT_REGULAR,
            fontSize=8.2,
            leading=10,
            textColor=COLORS["muted"],
        ),
        "arrow": ParagraphStyle(
            "arrow",
            fontName=FONT_REGULAR,
            fontSize=7.7,
            leading=9,
            textColor=COLORS["muted"],
        ),
    }


def draw_paragraph(pdf, text, style, x, top_y, width):
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, top_y - height)
    return height


def draw_round_panel(pdf, x, y, width, height, fill, stroke, radius=20, line_width=1.2):
    pdf.setFillColor(fill)
    pdf.setStrokeColor(stroke)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_card(pdf, styles, card):
    draw_round_panel(pdf, card["x"], card["y"], card["w"], card["h"], card["fill"], card["stroke"])
    pdf.setFillColor(card["stroke"])
    pdf.roundRect(card["x"], card["y"] + card["h"] - 28, card["w"], 28, 18, fill=1, stroke=0)
    draw_paragraph(pdf, card["title"], styles["card_title"], card["x"] + 12, card["y"] + card["h"] - 5, card["w"] - 24)
    top = card["y"] + card["h"] - 40
    for index, line in enumerate(card["lines"]):
        draw_paragraph(pdf, line, styles["code"], card["x"] + 12, top - index * 9, card["w"] - 24)


def draw_one_way_arrow(pdf, start, end):
    sx, sy = start
    ex, ey = end
    pdf.setStrokeColor(COLORS["line"])
    pdf.setLineWidth(1.6)
    pdf.line(sx, sy, ex, ey)

    dx = ex - sx
    dy = ey - sy
    length = max((dx * dx + dy * dy) ** 0.5, 1)
    ux = dx / length
    uy = dy / length
    size = 6
    px = ex - ux * 8
    py = ey - uy * 8
    left_x = px - uy * size
    left_y = py + ux * size
    right_x = px + uy * size
    right_y = py - ux * size
    pdf.line(ex, ey, left_x, left_y)
    pdf.line(ex, ey, right_x, right_y)


def draw_bi_arrow_horizontal(pdf, styles, x1, x2, y, outward="left"):
    offset = 5
    pdf.setStrokeColor(COLORS["line"])
    pdf.setLineWidth(1.4)

    if outward == "left":
        draw_one_way_arrow(pdf, (x2, y + offset), (x1, y + offset))
        draw_one_way_arrow(pdf, (x1, y - offset), (x2, y - offset))
    else:
        draw_one_way_arrow(pdf, (x1, y + offset), (x2, y + offset))
        draw_one_way_arrow(pdf, (x2, y - offset), (x1, y - offset))

    label_x = (x1 + x2) / 2 - 16
    draw_paragraph(pdf, "retour", styles["arrow"], label_x, y - 10, 40)


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

    draw_paragraph(pdf, "Terminus - chemin visuel", styles["title"], 26, PAGE_HEIGHT - 12, 420)
    draw_paragraph(
        pdf,
        "Cards bien séparées, flèches d'aller et flèches de retour quand tu repars du hub.",
        styles["subtitle"],
        26,
        PAGE_HEIGHT - 36,
        520,
    )

    for card in MAIN_CARDS:
        draw_card(pdf, styles, card)
    draw_card(pdf, styles, HUB_CARD)
    for card in BRANCH_CARDS:
        draw_card(pdf, styles, card)
    for card in BOTTOM_CARDS:
        draw_card(pdf, styles, card)

    # Main top path
    draw_one_way_arrow(pdf, (116, 431), (132, 431))
    draw_one_way_arrow(pdf, (244, 431), (260, 431))
    draw_one_way_arrow(pdf, (396, 431), (412, 431))
    draw_one_way_arrow(pdf, (514, 431), (530, 431))
    draw_one_way_arrow(pdf, (642, 431), (658, 431))
    draw_one_way_arrow(pdf, (740, 380), (421, 318))

    # Hub branches with explicit return
    draw_bi_arrow_horizontal(pdf, styles, 240, 334, 292, outward="left")
    draw_bi_arrow_horizontal(pdf, styles, 240, 334, 192, outward="left")
    draw_bi_arrow_horizontal(pdf, styles, 508, 602, 292, outward="right")
    draw_bi_arrow_horizontal(pdf, styles, 508, 602, 192, outward="right")

    # Main continuation downward
    draw_one_way_arrow(pdf, (421, 234), (322, 134))
    draw_one_way_arrow(pdf, (406, 88), (432, 88))
    draw_one_way_arrow(pdf, (612, 82), (638, 78))

    pdf.setFont(FONT_REGULAR, 8.2)
    pdf.setFillColor(COLORS["muted"])
    pdf.drawString(26, 12, "Version courte vérifiée sur le build local.")

    pdf.save()
    print(f"written {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
