from bs4 import BeautifulSoup

def html_to_dictionary(table):
    dictionary = []
    soup = BeautifulSoup(table, 'html.parser')
    trs = soup.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        if not tds[1].a.string == None:
            obj = {}
            obj["hanzi"]    = tds[1].a.string
            obj["pinyin"]   = tds[2].a.string
            obj["english"]  = next(tds[3].strings).rstrip()
            dictionary.append(obj)
    return dictionary

def print_dictionary(dictionary):
    for word in dictionary:
        print(word["hanzi"] + " - " + word["pinyin"] + " - " + word["english"])

if __name__ == "__main__":
    wiki1 = open("H:/Projects/Python/anki01/wiki1.html", "r", encoding="utf8").read()
    dict1 = html_to_dictionary(wiki1)
    print_dictionary(dict1)