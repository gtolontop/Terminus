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
    "ink": colors.HexColor("#18222D"),
    "muted": colors.HexColor("#5E6975"),
    "line": colors.HexColor("#C9D3DD"),
    "blue": colors.HexColor("#234E70"),
    "green": colors.HexColor("#2D6A4F"),
    "orange": colors.HexColor("#C96B1F"),
    "gold": colors.HexColor("#B88A1B"),
    "red": colors.HexColor("#B44338"),
    "soft_blue": colors.HexColor("#EAF2F8"),
    "soft_green": colors.HexColor("#EBF6EF"),
    "soft_orange": colors.HexColor("#FCF1E5"),
    "soft_gold": colors.HexColor("#FBF3DE"),
    "soft_red": colors.HexColor("#FAE9E6"),
}


CARDS = [
    {
        "title": "1. Départ",
        "subtitle": "prise en main",
        "lines": [
            "ls",
            "cat Palourde",
            "cd BoisDesLutins",
        ],
        "x": 26,
        "y": 390,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
    },
    {
        "title": "2. BoisDesLutins + Académie",
        "subtitle": "pwd puis mv",
        "lines": [
            "cat RentreChezToi",
            "cd AcadémieDesBots/Cours",
            "cat Professeur",
            "cd ../SalleDEntrainement",
            "mv Pilier* ~/",
        ],
        "x": 302,
        "y": 390,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "3. Prairie + Montagnes",
        "subtitle": "Poney, VieilHomme, Manuscrit",
        "lines": [
            "cd ~/Prairie",
            "cat Poney",
            "cd Montagnes",
            "cat VieilHomme",
            "cat Manuscrit",
        ],
        "x": 578,
        "y": 390,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "4. Cave -> Portail",
        "subtitle": "ouvrir le tunnel",
        "lines": [
            "cd Cave/SombreCorridor/Cellier",
            "mv Rocher PetitRenfoncement",
            "cd Tunnel/ChambreDePierre/Portail/PlaceDuVillage",
        ],
        "x": 26,
        "y": 238,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
    },
    {
        "title": "5. Marché",
        "subtitle": "unzip, mkdir, rm",
        "lines": [
            "cd PlaceDuMarché",
            "cat SacÀDos",
            "unzip SacÀDos.zip",
            "acheter mkdir puis rm",
        ],
        "x": 302,
        "y": 238,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "6. Boutique",
        "subtitle": "touch puis cp",
        "lines": [
            "cd ../BoutiqueArtisanale",
            "cat Artisane",
            "touch rouage",
            "cp rouage rouage1 ... rouage5",
        ],
        "x": 578,
        "y": 238,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
    },
    {
        "title": "7. Bibliothèque",
        "subtitle": "débloquer grep",
        "lines": [
            "cd ../Bibliothèque",
            "./IntrigantLevier",
            "cd PièceSecrète",
            "cat Grep",
        ],
        "x": 26,
        "y": 86,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
    },
    {
        "title": "8. CheminEnPierres + PontCassé",
        "subtitle": "rocher, planche, maison",
        "lines": [
            "cd ../../CheminEnPierres",
            "rm ÉnormeRocher",
            "cd ../PontCassé",
            "touch Planche",
            "cd Clairière",
            "mkdir Maison",
        ],
        "x": 302,
        "y": 86,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
    },
    {
        "title": "9. CaveDesTrolls",
        "subtitle": "sortie locale",
        "lines": [
            "cd CheminInquiétant",
            "rm RoncesTordues",
            "cd CaveDesTrolls",
            "rm TrollMoche",
            "mv Cage/EnfantKidnapé .",
        ],
        "x": 578,
        "y": 86,
        "w": 240,
        "h": 128,
        "fill": COLORS["soft_red"],
        "stroke": COLORS["red"],
    },
]


FINAL_CARD = {
    "title": "10. Finale",
    "subtitle": "FichiersNoyau -> Paradis",
    "lines": [
        "cd Toboggan -> cd FichiersNoyau",
        "cat Prospectus -> cat Instructions",
        "cd PlusDeFichiersNoyau -> grep pass *.txt",
        "Mot de passe : IHTFP",
        "sudo cat Certificat -> cd Paradis -> ls",
    ],
    "x": 470,
    "y": 10,
    "w": 348,
    "h": 68,
    "fill": COLORS["soft_gold"],
    "stroke": COLORS["gold"],
}


