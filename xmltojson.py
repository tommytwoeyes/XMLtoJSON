#!/usr/bin/env python

import xmltodict
import json


class XMLtoJson(object):
    
    def __init__(self, xml_string_or_file, debug=False):
        self.debug = debug
        
        # Check if I've been given a file
        try:
            xml_file = open(xml_string_or_file)
            self.xml_string = xml_file.read()
        except IOError:
            self.xml_string = xml_string_or_file
            
        self._create_dict()
            
    def _create_dict(self):
        self.data_object = xmltodict.parse(self.xml_string)
        if self.debug == True:
            print("Data object: {0}".format(self.data_object))
            
    def get_json(self):
        self.json = json.dumps(self.data_object)
        return self.json


if __name__ == "__main__":
	example_xml_file = "./example.xml"
	xmlparser = XMLtoJson(example_xml_file)
	print(xmlparser.get_json())