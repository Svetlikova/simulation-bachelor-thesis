import csv
import random
import matplotlib.pyplot as plt
import pandas as pd

# Sample space
rarity_three = ['Fang', 'Vanilla', 'Plume', 'Melantha', 'Cardigan', 'Beagle', 'Kroos',
                'Lava', 'Hibiscus', 'Ansel', 'Steward', 'Orchid', 'Catapult', 'Midnight', 'Spot', 'Popukar']
rarity_four = ['Haze', 'Jessica', 'Meteor', 'Shirayuki', 'Scavenger', 'Vigna', 'Doberman', 'Matoimaru', 'Frostleaf',
               'Mousse', 'Gravel', 'Rope', 'Myrrh', 'Perfumer', 'Matterhorn', 'Cuora', 'Gummy', 'Deepcolor',
               'Earthspirit', 'Shaw', 'Beehunter', 'Greyy', 'Vermeil', 'Myrtle', 'Sussurro', 'May', 'Ambriel',
               'Utage', 'Podenco', 'Click', 'Cutter', 'Jaye', 'Aciddrop', 'Arene', 'Jackie', 'Pinecone', 'Beanstalk',
               'Indigo', 'Roberta', 'Chestnut']
rarity_five = ['Ptilopsis', 'Zima', 'Texas',  # 'Franka',
               'Lappland', 'Specter', 'Blue Poison', 'Platinum',
               'Meteorite', 'Skyfire', 'Mayer', 'Silence', 'Warfarin', 'Nearl', 'Projekt Red', 'Liskarm',
               'Croissant', 'Provence', 'Firewatch', 'Cliffheart', 'Pramanix', 'Istina', 'Sora', 'Manticore',
               'FEater', 'Nightmare', 'Swire', 'Executor', 'Asthesia', 'Glaucus', 'Waai Fu', 'GreyThroat',
               'Reed', 'Broca', 'Hung', 'Leizi', 'Sesa', 'Leonhardt', 'Ayerscape', 'Asbestos', 'Tsukinogi',
               'Beeswax', 'Chiave', 'Shamare', 'Elysium', 'Andrena', 'Flint', 'April', 'Whisperian', 'Kafka',
               'Iris', 'Aosta', 'Mr. Nothing', 'Toddifons', 'Akafuyu', 'Kirara', 'La Pluma', 'Mulberry',
               'Ashlock', 'Corroserum', 'Aurora', 'Blacknight', 'Quercus', 'Kazemaru', 'Rockrock', 'Windflit',
               'Hibiscus the Purifier', 'Cantabile', 'Greyy the Lighteningbearer',  # 'Proviso'
               ]
rarity_six = ['Exusiai', 'Siege', 'Ifrit', 'Eyjafjalla', 'Angelina', 'Shining', 'Nightingale', 'Hoshiguma',
              'Saria', 'SilverAsh', 'Skadi', 'Ch\'en', 'Magallan', 'Hellagur', 'Schwarz', 'Mostima', 'Blaze',
              'Aak', 'Ceobe', 'Bagpipe', 'Rosa', 'Suzuran', 'Phantom', 'Weedy', 'Thorns', 'Eunectes', 'Surtr',
              'Mudrock', 'Mountain', 'Archetto', 'Blemishine', 'Saga', 'Passanger', 'Kal\'tsit', 'Carnelian',
              'Pallas', 'Mizuki', 'Saileach', 'Fartooth', 'Flametail', 'Gnosis', 'Lee', 'Goldenglow', 'Fiamemtta',
              'Horn', 'Irene', 'Ebenholz', 'Pozëmka', 'Dorothy',  # 'Mlynar'
              ]
# Value mapped at every point of experiment - determines probabilities
pity = 0.02
# Sample space - categories represent rarities
categories = [3, 4, 5, 6]

# Probability measure - assign probability based on pity - value changed by previous state
def probability_set(pity):
    # Increase the probability of RaritySix
    new_probability = [(((1 - pity) / 0.98) * 0.4), (((1 - pity) / 0.98) * 0.5), (((1 - pity) / 0.98) * 0.08), pity]
    # Decrese the other probabilities
    probabilities = new_probability
    # Normalization of the probabilities - to ensure their sum equals to 1
    total_probability = round(sum(new_probability), 16)
    if total_probability != 1:
        print(total_probability)
        raise "Total sum of probabilities has to equal! instead its value is" + str(total_probability) +"!"
    return probabilities

