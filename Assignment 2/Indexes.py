#Below are the Patients and their corrosponding Treatment Group List for clinical trials.


patient_list=['Patient001','Patient002','Patient003','Patient004','Patient005']
treatment_groups=["DrugA","Placebo","DrugB","placebo","DrugA"]


# positive grouping 
#. Print the patient ID and treatment group of the 2nd patient in the trial.
print(f'2nd patient ID is : {patient_list[1]} and Treatment Group is: {treatment_groups[1]} ')

#What is the treatment group of the 4th patient in the trial? Print it using positive indexing.
print(f'Treatment group of 4th patient : {treatment_groups[3]}')

#Print the patient ID of the 1st participant in the trial
print(f'patient ID of 1st patient : {patient_list[0]}')


# negative grouping

#Print the patient ID and treatment group of the last patient in the trial
print(f'Last Patient ID in the list is {patient_list[-1]} and corrosponding treatment group is  {treatment_groups[-1]}')

#Determine the treatment group of the 3rd to last patient in the trial
print(f'Treatment group of the 3rd to last patient {treatment_groups[-3:]}')

#Print the patient ID of the 2nd to last participant in the trial.

print(f'Patient ID of the 2nd to Last Participant if we know the length {patient_list[-(len(patient_list)-1):]}')    

print(f'Patient ID of the 2nd to Last Participant if we did not know the length {patient_list[-(len(patient_list)-1):]}')    


# PART B - Assignemnts for Methods

adverse_event_list=["Rash","Headache","Nausea","Fatigue"]

#Append a new adverse event named “Fatigue” to the below list “adverse_event_list”
adverse_event_list.append("Fatigue")

# Remove a adverse event named “Headache” from the below list “adverse_event_list”
adverse_event_list.remove("Headache")


# sorting severity list
severity_list=["Mild","Severe","Moderate"]
severity_list.sort()
print(severity_list)
