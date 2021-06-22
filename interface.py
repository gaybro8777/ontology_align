from ia.train_parser import TrainParser
from ia.machine_learning import learn
from ontology.get_ontos import GetOntos
from ontology.align import Align
from ontology.read import Read
import sys


class OntoInterface:
    def print_help(self):
        help = open("help", "r")
        print(help.read())
        help.close()

    def align_ontology(self):
        get_ontos = GetOntos()
        ontos = get_ontos.samples()
        Align(ontos)
        Align.align()

    def read_ontology(self):
        get_ontos = GetOntos()
        ontos = get_ontos.samples()
        Read(ontos)
        Read.read()
    
    def train_ml(self):
        dataset = sys.argv[2]
        
        get_ontos = GetOntos()
        ontos = get_ontos.data(dataset)
        reference = get_ontos.reference(dataset)

        train_parser = TrainParser()
        list_x, list_y = train_parser.create_tests(ontos, reference)

        ml = learn()
        ml.test_split(list_x, list_y)
        ml.train_ia()
        ml.predict_test()

if len(sys.argv) > 1:
    face = OntoInterface()
    type = sys.argv[1]
    if type == '-h':
        face.print_help()
    elif type == '-r':
        face.read_ontology()
    elif type == '-a':
        face.align_ontology()
    elif type == '-t':
        face.train_ml()
else:
    print("you have to pass a routine parameter")
