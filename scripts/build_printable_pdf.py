from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = Path("output/pdf/terminus-rendu.pdf")

COMMAND_ROWS = [
    ["Commande", "Obtention", "Utilite"],
    ["cd, ls, cat", "Disponibles au debut", "Explorer et lire"],
    ["pwd", "RentreChezToi", "Se reperer"],
    ["mv", "Professeur", "Debloquer academie et tunnel"],
    ["help, man", "Manuscrit", "Rappel de syntaxe"],
    ["unzip", "SacA Dos", "Ouvrir le sac du marche"],
    ["mkdir, rm", "Vendeur", "Maison, rocher, ronces, troll"],
    ["touch", "Artisane", "Planche et rouage"],
    ["cp", "touch rouage", "Copies de rouages"],
    ["grep", "Grep en PieceSecrete", "Trouver le mot de passe"],
    ["sudo", "Prospectus", "Lire le Certificat"],
]

STEPS = [
    "BoisDesLutins : cat RentreChezToi",
    "Academie : cat Professeur puis mv Pilier* ~/",
    "Prairie : cat Poney pour debloquer Montagnes",
    "Montagnes : cat VieilHomme puis cat Manuscrit",
    "Cellier : mv Rocher PetitRenfoncement",
    "PlaceDuMarche : cat SacA Dos, unzip SacA Dos.zip, acheter mkdir puis rm",
    "BoutiqueArtisanale : cat Artisane, touch rouage, cp rouage rouage1 ... rouage5",
    "Bibliotheque : ./IntrigantLevier puis cat Grep",
    "CheminEnPierres : rm EnormeRocher",
    "PontCasse : touch Planche puis mkdir Maison",
    "CheminInquietant : rm RoncesTordues",
    "CaveDesTrolls : rm TrollMoche puis mv Cage/EnfantKidnape .",
    "FichiersNoyau : cat Prospectus, cat Instructions, grep pass *.txt",
    "Mot de passe final : IHTFP",
    "Fin : sudo cat Certificat puis cd Paradis et ls",
]

FILE_TREE = """\
Depart
|-- BoisDesLutins
|   `-- AcademieDesBots
|       |-- Cours
|       `-- SalleDEntrainement
`-- Prairie
    `-- Montagnes
        `-- Cave
            `-- SombreCorridor
                `-- Cellier
                    `-- Tunnel
                        `-- ChambreDePierre
                            `-- Portail
                                `-- PlaceDuVillage
                                    |-- PlaceDuMarche
                                    |-- Bibliotheque
                                    |   `-- PieceSecrete
                                    |-- CheminEnPierres
                                    |   `-- Ferme
                                    |-- BoutiqueArtisanale
                                    `-- PontCasse
                                        `-- Clairiere
                                            |-- Maison
                                            `-- CheminInquietant
                                                `-- CaveDesTrolls
                                                    |-- Cage
                                                    `-- Toboggan
                                                        `-- FichiersNoyau
                                                            |-- PlusDeFichiersNoyau
                                                            `-- Paradis
"""


def add_page_number(canvas, doc):
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.grey)
    canvas.drawRightString(A4[0] - 1.5 * cm, 1 * cm, f"Page {doc.page}")


def build_story():
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCentered",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        spaceAfter=10,
    )
    subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#1E3A5F"),
        spaceBefore=8,
        spaceAfter=6,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        spaceAfter=5,
    )
    mono = ParagraphStyle(
        "Mono",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=8.2,
        leading=10,
    )

    story = [
        Paragraph("Solution de l'activite Terminus", title),
        Paragraph(
            "Document de rendu court pour impression. Cette synthese rassemble "
            "les commandes apprises, le cheminement global et un file tree lisible.",
            body,
        ),
        Spacer(1, 0.2 * cm),
        Paragraph("Commandes apprises", subtitle),
    ]

    table = Table(COMMAND_ROWS, colWidths=[3.2 * cm, 5.4 * cm, 7.2 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E3A5F")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph("Resolution rapide", subtitle))

    for index, step in enumerate(STEPS, start=1):
        story.append(Paragraph(f"{index}. {step}", body))

    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("File tree simplifie", subtitle))
    story.append(
        Preformatted(
            FILE_TREE,
            mono,
            dedent=0,
        )
    )

    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("Mot de passe final : IHTFP", subtitle))
    story.append(
        Paragraph(
            "Point clef : la derniere sequence repose sur grep dans "
            "PlusDeFichiersNoyau, puis sudo cat Certificat.",
            body,
        )
    )

    return story


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title="Solution Terminus",
        author="Codex",
    )
    doc.build(build_story(), onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"written {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
