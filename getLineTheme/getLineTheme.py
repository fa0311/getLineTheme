from dataclasses import dataclass
import requests
import re
import json

class getLineTheme:
    def __init__(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('Request Error')
        # 男は黙って正規表現
        reg_json = r'<script type="application/ld\+json">\s([\s\S]*?)\s</script>'
        content = json.loads(re.findall(reg_json, response.text)[0])
        self.content =  getLineThemeData(
            content["@context"],
            content["@type"],
            content["sku"],
            content["url"],
            content["name"],
            content["description"],
            content["image"],
            content["offers"],
        )

@dataclass
class getLineThemeData:
    context: str = None
    type: str = None
    sku: str = None
    url: str = None
    name: str = None
    description: str = None
    image: str = None
    offers: dict = None
    
    def __post_init__(self):
        reg_zip = r'WEBSTORE/.*$'
        self.zip = re.sub(reg_zip, 'ANDROID/theme.zip', self.image)
        self.offers = getLineThemeOffers(
            self.offers["@type"],
            int(self.offers["price"]),
            self.offers["priceCurrency"],
            self.offers["url"],
        )

@dataclass
class getLineThemeOffers:
    type: str = None
    price: str = None
    priceCurrency: str = None
    url: str = None
