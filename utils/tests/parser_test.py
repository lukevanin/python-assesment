from typing import List

from ..parser import Parser


def check_result(result: dict, title: str, image_urls: List[str], stylesheet_count: int):
    assert(result['title'] == title)
    assert(result['image_urls'] == image_urls)
    assert(result['stylesheet_count'] == stylesheet_count)


def test_parse_empty_doc():
    doc = """"""
    res = Parser().parse(doc)
    check_result(res, title='', image_urls=[], stylesheet_count=0)


def test_parse_title():
    doc = """<html><head><title>Foo</title></head></html>"""
    res = Parser().parse(doc)
    check_result(res, title='Foo', image_urls=[], stylesheet_count=0)
