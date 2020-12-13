# PCEX Model
# This scritp developps the PCEX Model 

import numpy as np
import pandas as pd
import random


def pcex(theta=0.2,G=20, alpha10=0.725, alpha2=0.4, Rbar= 0.025, T_shock = 30,
                theta_modified = 0.2, G_modified = 20, alpha10_modified = 0.725,
                alpha2_modified = 0.4, Rbar_modified = 0.025): #atencion la Rbar en el libro es 0.025
    """
        This function permit us to simulate the PCEX model with any shocks at T_shock period.
        The arguments needed are the following:
        
        theta   : tax rate
        G       : Government expenditure
        alpha10 : Propensity to consumpe from disposable income
        alpha2  : Marginal propensity to consume from Assets (cash money)
        Rbar    : Interest Rate fixed by the central bank 
        
        T_shock : The time in which the shock happens.
        
        theta_modified   : The new theta if there is a shock in theta
        G_modified       : The new G if there is a shock in G.
        alpha10_modified : The new alpha10 if there is a shock in alpha10.
        alpha2_modified  : The new alpha2 is there is a shock in alpha2
        Rbar_modified    : The new Rbar if there is a shock in Rbar.
            
        
    """
    

    # number of periods in the simulation.
    # In order to visualize the convergence to the steady state, we are going to adapt 
    # the T period of the graphic plotted 
    
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

    Hd=np.zeros(T) #Demand for cash
    Hh=np.zeros(T) #Cash held by households
    Bs=np.zeros(T) #Bills

    V = np.zeros(T) #Housegold wealth
    Ve = np.zeros(T) #Expected household wealth
    Bcb =np.zeros(T) #Government bills held by the Central Bank
    Bd =np.zeros(T)  #Demand for government bills
    dBs =np.zeros(T)  #Government bills supplied by the government
    Bh= np.zeros(T) #Government bills held by households
    dV =np.zeros(T) #change in wealth
    
    ##-----------------------------------------------------------------
    ## PCEX

    # Here we stablish the exogenous variables as vectors: 
    G = G*np.ones(T)    # Government expenditure
    R = Rbar*np.ones(T)   #Interest rate in government bills
    alpha1 = alpha10-5*R #Marginal propensity to consume from disposable Income 
    
    lambda0=  0.635       #Parameter in asset demand function
    lambda1=  5.0         #Parameter in asset demand function
    lambda2=   0.01       #Parameter in asset demand function



    # Modified parameters to simulate fiscal policy and monetary policy: 
    G_modified = (G_modified)*np.ones(T)
    R_modified = Rbar_modified*np.ones(T)
    alpha1_modified = alpha10_modified - 5* R_modified #iN THIS MODEL THE PROPENSITY TO consume of disposable income is an endogneous variable.
    
    
    

    # Defining the initial value of the expected disposable income at time 1. This equation follows 
    #equation 4.16 of the Godley and Lavoie's book:
    YDe[1] = (1-theta)*G[0]
    
    #In this model we  introduce a random factor that affects how households shape their expectations.
    random.seed(6)
    
    
    for i in range(1,T):
        #this part of the loop simulates the economy before the shock:      
        if i < T_shock:
            
            #This equation allows the loop to perform the evolution to the steady state:    
            YI = G[i] + alpha2*V[i-1]

            while abs(Y[i]-YI) > 0.00001:
                
                # In this recursion we find the evolution of Y, tax and consumption, as well as Bs, Hh, and Bcb.
                Y[i] = YI
                tax[i] = theta*(Y[i]+R[i-1]*Bh[i-1]) 
                C[i] = alpha1[i]*YDe[i] + alpha2*V[i-1]   
                YI   = C[i] + G[i]                     
                Bs[i]=G[i]-tax[i]+R[i-1]*(1+Bd[i-1]) 
                Hh[i] = V[i]-Bd[i]
                Bcb[i]= Bs[i]-Bd[i]
            # Actual Disposable Income
            YD[i]  = Y[i] - tax[i] + R[-1] *Bh[i-1]             
            if i < T-1:
                YDe[i+1] = YD[i] * (1+random.gauss(0,0.035)) 


            # flows of financial assets
            dHs[i] = Bcb[i]-Bcb[i-1]                                 
            Ve[i] = V[i-1]+ (YDe[i]-C[i])
            Bd[i] = Ve[i]*lambda0+Ve[i]*lambda1*R[i] - lambda2*YDe[i] # 
            Hd[i] = Ve[i]-Bd[i]
            dHd[i] = Hd[i]-Hd[i-1]
            dV[i]=YD[i]-C[i]

            dBs[i]=(G[i]+R[i-1]*Bs[i-1]) - (tax[i]+ R[i-1]*Bcb[i-1]) #
            Bh[i]=Bd[i];
            
            # update stock of financial wealth
            H[i] = V[i]-Bh[i]
            V[i]= V[i-1] + (YD[i]-C[i]);


        # This part of the loop simulates the economy after the shock
        else:
            YI = G_modified[i] + alpha2_modified*V[i-1]
            while abs(Y[i]-YI) > 0.00001:
                Y[i] = YI
                tax[i] = theta_modified*(Y[i]+R_modified[i-1]*Bh[i-1]) 
                C[i] = alpha1_modified[i]*YDe[i] + alpha2_modified*V[i-1]
                YI   = C[i] + G_modified[i]                     
                Bs[i]=G_modified[i]-tax[i]+R_modified[i-1]*(1+Bd[i-1])
                Hh[i] = V[i]-Bd[i]
                Bcb[i]= Bs[i]-Bd[i]

            YD[i]  = Y[i] - tax[i]+ R_modified[-1] *Bh[i-1]                                      
            if i < T-1:
                YDe[i+1] = YD[i] * (1+random.gauss(0,0.035))  

            # flows of financial assets
            dHs[i] = Bcb[i]-Bcb[i-1]                                     
            Ve[i] = V[i-1]+ (YDe[i]-C[i])
            Bd[i] = Ve[i]*lambda0+Ve[i]*lambda1*R_modified[i] - lambda2*YDe[i] 
            Hd[i] = Ve[i]-Bd[i]
            dHd[i] = Hd[i]-Hd[i-1]
            dV[i]=YD[i]-C[i]
 
            dBs[i]=(G_modified[i]+R_modified[i-1]*Bs[i-1]) - (tax[i]+ R_modified[i-1]*Bcb[i-1]) 
            Bh[i]=Bd[i];
            
            # update stock of financial wealth
            H[i] = V[i]-Bh[i]
            V[i]= V[i-1] + (YD[i]-C[i]); 
    
    
    # We put all the information on a DATAFRAME
    years = [] 
    for i in range(T):
        y = 1980+i
        years.append(y)
        
    data = {'year': years, "Income (Y)" : Y, 'Disposable income (YD)': YD, 'Expected Disp. Inc (YDe)': YDe, 'Tax Revenue': tax,
            'Consumption': C, 'Stock': V, 'flow': dV}
    df=pd.DataFrame(data)
    
    
    
    ## Calculation of the steady level: Now, based on the exogenous variables we calculate the steady state of the economy: 
    #Steady States (without any shock)
    a3 = (1-(alpha1))/alpha2
    Cee=G/((theta/(1-theta))-Rbar*(a3*(lambda0+lambda1*Rbar)-lambda2))
    Vee=a3*Cee
    Bhee= Cee*((lambda0+lambda1*Rbar)*a3-lambda2)
    Yee=G+Cee
    Tee=G+Rbar*Bhee
    
    #Steady States (whith shock)
    a3_shock = (1-(alpha1_modified))/alpha2_modified
    Cee_S=G_modified/((theta_modified/(1-theta_modified))-Rbar_modified*(a3_shock*(lambda0+lambda1*Rbar_modified)-lambda2))
    Vee_S=a3_shock*Cee_S
    Bhee_s= Cee*((lambda0+lambda1*Rbar_modified)*a3_shock-lambda2)
    Yee_S=G_modified+Cee_S
    Tee_S=G_modified+R_modified*Bhee_s
    
    noshock= [Yee[1], Tee[1], Cee[1], Vee[1]]
    shock= [Yee_S[1], Tee_S[1], Cee_S[1], Vee_S[1]]
    impact = [Yee_S[1]-Yee[1], Tee_S[1]-Tee[1], Cee_S[1]-Cee[1], Vee_S[1]-Vee[1]]
    impact_per = [(shock[0]/noshock[0]-1)*100, (shock[1]/noshock[1]-1)*100, (shock[2]/noshock[2]-1)*100, (shock[3]/noshock[3]-1)*100]
    
    
    
    #We creeate a dataframe to put the values of the steady states obtained: 
    steady_states = {'Steady State' : noshock, 'Steady State with shock': shock,'Impact': impact, 'Impact (%)':impact_per }
    df_steady_level=pd.DataFrame(steady_states)
    
    df_steady_level.rename(index={0:'Income (Y)',1:'Tax Revenue',2:'Consumption',3:'Stock'}, inplace=True)
     
    return df, df_steady_level



