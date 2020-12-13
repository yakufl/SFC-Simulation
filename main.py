# main
# This script contains the interface of the application 

import tkinter as tk
from tkinter import *
from SIMEX import *
from PCEX import *
from display import *
from Explanation import *


# We fixe a kind of sytle for the interface 
LARGE_FONT= ("Verdana", 12) 
TITLE_FONT= ("Verdana", 30)
SUBTITLE_FONT= ("Verdana", 12, "bold")
SUBPAGE_FONT=("Verdana", 18, "bold")


# This class contains the principales functions needed to implement the web environment 
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, simex_model, simex_baseline, simex_shock, pcex_model, pcex_baseline, pcex_shock, about, GoodBye):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)
        
    # This function will permit to open the windows entered as argument 
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    # This function will permit to open only the Goodbye page 
    def close(self):        
        frame = self.frames[GoodBye]
        frame.tkraise()
        
 
# We create the HomePage windows     
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label2 = tk.Label(self, text=" Welcome to the Economic Policy Simulator", font=TITLE_FONT, foreground= "blue")
        label2.pack(pady=10,padx=10)

        S = Scrollbar(self)
        T = Text(self, height=4, width=60)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
         
        #Adding the explanation of the app:
        
        T.insert(END,'\n    Simulating the Stock-Flow Consistent Approach: \n')

        quote = """
        On this App, you will be able to visualize the 
        evolution of macroeconomic variables and the final 
        impact of some exogenous shocks on a stylized 
        economy. The objective of this simulation is to 
        show how the Stock-Flow consistent (SCF) models work. 
        In order to do that, we replicate two SFC models 
        following Godley & Lavoie's book. 
        
        The model SIMEX corresponds to chapter 3 of the 
        book and the model PCEX corresponds to chapter 4.
        
            Let's try some shocks and evaluate how 
                    these models behave!
        

        """
        T.insert(END, quote)
        
        #About
        button3 = tk.Button(self, text= "About", background= "black", command=lambda:controller.show_frame(about) )
        button3.pack()


        label = tk.Label(self, text=" To start please choose a model:", font=LARGE_FONT, foreground= "black")

        label.pack(pady=10,padx=10)
              
        

        button = tk.Button(self, text="Model SIMEX",command=lambda: controller.show_frame(simex_model))
        button.pack()

        button2 = tk.Button(self, text="Model PCEX", command=lambda: controller.show_frame(pcex_model))
        button2.pack()
        
        #close
        button_close = tk.Button(self, text = 'Quit the app', command=lambda: controller.close())
        button_close.pack()
        

