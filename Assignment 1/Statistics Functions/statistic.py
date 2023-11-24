import statistics as stats

before_drug = [120, 118, 122, 124, 115]
after_drug = [110, 112, 108, 115, 113]

#Point 1a.
#getting mean before Drug
meanBefore=stats.mean(before_drug)
print(f'Mean Value Before Drug:-  {meanBefore}')

#getting mean After Drug
meanAfter=stats.mean(after_drug)
print(f'Mean Value After Drug:-  {meanAfter}')


#Point 1.b: 
#getting Standard Deviation Before Drug
standardDeviationBefore = stats.stdev(before_drug)
print(f'Standard Deviation Before Drug:-  {standardDeviationBefore}' )

#getting Standard Deviation Before Drug
standardDeviationAfter = stats.stdev(after_drug)
print(f'Standard Deviation After Drug:-  {standardDeviationAfter}' )

 
 #Point 2: 
 #Change in Means after drug administration
meanVariation = meanBefore - meanAfter
print(f'Variation is Mean :-  {meanVariation}')


 #Point 3: 
 #Change in Means after drug administration
stdDevVariation = standardDeviationBefore - standardDeviationAfter
print(f'Variation is Deviation :-  {stdDevVariation}')
 

#Indivdual Change in Standard Deviation

# PART B


patientResponseBefore=[65,70,62,68,75]
patientResponseAfter=[78,82,75,80,85]


## Mean value for Patient Repsonse Before
prMeanBefore = stats.mean(patientResponseBefore)
print(f'Patient Response Mean Value Before Treatment:- {prMeanBefore}')

## Mean value for Patient Repsonse Before
prMeanAfter = stats.mean(patientResponseAfter)
print(f'Patient Response Mean Value After Treatment:- {prMeanAfter}')

## Standard Deviation value for Patient Repsonse Before
prStandardDeviationBefore = stats.stdev(patientResponseBefore)
print(f'Patient Response Mean Value Before Treatment:- {prStandardDeviationBefore}')

## Standard Deviation value for Patient Repsonse Before
prStandardDeviationAfter = stats.stdev(patientResponseAfter)
print(f'Patient Response Mean Value After Treatment:- {prStandardDeviationAfter}')
  


 #Point 2: 
 #Change in Means after drug administration
meanVariationPR = prMeanBefore - prMeanAfter
print(f'Variation is Mean For Patient Response :-  {meanVariationPR}')


 #Point 3: 
 #Change in Means after drug administration
stdDevVariationPR = prStandardDeviationBefore - prStandardDeviationAfter
print(f'Variation is Deviation For Patient Response:-  {stdDevVariationPR}')
  
