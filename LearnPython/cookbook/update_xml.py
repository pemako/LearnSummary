# -*- coding:utf-8 -*-

from xml.etree.ElementTree import Element, parse

doc = parse('pred.xml')

root = doc.getroot()

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'This is a test'

root.insert(2, e)

doc.write('newpred.xml', xml_declaration=True)
