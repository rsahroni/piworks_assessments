from pathlib import Path
from datetime import datetime
from bin import utility as ut
from bin.utility import Initiate
import pandas as pd
import sys

init = Initiate

if not Path.exists(init.csv_output):
    ut.AddLog("Output file not found. Please run technical_assessment_v2.py first!")
    sys.exit()

ut.AddLog("Read the output file")
start_time = datetime.now()
df_output = pd.read_csv(init.csv_output, sep=',')
end_time = datetime.now()
ut.AddLog("Need {} to read output file".format(ut.CalcTime(start_time=start_time, end_time=end_time)))
ut.AddLog("###########################################################")
ut.AddLog("Answer the questions number 2 & 3")
ut.AddLog("[Q2] How many users played 346 distinct songs?")
ut.AddLog("Answer:")

df_346 = df_output[df_output['DISTINCT_PLAY_COUNT']==346]
print(df_346)

ut.AddLog("[Q3] What is the maximum number of distinct songs  played?")
ut.AddLog("Answer:")

max_played_song = df_output['DISTINCT_PLAY_COUNT'].max()
print(max_played_song)
