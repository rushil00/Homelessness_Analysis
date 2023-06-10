import requests
from bs4 import BeautifulSoup
def __main__():
    html_text = requests.get('https://censusindia.gov.in/nada/index.php/catalog/5047').text
    soup = BeautifulSoup(html_text, 'lxml')
    tr_ = soup.find_all('table' , class_ = "table table-bordered table-striped table-condensed xsl-table table-grid")
    li = tr_[7].find_all('tr')
    features = []
    for i in li:
        features.append(i.text.replace(' ','').replace('\n','').replace('\r',''))
    print(features)