# We create the about windows             
class about(tk.Frame):
    
      
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        texto = """ This is an application created by Yaku Fernandez and Frank Aquinga for the Programming Course in HEC-Lausanne.
        
        If you are interested in the  SFC approach you can read this book: 
            Monetary Economics - An Integrated Approach to Credit, Money, Income, Production and Wealth (Wynne Godley and Marc Lavoie).
            
            To more information please contact to yakufl@icloud.com or Frank.AlquingaMelo@unil.ch.

        """
        label = tk.Label(self, text=texto, font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.pack()
              
               
        
    
# We create the simex_model windows             
class simex_model(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Simulating a Model SIMEX",font=SUBPAGE_FONT, foreground="blue")
        label2 = tk.Label(self, text="You have 2 options:", font=LARGE_FONT)
        label.grid(row = 0, column = 1 )
        label2.grid(row=1,column=0)        
        label = tk.Label(self, text="See the Baseline Scenario", font=LARGE_FONT)
        label.grid(row = 2, column = 0)
        button1 = tk.Button(self, text="Baseline",command=lambda: controller.show_frame(simex_baseline))
        button1.grid(row = 2, column = 1)
        
        label = tk.Label(self, text="See the Shock Scenario", font=LARGE_FONT)
        label.grid(row = 3, column = 0)
        button1 = tk.Button(self, text="Shock",command=lambda: controller.show_frame(simex_shock))
        button1.grid(row = 3, column = 1)

        
        button2 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button2.grid(row = 10, column = 10)
        
        S = Scrollbar(self)
        T = Text(self, height=12, width=60)

        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
        T.insert(END,'\n    Simulating a model SIMEX: \n')

        quote = """
        There are  are two agents in this model : the 
        government which collect taxes and spend at some 
        level G, and households which earn wages and spend 
        in consumption (C). Households hold money (H) and 
        that money represents the unique stock in this 
        economy. 
        
        The SIMEX model has 4 exogenous variables:
            1) Government expenditure
            2) Level of taxes 
            3) Propensity to consume of disposable income 
            4) Propensity to consume of the stock. 
            
        You can simulate two scenarios: without any shock 
        (called baseline) and with shock. You can introduce 
        up to five shocks simultaneously. 
        
        In addition, you can select which endogenious 
        variables evoluation you want to plot. 
        In this model, the endogenous variables are: 
            
            - Income (Y)        - Consumption (C)
            - Tax revenue       - Stock 
        
        Let's try some shocks and evaluate how this model 
        behave!

        """
        T.insert(END, quote)
        T.grid(row = 4, column = 0)
        S.grid(row=4, column = 4)


# We create the simex_baseline windows             
class simex_baseline(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Simulating Model SIMEX ",font=SUBPAGE_FONT, foreground="blue")
        label.grid(row = 0, column = 2)

        label = tk.Label(self, text="Variables you can modify: ", font=LARGE_FONT)
        label.grid(row = 1, column = 1)
        
        var = tk.Label(self, text="      \n       Tax rate :   \n      ", font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25)
        var.grid(row = 2, column = 1)
        var = tk.Label(self, text="        \n Gouvernment expenditure: \n  ",font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
        var.grid(row = 3, column = 1)
        var = tk.Label(self, text="\n Propensity to consume \n from Disposable Income:\n" ,font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25) 
        var.grid(row = 4, column = 1)
        var = tk.Label(self, text="\n Propensity to consume \n from Assets (Cash money):\n",font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
        var.grid(row = 5, column = 1)
        
        
        # inputs given by the user 
        global tax_input1
        tax_input1 = tk.DoubleVar() 
        tax_scale1 = Scale(self, variable=tax_input1, from_=0.01, to=0.5, resolution=0.01,orient=HORIZONTAL)
        tax_scale1.grid(row = 2, column = 2)
        tax_scale1.set(0.2)
        
        global G_input1
        G_input1 = tk.DoubleVar()
        G_scale1 = Scale(self, variable=G_input1, from_=1, to=100, resolution=1,orient=HORIZONTAL)
        G_scale1.grid(row = 3, column = 2)
        G_scale1.set(20)
        
        global alpha1_input1
        alpha1_input1 = tk.DoubleVar()
        alpha1_scale1=Scale(self, variable=alpha1_input1, from_=0, to=0.99, resolution=0.01,orient=HORIZONTAL)
        alpha1_scale1.grid(row = 4, column = 2)
        alpha1_scale1.set(0.6)
        
        global alpha2_input1
        alpha2_input1 = tk.DoubleVar()
        alpha2_scale1=Scale(self, variable=alpha2_input1, from_=0.01, to=1, resolution=0.01,orient=HORIZONTAL)
        alpha2_scale1.grid(row = 5, column = 2)
        alpha2_scale1.set(0.4)
               
        
        ## Variables you can plot 
        label = tk.Label(self, text="Variables you can plot: ", font=LARGE_FONT)
        label.grid(row = 1, column = 3)
        
        global bouton1_input1
        bouton1_input1 = tk.IntVar()
        bouton1 = Checkbutton(self,variable = bouton1_input1, text="Income (Y)")
        bouton1.grid(row = 2,column = 3,sticky=W)
        
        global bouton2_input1 
        bouton2_input1 = tk.IntVar()
        bouton2 = Checkbutton(self,variable = bouton2_input1, text='Consumption')
        bouton2.grid(row = 3,column = 3,sticky=W)
        
        global bouton3_input1
        bouton3_input1 = tk.IntVar()
        bouton3 = Checkbutton(self, variable = bouton3_input1,text="Tax Revenue")
        bouton3.grid(row = 4,column = 3,sticky=W)
        
        global bouton4_input1
        bouton4_input1 = tk.IntVar()
        bouton4 = Checkbutton(self, variable = bouton4_input1,text="Stock")
        bouton4.grid(row = 5,column = 3,sticky=W)
        
        global bouton5_input1
        bouton5_input1 = tk.IntVar()
        bouton5 = Checkbutton(self, variable = bouton5_input1,text="Stock's Flow")
        bouton5.grid(row = 6,column = 3, sticky=W)
    
       
        
        # Button options for the user 
        button_plot = tk.Button(self, text="Visualize",command= self.plot)
        button_plot.grid(row = 8, column = 3)
        
        button2 = tk.Button(self, text="Change scenario",command=lambda: controller.show_frame(simex_model))
        button2.grid(row = 9, column = 5)

        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.grid(row = 10, column = 5)
        
    # This function will permit to give all the outputs     
    def plot(self):
        # It gets all the input's values entered by the user
        Tax = tax_input1.get()
        G = G_input1.get()
        alpha1 = alpha1_input1.get()
        alpha2 = alpha2_input1.get()
        
        ## variables:
        variables = []
        
        if bouton1_input1.get() == 1:
            variables.append("Income (Y)")
        if bouton2_input1.get() ==1:
            variables.append("Consumption")
        if bouton3_input1.get() ==1:
            variables.append('Tax Revenue')
        if bouton4_input1.get() ==1:
            variables.append('Stock')
        if bouton5_input1.get() ==1:
            variables.append('flow')
        
        else:
            pass
        
        df, df_steady = simex(theta=Tax,G=G, alpha1=alpha1, alpha2=alpha2,G_modified = G,
                   theta_modified = Tax, alpha1_modified = alpha1, alpha2_modified = alpha2)
        
        
        display(df,  variables = variables)
        
        dic = dic_steady_states(variables = variables, steady_data = df_steady)
        explanation = explain(dic)
        print(explanation)
        print("---------------------------------------------------------------------")
        print("--------------------------| Summarize table |------------------------")
       
        print(df_steady[['Steady State']])
        print("---------------------------------------------------------------------")
        print("")
        
        

# We create the simex_shock windows     
class simex_shock(tk.Frame):

    def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text= "Simulating Model SIMEX with shocks ",font=SUBPAGE_FONT, foreground="blue")
         label.grid(row = 0, column = 2)
         
         
         
         label = tk.Label(self, text="Baseline levels: ", font=LARGE_FONT)
         label.grid(row = 1, column = 2)
        
         var = tk.Label(self, text="\n Tax rate: \n  ", font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25)
         var.grid(row = 2, column = 1)
         var = tk.Label(self, text=" \n Gouvernment expenditure:\n ",font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 3, column = 1)
         var = tk.Label(self, text="\n Propensity to consume \n from disposable Income:\n " ,font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 4, column = 1)
         var = tk.Label(self, text="\n Propensity to consume \n from Assets (Cash money):\n ",font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 5, column = 1)

        
        
         # inputs given by the user 
         global tax_input
         tax_input = tk.DoubleVar() 
         tax_scale = Scale(self, variable=tax_input, from_=0.01, to=0.5, resolution=0.01,orient=HORIZONTAL)
         tax_scale.grid(row = 2, column = 2)
         tax_scale.set(0.2)
        
         global G_input
         G_input = tk.DoubleVar()
         G_scale = Scale(self, variable=G_input, from_=1, to=100, resolution=1,orient=HORIZONTAL)
         G_scale.grid(row = 3, column = 2)
         G_scale.set(20)
        
         global alpha1_input
         alpha1_input = tk.DoubleVar()
         alpha1_scale=Scale(self, variable=alpha1_input, from_=0, to=0.99, resolution=0.01,orient=HORIZONTAL)
         alpha1_scale.grid(row = 4, column = 2)
         alpha1_scale.set(0.6)
        
         global alpha2_input
         alpha2_input = tk.DoubleVar()
         alpha2_scale=Scale(self, variable=alpha2_input, from_=0.01, to=1, resolution=0.01,orient=HORIZONTAL)
         alpha2_scale.grid(row = 5, column = 2)
         alpha2_scale.set(0.4)
         
         
         
         # shocks given by the user       
         label = tk.Label(self, text="Shocks: ", font=LARGE_FONT)
         label.grid(row = 1, column = 3)
         label = tk.Label(self, text="Year of the shock ", font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         label.grid(row = 6, column = 1)
         
         # SHOCKS inputs given by the user 
         global tax_input_modified
         tax_input_modified = tk.DoubleVar() 
         tax_scale_modified = Scale(self, variable=tax_input_modified, from_=0.01, to=0.5, resolution=0.01,orient=HORIZONTAL)
         tax_scale_modified.grid(row = 2, column = 3)
         tax_scale_modified.set(0.2)
        
         global G_input_modified
         G_input_modified = tk.DoubleVar()
         G_scale_modified = Scale(self, variable=G_input_modified, from_=1, to=100, resolution=1,orient=HORIZONTAL)
         G_scale_modified.grid(row = 3, column = 3)
         G_scale_modified.set(20)
        
         global alpha1_input_modified
         alpha1_input_modified = tk.DoubleVar()
         alpha1_scale_modified=Scale(self, variable=alpha1_input_modified, from_=0, to=0.99, resolution=0.01,orient=HORIZONTAL)
         alpha1_scale_modified.grid(row = 4, column = 3)
         alpha1_scale_modified.set(0.6)
        
         global alpha2_input_modified
         alpha2_input_modified = tk.DoubleVar()
         alpha2_scale_modified=Scale(self, variable=alpha2_input_modified, from_=0.01, to=1, resolution=0.01,orient=HORIZONTAL)
         alpha2_scale_modified.grid(row = 5, column = 3)
         alpha2_scale_modified.set(0.4)
         
         global T_shock_input
         T_shock_input = tk.IntVar()
         T_shock_scale=Scale(self, variable=T_shock_input, from_=0, to=30, resolution=1,orient=HORIZONTAL)
         T_shock_scale.grid(row = 6, column = 3)
         T_shock_scale.set(15)
         
        
         ## Variables you can plot 
         label = tk.Label(self, text="Variables you can plot: ", font=LARGE_FONT)
         label.grid(row = 1, column = 5)
        
         global bouton1_input 
         bouton1_input = tk.IntVar()
         bouton1 = Checkbutton(self,variable = bouton1_input, text="Income (Y)")
         bouton1.grid(row = 2,column = 5,sticky=W)
         
         global bouton2_input 
         bouton2_input = tk.IntVar()
         bouton2 = Checkbutton(self,variable = bouton2_input, text="Consumption")
         bouton2.grid(row = 3,column = 5,sticky=W)
        
         global bouton3_input
         bouton3_input = tk.IntVar()
         bouton3 = Checkbutton(self, variable = bouton3_input,text="Tax Revenue")
         bouton3.grid(row = 4,column = 5,sticky=W)
         
         global bouton4_input
         bouton4_input = tk.IntVar()
         bouton4 = Checkbutton(self, variable = bouton4_input,text="Stock")
         bouton4.grid(row = 5,column = 5,sticky=W)
         
         global bouton5_input
         bouton5_input = tk.IntVar()
         bouton5 = Checkbutton(self, variable = bouton5_input,text="Stock's Flow")
         bouton5.grid(row = 6,column = 5,sticky=W)
      
                 
         # Buttons options for the user 
         button_plot = tk.Button(self, text="Visualize",command= self.plot)
         button_plot.grid(row = 8, column = 5)
    
         button2 = tk.Button(self, text="Change scenario",command=lambda: controller.show_frame(simex_model))
         button2.grid(row = 9, column = 6)

         button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
         button1.grid(row = 10, column =6 )
         
         
    # This function will permit to give all the outputs
    def plot(self):
        
        # It gets all the input's values entered by the user
        Tax = tax_input.get()
        G = G_input.get()
        alpha1 = alpha1_input.get()
        alpha2 = alpha2_input.get()
        T_shock = T_shock_input.get()
        
        Tax_modified = tax_input_modified.get()
        G_modified = G_input_modified.get()
        alpha1_modified = alpha1_input_modified.get()
        alpha2_modified = alpha2_input_modified.get()
        T_shock = T_shock_input.get()
        
        ## variables:
        variables = []
      
        if bouton1_input.get() == 1:
            variables.append("Income (Y)")
        if bouton2_input.get() ==1:
            variables.append("Consumption")
        if bouton3_input.get() ==1:
            variables.append('Tax Revenue')
        if bouton4_input.get() ==1:
            variables.append('Stock')
        if bouton5_input.get() ==1:
            variables.append('flow')
        
        else:
            pass
        
        df_without_shock, steady_without_shock = simex(theta=Tax,G=G, alpha1=alpha1, alpha2=alpha2, T_shock = T_shock, 
                   theta_modified = Tax, G_modified = G, 
                   alpha1_modified = alpha1, alpha2_modified = alpha2)
        df_shock, steady_with_shock= simex(theta=Tax,G=G, alpha1=alpha1, alpha2=alpha2, T_shock = T_shock, 
                   theta_modified = Tax_modified, G_modified = G_modified, 
                   alpha1_modified = alpha1_modified, alpha2_modified = alpha2_modified)
        
        display_with_without_shock(df_without_shock, df_shock,  variables = variables,T_shock = T_shock)
        
        dic = dic_steady_states(variables = variables, steady_data = steady_with_shock)
        explanation = explain(dic, Shock = True, T_shock = T_shock )
        print(explanation)
        print("---------------------------------------------------------------------")
        print("--------------------------| Summarize table |------------------------")
        print(steady_with_shock)
        print("---------------------------------------------------------------------")
        print("")
       

# We create the pcex_model windows             
class pcex_model(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Simulating Model PCEX",font=SUBPAGE_FONT, foreground="blue")
        label.grid(row = 0, column = 1)
          
        label2 = tk.Label(self, text="You have 2 options:", font=LARGE_FONT)
        label.grid(row = 0, column = 1)
        label2.grid(row=1,column=0)        
        label = tk.Label(self, text="See the Baseline Scenario", font=LARGE_FONT)
        label.grid(row = 2, column = 0)
        button1 = tk.Button(self, text="Baseline",command=lambda: controller.show_frame(pcex_baseline))
        button1.grid(row = 2, column = 1)
        
        label = tk.Label(self, text="See the Shock Scenario", font=LARGE_FONT)
        label.grid(row = 3, column = 0)
        button1 = tk.Button(self, text="Shock",command=lambda: controller.show_frame(pcex_shock))
        button1.grid(row = 3, column = 1)


        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.grid(row = 9, column = 5)
        
        S = Scrollbar(self)
        T = Text(self, height=12, width=60)

        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
        T.insert(END,'\n    Simulating a model PCEX: \n')

        quote = """
        The PCEX (portfolio choice with expectations) 
        model introduces a new exogenous variable the 
        interest rate and a new stock the government bills. 
        
        You can simulate two scenarios: without any shock 
        (called baseline) and with shock. You can introduce 
        up to five shocks simultaneously. 
        
        In addition, you can select which variables you want 
        to plot and visualize. In these models, the 
        endogenous variables are: 
            
            - Income (Y)        - Consumption (C)
            - Tax revenue       - Stock  
        
        Once you tap on "visualize" you shall see a figure 
        with the selected variables' evolution, and other 
        relevant information.
        
        Let's try some shocks and evaluate how this model 
        behave!

        """
        T.insert(END, quote)
        T.grid(row = 4, column = 0)
        S.grid(row=4, column = 4)

# We create the pcex_baseline windows             
class pcex_baseline(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text= "Simulating Model PCEX",font=SUBPAGE_FONT, foreground="blue")
        label.grid(row = 0, column = 2)

        label = tk.Label(self, text="Variables you can modify: ", font=LARGE_FONT)
        label.grid(row = 1, column = 1)
        
         
        label = tk.Label(self, text="Baseline Levels: ", font=LARGE_FONT)
        label.grid(row = 1, column = 2)
        
        var = tk.Label(self, text="Tax rate : ", font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25)
        var.grid(row = 2, column = 1)
        var = tk.Label(self, text=" Gouvernment expenditure:",font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25) 
        var.grid(row = 3, column = 1)
        var = tk.Label(self, text=" Propensity to consume from \n  Disposable Income " ,font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25) 
        var.grid(row = 4, column = 1)
        var = tk.Label(self, text="Marginal propensity to consume \n from Assets (cash money):",font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25) 
        var.grid(row = 5, column = 1)
        var = tk.Label(self, text="Central Bank's Interest Rate:",font=SUBTITLE_FONT, background= "#C6E5F0", height= 3, width= 25) 
        var.grid(row = 6, column = 1)
        
        
        # inputs given by the user 
        global tax_input_pcex1
        tax_input_pcex1 = tk.DoubleVar() 
        tax_scale = Scale(self, variable=tax_input_pcex1, from_=0.02, to=0.5, resolution=0.01,orient=HORIZONTAL)
        tax_scale.grid(row = 2, column = 2)
        tax_scale.set(0.2)
        
        global G_input_pcex1
        G_input_pcex1 = tk.DoubleVar()
        G_scale_pcex = Scale(self, variable=G_input_pcex1, from_=1, to=100, resolution=1,orient=HORIZONTAL)
        G_scale_pcex.grid(row = 3, column = 2)
        G_scale_pcex.set(20)
        #......................................------------------------¨!!!!!!!!!
        global alpha10_input_pcex1
        alpha10_input_pcex1 = tk.DoubleVar()
        alpha10_scale=Scale(self, variable=alpha10_input_pcex1, from_=0, to=1, resolution=0.01,orient=HORIZONTAL)
        alpha10_scale.grid(row = 4, column = 2)
        alpha10_scale.set(0.85)
        
        global alpha2_input_pcex1
        alpha2_input_pcex1 = tk.DoubleVar()
        alpha2_scale_pcex=Scale(self, variable=alpha2_input_pcex1, from_=0.01, to=1, resolution=0.01,orient=HORIZONTAL)
        alpha2_scale_pcex.grid(row = 5, column = 2)
        alpha2_scale_pcex.set(0.4)
        
        global Rbar_input_pcex1
        Rbar_input_pcex1 = tk.DoubleVar()
        Rbar_scale=Scale(self, variable=Rbar_input_pcex1, from_=0.001, to=0.1, resolution=0.001,orient=HORIZONTAL)
        Rbar_scale.grid(row = 6, column = 2)
        Rbar_scale.set(0.025)
        
               
        
        ## Variables you can plot 
        label = tk.Label(self, text="Variables you can plot: ", font=LARGE_FONT)
        label.grid(row = 1, column = 3)
        
        global bouton1_input_pcex1 
        bouton1_input_pcex1  = tk.IntVar()
        bouton1_pcex  = Checkbutton(self,variable = bouton1_input_pcex1 , text="Income (Y)")
        bouton1_pcex .grid(row = 2,column = 3,sticky=W)
        
        global bouton2_input_pcex1 
        bouton2_input_pcex1  = tk.IntVar()
        bouton2_pcex  = Checkbutton(self,variable = bouton2_input_pcex1 , text="Consumption")
        bouton2_pcex .grid(row = 3,column = 3,sticky=W)
        
        global bouton3_input_pcex1 
        bouton3_input_pcex1 = tk.IntVar()
        bouton3_pcex  = Checkbutton(self, variable = bouton3_input_pcex1,text="Tax Revenue")
        bouton3_pcex .grid(row = 4,column = 3,sticky=W)
        
        global bouton4_input_pcex1 
        bouton4_input_pcex1 = tk.IntVar()
        bouton4_pcex  = Checkbutton(self, variable = bouton4_input_pcex1,text="Stock")
        bouton4_pcex .grid(row = 5,column = 3,sticky=W)
        
        global bouton5_input_pcex1 
        bouton5_input_pcex1 = tk.IntVar()
        bouton5_pcex  = Checkbutton(self, variable = bouton5_input_pcex1,text="flow")
        bouton5_pcex .grid(row = 6,column = 3,sticky=W)
        
        # Buttons options for the user 
        button_plot = tk.Button(self, text="Visualize",command= self.plot)
        button_plot.grid(row = 8, column = 3)
        
        button2 = tk.Button(self, text="Change scenario",command=lambda: controller.show_frame(pcex_model))
        button2.grid(row = 9, column = 5)

        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.grid(row = 10, column = 5)
        
        
    # This function will permit to give all the outputs     
    def plot(self):
        
        # It gets all the input's values entered by the user
        Tax = tax_input_pcex1.get()
        G = G_input_pcex1.get()
        alpha10 = alpha10_input_pcex1.get()
        alpha2 = alpha2_input_pcex1.get()
        Rbar = Rbar_input_pcex1.get()
         
        ## variables:
        variables = []
      
        if bouton1_input_pcex1.get() == 1:
            variables.append("Income (Y)")
        if bouton2_input_pcex1.get() ==1:
            variables.append("Consumption")
        if bouton3_input_pcex1.get() ==1:
            variables.append('Tax Revenue')
        if bouton4_input_pcex1.get() ==1:
            variables.append('Stock')
        if bouton5_input_pcex1.get() ==1:
            variables.append('flow')
        
        
        df, steady = pcex(theta=Tax,G=G, alpha10=alpha10, alpha2=alpha2,Rbar= Rbar, G_modified = G,
                   theta_modified = Tax, alpha10_modified = alpha10, alpha2_modified = alpha2, Rbar_modified = Rbar)
        
        
        display(df,  variables = variables)
        
        dic = dic_steady_states(variables = variables, steady_data = steady)
        explanation = explain(dic)
        print(explanation)
        print("---------------------------------------------------------------------")
        print("--------------------------| Summarize table |------------------------")
       
        print(steady[['Steady State']])
        print("---------------------------------------------------------------------")
        print("")
       
        
        
# We create the pcex_shock windows     
class pcex_shock(tk.Frame):

    def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text= "Simulating Model PCEX with shocks ",font=SUBPAGE_FONT, foreground="blue")
         label.grid(row = 0, column = 2)
         
         label = tk.Label(self, text="Baseline Levels: ", font=LARGE_FONT)
         label.grid(row = 1, column = 2)
        
         var = tk.Label(self, text="\n Tax rate: \n ", font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25)
         var.grid(row = 2, column = 1)
         var = tk.Label(self, text=" \n Gouvernment expenditure:\n ",font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 3, column = 1)
         var = tk.Label(self, text="\n Propensity to consume from \n Disposable Income \n  " ,font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 4, column = 1)
         var = tk.Label(self, text="\n Propensity to consume \n from Assets (Wealth):\n ",font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 5, column = 1)
         var = tk.Label(self, text="\n Central Bank's Interest Rate :\n " ,font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 6, column = 1)
         var = tk.Label(self, text="\nYear of the shock \n" ,font=SUBTITLE_FONT, background= "#C6E5F0",  height= 3, width= 25) 
         var.grid(row = 7, column = 1) 
        
         # inputs given by the user 
         global tax_input_pcex2
         tax_input_pcex2 = tk.DoubleVar() 
         tax_scale = Scale(self, variable=tax_input_pcex2, from_=0.02, to=0.5, resolution=0.01,orient=HORIZONTAL)
         tax_scale.grid(row = 2, column = 2)
         tax_scale.set(0.2)
        
         global G_input_pcex2
         G_input_pcex2 = tk.DoubleVar()
         G_scale_pcex = Scale(self, variable=G_input_pcex2, from_=1, to=100, resolution=1,orient=HORIZONTAL)
         G_scale_pcex.grid(row = 3, column = 2)
         G_scale_pcex.set(20)
        
         global alpha10_input_pcex2
         alpha10_input_pcex2 = tk.DoubleVar()
         alpha10_scale_pcex2=Scale(self, variable=alpha10_input_pcex2, from_=0, to=1, resolution=0.01,orient=HORIZONTAL)
         alpha10_scale_pcex2.grid(row = 4, column = 2)
         alpha10_scale_pcex2.set(0.725)
        
         global alpha2_input_pcex2
         alpha2_input_pcex2 = tk.DoubleVar()
         alpha2_scale_pcex=Scale(self, variable=alpha2_input_pcex2, from_=0.01, to=1, resolution=0.01,orient=HORIZONTAL)
         alpha2_scale_pcex.grid(row = 5, column = 2)
         alpha2_scale_pcex.set(0.4)
         
         global Rbar_input_pcex2
         Rbar_input_pcex2 = tk.DoubleVar()
         Rbar_scale=Scale(self, variable=Rbar_input_pcex2, from_=0.001, to=0.10, resolution=0.001,orient=HORIZONTAL)
         Rbar_scale.grid(row = 6, column = 2)
         Rbar_scale.set(0.025)      
         
         # shocks given by the user 
         
         label = tk.Label(self, text="Shocks: ", font=LARGE_FONT)
         label.grid(row = 1, column = 3)
         
         # SHOCKS inputs given by the user 
         global tax_input_modified_pcex
         tax_input_modified_pcex = tk.DoubleVar() 
         tax_scale_modified_pcex = Scale(self, variable=tax_input_modified_pcex, from_=0.02, to=0.5, resolution=0.01,orient=HORIZONTAL)
         tax_scale_modified_pcex.grid(row = 2, column = 3)
         tax_scale_modified_pcex.set(0.2)
        
         global G_input_modified_pcex
         G_input_modified_pcex = tk.DoubleVar()
         G_scale_modified_pcex = Scale(self, variable=G_input_modified_pcex, from_=1, to=100, resolution=1,orient=HORIZONTAL)
         G_scale_modified_pcex.grid(row = 3, column = 3)
         G_scale_modified_pcex.set(20)
        
         global alpha10_input_modified_pcex
         alpha10_input_modified_pcex = tk.DoubleVar()
         alpha1_scale_modified_pcex=Scale(self, variable=alpha10_input_modified_pcex, from_=0, to=1, resolution=0.01,orient=HORIZONTAL)
         alpha1_scale_modified_pcex.grid(row = 4, column = 3)
         alpha1_scale_modified_pcex.set(0.725)
        
         global alpha2_input_modified_pcex
         alpha2_input_modified_pcex = tk.DoubleVar()
         alpha2_scale_modified_pcex=Scale(self, variable=alpha2_input_modified_pcex, from_=0.01, to=1, resolution=0.01,orient=HORIZONTAL)
         alpha2_scale_modified_pcex.grid(row = 5, column = 3)
         alpha2_scale_modified_pcex.set(0.4)
         
         global Rbar_input_modified_pcex
         Rbar_input_modified_pcex = tk.DoubleVar()
         Rbar_scale=Scale(self, variable=Rbar_input_modified_pcex, from_=0.001, to=0.10, resolution=0.001,orient=HORIZONTAL)
         Rbar_scale.grid(row = 6, column = 3)
         Rbar_scale.set(0.025)
         
         
         global T_shock_input_pcex
         T_shock_input_pcex = tk.IntVar()
         T_shock_scale_pcex=Scale(self, variable=T_shock_input_pcex, from_=0, to=30, resolution=1,orient=HORIZONTAL)
         T_shock_scale_pcex.grid(row = 7, column = 3)
         T_shock_scale_pcex.set(15)
        
         ## Variables you can plot 
         label = tk.Label(self, text="Variables you can plot: ", font=LARGE_FONT)
         label.grid(row = 1, column = 5)
        
         global bouton1_input_pcex2 
         bouton1_input_pcex2 = tk.IntVar()
         bouton1_pcex = Checkbutton(self,variable = bouton1_input_pcex2, text="Income (Y)")
         bouton1_pcex.grid(row = 2,column = 5,sticky=W)
        
         global bouton2_input_pcex2 
         bouton2_input_pcex2 = tk.IntVar()
         bouton2 = Checkbutton(self,variable = bouton2_input_pcex2, text="Consumption")
         bouton2.grid(row = 3,column = 5,sticky=W)
        
         global bouton3_input_pcex2
         bouton3_input_pcex2 = tk.IntVar()
         bouton3_pcex = Checkbutton(self, variable = bouton3_input_pcex2,text="Tax Revenue")
         bouton3_pcex.grid(row = 4,column = 5,sticky=W)
         
         global bouton4_input_pcex2
         bouton4_input_pcex2 = tk.IntVar()
         bouton4_pcex = Checkbutton(self, variable = bouton4_input_pcex2,text="Stock")
         bouton4_pcex.grid(row = 5,column = 5,sticky=W)
         
         
         global bouton5_input_pcex2
         bouton5_input_pcex2 = tk.IntVar()
         bouton5_pcex = Checkbutton(self, variable = bouton5_input_pcex2,text="Stock's Flow")
         bouton5_pcex.grid(row = 6,column = 5,sticky=W)
         
       
        
         button_plot = tk.Button(self, text="Visualize",command= self.plot)
         button_plot.grid(row = 8, column = 5)
         
         button2 = tk.Button(self, text="Change scenario",command=lambda: controller.show_frame(pcex_model))
         button2.grid(row = 9, column = 6)

         button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
         button1.grid(row = 10, column =6 )
         
    # this function gives all the output results    
    def plot(self):
        
        # It gets all the input's values entered by the user
        Tax = tax_input_pcex2.get()
        G = G_input_pcex2.get()
        alpha10 = alpha10_input_pcex2.get()
        alpha2 = alpha2_input_pcex2.get()
        Rbar = Rbar_input_pcex2.get()
        
        Tax_modified = tax_input_modified_pcex.get()
        G_modified = G_input_modified_pcex.get()
        alpha10_modified = alpha10_input_modified_pcex.get()
        alpha2_modified = alpha2_input_modified_pcex.get()
        Rbar_modified = Rbar_input_modified_pcex.get()
        T_shock = T_shock_input_pcex.get()        
        
        ## variables:    
        variables = []
      
        if bouton1_input_pcex2.get() == 1:
            variables.append("Income (Y)")
        if bouton2_input_pcex2.get() ==1:
            variables.append("Consumption")
        if bouton3_input_pcex2.get() ==1:
            variables.append('Tax Revenue')
        if bouton4_input_pcex2.get() ==1:
            variables.append('Stock')
        if bouton5_input_pcex2.get() ==1:
            variables.append('flow')
            
        
        df_without_shock, steady1 = pcex(theta=Tax,G=G, alpha10=alpha10, alpha2=alpha2,Rbar=Rbar, T_shock = T_shock, 
                   theta_modified = Tax, G_modified = G, 
                   alpha10_modified = alpha10, alpha2_modified = alpha2)
        
        df_shock, steady2 = pcex(theta=Tax,G=G, alpha10=alpha10, alpha2=alpha2, Rbar=Rbar, T_shock = T_shock, 
                   theta_modified = Tax_modified, G_modified = G_modified, alpha10_modified = alpha10_modified, alpha2_modified = alpha2_modified,
                   
                   Rbar_modified=Rbar_modified)
    
    
        display_with_without_shock(df_without_shock, df_shock,  variables = variables,T_shock = T_shock)
       
        
        dic = dic_steady_states(variables = variables, steady_data = steady2)
        explanation = explain(dic, Shock = True, T_shock = T_shock )
        print(explanation)
        print("---------------------------------------------------------------------")
        print("--------------------------| Summarize table |------------------------")
        print(steady2)
        print("---------------------------------------------------------------------")
        print("")
       
       
# We create the GoodBye windows     
class GoodBye(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        texto = """ 
        Thanks for using our program's simulation.
        We hope to see you again soon!
        GoodBye! """
        label = tk.Label(self, text= texto, font=TITLE_FONT, foreground="blue")
        label.pack(pady=10,padx=10)
        


app = SeaofBTCapp()
app.title('Economic Policy Simulator v1.0')
app.mainloop()
