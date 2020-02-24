from typing import List

from ..parser import Parser


def test_parser_init_empty_doc():
    doc = """"""
    parser = Parser(html=doc)
    assert(parser.title() == '')
    assert(parser.images() == [])
    assert(parser.stylesheets() == 0)


def test_parse_title():
    doc = """<html><head><title>Foo</title></head></html>"""
    parser = Parser(html=doc)
    assert(parser.title() == 'Foo')
