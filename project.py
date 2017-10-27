def get_keywords(keywords):
	start = keywords.find(':') + 1
	split_words = keywords[start:].split(',')
	for i in range(len(split_words)):
		split_words[i].strip()
		split_words[i] = split_words[i].lower()
	if '' in split_words:
		split_words.remove('')
	return split_words

""" Pulling from tags leaves 'On my shortlist' at the end of every title, this removes it"""
def clean_title(title):
	end = title.find('On my shortlist')
	return title[:end]


class Project():

	def __init__(self, title, keywords, description):
		self.title = clean_title(title)
		self.keywords = get_keywords(keywords)
		self.description = description

	def keywords_contain(self, search_string):
		return search_string.lower() in ' '.join(self.keywords)

	def broad_search(self, search_string):
		return self.keywords_contain(search_string) or search_string.lower() in self.title.lower() or search_string.lower() in self.description.lower()


	def __str__(self):
		return 'Title: ' + self.title + '\n' + 'Key Words: ' + ", ".join(str(x) for x in self.keywords)+ '\n' + 'Description: ' + self.description + '\n'