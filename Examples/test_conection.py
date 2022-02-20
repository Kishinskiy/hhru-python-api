from hhru.api import HeadHunter

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
con = HeadHunter()
con.params = headers

if __name__ == '__main__':
    vacations = con.get_vacancies("Python разработчик", 20)
    print(len(vacations['items']), vacations)
