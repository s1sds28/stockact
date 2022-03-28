from bs4 import BeautifulSoup
import requests

def fetch_search_results(last_name: str, filing_year: str):
    website = "https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure/ViewMemberSearchResult"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://disclosures-clerk.house.gov',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    data = {
      'LastName': last_name,
      'FilingYear': filing_year,
      'State': '',
      'District': ''
    }
    #contains full url for each Periodic Transaction Report
    url_list = []
    #contains transaction ID for saving pdf file
    file_name_list = []
    #requests and parses html data for path
    response = requests.post(website, headers=headers, data=data)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print(soup.prettify())

    #for each end link adds the beggining to make full url and stores in url_list
    for link in soup.find_all('a'):
        path = link.get('href')
        host = 'https://disclosures-clerk.house.gov'
        url = host + path
        url_list.append(url)

    #splits url to save as periodic transaction report filling # IDEA:
    for url in url_list:
        file_name = url.split('/')[-1]
        #print(file_name)

        response = requests.get(url)
        #print(response.text)

        with open(file_name, 'wb') as out_file:
            out_file.write(response.content)


if __name__ == "__main__":
    fetch_search_results('Pelosi', '2021')
