from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfgen import canvas


OUTPUT_PATH = Path("output/pdf/terminus-rendu.pdf")
PAGE_WIDTH, PAGE_HEIGHT = A4

PALETTE = {
    "paper": colors.HexColor("#F6F1E8"),
    "ink": colors.HexColor("#17212B"),
    "muted": colors.HexColor("#5A6573"),
    "blue": colors.HexColor("#214E6B"),
    "green": colors.HexColor("#2D6A4F"),
    "orange": colors.HexColor("#C46C1A"),
    "gold": colors.HexColor("#B48A28"),
    "line": colors.HexColor("#CAD2DB"),
    "panel": colors.white,
    "soft_blue": colors.HexColor("#EAF2F7"),
    "soft_green": colors.HexColor("#EAF5EE"),
    "soft_orange": colors.HexColor("#FCF1E4"),
    "soft_gold": colors.HexColor("#F8F1DD"),
}

FONT_REGULAR = "ArialTerminus"
FONT_BOLD = "ArialTerminusBold"
FONT_CODE = "ConsolasTerminus"

TITLE = "Terminus"
SUBTITLE = "Solution propre A4, carte et cheminement complet"

MAP_NODES = [
    {
        "key": "start",
        "title": "Depart",
        "subtitle": "cd, ls, cat",
        "x": 230,
        "y": 680,
        "w": 135,
        "h": 48,
        "fill": PALETTE["soft_blue"],
        "stroke": PALETTE["blue"],
        "tag": "Base",
    },
    {
        "key": "forest",
        "title": "BoisDesLutins",
        "subtitle": "pwd",
        "x": 60,
        "y": 610,
        "w": 140,
        "h": 48,
        "fill": PALETTE["soft_green"],
        "stroke": PALETTE["green"],
        "tag": "Commande",
    },
    {
        "key": "academy",
        "title": "AcademieDesBots",
        "subtitle": "mv",
        "x": 60,
        "y": 540,
        "w": 140,
        "h": 48,
        "fill": PALETTE["soft_green"],
        "stroke": PALETTE["green"],
        "tag": "Commande",
    },
    {
        "key": "meadow",
        "title": "Prairie",
        "subtitle": "Poney -> Montagnes",
        "x": 395,
        "y": 610,
        "w": 140,
        "h": 48,
        "fill": PALETTE["soft_orange"],
        "stroke": PALETTE["orange"],
        "tag": "Deblocage",
    },
    {
        "key": "mountain",
        "title": "Montagnes",
        "subtitle": "exit, help, man",
        "x": 395,
        "y": 540,
        "w": 140,
        "h": 48,
        "fill": PALETTE["soft_green"],
        "stroke": PALETTE["green"],
        "tag": "Commande",
    },
    {
        "key": "cave",
        "title": "Cave -> Cellier",
        "subtitle": "mv Rocher PetitRenfoncement",
        "x": 395,
        "y": 470,
        "w": 140,
        "h": 52,
        "fill": PALETTE["soft_orange"],
        "stroke": PALETTE["orange"],
        "tag": "Enigme",
    },
    {
        "key": "portal",
        "title": "Tunnel -> Portail",
        "subtitle": "Acces au village",
        "x": 395,
        "y": 392,
        "w": 140,
        "h": 48,
        "fill": PALETTE["soft_blue"],
        "stroke": PALETTE["blue"],
        "tag": "Passage",
    },
    {
        "key": "town",
        "title": "PlaceDuVillage",
        "subtitle": "Hub principal",
        "x": 230,
        "y": 305,
        "w": 135,
        "h": 52,
        "fill": PALETTE["soft_blue"],
        "stroke": PALETTE["blue"],
        "tag": "Hub",
    },
    {
        "key": "market",
        "title": "PlaceDuMarche",
        "subtitle": "unzip, mkdir, rm",
        "x": 26,
        "y": 205,
        "w": 120,
        "h": 52,
        "fill": PALETTE["soft_green"],
        "stroke": PALETTE["green"],
        "tag": "Commande",
    },
    {
        "key": "library",
        "title": "Bibliotheque",
        "subtitle": "Grep",
        "x": 168,
        "y": 205,
        "w": 120,
        "h": 52,
        "fill": PALETTE["soft_green"],
        "stroke": PALETTE["green"],
        "tag": "Commande",
    },
    {
        "key": "artisan",
        "title": "BoutiqueArtisanale",
        "subtitle": "touch, cp",
        "x": 310,
        "y": 205,
        "w": 120,
        "h": 52,
        "fill": PALETTE["soft_green"],
        "stroke": PALETTE["green"],
        "tag": "Commande",
    },
    {
        "key": "rocky",
        "title": "CheminEnPierres",
        "subtitle": "rm EnormeRocher",
        "x": 452,
        "y": 205,
        "w": 120,
        "h": 52,
        "fill": PALETTE["soft_orange"],
        "stroke": PALETTE["orange"],
        "tag": "Enigme",
    },
    {
        "key": "bridge",
        "title": "PontCasse",
        "subtitle": "touch Planche -> mkdir Maison",
        "x": 168,
        "y": 112,
        "w": 190,
        "h": 56,
        "fill": PALETTE["soft_orange"],
        "stroke": PALETTE["orange"],
        "tag": "Enigme",
    },
    {
        "key": "farm",
        "title": "Ferme",
        "subtitle": "",
        "x": 430,
        "y": 120,
        "w": 142,
        "h": 42,
        "fill": PALETTE["soft_blue"],
        "stroke": PALETTE["line"],
        "tag": "Optionnel",
    },
    {
        "key": "trolls",
        "title": "CaveDesTrolls",
        "subtitle": "rm TrollMoche + liberer l'enfant",
        "x": 168,
        "y": 28,
        "w": 190,
        "h": 62,
        "fill": PALETTE["soft_orange"],
        "stroke": PALETTE["orange"],
        "tag": "Finale locale",
    },
]

