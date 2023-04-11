import random

rarityThree = ['Fang', 'Vanilla', 'Plume', 'Melantha', 'Cardigan', 'Beagle', 'Kroos',
               'Lava', 'Hibiscus', 'Ansel', 'Steward', 'Orchid', 'Catapult', 'Midnight', 'Spot', 'Popukar']
#TODO finish lists so they are accurate
rarityFour = ['Haze', 'Jessica', 'Meteor', 'Shirayuki', 'Scavenger', 'Vigna', 'Doberman', 'Matoimaru']
rarityFive = ['test1', 'test2']
raritySix = ['wintest']

categories = ['rarityThree', 'rarityFour', 'rarityFive', 'raritySix']

#first rarity type is selected, the chances are defined below
probabilities = [0.4, 0.5, 0.08, 0.02]
#def select() =
selectRarity = random.choices(categories, probabilities)[0]
print(selectRarity)
set(selectRarity)

selectOperatorR3 = ''.join(random.choices(rarityThree))
selectOperatorR4 = ''.join(random.choices(rarityFour))
selectOperatorR5 = ''.join(random.choices(rarityFive))
selectOperatorR6 = ''.join(random.choices(raritySix))

selected = None
def selectOperator(selectRarity):
    if (selectRarity == 'rarityFour'):
        selected = selectOperatorR4
    elif (selectRarity== 'rarityThree'):
        selected= selectOperatorR3
    elif (selectRarity == 'rarityFive'):
        selected = selectOperatorR5
    if (selectRarity =='raritySix'):
        selected = selectOperatorR6
    return selected

print(selectOperator(selectRarity))

