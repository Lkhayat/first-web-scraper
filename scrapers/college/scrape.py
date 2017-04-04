import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "https://columbian.gwu.edu/2015-2016"
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
            year,department = cell.text.split(', ')
            list_of_cells.append(year.replace('(','').replace(')', ''))
            list_of_cells.append(department)            
        else: 
            list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["year", "department", "faculty", "sponsor", "title_of_project"])
writer.writerows(list_of_rows)
            