MAP_EDGES = [
    ("start", "forest"),
    ("start", "meadow"),
    ("forest", "academy"),
    ("meadow", "mountain"),
    ("mountain", "cave"),
    ("cave", "portal"),
    ("portal", "town"),
    ("town", "market"),
    ("town", "library"),
    ("town", "artisan"),
    ("town", "rocky"),
    ("town", "bridge"),
    ("rocky", "farm"),
    ("bridge", "trolls"),
]

STEP_GROUPS = [
    {
        "title": "Phase 1 - Debut et Academie",
        "accent": PALETTE["blue"],
        "items": [
            "ls",
            "cat Palourde",
            "cd BoisDesLutins",
            "cat RentreChezToi",
            "cd AcademieDesBots/Cours",
            "cat Professeur",
            "cd ../SalleDEntrainement",
            "mv Pilier* ~/",
        ],
    },
    {
        "title": "Phase 2 - Prairie, montagne et portail",
        "accent": PALETTE["green"],
        "items": [
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
        "title": "Phase 3 - Hub du village",
        "accent": PALETTE["orange"],
        "items": [
            "cd PlaceDuMarche",
            "cat SacA Dos",
            "unzip SacA Dos.zip",
            "acheter mkdir puis rm chez le Vendeur",
            "cd ../BoutiqueArtisanale",
            "cat Artisane",
            "touch rouage",
            "cp rouage rouage1 ... rouage5",
            "cd ../Bibliotheque",
            "./IntrigantLevier",
            "cd PieceSecrete",
            "cat Grep",
        ],
    },
    {
        "title": "Phase 4 - Fin de niveau et sortie",
        "accent": PALETTE["gold"],
        "items": [
            "cd ../../CheminEnPierres",
            "rm EnormeRocher",
            "cd ../PontCasse",
            "touch Planche",
            "cd Clairiere",
            "mkdir Maison",
            "cd CheminInquietant",
            "rm RoncesTordues",
            "cd CaveDesTrolls",
            "rm TrollMoche",
            "mv Cage/EnfantKidnape .",
        ],
    },
    {
        "title": "Phase 5 - FichiersNoyau et fin",
        "accent": PALETTE["blue"],
        "items": [
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
        ],
    },
]

COMMAND_TABLE = [
    ["Commande", "Ou", "A quoi elle sert"],
    ["pwd", "RentreChezToi", "Se reperer"],
    ["mv", "Professeur", "Piliers, Rocher, Enfant"],
    ["help / man", "Manuscrit", "Relire la syntaxe"],
    ["unzip", "SacA Dos", "Sortir rm_cost et mkdir_cost"],
    ["mkdir", "Vendeur", "Construire Maison"],
    ["rm", "Vendeur", "Rocher, Ronces, TrollMoche"],
    ["touch", "Artisane", "Planche, rouage"],
    ["cp", "Apres touch rouage", "Fabriquer les copies"],
    ["grep", "PieceSecrete", "Trouver IHTFP"],
    ["sudo", "Prospectus", "Lire le Certificat"],
]

FILE_TREE_LINES = [
    "Depart",
    "|-- BoisDesLutins",
    "|   `-- AcademieDesBots",
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
    "                                    |-- PlaceDuMarche",
    "                                    |-- Bibliotheque -> PieceSecrete",
    "                                    |-- BoutiqueArtisanale",
    "                                    |-- CheminEnPierres -> Ferme",
    "                                    `-- PontCasse -> Clairiere",
    "                                                        `-- CheminInquietant",
    "                                                            `-- CaveDesTrolls",
    "                                                                `-- Toboggan",
    "                                                                    `-- FichiersNoyau",
    "                                                                        |-- PlusDeFichiersNoyau",
    "                                                                        `-- Paradis",
]


def register_fonts():
    pdfmetrics.registerFont(TTFont(FONT_REGULAR, "C:/Windows/Fonts/arial.ttf"))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, "C:/Windows/Fonts/arialbd.ttf"))
    pdfmetrics.registerFont(TTFont(FONT_CODE, "C:/Windows/Fonts/consola.ttf"))


