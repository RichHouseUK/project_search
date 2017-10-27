import project_finder as finder
import project as p



def all_keywords(projects):
	for proj in projects:
		for k in proj.keywords:
			yield k

def count_keywords(projects):
	keywords = {}
	for k in all_keywords(projects):
		if not k in keywords:
			keywords[k] = 1
		else:
			keywords[k] += 1
	return keywords

def print_keywords(keyword_dict):
	for key, value in sorted(keyword_dict.items(), key=lambda item: (item[1], item[0]), reverse=True):
		print ('{}: {}'.format(key, value))

def current_selection(projects, masks):
	master_mask = []
	for m in masks:
		master_mask.extend(m)
	return [projects[i] for i in range(len(projects)) if not i in master_mask]

def keyword_search(projects, search_string):
	new_mask = []
	for i, proj in enumerate(projects):
		if not proj.keywords_contain(search_string):
			new_mask.append(i)
	return new_mask

def broad_search(projects, search_string):
	new_mask = []
	for i, proj in enumerate(projects):
		if not proj.broad_search(search_string):
			new_mask.append(i)
	return new_mask


def menu(remaining):
	print('\n\nProject Explorer - {} projects left in selection'.format(remaining))
	print('  1 - Display all remaining Project names')
	print('  2 - Display all Projects detailed')
	print('  3 - Display all remaining Keywords')
	print('  4 - Refine by Keyword')
	print('  5 - Refine by broad search (contained in title/keyword/description)')
	print('  6 - Go back one refinement')
	print('  7 - Reset to full list')
	print('  8 - Exit')
	return int(input("Enter option number: "))

def manage_option(projects, masks, input_value):
	print('\n')
	cur_projects = current_selection(projects, masks)
	if input_value == 8:
		return 1
	elif input_value == 1:
		for proj in cur_projects:
			print(proj.title)
	elif input_value == 2:
		for proj in cur_projects:
			print(proj)
	elif input_value == 3:
		print_keywords(count_keywords(cur_projects))
	elif input_value == 4:
		masks.append(keyword_search(projects, input("Enter search string: ")))
	elif input_value == 5:
		masks.append(broad_search(projects, input("Enter search string: ")))
	elif input_value == 6:
		if len(masks) > 0:
			masks.pop()
	elif input_value == 7:
		masks = []

	return 0

def user_loop(projects):
	masks = []
	input_value = 0
	while 1:
		input_value = menu(len(current_selection(projects, masks)))
		if manage_option(projects, masks, input_value):
			break

def main():
	projects = finder.retrieve_projects()
	user_loop(projects)
	



if __name__ == "__main__":
    main()