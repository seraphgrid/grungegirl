# Success code is 200. 
query = input("Drug: ")

req_site = req.get('https://psychonautwiki.org/wiki/' + query.lower() + '#Common_names')

print(req_site)

parser = bs(req_site.content, 'html.parser')
bodyContent = parser.find('div', id='bodyContent')
contentText = parser.find('div', class_='mw-parser-output')
wikifind = contentText.find_all(['p'])
dfind = bodyContent.find_all('p')

for line in wikifind:

    print(line.text)
