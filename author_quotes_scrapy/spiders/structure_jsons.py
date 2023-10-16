import json
import faker
import random
import string


fake = faker.Faker()

with open('json_files/quotes.json', 'r') as f:
    quotes = json.load(f)


def get_authors():
    authors = []

    for quote in quotes:
        if quote["author"] not in authors:
            authors.append(quote["author"])
    
    return authors



def structure_func():
    structured_data = []
    for author_name in get_authors():
        author_data = {}

        author_data["fullname"] = author_name
        author_data["born_date"] = str(fake.date_object().strftime('%B %d, %Y'))
        author_data["born_location"] = fake.city()
        author_data["description"] = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 50)))

        structured_data.append(author_data)

    return structured_data




def fill_authors(structured_data):
    with open('json_files/authors.json', 'w') as f:
        json.dump(structured_data, f)


if __name__=='__main__':
    fill_authors(structure_func())