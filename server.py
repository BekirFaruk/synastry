import requests 
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="postgres",
  passwd="postgres"
)

print(mydb)

url = 'https://astrowin.org/scripts/synastry_chart_acs.php'
result = requests.get(url)
result.headers
c = result.content
#print(c)

soup = BeautifulSoup(c, 'html.parser')
samples = soup.findAll('table')[1].findAll('tr')[2].findAll('td')
#print(samples)

post_params = {
    "name1": "Kaylien",
    "month1": "12",
    "day1": "6",
    "year1": "1996",
    "hour1": "17",
    "minute1": "30",
    "soc1": "1",
    "city1": "",
    "county1": "",
    "timezone1": "11",
    "time_type1": "",
    "long_deg1": "11",
    "ew1": "e",
    "long_min1": "11",
    "lat_deg1": "11",
    "ns1": "n",
    "lat_min1": "11",
    "name2": "Christine",
    "month2": "5",
    "day2": "19",
    "year2": "1996",
    "hour2": "10",
    "minute2": "45",
    "soc2": "1",
    "city2": "",
    "county2": "",
    "timezone2": "11",
    "time_type2": "",
    "long_deg2": "11",
    "ew2": "e",
    "long_min2": "11",
    "lat_deg2": "11",
    "ns2": "n",
    "lat_min2": "11",
    "submitted": "TRUE",
    "submit": "Submit above data",
}
response = requests.post(url, data=post_params)
#response = requests.post(url)

print(response.status_code)
with open('myfile.html', 'w') as f:
    f.write(response.text)
soup = BeautifulSoup(response.content, 'html.parser')

centers = soup.findAll('center')

score = centers[4].findAll('table')[0].find('tr').findAll('td')[0].findAll('font')[1].getText()
reasons = centers[5].findAll('table')[0].find('tr').findAll('td')[0].findAll('font')
natal_chart = centers[2].findAll('table')[0].findAll('tr')
#sun1 = natal_chart[1].getText()

for x in range(10):
    print(natal_chart[x + 1].findAll('td')[1].getText())

for x in range(10):
    print(natal_chart[x + 1].findAll('td')[4].getText())

#print(sun1)
#print(natal_chart)
reason1 = reasons[-3].getText()
reason2 = reasons[-4].getText()
reason3 = reasons[-5].getText()

#print(reasons)
with open('results.html', 'w') as f:
    f.write(score + "\n")
    f.write(reason1 + "\n" + reason2 + "\n" + reason3 + "\n")
    #f.write(natal_chart)
    for x in range(10):
      f.write(natal_chart[x + 1].findAll('td')[1].getText() + "\n")

    f.write("\n")
    for x in range(10):
        f.write(natal_chart[x + 1].findAll('td')[4].getText() + "\n")

#print(soup)
#print(soup.findAll('table'[0]))
#print("at least something's happening")