probabilities = probability_set(pity)



# Functions selecting specific operator in case defined rarity has been selected
def select_operator_r3():
    return ''.join(random.choices(rarity_three))


def select_operator_r4():
    return ' '.join(random.choices(rarity_four))


def select_operator_r5():
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


def select_operator_r6():
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



# Based on rarity this function selects operator
def select_operator(select_rarity):
    selected = None
    if select_rarity == 4:
        selected = selectOperatorR4()
    elif select_rarity == 3:
        selected = selectOperatorR3()
    elif select_rarity == 5:
        selected = selectOperatorR5()
    elif select_rarity == 6:
        selected = selectOperatorR6()
    return selected


# CSV writer, function used to transfer data into csv
# Change the name of CSV file for more outputs
def csv_write_data(data):
    with open('simulation.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
        print("_ _ _ _ _ _ _ _ _ _ _ _ ")
        print(data)

def csv_write_cost(rows_cost):
    with open('cost.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rows_cost)

# The main function of simulation
def simulation():
    # Define initial values
    number_of_rolls = 1000
    stop = False
    roll = 0
    pity = 0.02
    change = False
    pity_counter = 0
    cost = 0
    while not stop:
        probabilities = probability_set(pity)
        roll += 1
        cost += 600
        print("Pity counter value is: " + str(pity_counter)+"/50")
        print(probabilities)
        # Operator of the rarity 5 or 6 guaranteed in the first 10 rolls
        if roll == 10 and change is False:
            rarity = random.choices([5, 6], [0.8, 0.2])[0]
            operator = select_operator(rarity)
            data = [roll, rarity, operator]
            csv_write_data(data)
            if rarity != 6:
                pity_counter += 0.02
            else:
                pity_counter = 0
                pity = round (0.02, 2)
        elif roll <= number_of_rolls:
            rarity = random.choices(categories, probabilities)[0]
            operator = select_operator(rarity)
            data = [roll, rarity, operator]
            # write data in csv for further work with results
            csv_write_data(data)
            if rarity == 5:
                change = True
            if rarity != 6 and pity_counter < 50:
                pity_counter += 1
                if pity_counter == 50:
                    pity += 0.02
            elif rarity != 6 and pity_counter > 50:
                pity += 1
                pity = round(pity, 2)
            elif rarity == 6:
                change = True
                pity = 0.02
                pity_counter = 0
                # In case we want to predict real situation we set the 'stop' condition here
                # print('The desired outcome was achieved, rational player stops rolling.')
                if operator == 'Mlynar':
                    stop = True
                    rows_cost = [roll, cost, 1]
                    print('Desired outcome achieved, simulation finished. Total number of rolls was '+str(number_of_rolls)
                  + ' and total cost was '+ str(cost) + '.')
                    csv_write_cost(rows_cost)
        elif roll >= number_of_rolls:
            cost -= 600
            stop = True
            rows_cost = [roll, cost, 0]
            csv_write_cost(rows_cost)
            print('simulation finished, total number of rolls was '+str(number_of_rolls)
                  + ' and total cost was '+ str(cost) + '.')


# Run simulation 'n' number of times
# For analysis only set 'n' to '0'
n = 0
for _ in range(n):
    simulation()
    print('Simulation finished ' + str(n) + ' time(s).')


# Visualization of the outputs of simulation
df = pd.read_csv('simulation.csv')
print(df.describe())
# Histogram
plt.hist(df['Rarity'], bins=4)
plt.title('Histogram of rarity distribution \n')
plt.xlabel('Rarity')
plt.ylabel('Number of rolls')
plt.show()
# Boxplot
df.boxplot('Roll number', by='Rarity')
plt.title('\n')
plt.xlabel('Rarity')
plt.ylabel('Roll Number')
plt.show()

# Data about results, cost prediction
df = pd.read_csv('cost.csv')
print(df.describe())
# Histogram
plt.hist(df['Roll number'], bins=1)
plt.title('Histogram Result  \n')
plt.show()
# Boxplot
