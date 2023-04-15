import random
import csv

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

pity = 0.02
#first rarity type is selected, the chances are defined below


categories = ['rarityThree', 'rarityFour', 'rarityFive', 'raritySix']

def selectRarity(pity):
    probabilities = probabilitySet(pity)
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

def probabilityReset(probabilities, p1, p2, p3, p4):
    probabilities [p1] = 0.4
    probabilities [p2] = 0.5
    probabilities [p3] = 0.08
    probabilities [p4] = 0.02
    return probabilities

'''sets probability'''
def probabilitySet(pity):
# Increase the probability of RaritySix
    newProbability = [(((1 - pity) / 0.98) * 0.4), (((1 - pity) / 0.98) * 0.5), (((1 - pity) / 0.98) * 0.08), pity]
#Decrese the other probabilities
    probabilities = newProbability
#Normalization of the probabilities - to ensure their sum equals to 1
    totalProbability = round(sum(newProbability),15)
    if totalProbability != 1:
        print("!ERROR, TOTAL PROBABILITY HAS TO SUM TO 1, total probability:")
        print(totalProbability)
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


'''@simulation
roll tracks number of rolls'''
number_of_rolls = 100

def simulation(number_of_rolls):
    stop = False
    roll = 0
    pity = 0.02
    while not stop:
        roll += 1
        if roll <= number_of_rolls:
            rarity = selectRarity(pity)
            operator = select_operator(rarity)
            print("_ _ _ _ _ _ _ _ _ _ _ _ ")
            if rarity != 'raritySix' and roll < 50:
                print(roll)
                print(rarity)
                print(operator)
                #print(pity)
                print(probabilitySet(pity))
            elif rarity != 'raritySix' and roll >= 50:
                pity += 0.02
                pity = round(pity, 2)
                probabilitySet(pity)
                print(roll)
                print(rarity)
                print(operator)
                #print(pity)
                print(probabilitySet(pity))
                '''TODO pity rate up'''
            elif rarity == 'raritySix':
                pity = 0.02
                probabilitySet(pity)
                print(roll)
                print(rarity)
                print(operator)
                #print(pity)
                print(probabilitySet(pity))
                print('the desired outcome was achieved, rational player stops rolling')
                stop = True
        elif roll >= number_of_rolls:
            stop = True
            print('simulation finished')

print(simulation(number_of_rolls))