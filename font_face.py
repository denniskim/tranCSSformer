# coding: utf8
"""
    tinycss.font_face

    Support for @font-face syntax
"""

from __future__ import unicode_literals, division
from tinycss.css21 import CSS21Parser, ParseError


class fontFaceRule(object):
    """
    A parsed CSS @font-face rule

    http://www.w3.org/TR/css3-fonts/#font-face-rule
    """
    at_keyword = '@font-face'

    def __init__(self, declarations, line, column):
        self.declarations = declarations
        self.line = line
        self.column = column


class CSSFontFaceParser(CSS21Parser):
    """
    Extend CSS21Parser for @font-face syntax
    """

    def parse_at_rule(self, rule, previous_rules, errors, context):
        declarations, body_errors = self.parse_declaration_list(rule.body)
        errors.extend(body_errors)
        return fontFaceRule(declarations, rule.line, rule.column)
