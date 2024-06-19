# Python DOM example

# import minidom module from the xml.dom package and assign it the alias m for convenience
import xml.dom.minidom as m

# Parse the XML file
doc = m.parse(r"C:\Projects\Py\chap1.xml")
#where r before the file path makes it a raw string, which means backslashes are treated as literal characters and not escape characters

# Get the node name of the document object (should be "#document")
node_name = doc.nodeName

# Retrieve a list of all <para> elements in the document
p_list = doc.getElementsByTagName("para")

# Example of processing the list of <para> elements
for para in p_list:
    print(para.toxml())  # Print the XML for each <para> element
