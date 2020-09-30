from pathlib import Path
from datetime import datetime

class Initiate():
    base_dir = Path.cwd()
    input_dir = base_dir.joinpath('input')
    output_dir = base_dir.joinpath('output')
    # csv_input = input_dir.joinpath('sample.csv')
    csv_input = input_dir.joinpath('exhibitA-input.csv')
    csv_output = output_dir.joinpath('exhibitA-output.csv')

def AddLog(msg):
    print(datetime.now().strftime("%Y-%m-%d %H:%m:%S"), msg)

def CalcTime(start_time, end_time):
    total_time = datetime.now()
    total_time = end_time - start_time
    return str(round(total_time.total_seconds(),2)) + " seconds"