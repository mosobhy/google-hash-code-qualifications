import random


def writeOutput(orders, outputs):
    
    with open('output', "w") as file:
        file.write(str(orders))
        file.write("\n")
        
        # iterate and print the output list of dicts
        for output in outputs:
            file.write(str(len(output)))
            file.write(' ')
            for id, pizza in output.items():
                file.write(str(id))
                file.write(' ')
            file.write('\n')

def maximizeForTwoPersons(pizzas):
    """
    The format of orders: 
    {
        team_type: #of_orders
    }
    The format of pizzas:
    {
        id: [#of_ingrediants, [ componente1, compenent2 ]]
    }
    """
    pizzas_entry_list = list(pizzas.items())
    # generate two random pizzas one first and then the other one should be unique
    team_2_pizzas = {}
    pizza_1 = random.choice(pizzas_entry_list)
    team_2_pizzas[pizza_1[0]] = pizza_1[1]
    # print(team_2_pizzas)

    # push the pizza ingrediatns to a stack to pop up from it
    # to keep iterating while checking
    ingrediants_stack = [ item for item in pizza_1[1][1] ]
    
    while len(ingrediants_stack) >= 0:
        # get a random pizza from the pizzas object
        pizza_2 = random.choice(pizzas_entry_list)

        # check if the pizza_id == pizza_id: skip this one
        if pizza_1[0] == pizza_2[0]:
            continue

        # iterate over the ingrediants of this pizza and pop the common items
        else:
            for item in pizza_2[1][1]:
                if item in ingrediants_stack:
                    ingrediants_stack.remove(item)
            
            if len(ingrediants_stack) == 0: # this means the two pizzas are identical
                continue

            team_2_pizzas[pizza_2[0]] = pizza_2[1]
            if len(team_2_pizzas) == 2:
                break

    return team_2_pizzas

                
def maximizeFor(team, pizzas):
    '''
    This function is going to maximize for the 4-team, 3-team based on
    the generated pizzas from maximizeForTwoPersons() function
    '''
        # for team_3
    pizzas_entry_list = list(pizzas.items())
    if team == 'team_3':

        team_3_pizzas = {}
        two_person_pizzas = maximizeForTwoPersons(pizzas)
        for id, pizza in two_person_pizzas.items():
            team_3_pizzas[id] = pizza

        # create the stack of ingreidants to pop up while iterating over the remaining pizza
        ingrediants_stack = []
        for id, pizza in two_person_pizzas.items():
            for item in pizza[1]:
                ingrediants_stack.append(item)

        while len(ingrediants_stack) >= 0:
            # the other remaining one pizza
            pizza_3 = random.choice(pizzas_entry_list)

            if pizza_3[0] in team_3_pizzas:
                continue
            
            else:
                # now iterate and remove the similarties
                for item in pizza_3[1][1]:
                    if item in ingrediants_stack:
                        ingrediants_stack.remove(item)
                
                if len(ingrediants_stack) == 0:
                    continue

                # append this unique pizza to the team_3 pizzas
                team_3_pizzas[pizza_3[0]] = pizza_3[1]
                if len(team_3_pizzas) == 3:
                    break

        return team_3_pizzas
        
    elif team == 'team_4':
        # unique pizzas for 4 persons are twice as unique pizzas for 2 persons
        return { **maximizeForTwoPersons(pizzas), **maximizeForTwoPersons(pizzas) }         

def getMaxIngrediants(M, teams, pizzas):
    '''
    Retunr the ouput in a file
    '''
    temp_pizza = M
    order_count = 0
    outputs = []
    while temp_pizza > 1:
        if temp_pizza % 2 != 0 or (teams[0] == 0 and teams[2] == 0 ) and teams[1] > 0:
            order_count += 1
            temp_pizza -= 3
            output = maximizeFor('team_3', pizzas)
            outputs.append(output)         # write the output to a file
        
        if temp_pizza % 2 == 0 or teams[1] == 0:
            if teams[2] > 0 and temp_pizza >= 4:
                temp_pizza -=4
                order_count += 1
                output = maximizeFor('team_4', pizzas)
                outputs.append(output)     # write the output to a file
            
            if teams[1] > 0 and temp_pizza >= 2:
                temp_pizza -= 2
                order_count += 1
                output = maximizeForTwoPersons(pizzas)
                outputs.append(output)     # write the output to a file

        writeOutput(order_count, outputs)
    

if __name__ == '__main__':

    with open('b_little_bit_of_everything.in', "r") as file:

        # num of avai pizzas
        file_content = file.read().split('\n')
        input_desc = file_content[0].split()
        
        M = input_desc[0]
        teams = []
        for i in range(1, len(input_desc)):
            teams.append(int(input_desc[i]))

        # getting the pizzas details
        pizzas = {}
        for i in range(1, len(file_content)-1):
            ingrediants = []
            slot = file_content[i].split()
            ingrediants.append(slot[0])
            
            ingrediants.append(list(slot[1:]))
            # print(ingrediants)
            pizzas[i-1] = ingrediants

        # pass the input to the funciton
        getMaxIngrediants(int(M), teams, pizzas)
        