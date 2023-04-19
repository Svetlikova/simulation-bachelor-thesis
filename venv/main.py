import csv
import random

import matplotlib.pyplot as mpt
import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd

# Sample space
rarity_three = ['Fang', 'Vanilla', 'Plume', 'Melantha', 'Cardigan', 'Beagle', 'Kroos',
               'Lava', 'Hibiscus', 'Ansel', 'Steward', 'Orchid', 'Catapult', 'Midnight', 'Spot', 'Popukar']
rarity_four = ['Haze', 'Jessica', 'Meteor', 'Shirayuki', 'Scavenger', 'Vigna', 'Doberman', 'Matoimaru', 'Frostleaf',
              'Mousse', 'Gravel', 'Rope', 'Myrrh', 'Perfumer', 'Matterhorn', 'Cuora', 'Gummy', 'Deepcolor',
              'Earthspirit', 'Shaw', 'Beehunter', 'Greyy', 'Vermeil', 'Myrtle', 'Sussurro', 'May', 'Ambriel',
              'Utage', 'Podenco', 'Click', 'Cutter', 'Jaye', 'Aciddrop', 'Arene', 'Jackie', 'Pinecone', 'Beanstalk',
              'Indigo', 'Roberta', 'Chestnut']
rarity_five = ['Ptilopsis', 'Zima', 'Texas',  #'Franka',
              'Lappland', 'Specter', 'Blue Poison', 'Platinum',
              'Meteorite', 'Skyfire', 'Mayer', 'Silence', 'Warfarin', 'Nearl', 'Projekt Red', 'Liskarm',
              'Croissant', 'Provence', 'Firewatch', 'Cliffheart', 'Pramanix', 'Istina', 'Sora', 'Manticore',
              'FEater', 'Nightmare', 'Swire', 'Executor', 'Asthesia', 'Glaucus', 'Waai Fu', 'GreyThroat',
              'Reed', 'Broca', 'Hung', 'Leizi', 'Sesa', 'Leonhardt', 'Ayerscape', 'Asbestos', 'Tsukinogi',
              'Beeswax', 'Chiave', 'Shamare', 'Elysium', 'Andrena', 'Flint', 'April', 'Whisperian', 'Kafka',
              'Iris', 'Aosta', 'Mr. Nothing', 'Toddifons', 'Akafuyu', 'Kirara', 'La Pluma', 'Mulberry',
              'Ashlock', 'Corroserum', 'Aurora', 'Blacknight', 'Quercus', 'Kazemaru', 'Rockrock', 'Windflit',
              'Hibiscus the Purifier', 'Cantabile', 'Greyy the Lighteningbearer',  #'Proviso'
               ]
rarity_six = ['Exusiai', 'Siege', 'Ifrit', 'Eyjafjalla', 'Angelina', 'Shining', 'Nightingale', 'Hoshiguma',
             'Saria', 'SilverAsh', 'Skadi', 'Ch\'en', 'Magallan', 'Hellagur', 'Schwarz', 'Mostima', 'Blaze',
             'Aak', 'Ceobe', 'Bagpipe', 'Rosa', 'Suzuran', 'Phantom', 'Weedy', 'Thorns', 'Eunectes', 'Surtr',
             'Mudrock', 'Mountain', 'Archetto', 'Blemishine', 'Saga', 'Passanger', 'Kal\'tsit', 'Carnelian',
             'Pallas', 'Mizuki', 'Saileach', 'Fartooth', 'Flametail', 'Gnosis', 'Lee', 'Goldenglow', 'Fiamemtta',
             'Horn', 'Irene', 'Ebenholz', 'Pozëmka', 'Dorothy', #'Mlynar'
             ]
# Value mapped at every point of experiment - determines probabilities
pity = 0.02

# Sample space - categories represent rarities
categories = [3, 4, 5, 6]

def selectRarity(pity):
    probabilities = probabilitySet(pity)
    return random.choices(categories, probabilities)[0]

# Functions
def selectOperatorR3():
    return ''.join(random.choices(rarity_three))


def selectOperatorR4():
    return' '.join(random.choices(rarity_four))


