import requests
import bs4
import string # for string.punctuation
import project as p

def request_and_soup(url, payload):
	with requests.session() as s:
	    r = s.post(url + '/login.php', data=payload)
	    resp = s.get(url)
	    return bs4.BeautifulSoup(resp.text, "html.parser")

def get_site_xml():
	url = "https://teaching.dcs.aber.ac.uk/mmp"
	payload = {'username': 'USERNAME/EMAIL', 'password': 'PASSWORD'}

	payload['username'] = input("User id: ")
	payload['password'] = input("User Password: ")
	page = request_and_soup(url, payload)
	return page

def get_all_titles(page):
	titles = []
	for t in page.find_all('h3', {'class':'accHeader'}):
		titles.append(t.get_text())
	return titles

def get_all_keywords(page):
	keywords = []
	temp = ''
	for div in page.find_all('div', {'class':None, 'style':None,'id':None}):
		d = div.find('div', {'class':'suggestionBody'})
		h = div.find('h3')
		if not d is None and h is None:
			for kw in div.find_all('p'):
				if 'Keywords:' in kw.get_text():
					temp = kw.get_text()
					break
				else:
					temp = ''
			keywords.append(temp)
	return keywords

def div_search(page):
	for div in page.find_all('div', {'class':None, 'style':None,'id':None}):
		d = div.find('div', {'class':'suggestionBody'})
		h = div.find('h3')
		if not d is None and h is None:
			print(get_all_keywords(div))
			

def get_all_descriptions(page):
	descriptions = []
	for d in page.find_all('div', {'class':'suggestionBody'}):
		descriptions.append(d.get_text())
	return descriptions

def link_project_components(titles, keywords, descriptions):
	projects = []
	for i in range(len(titles)):
		projects.append(p.Project(titles[i], keywords[i], descriptions[i]))
	return projects
		

def extract_page_projects(page):
	titles = get_all_titles(page)
	keywords = get_all_keywords(page)
	descriptions = get_all_descriptions(page)
	print(len(titles), len(keywords), len(descriptions))
	return link_project_components(titles, keywords, descriptions)


def main():
	page = get_site_xml()
	projects = extract_page_projects(page)
	x = 0
	for i in range(5):
		x= int(input("Project Number: "))
		print(projects[x])



if __name__ == "__main__":
    main()