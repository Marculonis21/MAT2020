#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse('cd_catalog.xml')
root = tree.getroot()

cd_vars = []
for cd in root:
    _vars = []
    for var in cd:
        _vars.append(var.text)

    cd_vars.append(_vars)

cd_vars = sorted(cd_vars, key = lambda x: x[-1])

for title,artist,country,company,prize,year in cd_vars:
    print("Titul CD: {}".format(title))
    print("Umělec: {}".format(artist))
    print("Vydavatel: {} - rok: {}".format(company, year))
    print("Cena: {}$".format(prize))
    print()
