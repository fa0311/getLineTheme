# getLineTheme

LINE 着せ替えの情報を取得するライブラリです<br>
<br>
[getLineStamp](https://github.com/fa0311/getLineStamp) / getLineTheme<br>

## Usage

```python
from getLineTheme import getLineTheme
LineTheme = getLineTheme.getLineTheme("https://store.line.me/themeshop/product/09d8f1c5-b0f2-45a4-a0e6-222a9b94156a")

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
