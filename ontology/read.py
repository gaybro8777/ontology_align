from owlready2 import *


class Read:
    def __init__(self, ontos):
        self.ontos = ontos

    def read(self):
        for pos in range(self.ontos):
            file = open("./results/ontology"+pos+".txt", "w+")

            file.write("Classes - ")
            list_classes = list(self.ontos[pos].classes())
            file.write(list_classes)

            file.write("Individuals - ")
            list_individuals = list(self.ontos[pos].individuals())
            file.write(list_individuals)

            file.write("Object properties - ")
            list_object_properties = list(self.ontos[pos].object_properties())
            file.write(list_object_properties)

            file.write("Data properties - ")
            list_data_properties = list(self.ontos[pos].data_properties())
            file.write(list_data_properties)
