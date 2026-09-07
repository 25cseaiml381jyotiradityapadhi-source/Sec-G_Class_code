'''def build_html_tag(tag, *content, **attributes):

    attr = ""
    for key, value in attributes.items():
        attr += f' {key}="{value}"'

    inner_content = "".join(content)

    return f"<{tag}{attr}>{inner_content}</{tag}>"
'''

def build_html_tag(tag, *content, **attributes):
    attr = ""

    for key, value in attributes.items():
        attr += f' {key}="{value}"'

    text = ""

    for item in content:
        text += item

    html = f"<{tag}{attr}>{text}</{tag}>"
    print(html)


tag = input("Enter HTML tag: ")
n = int(input("Enter number of content items: "))

content = []
for i in range(n):
    content.append(input("Enter content: "))

m = int(input("Enter number of attributes: "))

attributes = {}
for i in range(m):
    key = input("Enter attribute name: ")
    value = input("Enter attribute value: ")
    attributes[key] = value

build_html_tag(tag, *content, **attributes)