def make_styles():
    return {
        "hero": ParagraphStyle(
            "hero",
            fontName=FONT_BOLD,
            fontSize=25,
            leading=29,
            textColor=colors.white,
            alignment=TA_LEFT,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            fontName=FONT_REGULAR,
            fontSize=11,
            leading=14,
            textColor=colors.white,
        ),
        "section": ParagraphStyle(
            "section",
            fontName=FONT_BOLD,
            fontSize=16,
            leading=19,
            textColor=PALETTE["ink"],
        ),
        "body": ParagraphStyle(
            "body",
            fontName=FONT_REGULAR,
            fontSize=10.2,
            leading=13.2,
            textColor=PALETTE["ink"],
        ),
        "small": ParagraphStyle(
            "small",
            fontName=FONT_REGULAR,
            fontSize=8.8,
            leading=11,
            textColor=PALETTE["muted"],
        ),
        "card_title": ParagraphStyle(
            "card_title",
            fontName=FONT_BOLD,
            fontSize=10.6,
            leading=12,
            textColor=PALETTE["ink"],
            alignment=TA_CENTER,
        ),
        "card_subtitle": ParagraphStyle(
            "card_subtitle",
            fontName=FONT_REGULAR,
            fontSize=8.1,
            leading=9.2,
            textColor=PALETTE["muted"],
            alignment=TA_CENTER,
        ),
        "label": ParagraphStyle(
            "label",
            fontName=FONT_BOLD,
            fontSize=8,
            leading=9,
            textColor=colors.white,
            alignment=TA_CENTER,
        ),
        "step_title": ParagraphStyle(
            "step_title",
            fontName=FONT_BOLD,
            fontSize=12,
            leading=14,
            textColor=PALETTE["ink"],
        ),
        "code": ParagraphStyle(
            "code",
            fontName=FONT_CODE,
            fontSize=8.4,
            leading=10.2,
            textColor=PALETTE["ink"],
        ),
    }


def draw_paragraph(pdf, text, style, x, top_y, width):
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(pdf, x, top_y - height)
    return height


def draw_round_panel(pdf, x, y, width, height, fill, stroke, radius=16, line_width=1):
    pdf.setFillColor(fill)
    pdf.setStrokeColor(stroke)
    pdf.setLineWidth(line_width)
    pdf.roundRect(x, y, width, height, radius, fill=1, stroke=1)


