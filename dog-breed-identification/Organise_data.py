import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import os

directory='C:/Users/savad/dog-breed-identification'
directories=['/images/train','/images/test']
labels=pd.read_csv('labels.csv',sep=',')
os.mkdir(directory+directories[0])
os.mkdir(directory+directories[1])

for filename in os.listdir(directory+'/train'):
    print(filename)
    n_dir=1
    print(np.random.binomial(size=1,n=1,p=0.7))
    if np.random.binomial(size=1,n=1,p=0.7)[0]==1:
        n_dir=0
    if not os.path.isdir(directory+directories[n_dir] +"/"+labels[labels['id']==filename.strip('.jpg')].iloc[0,1]):
        os.mkdir(directory+directories[n_dir] +"/"+labels[labels['id']==filename.strip('.jpg')].iloc[0,1])
    shutil.move(directory+'/train/'+ filename, directory+directories[n_dir] +'/'+ labels[labels['id']==filename.strip('.jpg')].iloc[0,1]+'/'+filename) 