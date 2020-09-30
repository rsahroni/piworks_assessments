# Rahmat Hidayat
# rh.sahroni@gmail.com

from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
from bin import utility as ut
from bin.utility import Initiate 

start_process_time = datetime.now()
ut.AddLog("Initiate script location")
init = Initiate

if not Path.exists(init.output_dir):
    Path.mkdir(init.output_dir)

ut.AddLog("Read CSV: " + str(init.csv_input))
start_time = datetime.now()
df = pd.read_csv(init.csv_input, delimiter='\t')
end_time = datetime.now()
ut.AddLog("CSV read time: " + ut.CalcTime(start_time=start_time, end_time=end_time))

ut.AddLog("Split the PLAY_TS into PLAY_DATE and PLAY_TIME")
start_time = datetime.now()
playts = df['PLAY_TS'].str.split(" ", n=1, expand = True)
df['PLAY_DATE'] = playts[0]
df['PLAY_TIME'] = playts[1]
end_time = datetime.now()
ut.AddLog("Need {} to split PLAY_ID".format(ut.CalcTime(start_time=start_time, end_time=end_time)))

ut.AddLog("Filter data to 10/08/2016")
start_time = datetime.now()
ls_10aug = df['PLAY_DATE']=='10/08/2016'
df_10aug = df[ls_10aug]
end_time = datetime.now()
ut.AddLog("Need {} to filter the data".format(ut.CalcTime(start_time=start_time, end_time=end_time)))

ut.AddLog("First step pivot, count PLAY_ID per CLIENT_ID & SONG_ID")
start_time = datetime.now()
df_10aug_pv1 = pd.pivot_table(df_10aug, values='PLAY_ID', index=['CLIENT_ID','SONG_ID'], aggfunc=np.count_nonzero)
df_10aug_pv1.reset_index(inplace=True)
end_time = datetime.now()
ut.AddLog("Need {} to finish the first step pivot".format(ut.CalcTime(start_time=start_time, end_time=end_time)))

ut.AddLog("Second step pivot, count distinct SONG_ID per CLIENT_ID")
start_time = datetime.now()
df_10aug_pv2 = pd.pivot_table(df_10aug_pv1, values='SONG_ID', index='CLIENT_ID', aggfunc=np.count_nonzero)
df_10aug_pv2.reset_index(inplace=True)
end_time = datetime.now()
ut.AddLog("Need {} to finish the second step pivot".format(ut.CalcTime(start_time=start_time, end_time=end_time)))

ut.AddLog("Third step pivot, count CLIEND_ID per distinct SONG_ID")
start_time = datetime.now()
df_10aug_pv3 = pd.pivot_table(df_10aug_pv2, values='CLIENT_ID', index='SONG_ID', aggfunc=np.count_nonzero)
df_10aug_pv3.reset_index(inplace=True)
df_10aug_pv3.columns = ['DISTINCT_PLAY_COUNT', 'CLIENT_COUNT']
end_time = datetime.now()
ut.AddLog("Need {} to finish the third step pivot".format(ut.CalcTime(start_time=start_time, end_time=end_time)))

ut.AddLog("Write output file in CSV format to {}".format(init.csv_output))
start_time = datetime.now()
df_10aug_pv3.to_csv(init.csv_output, sep=',', index=False)
end_time = datetime.now()
ut.AddLog("Need {} to write the output CSV file".format(ut.CalcTime(start_time=start_time, end_time=end_time)))

end_process_time = datetime.now()
ut.AddLog("Finish all process in {}".format(ut.CalcTime(start_time=start_process_time, end_time=end_process_time)))