def draw_header(pdf, styles, page_title, page_note, page_number):
    pdf.setFillColor(PALETTE["paper"])
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    pdf.setFillColor(PALETTE["blue"])
    pdf.rect(0, PAGE_HEIGHT - 112, PAGE_WIDTH, 112, fill=1, stroke=0)
    pdf.setFillColor(PALETTE["gold"])
    pdf.rect(0, PAGE_HEIGHT - 118, PAGE_WIDTH, 6, fill=1, stroke=0)

    draw_paragraph(pdf, page_title, styles["hero"], 42, PAGE_HEIGHT - 30, PAGE_WIDTH - 84)
    draw_paragraph(pdf, page_note, styles["subtitle"], 42, PAGE_HEIGHT - 66, PAGE_WIDTH - 84)

    pdf.setFillColor(colors.white)
    pdf.setFont(FONT_BOLD, 10)
    pdf.drawRightString(PAGE_WIDTH - 42, PAGE_HEIGHT - 30, f"Page {page_number}")


def node_center(node):
    return node["x"] + node["w"] / 2, node["y"] + node["h"] / 2


def draw_connector(pdf, node_a, node_b):
    ax, ay = node_center(node_a)
    bx, by = node_center(node_b)
    pdf.setStrokeColor(PALETTE["line"])
    pdf.setLineWidth(1.4)
    pdf.line(ax, ay, bx, by)

    angle_dx = bx - ax
    angle_dy = by - ay
    length = max((angle_dx ** 2 + angle_dy ** 2) ** 0.5, 1)
    ux = angle_dx / length
    uy = angle_dy / length
    arrow_size = 6
    px = bx - ux * 8
    py = by - uy * 8
    left_x = px - uy * arrow_size
    left_y = py + ux * arrow_size
    right_x = px + uy * arrow_size
    right_y = py - ux * arrow_size
    pdf.setFillColor(PALETTE["line"])
    pdf.wedge(left_x - 0.1, left_y - 0.1, left_x + 0.1, left_y + 0.1, 0, 360, fill=0, stroke=0)
    pdf.line(bx, by, left_x, left_y)
    pdf.line(bx, by, right_x, right_y)


def draw_map_node(pdf, styles, node):
    draw_round_panel(pdf, node["x"], node["y"], node["w"], node["h"], node["fill"], node["stroke"], radius=14)
    label_width = min(52, node["w"] - 18)
    pdf.setFillColor(node["stroke"])
    pdf.roundRect(node["x"] + 8, node["y"] + node["h"] - 18, label_width, 14, 7, fill=1, stroke=0)
    draw_paragraph(pdf, node["tag"], styles["label"], node["x"] + 8, node["y"] + node["h"] - 4, label_width)
    draw_paragraph(pdf, node["title"], styles["card_title"], node["x"] + 8, node["y"] + node["h"] - 22, node["w"] - 16)
    draw_paragraph(pdf, node["subtitle"], styles["card_subtitle"], node["x"] + 8, node["y"] + 18, node["w"] - 16)