def selectOperatorR5():
    # Specific operators rate up - 50% chance one of the 5 star operators will be one of selected
    rate_up = ['Franka', 'Proviso']
    rate_up_choice = ['rate_up', 'no_rate_up']
    chose = ''.join(random.choices(rate_up_choice))
    if chose == 'rate_up':
        result = ''.join(random.choices(rate_up))
    elif chose == 'no_rate_up':
        result = ''.join(random.choices(rarity_five))
    else:
        raise "Error, invalid value in rarity 5 selection."
    return result


def selectOperatorR6():
    rate_up = ['Mlynar']
    rate_up_choice = ['rate_up', 'no_rate_up']
    chose = ''.join(random.choices(rate_up_choice))
    if chose == 'rate_up':
        result = ''.join(random.choices(rate_up))
    elif chose == 'no_rate_up':
        result = ''.join(random.choices(rarity_six))
    else:
        raise "Error, invalid value in rarity 6 selection."
    return result


selected = None
'''function selects operation depending on selected rarity'''


# Probability measure - assign probability based on pity - value changed by previous state
def probabilitySet(pity):
# Increase the probability of RaritySix
    newProbability = [(((1 - pity) / 0.98) * 0.4), (((1 - pity) / 0.98) * 0.5), (((1 - pity) / 0.98) * 0.08), pity]
#Decrese the other probabilities
    probabilities = newProbability
#Normalization of the probabilities - to ensure their sum equals to 1
    totalProbability = round(sum(newProbability),15)
    if totalProbability != 1:
        print(totalProbability)
        return("!ERROR, TOTAL PROBABILITY HAS TO SUM TO 1, total probability: ")
    return probabilities



def select_operator(selectRarity):
    selected = None
    if selectRarity == 4:
        selected = selectOperatorR4()
    elif selectRarity == 3:
        selected= selectOperatorR3()
    elif selectRarity == 5:
        selected = selectOperatorR5()
    elif selectRarity == 6:
        selected = selectOperatorR6()
    return selected

def csv_write_data(data):
    with open('simulation.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


'''Set number of rolls'''
number_of_rolls = 100

def simulation(number_of_rolls):
    stop = False
    roll = 0
    pity = 0.02
    change = []
    while not stop:
        roll += 1
        #operator of the rarity 5 or 6 guaranteed in the first 10 rolls
        if roll==10 and (5 or 6) not in change:
            rarity =random.choices([5, 6], [0.8, 0.2])[0]
            operator = select_operator(rarity)
            data = [roll, rarity, operator]
            csv_write_data(data)
        elif roll <= number_of_rolls:
            rarity = selectRarity(pity)
            operator = select_operator(rarity)
            data = [roll, rarity, operator]
            change.append(rarity)
            print("_ _ _ _ _ _ _ _ _ _ _ _ ")
            #write data in csv for further work with results
            csv_write_data(data)
            if rarity != 6 and roll < 50:
                print(roll)
                print(rarity)
                print(operator)
                print(probabilitySet(pity))
            elif rarity != 6 and roll >= 50:
                pity += 0.02
                pity = round(pity, 2)
                probabilitySet(pity)
                print(roll)
                print(rarity)
                print(operator)
                #print(pity)
                print(probabilitySet(pity))
            elif rarity == 6:
                pity = 0.02
                probabilitySet(pity)
                print(roll)
                print(rarity)
                print(operator)
                #print(pity)
                print(probabilitySet(pity))
                #print('the desired outcome was achieved, rational player stops rolling')
                #stop = True
        elif roll>=number_of_rolls:
            stop = True
            print('simulation finished')

print(simulation(number_of_rolls))


'''graphical representation of resaults - histogram a poxplot from data'''
df = pd.read_csv('simulation.csv')
print(df.describe())
plt.hist(df['Rarity'], bins=4)
plt.title('Histogram of rarity distribution \n')
plt.show()

df.boxplot('Roll Number', by='Rarity')
plt.title('\n')
plt.xlabel('Rarity')
plt.ylabel('Roll Number')
plt.show()

