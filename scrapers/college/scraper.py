import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://columbian.gwu.edu/2015-2016','https://columbian.gwu.edu/2014-2015','https://columbian.gwu.edu/2013-2014','https://columbian.gwu.edu/2012-2013','https://columbian.gwu.edu/2011-2012','https://columbian.gwu.edu/2010-2011'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
counter = 1
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        if cell.find('a'):
            list_of_cells.append('https://columbian.gwu.edu/2015-2016','https://columbian.gwu.edu/2014-2015','https://columbian.gwu.edu/2013-2014','https://columbian.gwu.edu/2012-2013','https://columbian.gwu.edu/2011-2012','https://columbian.gwu.edu/2010-2011') + cell.find('a')['href'])
        else:
            list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("CCAS.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["year", "department", "faculty", "sponsor", "title_of_project"])
writer.writerows(list_of_rows)
