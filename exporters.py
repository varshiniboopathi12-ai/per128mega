from fpdf import FPDF
import os


def save_pdf(layout):

    os.makedirs("static/exports", exist_ok=True)

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    for panel in layout:

        pdf.add_page()

        pdf.set_font(
            "Arial",
            "B",
            16
        )

        pdf.cell(
            0,
            10,
            panel["title"],
            ln=True
        )

        pdf.image(
            panel["image"],
            x=10,
            y=30,
            w=190
        )

        pdf.set_y(150)

        pdf.set_font(
            "Arial",
            size=11
        )

        pdf.multi_cell(
            0,
            8,
            panel["text"]
        )

    filepath = "static/exports/comic.pdf"

    pdf.output(filepath)

    return filepath