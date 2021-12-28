# -*- coding: utf-8 -*-
"""

   - Loads the dataset
   - Adds class labels to the data
   - Normalizes the data
   - Returns arrays of attributes, classes for the CNN

"""

from Bio import SeqIO
import numpy as np
from imblearn.over_sampling import SMOTEN
from sklearn.model_selection import train_test_split

def execute():
    print("Load and preprocessing")
    print()

    # Load each dataset separately
    # for each one, create an array with the class labels
    # COVID -> 0, DENGUE -> 1, EBOLA -> 2, MERS -> 3, SARS -> 4

    classesDict = {0: "COVID", 1: "DENGUE", 2: "EBOLA", 3: "MERS", 4: "SARS"}
    attributes = np.array([])
    classes = np.array([])
    
    for key in classesDict:
        fasta_sequences = SeqIO.parse(open("data/sequences"+classesDict[key]+".fasta"), 'fasta')
        attrsSize = attributes.shape[0]           
        attributes = np.concatenate ((attributes, np.array([str(fasta.seq) for fasta in fasta_sequences])))
        classSize = attributes.shape[0] - attrsSize
        currentClass = np.empty(classSize)
        currentClass.fill(key)
        classes = np.concatenate ((classes, currentClass))
        print("class ", classesDict[key], " size: ", currentClass.shape[0])
        
    print("total attributes size before oversampling: ", attributes.shape[0])
    print("total classes size before oversampling: ", classes.shape[0])

    # oversampling the classes with less occurrencias using SMOTE
    attributes = attributes.reshape(-1,1)
    oversampling_classes = {1 : 13000, 2 : 13000, 3 : 13000, 4 : 13000}
    sampler = SMOTEN(sampling_strategy=oversampling_classes, random_state=0)
    X_res, y_res = sampler.fit_resample(attributes, classes)
        
    maxSequence = 6000 
            
    X_resBinarized = np.empty((0, maxSequence), dtype=np.uint8)
    for sequence in X_res:
        sequenceStr = sequence[0]
        sequenceBinarizedStr = ""
        index = 0
        for char in sequenceStr:
            if index < maxSequence:
                if char == 'a':
                    sequenceBinarizedStr += "1"
                elif char == 'c':
                    sequenceBinarizedStr += "2"
                elif char == 'g':
                    sequenceBinarizedStr += "3"
                elif char == 't':
                    sequenceBinarizedStr += "4"
                else:
                    sequenceBinarizedStr += "0"
            index += 1
            
        if len(sequenceStr) < maxSequence:
            sequenceLength = len(sequenceStr)
            while sequenceLength < maxSequence:
                sequenceBinarizedStr += "0"
                sequenceLength += 1
        
        sequenceBinarized = np.array(list(sequenceBinarizedStr), dtype=np.uint8)
        X_resBinarized = np.append(X_resBinarized, [sequenceBinarized], axis=0)
        
    
    # 70% train, 30% validation/test
    x_train, x_test, y_train, y_test = train_test_split(X_resBinarized, y_res, test_size=0.3, random_state=4, stratify=y_res)
    
    print("x_train size: ", x_train.shape[0])
    print("y_train size: ", y_train.shape[0])
    print("x_test size: ", x_test.shape[0])
    print("y_test size: ", y_test.shape[0])

    
    return (x_train, y_train), (x_test, y_test)
