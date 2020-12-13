# SIMEX MODEL
# This scritp developps the SIMEX Model 

import numpy as np
import pandas as pd

def simex(theta=0.2,G=20, alpha1=0.6, alpha2=0.4, T_shock = 30,
                theta_modified = 0.2, G_modified = 20, alpha1_modified = 0.725,
                alpha2_modified = 0.4):
    """
        This function permits us to simulate the SIMEX model with any shocks at T_shock time.
        The arguments needed are the following:
        
        theta   : tax rate
        G       : Government expenditure
        alpha1  : Maginal propensity to consume from Disposable Income 
        alpha2  : Marginal propensity to consume from Assets (cash money)
        T_shock : The time in which the shock happens.
        
        Each of the above variables has the modified version, that allows
        us to define the shocks: 
        theta_modified,  G_shock, alpha1_modified, alpha2_modified, Rbar_modified.     
        
    """

    # number of periods in the simulation.
    # In order to visualize the convergence to the steady state, we are going to adjust 
    # the T period of the graphic plotted acording to the T_shock selected.
    
    if T_shock> 30:
        T = 2 * T_shock
    else:
        T = T_shock + 30 



    # To beging  with the simulation we create the endogenous variables:
    
    C = np.zeros(T)     #Consumption: spending of the households
    H = np.zeros(T)     # The stock variable: in SIMEX model this is cash held by households.
    Y = np.zeros(T)     # Gross Output
    YD = np.zeros(T)    # Disposable income (household)
    YDe = np.zeros(T)   # Expected Disposable Income: this is a feature of the expectations of households
    tax = np.zeros(T)   # Tax revenue, colected by the government 
    dHs = np.zeros(T)   # The flow of cash
    dHd = np.zeros(T)   # The flow of cash desided by households
    dHh = np.zeros(T)   # Change of cash held by household
    dH  = np.zeros(T)   # Actual change of the cash


    # Here we stablish the government expenditure: 
    G = G*np.ones(T)    
    
    # Government expenditure modified (to simulate fiscal shock policy)
    G_modified = (G_modified)*np.ones(T)

    # Defining the initial value of the expected disposable income at time 1. This equation follows 
    #equation 3.5 of the Godley and Lavoie's book:
    YDe[1] = (1-theta)*G[0]

    ## Initialize the loop

    for i in range(1,T):
        
        #this part of the loop simulates the economy before the shock:
        if i < T_shock: 
            
            #This equation allows the loop to perform the evolution to the steady state:    
            YI = G[i] + alpha2*H[i-1]
            # In this recursion we find the evolution of Y, tax and consumption 
            while abs(Y[i]-YI) > 0.00001:
                Y[i] = YI
                tax[i] = theta*Y[i] #Equation 3.6, it describes the evolution of revenues from taxes
                C[i] = alpha1*YDe[i] + alpha2*H[i-1]   # it describes tne evolution cof consumption
                YI   = C[i] + G[i]                     # it describes the evolution of the total income or output in this economy

            # Actual Disposable Income based on the equatin 3.5:
            YD[i]  = Y[i] - tax[i]                                    
            if i < T-1:

                YDe[i+1] = YD[i]  # Equation 3.20, it defines the evolution of the expected disposable income
                #as the previous disposable income observed by households.


            # Now, we define the flows of the assets
            dHs[i] = G[i] - tax[i]           # It describes fiscal deficit in thois economy
            dHh[i] = YD[i] - C[i];           # It describes the evolution of cash that household hold.
            dH[i] = dHh[i]          ;       
            dHd[i]= YDe[i] - C[i]            # The evolution of desired holdings: equation  3.18. 

            # The final stock of cash:
            H[i] = H[i-1] + dH[i];
            

        # This part of the loop simulates the economy after the shock
        else:
            YI = G_modified[i] + alpha2*H[i-1]
            while abs(Y[i]-YI) > 0.00001:
                Y[i] = YI
                tax[i] = theta_modified*Y[i]
                C[i] = alpha1_modified*YDe[i] + alpha2_modified*H[i-1]   
                YI   = C[i] + G_modified[i]                    

           
            YD[i]  = Y[i] - tax[i]                                   
            if i < T-1:

                YDe[i+1] = YD[i]  
            
            dHs[i] = G_modified[i] - tax[i]                                     
            dHh[i] = YD[i] - C[i];                                  
            dH[i] = dHh[i]; 
            dHd[i]= YDe[i] - C[i]                                     

            H[i] = H[i-1] + dH[i];
            
    
    # We put all the information on a DATAFRAME
    years = [] 
    for i in range(T):
        y = 1980+i
        years.append(y)
        
    data = {'year': years, "Income (Y)" : Y, 'Disposable income (YD)': YD, 'Expected Disp. Inc (YDe)': YDe, 'Tax Revenue': tax,
            'Consumption': C, 'Stock': H, 'flow': dH}
    df=pd.DataFrame(data)
    
    
    #  Calculation of the steady level: Now, based on the exogenous variables we calculate the steady state of the economy: 
    #  Steady States (without any shock)
    a3 = (1-(alpha1))/alpha2
    Yee=G/theta
    Cee=G*(1-theta)/theta
    Hee= a3*G*(1-theta)/theta
    
    # Steady States (with shock)
    a3_S = (1-(alpha1_modified))/alpha2_modified
    Yee_S=G_modified/theta_modified
    Cee_S=G_modified*(1-theta)/theta_modified
    Hee_S= a3_S*G_modified*(1-theta_modified)/theta_modified
    
    noshock= [Yee[1], G[1], Cee[1], Hee[1]]
    shock= [Yee_S[1], G_modified[1], Cee_S[1], Hee_S[1]]
    impact = [Yee_S[1]-Yee[1], G_modified[1]-G[1], Cee_S[1]-Cee[1], Hee_S[1]-Hee[1]]
    impact_per = [(shock[0]/noshock[0]-1)*100, (shock[1]/noshock[1]-1)*100, (shock[2]/noshock[2]-1)*100, (shock[3]/noshock[3]-1)*100]
    
    # We creeate a dataframe to put the values of the steady states obtained: 
    steady_states = {'Steady State' : noshock, 'Steady State with shock': shock,
                     'Impact': impact, 'Impact (%)':impact_per }
    df_steady_level=pd.DataFrame(steady_states)
    df_steady_level.rename(index={0:'Income (Y)',1:'Tax Revenue',2:'Consumption',3:'Stock'}, inplace=True)
     
    
    return df, df_steady_level
    
        

