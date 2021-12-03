# getLineTheme

LINE 着せ替えの情報を取得するライブラリです<br>
<br>

## Usage

```python
from getLineTheme import getLineTheme
getLineTheme = getLineTheme.getLineTheme("https://store.line.me/stickershop/product/23822/ja")

# @context
print(LineTheme.content.context)
# @type
print(LineTheme.content.type)
# package id
print(LineTheme.content.sku)
# package url
print(LineTheme.content.url)
# package name
print(LineTheme.content.name)
# package description
print(LineTheme.content.description)
# package image
print(LineTheme.content.image)
# offer @type
print(LineTheme.content.offers.type)
# offer price
print(LineTheme.content.offers.price)
# offer price currency
print(LineTheme.content.offers.priceCurrency)
# offer url
print(LineTheme.content.offers.url)
# zip url
print(LineTheme.content.zip)
```
