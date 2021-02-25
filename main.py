import random

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
    # write the total number of orders to the file.

    # the meaning of team_2 is that they need 2 pizzas
        # maxmize for 2 pizzas ( find the most unique pizzas' index )
    # the meaning of team_3 is that they need 3 pizzas
        # maxmize for 3 pizzas ( find the most unique pizzas' index )
    # the meaning of team_4 is that they need 4 pizzas
        # maxmize for 4 pizzas ( find the most unique pizzas' index )
    
    # print(team, pizzas)
    # pizza_index_of_less_common_ingreidants = [[2, set()],]   # 2 is random number
    # pizzas_that_are_unique = []
    # if team == 'team_2':
    #     for i in range(1, len(pizzas)):
    #         common_pizza_ingrediants = set(pizzas[i-1][1]).intersection(set(pizzas[i][1]))        # this is going to dereference of the pizzas' ingrediants
    #         unique_pizza_ingrediants = set(pizzas[i-1][1]).union(set(pizzas[i][1]))
    #         print('common pizza ingrediants', common_pizza_ingrediants)
    #         print(pizza_index_of_less_common_ingreidants)
    #         if len(common_pizza_ingrediants) < pizza_index_of_less_common_ingreidants[i-1][i]:
    #             pizza_index_of_less_common_ingreidants.append([i, common_pizza_ingrediants])
    #             # append the index of the good two pizza to deliver
    #             if i - 1 not in pizzas_that_are_unique:
    #                 pizzas_that_are_unique.append(i-1)
    #             pizzas_that_are_unique.append(i)

    # print(pizzas_that_are_unique)
    
    # if team == 'team_3':
    #     pizza_delivery_for_team3_index = []
    #     pizza_ingredants = set()
    #     for index, ingrediants in pizzas.items():
    #         for ing in ingrediants[1]:
    #             pizza_ingredants.add(ing)
    pizzas_entry_list = list(pizzas.items())
    # generate two random pizzas one first and then the other one should be unique
    team_2_pizzas = {}
    pizza_1 = random.choice(pizzas_entry_list)
    team_2_pizzas[pizza_1[0]] = pizza_1[1]
    # print(team_2_pizzas)

    # push the pizza ingrediatns to a stack to pop up from it
    # to keep iterating while checking
    ingrediants_stack = [item for item in pizza_1[1][1] if len(pizza_1[1][1]) >= 3]
    print(ingrediants_stack)
    # print(ingrediants_stack)
    
    while len(ingrediants_stack) >= 0:
        # get a random pizza from the pizzas object
        pizza_2 = random.choice(pizzas_entry_list)
        print(pizza_2)
        print(11111111)
        print(ingrediants_stack)

        # check if the pizza_id == pizza_id: skip this one
        if pizza_1[0] == pizza_2[0]:
            print(22222222)
            continue

        # iterate over the ingrediants of this pizza and pop the common items
        # print(pizza_2)
        for item in pizza_2[1][1]:
            if item in ingrediants_stack:
                ingrediants_stack.remove(item)
                print(3333333)
        
        if len(ingrediants_stack) == 0 or len(ingrediants_stack) == 1: # this means the two pizzas are identical
            # ['ingre1', 'ingre2', 'ingre3']
            # ['ingr2', 'ingre3']
            print(44444444)
            continue

        team_2_pizzas[pizza_2[0]] = pizza_2[1]
        print(5555555)
        if len(team_2_pizzas) == 2:
            print(666666)
            break

    return team_2_pizzas

                
# def maximizeFor(team, pizzas):
    '''
    This function is going to maximize for the 4-team, 3-team based on
    the generated pizzas from maximizeForTwoPersons() function
    '''
        # for team_3
    pizzas_entry_list = list(pizzas.items())
    if team == 'team_3':

        team_3_pizzas = {}
        two_person_pizzas = maximizeForTwoPersons(pizzas)
        print(two_person_pizzas)

        # create the stack of ingreidants to pop up while iterating over the remaining pizza
        ingrediants_stack = []

        pizza_1 = random.choice(pizzas_entry_list)
        print(pizza_1)
        team_3_pizzas[pizza_1[0]] = pizza_1[1]

        # generating uniqe pizza ingrediants for 3 pizzas is the same
        # as for 2 pizzas + 1 more unique pizza
        # create the stack to pop up the similarites

    elif team == 'team_4':
        print('Hello World')
                
                

def getMaxIngrediants(M, teams, pizzas):
    '''
    Retunr the ouput in a file
    '''
    '''
    SAMPLE INPUT:
    5 1 2 1 
    3 onion pepper olive
    3 mushroom tomato basil
    3 chicken mushroom pepper
    3 tomato mushroom basil
    2 chicken basil

    SAMPLE OUTPUT:
    2                   # number of orders delived ( one per team)                              
    2   1   4           # order 1 consists of two pizzas[1, 4] for 2-person team
    3   0   2   3       # order 2 consists of three pizzas[0, 2, 3] for 3-person team


    7 2 0 1
    8 0 2 0
    2 0 1 0 || 2 0 0 1
    21 1 0 4
    '''
    temp_pizza = M
    order_count = 0
    # orders = {
    #     'team_2': 0,
    #     'team_3': 0,
    #     'team_4': 0
    # }
    while temp_pizza > 1:
        if temp_pizza % 2 != 0 or (teams[0] == 0 and teams[2] == 0 ) and teams[1] > 0:
            # output = maximizeFor('team_3', pizzas)   # this function should wirte the pizzas to file
            order_count += 1
            temp_pizza -= 3
        
        if temp_pizza % 2 == 0 or teams[1] == 0:
            if teams[2] > 0 and temp_pizza >= 4:
                temp_pizza -=4
                # output = maximizeFor('team_4', pizzas)
                order_count += 1
            
            if teams[1] > 0 and temp_pizza >= 2:
                temp_pizza -= 2
                output = maximizeForTwoPersons(pizzas)
                print(output)
                order_count += 1
    
    # print(orders)
    # pass the orders to the maximize function
    # maximizePerOrder(orders, pizzas)

if __name__ == '__main__':

    with open('a_example', "r") as file:

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
        # print(pizzas)

        # pass the input to the funciton
        getMaxIngrediants(int(M), teams, pizzas)
        