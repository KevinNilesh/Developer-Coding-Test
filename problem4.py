def sort_dict_by_values(d: dict) -> dict:
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    return sorted_dict


print(sort_dict_by_values({"a": 2, "b": 1, "c": 3}))
