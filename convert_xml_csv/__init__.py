import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

PATH = os.path.dirname(os.path.realpath(__file__))
SRC_PATH = os.path.join(PATH, "Annotations")
TARGET_PATH = os.path.join(PATH, "Result")

if __name__ == "__main__":
    index = 0
    for file in os.listdir(SRC_PATH):
        tree = ET.parse(os.path.join(SRC_PATH, file))
        root = tree.getroot()
        filename = "Name"
        label = "Label"
        xmin = "Xmin"
        ymin = "Ymin"
        xmax = "Xmax"
        ymax = "Ymax"
        items = []
        for child in root:
            if child.tag == "filename":
                filename = child.text
            if child.tag == "object":
                for x in child:
                    if x.tag == "name":
                        label = x.text
                    if x.tag == "bndbox":
                        for y in x:
                            if y.tag == "xmin":
                                xmin = y.text
                            if y.tag == "ymin":
                                ymin = y.text
                            if y.tag == "xmax":
                                xmax = y.text
                            if y.tag == "ymax":
                                ymax = y.text
                        items.append({
                            "label": label,
                            "xmin": xmin,
                            "ymin": ymin,
                            "xmax": xmax,
                            "ymax": ymax
                        })

        for item in items:
            f = open(TARGET_PATH + str(index) + filename + ".csv", "wt")
            f.write(filename + "," + item['xmin'] + "," + item['xmax'] + "," + item['ymin'] + "," + item['ymax'] + "," + item['label'])
            f.close()