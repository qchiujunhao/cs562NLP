import gzip
import argparse
import sys
from lxml import etree

parser = argparse.ArgumentParser()
parser.add_argument("file_names", nargs='*')
args = parser.parse_args()

for f in args.file_names:
	with gzip.open(f, 'r') as fin:
		content = fin.read()

	xml_parser = etree.XMLParser(remove_blank_text=True)
	et = etree.XML(content, parser=xml_parser)
	text = et.xpath("//DOC[@type='story']/TEXT/P/text()")

	for t in text:
		print(t)




