from ia.machine_learning import learn
from ia.train_parser import TrainParser

class Align:
    def __init__(self, ontos):
        self.ontos = ontos

    def align(self):
        train_parser = TrainParser()
        list_input = train_parser.parser_input(self.ontos)

        ml = learn()
        predict = ml.predict(list_input)
        if(predict > 0.95):
            print('Ontologies can be aligned')
        else:
            print('Ontologies cannot be aligned')