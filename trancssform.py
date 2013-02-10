__author__ = 'dennis'

from sys import argv
from os.path import exists
import tinycss
from font_face import CSSFontFaceParser

script, style, inFileName, outFileName = argv


def init():
    """
    initialize and check inputs
    @return: errors
    """
    parser = tinycss.make_parser(CSSFontFaceParser)

    inFile = open(inFileName, 'r')

    stylesheet = parser.parse_stylesheet_file(inFile)

    if len(stylesheet.errors):
        print "Input stylesheet contains errors. Please validate your stylesheet and try again."
        print stylesheet.errors
        exit(0)
    else:
        print "Working on %s." % inFileName
        convertedStyles = convertStyles(stylesheet)


def convertStyles(stylesheet, style='block'):
    """
    Converts parsed stylesheet to specified style
    @param stylesheet: tinycss parsed Stylesheet object
    @param style: style to convert to, 'oneline' or 'block' (default)
    @return: list of output lines
    """
    print "Converting styles..."

    convertedStyles = []

    for rule in stylesheet.rules:
        if rule.at_keyword == None: # this is a plain rule
            # remove whitespace tokens and convert to string
            selector = "".join([str(token.value) for token in rule.selector if token.type != 'S'])
            selector = selector.replace(',', ',\n')
            print "{} {{ {}}}".format(selector, textDeclaration(rule.declarations))
        else:
            # just use @declarations as they are
            print rule


    return 0

def textDeclaration(properties):
    """
    serializes Declarations for output to a CSS file
    @param properties: object of class Declaration
    @return: serialized string of properties
    """
    propString = ''

    for property in properties:
        # remove newlines from whitespace tokens and convert to string
        propValue = ''
        for token in property.value:
            propValue += token.as_css().replace('\n', '')

        propString += "{}: {}; ".format(property.name, propValue)

    return propString


init()
