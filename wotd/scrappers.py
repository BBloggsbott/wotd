from lxml import etree
import requests
import re

from languages import Language, ENGLISH

TRANSPARENT_LANGUAGE_URL = "http://feeds.feedblitz.com/"
MERRIAM_WEBSTER_URL = "https://www.merriam-webster.com/word-of-the-day"

WORD_KEY = "word"
MEANING_KEY = "meaning"
POS_KEY = "pos"
EXAMPLE_KEY = "example"
EXAMPLE_EN_KEY = "example_en"


def get_from_transparent_language(lang :Language):
    url = TRANSPARENT_LANGUAGE_URL + lang.transparent_language_endpoint
    TL_POS_KEY = "Part of speech:"
    TL_EXAMPLE_KEY = "Example sentence:"
    TL_EXAMPLE_EN_KEY = "Sentence meaning:"

    word_of_the_day = {}
    
    response = requests.get(url)
    if response.status_code == 200:
        xml_root = etree.fromstring(response.content)
        channel = xml_root.find("channel")
        item = channel.find("item")
        title = item.find("title")
        description = item.find("description")
        html = etree.HTML(description.text)
        body = html.getchildren()[0]
        table = body.getchildren()[0]
        rows = table.getchildren()

        for row in rows:
            th = row.find("th")
            td = row.find("td")
            if th.text == TL_POS_KEY:
                word_of_the_day[POS_KEY] = td.text
            elif th.text == TL_EXAMPLE_KEY:
                word_of_the_day[EXAMPLE_KEY] = td.text
            elif th.text == TL_EXAMPLE_EN_KEY:
                word_of_the_day[EXAMPLE_EN_KEY] = td.text

        word_of_the_day[WORD_KEY] = title.text.split(":")[0]
        word_of_the_day[MEANING_KEY] = title.text.split(":")[1].strip()

        return word_of_the_day

def get_from_merriam_webster(lang :Language):
    url = MERRIAM_WEBSTER_URL
    response = requests.get(url)
    if response.status_code == 200:
        html_re = re.compile(r'<.*?>')
        doc = etree.HTML(response.content.decode("utf-8"))
        word_div = doc.xpath("//div[@class='word-and-pronunciation']")[0]
        word = word_div.find("h1").text
        pos_span = doc.xpath("//span[@class='main-attr']")[0]
        pos = pos_span.text
        meaning_div = doc.xpath("//div[@class='wod-definition-container']")[0]
        meaning_p = meaning_div.find("p")
        meaning = html_re.sub("", etree.tostring(meaning_p).decode("utf-8"))[1:].strip()
        example_div = doc.xpath("//div[@class='wotd-examples']")[0]
        example_p = example_div.find("p")
        example = html_re.sub("", etree.tostring(example_p).decode("utf-8")).strip().replace("&#8212;", "-")

        word_of_the_day = {
            WORD_KEY: word,
            MEANING_KEY: meaning,
            POS_KEY: pos,
            EXAMPLE_KEY: example
        }

        return word_of_the_day
