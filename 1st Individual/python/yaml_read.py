import yaml
from yaml.loader import SafeLoader

with open('./Files/data.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
