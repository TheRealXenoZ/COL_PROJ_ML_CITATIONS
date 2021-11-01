from sklearn.ensemble import VotingClassifier,RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.metrics import accuracy_score
clf1 = LogisticRegression(multi_class='multinomial', random_state=1)
clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
clf3 = GaussianNB()
df = pd.read_csv('physdata.csv')
df["BFC"] = df["BFC"].map({'BFCO':1,'BFCN':0})
df["CardiacCycle"] = df["CardiacCycle"].map({'CardiacCycleO':1,'CardiacCycleN':0})
df["CardiacOutput"] = df["CardiacOutput"].map({'CardiacOutputO':1,'CardiacOutputN':0})
df["LungVolume"] = df["LungVolume"].map({'LungVolumeO':1,'LungVolumeN':0})
df["EffectsOfLesions"] = df["EffectsOfLesions"].map({'EffectsOfLesionsO':1,'EffectsOfLesionsN':0})
df["Micturition"] = df["Micturition"].map({'MicturitionO':1,'MicturitionN':0})
df["Testosterone"] = df["Testosterone"].map({'TestosteroneO':1,'TestosteroneN':0})
df["lesions"] = df["lesions"].map({'lesionsO':1,'lesionsN':0})
df["TubularFunctions"] = df["TubularFunctions"].map({'TubularFunctionsO':1,'TubularFunctionsN':0})
df["Bladder"] = df["Bladder"].map({'BladderO':1,'BladderN':0})
df["Insulin"] = df["Insulin"].map({'InsulinO':1,'InsulinN':0})
df["Estrogen"] = df["Estrogen"].map({'EstrogenO':1,'EstrogenN':0})
df["Neurotransmitters"] = df["Neurotransmitters"].map({'NeurotransmittersO':1,'NeurotransmittersN':0})
df["Cerebellum"] = df["Cerebellum"].map({'CerebellumO':1,'CerebellumN':0})
df["Hypothalamus"] = df["Hypothalamus"].map({'HypothalamusO':1,'HypothalamusN':0})
df["EEG"] = df["EEG"].map({'EEGO':1,'EEGN':0})
df["SEEG"] = df["SEEG"].map({'SEEGO':1,'SEEGN':0})
df["ECG"] = df["ECG"].map({'ECGO':1,'ECGN':0})
df["Periosteal"] = df["Periosteal"].map({'PeriostealO':1,'PeriostealN':0})
df["Actnomycosis"] = df["Actnomycosis"].map({'ActnomycosisO':1,'ActnomycosisN':0})
df["BoneCyst"] = df["BoneCyst"].map({'BoneCystO':1,'BoneCystN':0})
df["Symes"] = df["Symes"].map({'SymesM':2,'SymesO':1,'SymesN':0})
df["WBC"] = df["WBC"].map({'WBCO':1,'WBCN':0})
df["Sarcomere"] = df["Sarcomere"].map({'SarcomereM':2,'SarcomereO':1,'SarcomereN':0})
df["VQratioOxygen"] = df["VQratioOxygen"].map({'VQratioOxygenM':2,'VQratioOxygenO':1,'VQratioOxygenN':0})
df["GFR"] = df["GFR"].map({'GFRM':2,'GFRO':1,'GFRN':0})
df["GIhormones"] = df["GIhormones"].map({'GIhormonesM':2,'GIhormonesO':1,'GIhormonesN':0})
df["Pituitary"] = df["Pituitary"].map({'PituitaryM':2,'PituitaryO':1,'PituitaryN':0})
df["Thyroid"] = df["Thyroid"].map({'ThyroidM':2,'ThyroidO':1,'ThyroidN':0})
df["Osteomyelits"] = df["Osteomyelits"].map({'OsteomyelitsM':2,'OsteomyelitsO':1,'OsteomyelitsN':0})
df["Citations?"] = df["Citations?"].map({'Yes':1,'No':0})
data = df[["BFC","Sarcomere","CardiacCycle","CardiacOutput","LungVolume","EffectsOfLesions","VQratioOxygen","GFR","Micturition","Testosterone","lesions","TubularFunctions","Bladder","GIhormones","Pituitary","Thyroid","Insulin","Estrogen","Neurotransmitters","Cerebellum","Hypothalamus","EEG","SEEG","ECG","Periosteal","Osteomyelits","Actnomycosis","BoneCyst","Symes","WBC","Citations?"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:350]
training_outputs = outputs[:350]
testing_inputs = inputs[350:]
testing_outputs = outputs[350:]
drlclassifier = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='hard')
drlclassifier.fit(training_inputs, training_outputs)
predictions = drlclassifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of Drl Classifier on testing data is: " + str(accuracy))
testSet = [[1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0]]
test = pd.DataFrame(testSet)
drlclassifier.fit(inputs,outputs)
predictions = drlclassifier.predict(test)
print('DRL Prediction on the first test set is:',predictions)
testSet2 = [[1,1,1,1,1,2,2,1,2,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,2,1,1,1,0,1]]
test = pd.DataFrame(testSet2)
predictions = drlclassifier.predict(test)
print('DRL Prediction on the second test set is:',predictions)
#Note: The result 0 indicates 'No Citation' in research papers. 1 indicates 'Citation'.
