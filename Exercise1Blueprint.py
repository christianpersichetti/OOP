import random
#THE BLUEPRINT, USED TO CREATE A CLASS


class Insect:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(insect, wings, legs, flight):
        insect.flight = 0
        insect.wings = 2
        insect.legs = 4


    def toss(insect):
        if random.rand(0,2,4) == 2:
             insect.wings = 'The insect has 2 wings'
        elif random.rand(0,2,4) == 4:
             insect.legs = 'The insect has 4 legs'
        else:
             insect.fligt = 'flight is ____________'
             



    def get_sideup(insect):
            return insect.wings, insect.legs, insect.flight
