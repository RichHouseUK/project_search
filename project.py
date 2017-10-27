def get_keywords(keywords):
	start = keywords.find(':') + 1
	return keywords[start:].split(',')

def clean_title(title):
	end = title.find('On my shortlist')
	return title[:end]


class Project():

	def __init__(self, title, keywords, description):
		self.title = clean_title(title)
		self.keywords = get_keywords(keywords)
		self.description = description

	def __str__(self):
		return 'Title: ' + self.title + '\n' + 'Key Words: ' + ", ".join(str(x) for x in self.keywords)+ '\n' + 'Description: ' + self.description + '\n'