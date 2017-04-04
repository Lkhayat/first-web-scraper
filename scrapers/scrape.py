import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "http://m.nationals.mlb.com/roster/transactions/2017/01"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
counter = 1
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        if cell.text == '':
            list_of_cells.append(counter)
            counter += 1
        elif cell.text!= '' and cell.text[0] == '(':
            text, url = cell.text.split(', ')
            list_of_cells.append(text.replace('(','').replace(')', ''))
            list_of_cells.append(url)            
        else: 
            list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "text", "url"])
writer.writerows(list_of_rows)
