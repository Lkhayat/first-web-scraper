import csv
import requests
from BeautifulSoup import BeautifulSoup

url=" http://files.peacecorps.gov/university-rankings/2017/topschools2017.pdf"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find ('table')

list_of_rows = []
counter = 1
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        if cell.find('a'):
            list_of_cells.append('http://files.peacecorps.gov/university-rankings/2017/topschools2017.pdf') + cell.find('a')['href']
        else:
            list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("CCAS.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["year", "department", "faculty", "sponsor", "title_of_project"])
writer.writerows(list_of_rows)
        
