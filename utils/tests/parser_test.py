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


def test_parse_image():
    doc = """<html><body><img src="http://example.org/foo.png" ></body></html>"""
    parser = Parser(html=doc)
    assert(parser.images() == ['http://example.org/foo.png'])


def test_parse_no_src_image():
    doc = """<html><body><img ></body></html>"""
    parser = Parser(html=doc)
    assert(parser.images() == [])


def test_parse_no_image():
    doc = """<html><body></body></html>"""
    parser = Parser(html=doc)
    assert(parser.images() == [])
