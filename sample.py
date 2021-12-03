from getLineTheme import getLineTheme


if __name__ == '__main__':
    print("Enter the LineTheme URL")
    print("Example: https://store.line.me/themeshop/product/09d8f1c5-b0f2-45a4-a0e6-222a9b94156a")
    url = input()
    LineTheme = getLineTheme.getLineTheme(url)
    print(LineTheme.content.context)
    print(LineTheme.content.type)
    print(LineTheme.content.sku)
    print(LineTheme.content.url)
    print(LineTheme.content.name)
    print(LineTheme.content.description)
    print(LineTheme.content.image)
    print(LineTheme.content.offers.type)
    print(LineTheme.content.offers.price)
    print(LineTheme.content.offers.priceCurrency)
    print(LineTheme.content.offers.url)
    print(LineTheme.content.zip)