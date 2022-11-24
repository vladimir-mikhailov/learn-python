# TODO add db

directory = []

USER_SCHEMA = {
    'first_name': str,
    'last_name': str,
    'phone': str,
    'sex': str,
}


def add_fixtures(num):
    from faker import Faker
    from faker.providers import person, phone_number
    import random

    fake = Faker('ru_RU')
    new_users_ids = []

    for i in range(num):
        sex = random.randint(0, 2)
        user_data = {
            'first_name': fake.first_name_male() if sex else fake.first_name_female(),
            'last_name': fake.last_name_male() if sex else fake.last_name_female(),
            'phone': fake.phone_number(),
            'sex': 'M' if sex else 'F',
        }
        new_users_ids.append(add_user(user_data))
    return new_users_ids


def get_user(id):
    for user in directory:
        if user.get('id') == id:
            return user


def get_users():
    return directory


def add_user(user_data):
    id = len(directory) + 1
    new_user = {
        'id': id,
    }
    new_user.update(user_data)
    directory.append(new_user)
    return id


def update_user(id, user_data):
    for user in directory:
        if user['id'] == id:
            user.update(user_data)


def delete_user(id):
    global directory
    directory = [user for user in directory if user.get('id') != id]
    return True


def find_user_by_tg_id(tg_id):
    for user in directory:
        if user.get('tg_id') == tg_id:
            id = user.get('id')
            return id


if __name__ == '__main__':
    add_fixtures(3)
    print(*directory, sep='\n')
