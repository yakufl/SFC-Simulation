# Explanation

def dic_steady_states(variables, steady_data):
    """ function which returns a dictionary with the exact steady states of the variables 
        as well as the impact of any shock on the variables.
        
        Arguments needed. 
        variables   : a list containing the variables the user decided to plot
        steady_data : a dataframe containg all the information about the steady states
    """
    # we create the dictionary to stock the steady amounts of the variable the user decided to plot
    dic = {}
    
    for var in variables:
        # we stock the information for each dictionary key in a list 
        lista =[]
        
        # As the variable flow have an stedy state = 0 we pass 
        if var == 'flow':
            pass
        else:
            for i in steady_data.columns:
                objeto = steady_data.loc[var,i]
                lista.append(objeto)
            dic[var] = lista

    return dic


def explain(dictionary={}, Shock = False, T_shock=0):
    
    """ This function is going to print the information about the steady states of the 
        variables that the user decided to plot as well as the impact of any shock 
        (if a shock exists) on the steady states.
    """
    
    message = "\n " + "\n "
    year_shock = T_shock + 1980
    # we take the variables the user decided to plot
    variables_plotted = list(dictionary.keys())
    #steady_information
    
    if Shock == False:
        for variable in variables_plotted:
            # As the variable flow have an stedy state = 0 we pass 
            if variable == 'flow':
                pass
            else:
                steady_information = list(dictionary[variable])
                message = message + "The " + str(variable) + " variable you decided to plot attains a steady state of " +  str(round(steady_information[0],2)) + "\n " + "\n "
            
    else:
        for variable in variables_plotted:
            if variable == 'flow':
                pass
            else:
                steady_information = list(dictionary[variable])
                message = message + "Following the shock that takes place in year " + str(year_shock-1)+ " the " + str(variable) + " attains a steady state of  " +  str(round(steady_information[1],2)) + "\n " + " Therefore there is an impact of " + str(round(steady_information[2],2)) + " with repect to the steady state without shock of " +  str(round(steady_information[0],2)) + "\n " + "That implies an impact of " + str(round(steady_information[3],2)) + "%" +"\n "+"\n " 
    return message
                                                                        
    