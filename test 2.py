from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm

from eq import fml
from page_number import addPageNumber

doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='test_2')


f = [fml('$$$\\dfrac {di_L} {dt} = \\dfrac {1} {L} i_1 R1$$$')]

doc.build(f, onLaterPages=addPageNumber)
