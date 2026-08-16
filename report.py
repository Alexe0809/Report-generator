from openpyxl import Workbook
from openpyxl.styles import Font
from analytics import get_total_revenue, get_order_count, get_average_check, get_sales_by_product, get_sales_by_customer, get_sales_by_day

def create_report():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Report'

    ws['A1'] = 'Revenue'
    ws['B1'] = 'Order count'
    ws['C1'] = 'Average check'
    ws['A2'] = get_total_revenue()
    ws['B2'] = get_order_count()
    ws['C2'] = get_average_check()
    for addr in ['A1', 'B1', 'C1']:
        ws[addr].font = Font(bold=True)
    for addr in ['A2', 'B2', 'C2']:
        ws[addr].number_format = '#,##0.00'

    ws.append([])
    ws.append(['Product', 'Revenue'])
    header_row = ws.max_row

    for cell in ws[header_row]:
        cell.font = Font(bold=True)

    for product, revenue in get_sales_by_product():
        ws.append([product, revenue])

    for row in range(header_row+1, ws.max_row+1):
        ws.cell(row=row, column=2).number_format = '#,##0.00'

    ws.auto_filter.ref = f'A{header_row}:B{ws.max_row}'


    start_col = 4          # D (A=1, B=2, C=3, D=4)
    start_row = 4          # с какой строки начать

    # шапка
    ws.cell(row=start_row, column=start_col, value='Customer').font = Font(bold=True)
    ws.cell(row=start_row, column=start_col + 1, value='Revenue').font = Font(bold=True)

    # данные — свой счётчик строки, потому что append не используем
    r = start_row + 1
    for customer, revenue in get_sales_by_customer():
        ws.cell(row=r, column=start_col,     value=customer)
        ws.cell(row=r, column=start_col + 1, value=revenue).number_format = '#,##0.00'
        r += 1




    start_col = 7          # D (A=1, B=2, C=3, D=4)

    # шапка
    ws.cell(row=start_row, column=start_col, value='date').font = Font(bold=True)
    ws.cell(row=start_row, column=start_col + 1, value='Revenue').font = Font(bold=True)

    # данные — свой счётчик строки, потому что append не используем
    r = start_row + 1
    for customer, revenue in get_sales_by_day():
        ws.cell(row=r, column=start_col,     value=customer)
        ws.cell(row=r, column=start_col + 1, value=revenue).number_format = '#,##0.00'
        r += 1
        wb.save('reports/report.xlsx')
    print('Report was sucesfully created')




if __name__ == '__main__':
    create_report()