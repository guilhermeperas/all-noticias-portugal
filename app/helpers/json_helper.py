from flask import json


def get_nested_value(data, path):
    if not path or not isinstance(path, str): return None
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        elif isinstance(current, list) and key.isdigit():
            try:
                current = current[int(key)]
            except IndexError:
                return None
        else:
            return None
        if current is None: return None
    return current

def save_json(data,data_mapping):
    news = []

    container_key = data_mapping.get('container')
    base_img_url = data_mapping.get('base_img_url', "")
    items_list = data.get(container_key)

    for raw_item in items_list:
        clean_item = {}
        for key, path in data_mapping.items():
            if key in ["container", "base_img_url"]:
                continue

            value = get_nested_value(raw_item, path)
            clean_item[key] = value
        if clean_item.get("img") and base_img_url:
            clean_item["img"] = base_img_url + clean_item["img"]

        news.append(clean_item)
    return news

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data