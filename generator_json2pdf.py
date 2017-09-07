from reportlab.lib import colors
from reportlab.lib.pagesizes import  cm, A4
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet

from json_data import JSON_DATA_EXAMPLE


def main():
    doc = SimpleDocTemplate("json2pdf_example.pdf", pagesize=A4)
    # container for the 'Flowable' objects
    elements = []

    styleSheet = getSampleStyleSheet()

    I = Image('BMW.gif')
    I.drawHeight = 1.25 * cm * I.drawHeight / I.drawWidth
    I.drawWidth = 1.25 * cm
    P0 = Paragraph('''
                   <b>A pa<font color=red>r</font>a<i>graph</i></b>
                   <super><font color=yellow>1</font></super>''',
                   styleSheet["BodyText"])
    P = Paragraph('''
        <para align=center spaceb=3>The <b>ReportLab Left
        <font color=red>Logo</font></b>
        Image</para>''',
                  styleSheet["BodyText"])
    data = [['A', 'B', 'C', P0, 'D'],
            ['00', '01', '02', [I, P], '04'],
            ['10', '11', '12', [P, I], '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]

    style = [('GRID', (1, 1), (-2, -2), 1, colors.green),
                           ('BOX', (0, 0), (1, -1), 2, colors.red),
                           ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
                           ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
                           ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                           ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                           ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                           ('BOX', (0, 0), (-1, -1), 2, colors.black),
                           ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                           ('VALIGN', (3, 0), (3, 0), 'BOTTOM'),
                           ('BACKGROUND', (3, 0), (3, 0), colors.limegreen),
                           ('BACKGROUND', (3, 1), (3, 1), colors.khaki),
                           ('ALIGN', (3, 1), (3, 1), 'CENTER'),
                           ('BACKGROUND', (3, 2), (3, 2), colors.beige),
                           ('ALIGN', (3, 2), (3, 2), 'LEFT'),
                           ]

    style1 = [('BACKGROUND', (0, 0), (-1, 0), colors.limegreen)]
    t = Table(data, style=style)
    t._argW[3] = 1.5 * cm

    elements.append(t)
    # write the document to disk
    doc.build(elements)


def create_table(json_data):
    table_data = []
    # Get headers for table
    table_headers = list(json_data[0].keys())
    table_data.append(table_headers)

    data_len = len(json_data)

    for row in range(data_len - 1):
        if row % 2 == 0:
            print('Odd', json_data[row])
        else:
            print('Even', json_data[row])

if __name__ == '__main__':
    main()
    create_table(JSON_DATA_EXAMPLE.get('DTP_Part').get('DTP'))
