# Used in API and legacy XML validation

from lxml import etree as ET

tree = ET.parse("animals2.xml")
root = tree.getroot()

# find all animals names
names = root.xpath("//animal/name/text()")
print(names)

sounds = root.xpath("//animal/sound/text()")
print(sounds)

species = root.xpath("//animal/species/text()")
print(species)

# Find animal by species
dog_name = root.xpath("//animal[species='Dog']/name/text()")
print(dog_name)

cat_name = root.xpath("//animal[species='Cat']/name/text()")
print(cat_name)

dog_sound = root.xpath("//animal[name='Rintintin']/sound/text()")
print(dog_sound)

animal_id_2 = root.xpath("//animal[@id='2']/name/text()")
print(animal_id_2)
