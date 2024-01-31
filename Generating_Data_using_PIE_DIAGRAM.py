import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import(
    PieChart3D,
    Reference
    )
wb_pie_chart=Workbook()
wb_pie_chart=wb_pie_chart.active
data=[
    ("Type of Expense","Amount Spent"),
    ("Grocery",300),
    ("Electricity",150),
    ("CHild Tuition",125),
    ("House Keeping",35),
    ("Gardening",30),
    ("Misl.Expense",500),
    ]
for row in data:
    wb_pie_chart.append(row)
pie=PieChart3D()
labels=Reference(wb_pie_chart,min_col=1,min_row=2,max_row=7)
data=Reference(wb_pie_chart,min_col=2,min_row=1,max_row=7)
pie.add_data(data,title_from_data=True)
pie.set_categories(labels)
pie.title="Expenditures Pie Chart"
wb_pie_chart.add_chart(pie,"C10")
wb_pie_chart.save("C:/MScITPracs/DS/Organizing data/pie.xlsx")
print("data saved")