def draw_page_one(pdf, styles):
    draw_header(
        pdf,
        styles,
        f"{TITLE} - carte de progression",
        "Vue d'ensemble du jeu, des zones clefs et des commandes a apprendre pour atteindre Paradis.",
        1,
    )

    draw_paragraph(
        pdf,
        "Objectif final : debloquer <b>Paradis</b> en resolvant les zones dans le bon ordre, "
        "puis en utilisant <b>grep</b> et <b>sudo</b> pour obtenir le mot de passe <b>IHTFP</b>.",
        styles["body"],
        42,
        PAGE_HEIGHT - 136,
        PAGE_WIDTH - 84,
    )

    node_by_key = {node["key"]: node for node in MAP_NODES}
    for source, target in MAP_EDGES:
        draw_connector(pdf, node_by_key[source], node_by_key[target])

    for node in MAP_NODES:
        draw_map_node(pdf, styles, node)

    finale_x = 372
    finale_y = 18
    finale_w = 200
    finale_h = 70
    draw_round_panel(
        pdf,
        finale_x,
        finale_y,
        finale_w,
        finale_h,
        PALETTE["soft_gold"],
        PALETTE["gold"],
        radius=18,
        line_width=1.2,
    )
    draw_paragraph(pdf, "Finale noyau", styles["step_title"], finale_x + 14, finale_y + finale_h - 10, finale_w - 28)
    draw_paragraph(
        pdf,
        "cat Prospectus<br/>cat Instructions<br/>grep pass *.txt<br/><b>sudo cat Certificat -> Paradis</b>",
        styles["body"],
        finale_x + 14,
        finale_y + finale_h - 30,
        finale_w - 28,
    )

    troll_node = node_by_key["trolls"]
    pdf.setStrokeColor(PALETTE["line"])
    pdf.setLineWidth(1.4)
    pdf.line(
        troll_node["x"] + troll_node["w"],
        troll_node["y"] + 18,
        finale_x,
        finale_y + finale_h - 20,
    )

    legend_y = 100
    legends = [
        ("Commande", PALETTE["soft_green"], PALETTE["green"]),
        ("Enigme", PALETTE["soft_orange"], PALETTE["orange"]),
        ("Lieu / hub", PALETTE["soft_blue"], PALETTE["blue"]),
        ("Fin", PALETTE["soft_gold"], PALETTE["gold"]),
    ]
    x = 42
    for title, fill, stroke in legends:
        pdf.setFillColor(fill)
        pdf.setStrokeColor(stroke)
        pdf.roundRect(x, legend_y, 16, 10, 5, fill=1, stroke=1)
        pdf.setFillColor(PALETTE["ink"])
        pdf.setFont(FONT_REGULAR, 8.5)
        pdf.drawString(x + 22, legend_y + 2, title)
        x += 120

    draw_paragraph(
        pdf,
        "Astuce : dans le vrai jeu, utilise <b>Tab</b> pour auto-completer les noms exacts et eviter les erreurs sur les accents.",
        styles["small"],
        42,
        88,
        PAGE_WIDTH - 84,
    )


def draw_step_panel(pdf, styles, x, y, width, title, accent, items):
    line_height = 10.8
    panel_height = 36 + len(items) * line_height
    draw_round_panel(pdf, x, y, width, panel_height, colors.white, PALETTE["line"], radius=16, line_width=1)
    pdf.setFillColor(accent)
    pdf.roundRect(x, y, 10, panel_height, 5, fill=1, stroke=0)
    draw_paragraph(pdf, title, styles["step_title"], x + 22, y + panel_height - 10, width - 34)

    code_top = y + panel_height - 30
    for index, item in enumerate(items):
        draw_paragraph(pdf, f"{index + 1}. {item}", styles["code"], x + 22, code_top - index * line_height, width - 34)

    return panel_height


def draw_page_two(pdf, styles):
    draw_header(
        pdf,
        styles,
        "Solution pas a pas",
        "Les commandes ci-dessous forment le chemin le plus propre pour finir le jeu sans se bloquer.",
        2,
    )

    left_x = 42
    right_x = 306
    width = 246
    top_y = 650

    left_height = 0
    for group in STEP_GROUPS[:3]:
        height = draw_step_panel(pdf, styles, left_x, top_y - left_height - 110, width, group["title"], group["accent"], group["items"])
        left_height += height + 16

    right_height = 0
    for group in STEP_GROUPS[3:]:
        height = draw_step_panel(pdf, styles, right_x, top_y - right_height - 110, width, group["title"], group["accent"], group["items"])
        right_height += height + 16

    callout_y = 42
    draw_round_panel(pdf, 42, callout_y, 510, 74, PALETTE["soft_gold"], PALETTE["gold"], radius=18, line_width=1.2)
    draw_paragraph(pdf, "Sequence critique a retenir", styles["step_title"], 56, callout_y + 64, 250)
    draw_paragraph(
        pdf,
        "<b>grep pass *.txt</b> dans PlusDeFichiersNoyau donne <b>IHTFP</b>.<br/>"
        "Ensuite : <b>sudo cat Certificat</b>, entrer <b>IHTFP</b>, puis <b>cd Paradis</b> et <b>ls</b>.",
        styles["body"],
        56,
        callout_y + 40,
        470,
    )


