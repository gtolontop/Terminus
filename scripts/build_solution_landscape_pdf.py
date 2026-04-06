from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas


OUTPUT_PATH = Path("output/pdf/terminus-solution-paysage.pdf")
PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

FONT_REGULAR = "ArialTerminus"
FONT_BOLD = "ArialTerminusBold"
FONT_CODE = "ConsolasTerminus"

COLORS = {
    "bg": colors.HexColor("#F7F2E8"),
    "panel": colors.white,
    "ink": colors.HexColor("#1B2430"),
    "muted": colors.HexColor("#5E6B78"),
    "blue": colors.HexColor("#234E70"),
    "green": colors.HexColor("#2D6A4F"),
    "orange": colors.HexColor("#C96B1F"),
    "gold": colors.HexColor("#B88A1B"),
    "line": colors.HexColor("#CFD8E2"),
    "soft_blue": colors.HexColor("#EAF2F8"),
    "soft_green": colors.HexColor("#EBF6EF"),
    "soft_orange": colors.HexColor("#FDF1E5"),
    "soft_gold": colors.HexColor("#FBF3DE"),
}


FILE_TREE = [
    "Départ",
    "|-- BoisDesLutins",
    "|   `-- AcadémieDesBots",
    "|       |-- Cours",
    "|       `-- SalleDEntrainement",
    "`-- Prairie",
    "    `-- Montagnes",
    "        `-- Cave",
    "            `-- SombreCorridor",
    "                `-- Cellier",
    "                    `-- Tunnel",
    "                        `-- ChambreDePierre",
    "                            `-- Portail",
    "                                `-- PlaceDuVillage",
    "                                    |-- PlaceDuMarché",
    "                                    |-- Bibliothèque",
    "                                    |   `-- PièceSecrète",
    "                                    |-- BoutiqueArtisanale",
    "                                    |-- CheminEnPierres",
    "                                    |   `-- Ferme",
    "                                    `-- PontCassé",
    "                                        `-- Clairière",
    "                                            `-- CheminInquiétant",
    "                                                `-- CaveDesTrolls",
    "                                                    `-- Toboggan",
    "                                                        `-- FichiersNoyau",
    "                                                            |-- PlusDeFichiersNoyau",
    "                                                            `-- Paradis",
]


GROUPS = [
    {
        "title": "1. Début et Académie",
        "fill": COLORS["soft_blue"],
        "stroke": COLORS["blue"],
        "lines": [
            "ls",
            "cat Palourde",
            "cd BoisDesLutins",
            "cat RentreChezToi",
            "cd AcadémieDesBots/Cours",
            "cat Professeur",
            "cd ../SalleDEntrainement",
            "mv Pilier* ~/",
        ],
    },
    {
        "title": "2. Prairie, montagne, portail",
        "fill": COLORS["soft_green"],
        "stroke": COLORS["green"],
        "lines": [
            "cd ~/Prairie",
            "cat Poney",
            "cd Montagnes",
            "cat VieilHomme",
            "cat Manuscrit",
            "cd Cave/SombreCorridor/Cellier",
            "mv Rocher PetitRenfoncement",
            "cd Tunnel/ChambreDePierre/Portail/PlaceDuVillage",
        ],
    },
    {
        "title": "3. Hub du village",
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
        "lines": [
            "cd PlaceDuMarché",
            "cat SacÀDos",
            "unzip SacÀDos.zip",
            "acheter mkdir puis rm chez le Vendeur",
            "cd ../BoutiqueArtisanale",
            "cat Artisane",
            "touch rouage",
            "cp rouage rouage1 ... rouage5",
            "cd ../Bibliothèque",
            "./IntrigantLevier",
            "cd PièceSecrète",
            "cat Grep",
        ],
    },
    {
        "title": "4. Fin du niveau",
        "fill": COLORS["soft_orange"],
        "stroke": COLORS["orange"],
        "lines": [
            "cd ../../CheminEnPierres",
            "rm ÉnormeRocher",
            "cd ../PontCassé",
            "touch Planche",
            "cd Clairière",
            "mkdir Maison",
            "cd CheminInquiétant",
            "rm RoncesTordues",
            "cd CaveDesTrolls",
            "rm TrollMoche",
            "mv Cage/EnfantKidnapé .",
        ],
    },
]


FINAL_LINES = [
    "cd Toboggan",
    "cd FichiersNoyau",
    "cat Prospectus",
    "cat Instructions",
    "cd PlusDeFichiersNoyau",
    "grep pass *.txt",
    "Mot de passe : IHTFP",
    "cd ..",
    "sudo cat Certificat",
    "cd Paradis",
    "ls",
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
            fontSize=24,
            leading=28,
            textColor=colors.white,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            fontName=FONT_REGULAR,
            fontSize=10.5,
            leading=13,
            textColor=colors.white,
        ),
        "section": ParagraphStyle(
            "section",
            fontName=FONT_BOLD,
            fontSize=14,
            leading=17,
            textColor=COLORS["ink"],
        ),
        "body": ParagraphStyle(
            "body",
            fontName=FONT_REGULAR,
            fontSize=9.6,
            leading=12.2,
            textColor=COLORS["ink"],
        ),
        "small": ParagraphStyle(
            "small",
            fontName=FONT_REGULAR,
            fontSize=8.5,
            leading=10.2,
            textColor=COLORS["muted"],
        ),
        "code": ParagraphStyle(
            "code",
            fontName=FONT_CODE,
            fontSize=8.2,
            leading=10,
            textColor=COLORS["ink"],
        ),
    }


