# Display

import matplotlib.pyplot as plt


def display(df, variables):
    """ 
        Function which permit us to show the variables evolutation along time.
        
        Arguments.          
               df: it is a dataframe containing the model information of all the variables.
        variables: it is a list that contains the name of the variables that the user will select to display.
        
    """
    plt.figure(figsize=(8.5,5.5))
    for i in variables:
        ax = plt.gca()
        df.plot(kind = 'line', x='year', y=i, ax=ax)
        plt.title(" Figure 1: Varibles' Evolution ", fontsize= 12)
    return plt.show()


def display_with_without_shock(df_without_shock,df_with_shock, variables, T_shock):
    """ 
        Function which permit us to visualize the variables evolutation along time
        with shocks and without shocks at the same time.
        
        Arguments.
               df_without_shock : dataframe with the model's information without shock
               df_with_shock    : dataframe with the model's information with shock
               variables        : it is a list that contains the name of the variables that the user will select to display.
               T_shock          : The time when the shock will take place.
               
     """
    Year_shock = T_shock + 1980
    
    plt.figure(figsize=(8.5,5.5))
    for i in variables:
        ax = plt.gca()
        df_without_shock.plot(kind = 'line', x='year', y=i, ax=ax, style = 'k--', legend=False)
        df_with_shock.plot(kind = 'line', x = 'year', y = i, ax=ax)
    plt.axvline(x=Year_shock-1, linewidth=1, color='grey', linestyle='dashed' )
    plt.title(" Figure 1: Varibles' Evolution ", fontsize= 12)

    
    return plt.show()

