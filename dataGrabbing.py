import pandas as pd
import os
folder = "scratch"
filepaths = [f for f in os.listdir(f"C:\\Users\\John Anticev\\OneDrive - stevens.edu\\SIMNET\\{folder}") if f.endswith('.csv')]
os.chdir(f"C:\\Users\\John Anticev\\OneDrive - stevens.edu\\SIMNET\\{folder}")
#df = pd.concat(map(pd.read_csv, filepaths),axis=1)
#curr_cols = df.columns.values()
#splitter = lambda x: x.split('-outputs_')[1].split('-tag-')[0] ##three_fin
#splitter = lambda x: x.split('-outputs_')[1].split('-tag-')[0] ##annular
splitter = lambda x: x.split('run-')[1].split('-tag-')[0] ##ldc
df = pd.concat(map(lambda x: pd.read_csv(x).rename(
            columns = {'Wall time':splitter(x)+'_Walltime',
                       'Step':splitter(x)+'_Step',
                       'Value':splitter(x)+'_Value:'+x.split('relative_error_')[1].split('.csv')[0]}), filepaths),axis=1)
df = df.loc[:,~df.columns.duplicated()].copy()
scaleCols = df.filter(like='Walltime').columns.values
import numpy as np
new_df = df.apply(lambda x: np.divide(x-x[0],3600) if x.name in scaleCols else x)
new_df.to_csv(f'C:\\Users\\John Anticev\\OneDrive - stevens.edu\\SIMNET\\{folder}\\output.csv')