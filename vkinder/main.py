from typing import List
import json
from .parameters import SearchParams
from .evaluators import evaluate_city, city_to_string, dummy


EVALUATORS = {
    'city': evaluate_city
}
ADAPTERS = {
    'city': city_to_string
}


def data_gaining(search_params: SearchParams, candidates: List[dict]) -> dict:
    assert isinstance(candidates, list)
    data = dict()

    for user_raw in candidates:
        weight = 0
        for field, evaluator in EVALUATORS.items():
            if not user_raw.get(field):
                continue
            if not search_params.registry.get(field):
                continue
            field_object = search_params.registry[field]

            adapter = ADAPTERS.get(
                field, dummy)

            weight += evaluator(
                adapter(user_raw[field]),
                field_object.value,
                field_object.weight,
            )

        data[user_raw['id']] = {'weight': weight, 'user': user_raw}

        filename = 'medium.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data,
                               sort_keys=False,
                               indent=4,
                               ensure_ascii=False,
                               separators=(',', ': ')))

    return data


def sorting_data(data):
    sorting_dict = {}
    for u_id, user in data.items():
        sorting_dict[u_id] = user['weight']

    sort_weight = dict(sorted(sorting_dict.items(), key=lambda item: item[1], reverse=True))

    filename = 'final.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(sort_weight,
                           sort_keys=False,
                           indent=2,
                           ensure_ascii=True,
                           separators=(',', ': ')))

    user_list = []
    for user in sort_weight.keys():
        user_list.append(user)
    top_10 = user_list[0:10]

    print(f'Десять лучших кандидатов - {top_10}')

    return sort_weight
