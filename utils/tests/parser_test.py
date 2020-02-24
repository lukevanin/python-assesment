from typing import List

from ..parser import Parser


def test_parser_init_empty_doc():
    doc = """"""
    parser = Parser(html=doc)


def test_complete_doc():
    doc = """<html>
    <head>
        <title>Bar</title>
        <style></style>
        <link type="text/css" />
        <link />
        <link type="text/css" />
    </head>
    <body>
        <img src="http://example.org/foo.png" >
        <img >
        <img src="http://example.org/bar.jpg" >
    </body>
    </html>"""
    p = Parser(html=doc)
    assert(p.title() == 'Bar')
    assert(p.images() == ['http://example.org/foo.png', 'http://example.org/bar.jpg'])
    assert(p.stylesheets() == 3)


# Title


def test_parse_no_title():
    doc = """"""
    parser = Parser(html=doc)
    assert(parser.title() == '')


def test_parse_title():
    doc = """<html><head><title>Foo</title></head></html>"""
    parser = Parser(html=doc)
    assert(parser.title() == 'Foo')


# Images


def test_parse_no_images():
    doc = """"""
    parser = Parser(html=doc)
    assert(parser.images() == [])


def test_parse_image():
    doc = """<html><body><img src="http://example.org/foo.png" ></body></html>"""
    parser = Parser(html=doc)
    assert(parser.images() == ['http://example.org/foo.png'])


def test_parse_no_src_image():
    doc = """<html><body><img ></body></html>"""
    parser = Parser(html=doc)
    assert(parser.images() == [])


# Stylesheets


def test_parse_no_stylesheets():
    doc = """"""
    parser = Parser(html=doc)
    assert(parser.stylesheets() == 0)


def test_parse_one_head_style_tag():
    doc = """<html><head><style></style></head></html>"""
    parser = Parser(html=doc)
    assert(parser.stylesheets() == 1)


def test_parse_one_body_style_tag():
    doc = """<html><body><style></style></body></html>"""
    parser = Parser(html=doc)
    assert(parser.stylesheets() == 1)


def test_parse_one_style_link_tag():
    doc = """<html><head><link type="text/css" /></head></html>"""
    parser = Parser(html=doc)
    assert(parser.stylesheets() == 1)


def test_parse_mixed_style_and_link_tags():
    doc = """<html><head><style></style><link type="text/css" /></head></html>"""
    parser = Parser(html=doc)
    assert(parser.stylesheets() == 2)


def test_parse_one_non_style_link_tag():
    doc = """<html><head><link /></head></html>"""
    parser = Parser(html=doc)
    assert(parser.stylesheets() == 0)