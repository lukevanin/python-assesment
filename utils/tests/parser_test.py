from ..parser import Parser


def test_parse_empty_doc():
    doc = """"""
    p = Parser().parse(doc)
    assert(p['title'] == '')
    assert(p['image_urls'] == [])
    assert(p['stylesheet_count'] == 0)