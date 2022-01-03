import requests
from bs4 import BeautifulSoup
from just_txt import only_txt
import xlsxwriter

wb = xlsxwriter.Workbook("content.xlsx")
ws = wb.add_worksheet('content')

urls = {
    "Home" : "https://www.yugo.com/about-us",
    "Team" : "https://www.yugo.com/the-team",
    "Work_with_us" : "https://www.yugo.com/work-with-us"
} 


def writing():
    bold = wb.add_format({'bold': True})
    ws.write("A1", "Page Name", bold)
    ws.write("B1", "Content", bold)

    row_index = 2

    for keys in urls:
        ws.set_row(row_index, 50)
        ws.set_column("A:A", 20)
        ws.write("A"+ str(row_index), keys)
        
        ws.set_column("B:B", 50)
        ws.write("B" + str(row_index), only_txt(urls[keys]))
       
        row_index += 1

    wb.close()


if __name__ == '__main__':
    writing()