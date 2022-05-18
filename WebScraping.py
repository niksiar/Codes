"""
The full list of courses available on the maktabkhooneh website (at the time we are writing this question) can be viewed 
in 56 pages at this link. 

Information on various courses including:

Name of Course
Lesson teacher name
Name of the educational institution offering the course

Extract and save in a dictionary or list and then save it to a file.
"""


import requests
from bs4 import BeautifulSoup

dic = {}


def append_value(dict_obj, key, value):
    if key in dict_obj:

        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]

        dict_obj[key].append(value)
    else:
        dict_obj[key] = value


for page_no in range(1, 56):
    print('Now Searching Page Number ' + str(page_no))
    page = requests.get(f"https://maktabkhooneh.org/learn/?p={page_no}")
    soup = BeautifulSoup(page.text, 'html.parser')

    course_names = []
    course_teachers = []
    course_institution = []
    for div in soup.find_all('div', {'class': "course-card__title"}):
        course_names.append(div.text.strip())

    for div in soup.find_all('div', {'class': "course-card__teacher"}):
        course_teachers.append(div.text.strip())

    for div in soup.find_all('div', {'class': "course-card__uni-title"}):
        course_institution.append(div.text.strip())

    # print('names', course_names)
    # print('teachers', course_teachers)
    # print('unis', course_institution)

    for x in range(len(course_names)):
        append_value(dic, course_institution[x], course_names[x])
        append_value(dic, course_institution[x], course_teachers[x])
# print('dic', dic)
f = open("/Users/saman/Desktop/maktabkhoone/maktabkhoone.txt", "r+")
with open('/Users/saman/Desktop/maktabkhoone/maktabkhoone.txt', 'w+') as file:
    for x in dic:
        no = 1
        file.write('لیست دروس ' + '<' + x + '>' + '\n')
        for t in range(0, len(dic[x]), 2):
            try:
                file.write(str(no) + '-' + dic[x][t] + ': ' + dic[x][t + 1] + '\n')
                no += 1
            except:
                continue
        file.write('\n')
print(f.read())
