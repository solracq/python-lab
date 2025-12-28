import xml.etree.ElementTree as ET
import json

tree = ET.parse("animals.xml")
root = tree.getroot()

data = []

for animal in root:
    data.append({
        "species": animal.find("species").text,
        "name": animal.find("name").text,
        "sound": animal.find("sound").text
    })

json_data = json.dumps(data, indent=4)
print(json_data)