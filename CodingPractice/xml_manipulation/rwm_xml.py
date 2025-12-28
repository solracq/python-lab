import xml.etree.ElementTree as ET

tree = ET.parse("animals.xml")
root = tree.getroot()

#read
for animal in root.findall("animal"):
    species = animal.find("species").text
    name = animal.find("name").text
    sound = animal.find("sound").text
    print(f"{name}, {species}, {sound}")

#Modify
for animal in root.findall("animal"):
    if animal.find("species").text == "Bird":
        animal.find("species").text = "Cat"
        animal.find("name").text = "Garfield"

for animal in root.findall("animal"):
    species = animal.find("species").text
    name = animal.find("name").text
    print(f"{species}, {name}")

# Add
new_animal = ET.Element("animal")
species = ET.SubElement(new_animal, "species")
species.text = "Cat"

name = ET.SubElement(new_animal, "name")
name.text = "Michi"

sound = ET.SubElement(new_animal, "sound")
sound.text = "Meow"

root.append(new_animal)

tree.write("animals2.xml")

def validate_animal_exists(species):
    tree = ET.parse("animals.xml")
    root = tree.getroot()
    for animal in root.findall("animal"):
        if animal.find("species").text == species:
            return True
    return False

assert validate_animal_exists("Dog")