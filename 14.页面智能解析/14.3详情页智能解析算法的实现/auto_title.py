from lxml.html import HtmlElement, fromstring

html = open('detail.html', encoding='utf-8').read()
element = fromstring(html=html)

METAS = [
    './/meta[starts-with(@property, "og:title")]/@content',
    './/meta[starts-with(@name, "og:title")]/@content',
    './/meta[starts-with(@property, "title")]/@content',
    './/meta[starts-with(@name, "title")]/@content',
    './/meta[starts-with(@property, "page:title")]/@content'
]


# 根据METAS列表提取标题
def extract_by_meta(element: HtmlElement) -> str:
    for xpath in METAS:
        title = element.xpath(xpath)
        if title:
           return ''.join(title)


# 根据title标签提取标题
def extract_by_title(element: HtmlElement):
    return ''.join(element.xpath('//title//text()')).strip()


# 根据h标签提取标题
def extract_by_h(element: HtmlElement):
    hs = element.xpath('//h1//text()|//h2//text()|//h3//text()')
    return hs or []


def similarity(s1, s2, i):
    i += 1
    if not s1 or not s2:
        return 0
    s1_set = set(list(s1))
    s2_set = set(list(s2))
    intersection = s1_set.intersection(s2_set)
    union = s2_set.intersection(s2_set)
    return len(intersection) / len(union)


def extract_title(element: HtmlElement):
    title_extracted_by_meta = extract_by_meta(element)
    title_extracted_by_title = extract_by_title(element)
    title_extracted_by_h = extract_by_h(element)

    # if title_extracted_by_meta:
    #     return title_extracted_by_meta
    i = 0
    title_extracted_by_h = sorted(title_extracted_by_h,
                                  key=lambda x: similarity(x, title_extracted_by_title, i),
                                  reverse=True)

    if title_extracted_by_h:
        return title_extracted_by_h[0]

    return title_extracted_by_title


print(extract_title(element))
