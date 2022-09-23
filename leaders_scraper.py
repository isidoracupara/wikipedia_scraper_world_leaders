import json
import bs4
import re
import requests

cache = {}
def hashable_cache(f):
    def inner(url, session):
        if url not in cache:
            cache[url] = f(url, session)
        return cache[url]
    return inner

def get_leaders():
    root_url = "https://country-leaders.herokuapp.com"
    leaders_url = root_url + "/leaders"
    cookie_url = root_url + "/cookie"
    countries_url = root_url + "/countries"
    
    req_cookies = requests.get(cookie_url)
    cookies = req_cookies.cookies
    #print(cookies)

    req_countries = requests.get(countries_url, cookies=cookies)
    countries = req_countries.json()
    #print(countries)

    session = requests.Session()

    leaders_per_country = {}

    for country in countries:
        req = requests.get(leaders_url, cookies = cookies, params = {"country" : country})
        
        if(req.status_code == 403):
            req_cookies = requests.get(cookie_url)
            cookies = req_cookies.cookies
            req = requests.get(leaders_url, cookies = cookies, params = {"country" : country})
        
        leaders_json = req.json()
        # print(leaders_json)

        leaders_per_country[country] = []

        for leader_dictionary in leaders_json:
            wiki_first_paragraph = get_first_paragraph(leader_dictionary['wikipedia_url'], session)

            leader_dictionary['wikipedia_first_paragraph'] = wiki_first_paragraph

            leaders_per_country[country].append(leader_dictionary)

    return leaders_per_country

@hashable_cache
def get_first_paragraph(wikipedia_url, session):   

    req = session.get(wikipedia_url)

    soup = bs4.BeautifulSoup(req.text , 'html.parser')

    for paragraph in soup.find_all('p'):
        if paragraph.find('b'):
            regexes = r"/\/.+\//m|/\\n/m|/\[.+\]/m"
            print(regexes)
            paragraph_after_regex = re.sub(r"/\/.+\//m|/\\n/m|/\[.+\]/m", "", paragraph.text)
            print(paragraph_after_regex)
            return paragraph_after_regex

def save():
    filename = "leaders.json"
    with open(filename, "w") as my_file:
        my_file.write(json.dumps(leaders_per_country))



leaders_per_country = get_leaders()
#save()
print(leaders_per_country())