ARROWS = [
    ((266, 454), (302, 454)),
    ((542, 454), (578, 454)),
    ((146, 390), (146, 366)),
    ((422, 390), (422, 366)),
    ((698, 390), (698, 366)),
    ((266, 302), (302, 302)),
    ((542, 302), (578, 302)),
    ((146, 238), (146, 214)),
    ((422, 238), (422, 214)),
    ((698, 238), (698, 214)),
    ((698, 86), (698, 78)),
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
            fontSize=23,
            leading=27,
            textColor=colors.white,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            fontName=FONT_REGULAR,
            fontSize=10.2,
            leading=13,
            textColor=colors.white,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            fontName=FONT_BOLD,
            fontSize=12.5,
            leading=15,
            textColor=COLORS["ink"],
        ),
        "card_subtitle": ParagraphStyle(
            "card_subtitle",
            fontName=FONT_REGULAR,
            fontSize=8.8,
            leading=10,
            textColor=COLORS["muted"],
        ),
        "code": ParagraphStyle(
            "code",
            fontName=FONT_CODE,
            fontSize=8.2,
            leading=9.8,
            textColor=COLORS["ink"],
        ),
        "small": ParagraphStyle(
            "small",
            fontName=FONT_REGULAR,
            fontSize=8.3,
            leading=10,
            textColor=COLORS["muted"],
        ),
    }


def draw_paragraph(pdf, text, style, x, top_y, width):
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, top_y - height)
    return height


def draw_round_panel(pdf, x, y, width, height, fill, stroke, radius=18, line_width=1.2):
    pdf.setFillColor(fill)
    pdf.setStrokeColor(stroke)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_arrow(pdf, start, end):
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


def draw_card(pdf, styles, card):
    draw_round_panel(pdf, card["x"], card["y"], card["w"], card["h"], card["fill"], card["stroke"])
    pdf.setFillColor(card["stroke"])
    pdf.roundRect(card["x"], card["y"] + card["h"] - 28, card["w"], 28, 18, fill=1, stroke=0)
    draw_paragraph(pdf, card["title"], styles["subtitle"], card["x"] + 14, card["y"] + card["h"] - 6, card["w"] - 28)
    draw_paragraph(pdf, card["subtitle"], styles["card_subtitle"], card["x"] + 14, card["y"] + card["h"] - 34, card["w"] - 28)
    top = card["y"] + card["h"] - 48
    for index, line in enumerate(card["lines"]):
        draw_paragraph(pdf, f"{index + 1}. {line}", styles["code"], card["x"] + 14, top - index * 10, card["w"] - 28)


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
    pdf.rect(0, PAGE_HEIGHT - 68, PAGE_WIDTH, 68, fill=1, stroke=0)
    pdf.setFillColor(COLORS["gold"])
    pdf.rect(0, PAGE_HEIGHT - 72, PAGE_WIDTH, 4, fill=1, stroke=0)

    draw_paragraph(pdf, "Terminus - solution en cards", styles["title"], 28, PAGE_HEIGHT - 14, 430)
    draw_paragraph(
        pdf,
        "Une page paysage, uniquement en cards, avec les commandes exactes dans l'ordre.",
        styles["subtitle"],
        28,
        PAGE_HEIGHT - 40,
        520,
    )

    for start, end in ARROWS:
        draw_arrow(pdf, start, end)

    for card in CARDS:
        draw_card(pdf, styles, card)

    draw_round_panel(
        pdf,
        FINAL_CARD["x"],
        FINAL_CARD["y"],
        FINAL_CARD["w"],
        FINAL_CARD["h"],
        FINAL_CARD["fill"],
        FINAL_CARD["stroke"],
        radius=18,
        line_width=1.2,
    )
    pdf.setFillColor(FINAL_CARD["stroke"])
    pdf.roundRect(FINAL_CARD["x"], FINAL_CARD["y"] + FINAL_CARD["h"] - 24, FINAL_CARD["w"], 24, 18, fill=1, stroke=0)
    draw_paragraph(pdf, FINAL_CARD["title"], styles["subtitle"], FINAL_CARD["x"] + 14, FINAL_CARD["y"] + FINAL_CARD["h"] - 4, FINAL_CARD["w"] - 28)

    final_top = FINAL_CARD["y"] + FINAL_CARD["h"] - 28
    for index, line in enumerate(FINAL_CARD["lines"]):
        draw_paragraph(pdf, line, styles["code"], FINAL_CARD["x"] + 14, final_top - index * 9, FINAL_CARD["w"] - 28)

    pdf.setFont(FONT_REGULAR, 8.4)
    pdf.setFillColor(COLORS["muted"])
    pdf.drawString(26, 16, "Version courte verifiee sur le build local.")

    pdf.save()
    print(f"written {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