def draw_page_three(pdf, styles):
    draw_header(
        pdf,
        styles,
        "Pense-bete final",
        "Resume pour recopier sur papier : tableau des commandes, arbre express et note de fin.",
        3,
    )

    draw_round_panel(pdf, 42, 410, 290, 300, colors.white, PALETTE["line"], radius=18, line_width=1)
    draw_paragraph(pdf, "Commandes apprises", styles["section"], 58, 690, 220)

    table = Table(COMMAND_TABLE, colWidths=[64, 94, 114], rowHeights=22)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALETTE["blue"]),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
                ("FONTNAME", (0, 1), (-1, -1), FONT_REGULAR),
                ("FONTSIZE", (0, 0), (-1, -1), 8.4),
                ("LEADING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    table.wrapOn(pdf, 250, 260)
    table.drawOn(pdf, 58, 434)

    draw_round_panel(pdf, 350, 522, 202, 188, PALETTE["soft_blue"], PALETTE["blue"], radius=18, line_width=1.1)
    draw_paragraph(pdf, "Arbre express", styles["section"], 366, 690, 150)

    code_y = 660
    for line in FILE_TREE_LINES:
        draw_paragraph(pdf, line, styles["code"], 366, code_y, 168)
        code_y -= 10

    draw_round_panel(pdf, 350, 410, 202, 96, PALETTE["soft_gold"], PALETTE["gold"], radius=18, line_width=1.1)
    draw_paragraph(pdf, "Mot de passe final", styles["section"], 366, 488, 150)
    draw_paragraph(pdf, "<b>IHTFP</b>", styles["step_title"], 366, 456, 120)
    draw_paragraph(
        pdf,
        "Trouve avec <b>grep pass *.txt</b> dans <b>PlusDeFichiersNoyau</b>.",
        styles["body"],
        366,
        436,
        168,
    )

    draw_round_panel(pdf, 42, 300, 510, 84, PALETTE["soft_green"], PALETTE["green"], radius=18, line_width=1.1)
    draw_paragraph(pdf, "Ordre conseille", styles["section"], 58, 364, 180)
    draw_paragraph(
        pdf,
        "BoisDesLutins -> Academie -> Prairie -> Montagnes -> Cave -> PlaceDuVillage -> "
        "Marche -> Boutique -> Bibliotheque -> CheminEnPierres -> PontCasse -> "
        "CheminInquietant -> CaveDesTrolls -> FichiersNoyau -> Paradis",
        styles["body"],
        58,
        338,
        470,
    )

    draw_round_panel(pdf, 42, 182, 510, 96, colors.white, PALETTE["line"], radius=18, line_width=1)
    draw_paragraph(pdf, "Conseil de rendu", styles["section"], 58, 258, 180)
    draw_paragraph(
        pdf,
        "Si tu dois recopier sur feuille, appuie-toi sur cette structure : "
        "<b>1. commandes apprises</b>, <b>2. carte des lieux</b>, <b>3. solution etape par etape</b>, "
        "<b>4. mot de passe final</b>. Le plus important est de montrer la logique du parcours.",
        styles["body"],
        58,
        232,
        470,
    )

    draw_paragraph(
        pdf,
        "Document genere automatiquement depuis le dossier de travail local pour un rendu propre et imprimable.",
        styles["small"],
        42,
        120,
        PAGE_WIDTH - 84,
    )


def main():
    register_fonts()
    styles = make_styles()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    pdf = canvas.Canvas(str(OUTPUT_PATH), pagesize=A4)
    pdf.setTitle("Terminus - solution A4")
    pdf.setAuthor("Codex")

    draw_page_one(pdf, styles)
    pdf.showPage()

    draw_page_two(pdf, styles)
    pdf.showPage()

    draw_page_three(pdf, styles)
    pdf.showPage()

    pdf.save()
    print(f"written {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
