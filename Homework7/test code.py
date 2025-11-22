import yaml
import json
with open("menu_price.json", "r", encoding="utf-8") as data:
    data = json.load(data)
print(yaml.dump(data, default_flow_style=False))