import random
networksize = 20
trials = 10000 
infection_probability = .1
it_removal_num = 5
total_days = 0
total_all_computers_infected = 0
total_num_computers_infected = 0
def print_2d_array(arr):
    """method for printing the 2d array"""
    for row in arr:
        for element in row:
            print(element, end='\t') 
        print()
        
def numInfected(arr):
    second_row = arr[1]
    infected_count = sum(1 for element in second_row if element != 0)
    return infected_count
def check_all_infected(arr):
    second_row = arr[1]
    return int(all(element != 0 for element in second_row))

def check_clean(network):
    top_row = network[0]
    if all(element == 0 for element in top_row):
        return 1
    else:
        return 0
def infection_rate(probability):
    random_value = random.random()
    if random_value <= probability:
        return 1
    else:
        return 0

def simulation_start(NUMOFCOMPUTERS,infectionprob,removal_num):

    #initializing the 2d array to simulate the computer network
    #the first row is whether the computer is infected or not and the second row is
    # how many times it has been infected
    networkComputers = [[0 for _ in range(NUMOFCOMPUTERS)] for _ in range(2)]

    #randomly pick a computer that will start with the virus
    initalComputer = random.randint(1,NUMOFCOMPUTERS)
    networkComputers[0][initalComputer-1] = 1
    networkComputers[1][initalComputer-1] += 1
    print("Initializing network")
    print_2d_array(networkComputers)
    return simulation(networkComputers, infectionprob,removal_num)


def simulation(network, infection, removal):
    day = -1
    while check_clean(network) == 0:
        day += 1
        print("Day: ", day)
        print("Infection Spreading")
        #Infection spread simulation
        for x in range(len(network[0])):
            if network[0][x] != 1:
                network[0][x] = infection_rate(infection)
                if network[0][x] == 1:
                    network[1][x] += 1
        print_2d_array(network)
        print("IT Cleaning")
        #IT virus removal simulation
        top_row = network[0]
        infected_indices = [index for index, value in enumerate(top_row) if value == 1]
        computers_to_be_cleaned = random.sample(infected_indices, min(removal, len(infected_indices)))
        for index in computers_to_be_cleaned:
            top_row[index] = 0
        print_2d_array(network)
    data = day, check_all_infected(network), numInfected(network)
    return data

networksize = int(input("Enter the network size: "))
trials = int(input("Enter the number of trials: "))
infection_probability = float(input("Enter the infection probability: "))
it_removal_num = int(input("Enter the number of virus IT removes in a day: "))

for _ in range(trials):
    print("Trial: ", _+1)
    trial_data = simulation_start(networksize,infection_probability,it_removal_num)
    total_days += trial_data[0]
    total_all_computers_infected += trial_data[1]
    total_num_computers_infected += trial_data[2]

print("Expected days to rid the network of the virus: ", total_days/trials)
print("Probability each computer got infected once: ", total_all_computers_infected/trials)
print("Expected number of computers that get infected: ", total_num_computers_infected/trials)