def draw_round_panel(pdf, x, y, width, height, fill, stroke, radius=16, line_width=1):
    pdf.setFillColor(fill)
    pdf.setStrokeColor(stroke)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_paragraph(pdf, text, style, x, top_y, width):
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, top_y - height)
    return height


def draw_code_lines(pdf, lines, x, top_y, width, line_gap=10.2):
    styles = make_styles()
    for index, line in enumerate(lines):
        draw_paragraph(pdf, f"{index + 1}. {line}", styles["code"], x, top_y - index * line_gap, width)


def draw_group_panel(pdf, styles, x, y, width, height, group):
    draw_round_panel(pdf, x, y, width, height, group["fill"], group["stroke"], radius=18, line_width=1.1)
    pdf.setFillColor(group["stroke"])
    pdf.roundRect(x, y + height - 28, width, 28, 18, fill=1, stroke=0)
    draw_paragraph(pdf, group["title"], styles["subtitle"], x + 12, y + height - 6, width - 24)
    current_top = y + height - 38
    for index, line in enumerate(group["lines"]):
        draw_paragraph(pdf, f"{index + 1}. {line}", styles["code"], x + 12, current_top - index * 10, width - 24)


def build_pdf():
    register_fonts()
    styles = make_styles()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    pdf = canvas.Canvas(str(OUTPUT_PATH), pagesize=landscape(A4))
    pdf.setTitle("Solution Terminus paysage")
    pdf.setAuthor("Codex")

    pdf.setFillColor(COLORS["bg"])
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    pdf.setFillColor(COLORS["blue"])
    pdf.rect(0, PAGE_HEIGHT - 70, PAGE_WIDTH, 70, fill=1, stroke=0)
    pdf.setFillColor(COLORS["gold"])
    pdf.rect(0, PAGE_HEIGHT - 74, PAGE_WIDTH, 4, fill=1, stroke=0)

    draw_paragraph(pdf, "Terminus - solution seule", styles["title"], 30, PAGE_HEIGHT - 16, 380)
    draw_paragraph(
        pdf,
        "A4 paysage, sans annexe : seulement le chemin des lieux, les commandes utiles et la fin exacte du jeu.",
        styles["subtitle"],
        30,
        PAGE_HEIGHT - 42,
        520,
    )

    left_x = 24
    right_x = 290

    draw_round_panel(pdf, left_x, 54, 242, 404, COLORS["soft_blue"], COLORS["blue"], radius=18, line_width=1.1)
    draw_paragraph(pdf, "Chemin des lieux", styles["section"], left_x + 16, 444, 180)
    draw_paragraph(
        pdf,
        "Arbre compact du parcours principal a suivre.",
        styles["small"],
        left_x + 16,
        422,
        200,
    )

    line_top = 400
    for line in FILE_TREE:
        draw_paragraph(pdf, line, styles["code"], left_x + 16, line_top, 210)
        line_top -= 10

    draw_round_panel(pdf, right_x, 264, 258, 194, COLORS["panel"], COLORS["line"], radius=18, line_width=1.0)
    draw_round_panel(pdf, 560, 264, 258, 194, COLORS["panel"], COLORS["line"], radius=18, line_width=1.0)
    draw_round_panel(pdf, right_x, 54, 258, 194, COLORS["panel"], COLORS["line"], radius=18, line_width=1.0)
    draw_round_panel(pdf, 560, 54, 258, 194, COLORS["panel"], COLORS["line"], radius=18, line_width=1.0)

    panel_positions = [
        (right_x, 264, 258, 194),
        (560, 264, 258, 194),
        (right_x, 54, 258, 194),
        (560, 54, 258, 194),
    ]
    for group, position in zip(GROUPS, panel_positions):
        draw_group_panel(pdf, styles, *position, group)

    draw_round_panel(pdf, 290, 460, 404, 56, COLORS["soft_gold"], COLORS["gold"], radius=16, line_width=1.1)
    draw_paragraph(pdf, "Fin du jeu", styles["section"], 304, 506, 100)
    draw_paragraph(
        pdf,
        "cd Toboggan -> cd FichiersNoyau -> cat Prospectus<br/>"
        "cat Instructions -> cd PlusDeFichiersNoyau -> grep pass *.txt<br/>"
        "sudo cat Certificat -> cd Paradis -> ls",
        styles["code"],
        420,
        504,
        258,
    )

    draw_round_panel(pdf, 706, 460, 112, 56, COLORS["soft_green"], COLORS["green"], radius=16, line_width=1.1)
    draw_paragraph(pdf, "<b>IHTFP</b>", styles["section"], 720, 504, 84)
    draw_paragraph(pdf, "mot de passe", styles["small"], 720, 484, 84)

    pdf.setFont(FONT_REGULAR, 8.5)
    pdf.setFillColor(COLORS["muted"])
    pdf.drawString(24, 16, "Version verifiee sur le build local et les scripts du jeu.")

    pdf.save()
    print(f"written {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
