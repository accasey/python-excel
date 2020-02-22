import openpyxl
from openpyxl.chart import PieChart, Reference, Series, PieChart3D

wb = openpyxl.Workbook()
ws = wb.active

data = [
    ['Flavour','Sold'],
    ['Vanilla', 1500],
    ['Chocolate', 1700],
    ['Strawberry', 600],
    ['Pumpkin Spice', 950]
]

for row in data:
    ws.append(row)

chart = PieChart()
labels = Reference(ws, min_col=1, min_row=2, max_row=5)
data = Reference(ws, min_col=2, min_row=1, max_row=5)
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)
chart.title = 'Ice Cream by Flavour'
ws.add_chart(chart, 'C1')
wb.save('Pie.xlsx')