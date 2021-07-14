import vk


APP_ID = 205147787
VERSION = 5.89
TOKEN = input('Пожалуйста, введите ваш токен: ')


def search(login, password, fields, age_min, age_max, sex, relation, is_closed) -> list:

    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password
                             )

    vkapi = vk.API(session)

    return vkapi.users.search(
        v=VERSION,
        count=1000,
        sex=sex,
        age_from=age_min,
        fields=','.join(fields),
        age_to=age_max,
        access_token=TOKEN,
        relation=6,
        is_closed=False
    )['items']


def get_photos(login, password, owner_id) -> list:
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password,
                             access_token=TOKEN
                             )

    vkapi = vk.API(session)

    photos_response = vkapi.photos.get(
        v=VERSION,
        count=1000,
        album_id='profile',
        extended=1,
        owner_id=owner_id,
        access_token=TOKEN
    )['items']

    return photos_response
