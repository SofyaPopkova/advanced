from vkinder.parameters import SearchParams, StringField
from vkinder.vk import search, get_photos
from vkinder.main import data_gaining, sorting_data
import time


def _main():
    vk_login = ''
    vk_pw = ''
    age_min = input('Пожалуйста, введите минимальный желаемый возраст кандидата: ')
    age_max = input('Пожалуйста, введите максимальный желаемый возраст кандидата: ')
    city = input('Пожалуйста, введите ваш город: ')
    sex_choice = input('Пожалуйста, введите пол кандидата - 1 (если ищете женщину) или 2 (если ищете мужчину): ')
    params = SearchParams([
        StringField(name='city', value=city, weight=50),
    ])

    candidates = search(
        login=vk_login,
        password=vk_pw,
        fields=list(params.registry),
        age_min=age_min,
        age_max=age_max,
        sex=sex_choice,
        relation=6,
        is_closed=False
    )

    top_10 = data_gaining(search_params=params, candidates=candidates)
    sorted_result = sorting_data(top_10)
    sorted_top_10 = list(sorted_result)[0:10]

    for candidate in sorted_top_10:
        time.sleep(0.5)
        photos = get_photos(
            login=vk_login,
            password=vk_pw,
            owner_id=candidate,
        )
        photos_dict = dict()
        for photo in photos:
            likes = photo['likes']['count']
            for size in photo['sizes']:
                if size['type'] == 'x':
                    url = size['url']
            photos_dict[url] = likes
        top3_photos = sorted(photos_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
        print(f'Лучшие фото для кандидата (id {candidate}) - {top3_photos}')


if __name__ == '__main__':
    _main()
