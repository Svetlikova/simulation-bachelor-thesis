import random

rarityThree = ['Fang', 'Vanilla', 'Plume', 'Melantha', 'Cardigan', 'Beagle', 'Kroos',
               'Lava', 'Hibiscus', 'Ansel', 'Steward', 'Orchid', 'Catapult', 'Midnight', 'Spot', 'Popukar']
#TODO finish lists so they are accurate
rarityFour = ['Haze', 'Jessica', 'Meteor', 'Shirayuki', 'Scavenger', 'Vigna', 'Doberman', 'Matoimaru', 'Frostleaf',
              'Mousse', 'Gravel', 'Rope', 'Myrrh', 'Perfumer', 'Matterhorn', 'Cuora', 'Gummy', 'Deepcolor',
              'Earthspirit', 'Shaw', 'Beehunter', 'Greyy', 'Vermeil', 'Myrtle', 'Sussurro', 'May', 'Ambriel',
              'Utage', 'Podenco', 'Click', 'Cutter', 'Jaye', 'Aciddrop', 'Arene', 'Jackie', 'Pinecone', 'Beanstalk',
              'Indigo', 'Roberta', 'Chestnut']
rarityFive = ['Ptilopsis', 'Zima', 'Texas', 'Franka', 'Lappland', 'Specter', 'Blue Poison', 'Platinum',
              'Meteorite', 'Skyfire', 'Mayer', 'Silence', 'Warfarin', 'Nearl', 'Projekt Red', 'Liskarm',
              'Croissant', 'Provence', 'Firewatch', 'Cliffheart', 'Pramanix', 'Istina', 'Sora', 'Manticore',
              'FEater', 'Nightmare', 'Swire', 'Executor', 'Asthesia', 'Glaucus', 'Waai Fu', 'GreyThroat',
              'Reed', 'Broca', 'Hung', 'Leizi', 'Sesa', 'Leonhardt', 'Ayerscape', 'Asbestos', 'Tsukinogi',
              'Beeswax', 'Chiave', 'Shamare', 'Elysium', 'Andrena', 'Flint', 'April', 'Whisperian', 'Kafka',
              'Iris', 'Aosta', 'Mr. Nothing', 'Toddifons', 'Akafuyu', 'Kirara', 'La Pluma', 'Mulberry',
              'Ashlock', 'Corroserum', 'Aurora', 'Blacknight', 'Quercus', 'Kazemaru', 'Rockrock', 'Windflit',
              'Hibiscus the Purifier', 'Cantabile', 'Greyy the Lighteningbearer', 'Proviso']
raritySix = ['testName']

n = 0.02
#first rarity type is selected, the chances are defined below

'''it ncreses by 0.02 but there are 3 values, meaning '''
probabilities = [0.4, 0.5, 0.08, n]
categories = ['rarityThree', 'rarityFour', 'rarityFive', 'raritySix']

def selectRarity():
    return random.choices(categories, probabilities)[0]

def selectOperatorR3():
    return ''.join(random.choices(rarityThree))

def selectOperatorR4():
    return' '.join(random.choices(rarityFour))
'''functions for 5/6* operators 
TODO: rate up, needs to allow changes, when you add new operator or easily change up rarities'''
def selectOperatorR5():
    return ''.join(random.choices(rarityFive))
'''TODO rate up'''

def selectOperatorR6():
    return''.join(random.choices(raritySix))

selected = None
'''function selects operation depending on selected rarity'''

def probabilityReset(probabilities):
    probabilities == [0.4, 0.5, 0.08, n]
    return probabilities

'''sets probability'''
def pprobabilitySet(probabilities, n, pity):
    floatPity = pity
    intPity = int(floatPity)
    probabilities[int (n)] = intPity
    return probabilities


    


def select_operator(selectRarity):
    selected = None
    if selectRarity == 'rarityFour':
        selected = selectOperatorR4()
    elif selectRarity == 'rarityThree':
        selected= selectOperatorR3()
    elif selectRarity == 'rarityFive':
        selected = selectOperatorR5()
    elif selectRarity == 'raritySix':
        selected = selectOperatorR6()
    return selected


'''simulation, rational players, stops after he gets what he wanted'''

pity = 0
'''@simulation
roll tracks number of rolls'''


def simulation():
    stop = False
    roll = 0
    pity = 0.02
    while not stop:
        roll += 1
        if roll <= 100:
            rarity = selectRarity()
            operator = select_operator(rarity)
            if rarity != 'raritySix' and roll < 50:
                print(roll)
                print(rarity)
                print(operator)
                print(pity)
            elif rarity != 'raritySix' and roll >= 50:
                pity += 0.02
                pity = round(pity, 2)
                print(roll)
                print(rarity)
                print(operator)
                print(pity)
                pprobabilitySet(probabilities, n, pity)
                '''TODO pity rate up'''
            elif rarity == 'raritySix':
                pity = 0
                probabilityReset(probabilities)
                print(roll)
                print(rarity)
                print(operator)
                print('the desired outcome was achieved, rational player stops rolling')
                stop = True
        elif roll >= 100:
            stop = True
            print('simulation finished')

print(simulation())