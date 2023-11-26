import pandas as pd

# •	Experiment_ID: Unique identifier for each experiment.
# •	Enzyme_Name: Name of the enzyme used in the experiment.
# •	Substrate: Substrate used in the reaction.
# •	Temperature: Temperature at which the experiment was conducted.
# •	pH: pH of the reaction medium.
# •	Reaction_Rate: Rate of the enzymatic reaction observed in the experiment.
# •	Substrate_Concentration: Initial concentration of the substrate in the reaction.
# •	Enzyme_Concentration: Concentration of the enzyme in the reaction.
# •	Time: Reaction time.


experiment_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
enzyme_names = ['Lipase', 'Amylase', 'Lipase', 'DNA Polymerase', 'Amylase', 'Lipase', 'DNA Polymerase', 'Amylase', 'Lipase', 'DNA Polymerase']
substrates = ['Triacylglycerol', 'Starch', 'Triacylglycerol', 'DNA Template', 'Starch', 'Triacylglycerol', 'DNA Template', 'Starch', 'Triacylglycerol', 'DNA Template']
temperatures = [25, 30, 25, 35, 30, 32, 28, 33, 29, 31]
ph_values = [7.0, 6.5, 7.2, 6.8, 7.0, 6.7, 7.5, 6.9, 7.2, 6.8]
reaction_rates = [0.05, 0.08, 0.06, 0.12, 0.09, 0.07, 0.11, 0.1, 0.08, 0.09]
substrate_concentrations = [10, 15, 10, 20, 15, 12, 18, 14, 16, 11]
enzyme_concentrations = [2, 1.5, 2, 1, 1.8, 2.2, 1.3, 1.9, 2.1, 1.7]
times = [10, 15, 12, 20, 18, 14, 16, 13, 19, 17]


#creating a List for all columns 
Enzyme_Kinetics = pd.DataFrame({
'Experiment_ID' : experiment_ids,
'Enzyme_Name': enzyme_names,
'Substrate': substrates,
'Temperature': temperatures,
'pH': ph_values,
'Reaction_Rate': reaction_rates,
'Substrate_Concentration': substrate_concentrations,
'Enzyme_Concentration': enzyme_concentrations,
'Time': times
})
print(Enzyme_Kinetics)

#Displaying first 5 rows 
print(Enzyme_Kinetics.head())

#Display the last 3 rows of the DataFrame using tail().
print(Enzyme_Kinetics.tail(3))

#Provide an overview of the DataFrame using info().
print(Enzyme_Kinetics.info())

#Using loc(), display information for experiments conducted at a specific temperature (Temperature = 30).
print(Enzyme_Kinetics.loc[Enzyme_Kinetics['Temperature'] == 30])
#Using loc(), display information for experiments conducted at a specific temperature (PH = 7).
print(Enzyme_Kinetics.loc[Enzyme_Kinetics['pH'] == 7])

#Use boolean filtering to extract rows where the 'Reaction_Rate' is greater than 0.1.
print(Enzyme_Kinetics.loc[Enzyme_Kinetics['Reaction_Rate'] > 0.1])

#Create a new DataFrame containing only experiments with a specific enzyme (DNA Polymerase) and store it in variable “DNA_Polymerase”.
DNA_Polymerase = Enzyme_Kinetics.loc[Enzyme_Kinetics['Enzyme_Name'] == 'DNA Polymerase']
print(DNA_Polymerase)
#Display a summary of the new DataFrame “DNA_Polymerase” using info().
print(DNA_Polymerase.info())

#Identify experiments where the reaction time is greater than 15 minutes.
print(Enzyme_Kinetics.loc[Enzyme_Kinetics['Time'] > 15])
#for New DataFrame of DNA 
print(DNA_Polymerase.loc[DNA_Polymerase['Time'] > 15])