import xml.dom.minidom
  
docs = xml.dom.minidom.parse("./Files/data.xml")

print(docs.toxml())