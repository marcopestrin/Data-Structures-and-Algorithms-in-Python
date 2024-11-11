import pandas as pd
import math
from datetime import datetime

GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"  # Reset to default
BOLD = "\033[1m"
MONTHS = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

def process_file(file_path):
    asset_data = {}

    df = pd.read_excel(file_path, header=None)
    df = df.iloc[1:15] # rows of assets

    for _, row in df.iterrows():
        ticker = row[0]
        asset_name = row[1]
        broker = row[2]
        full_name = broker + ' - ' + ticker + ' - ' + asset_name


        if ticker == 'XCS6':
            print (ticker)

        monthly_data = processin_data(
            values= row[5:17].to_numpy(),  # get month values and start with index 0
            pac_value=row[3],
            pac_start=row[4]
            )
        
        asset_data[full_name] = monthly_data
        print_data(asset_data, pac_start=row[4], pac_value=row[3])


def get_pecentage_yield(value, base_value, compared_value):
    if base_value == 0 or value == 0:
        return 0
    return (value - base_value) / compared_value * 100

def is_pac_started(pac_start, month_index):
    # TO DO!!
    try:
        # Format the date in MM-YY
        today = datetime.now().strftime("%m-%y")
        month, year = pac_start.split('-')
        return True
    except:
        return 0

def processin_data(values, pac_value, pac_start):
    monthly_data = []
    for month_index, value in enumerate(values):
        # month_index --> january == 0
        # pac_start --> january == 1
        # monthly_data --> january == 0

        pac_started = pac_start <= month_index +1 #_pac_started(pac_start, month_index)
        monthly_info = {
            'base_value': 0,
            'current_value': 0,
            'delta_percentage': 0
        }

        if not math.isnan(value) and value != 0.0:
            value = float(value)
            if len(monthly_data) > 0:
                # no first month of year
                previous_month_value = monthly_data[month_index - 1]['current_value'] or 0
                if pac_started:
                    # the yield must be net of the monthly contribution
                    base_value = round(previous_month_value + pac_value, 2)
                    if previous_month_value == 0 or previous_month_value == 1: 
                        # first contribution of PAC
                        delta_percentage = get_pecentage_yield(value=value, base_value=base_value, compared_value=base_value)
                    else:
                        # no first month with PAC
                        delta_percentage = get_pecentage_yield(value=value, base_value=base_value, compared_value=previous_month_value)
                else:
                    # no PAC for this asset this month
                    delta_percentage = get_pecentage_yield(
                        value=value,
                        base_value=round(previous_month_value, 2),
                        compared_value=previous_month_value
                        )

            else:
                # january 
                if pac_started:
                    base_value = pac_value 
                    delta_percentage = get_pecentage_yield(value=value, base_value=pac_value, compared_value=pac_value)
                else:
                    base_value = 0
                    delta_percentage = 0

            monthly_info['base_value'] = base_value
            monthly_info['current_value'] = round(value, 2)
            monthly_info['delta_percentage'] = round(delta_percentage, 2)
        
        monthly_data.append(monthly_info)
    return monthly_data
            

def print_data(data, pac_start, pac_value):
    for asset, values in data.items():
        print(f" ")
        print(f"{BOLD}{asset}:{RESET}")
        print(f" €"+str(pac_value)+' since '+str(pac_start))
        print(f" ")

        for month_index, month_info in enumerate(values):

            delta_color = GREEN if month_info['delta_percentage'] > 0 else RED
            delta_value = f"{month_info['delta_percentage']:.2f}"
            month_name = MONTHS[month_index]
    
            if month_info['current_value'] == 0:
                continue

            print(f"  {month_name}: Base Value = {month_info['base_value']},     "
                f"Value = {month_info['current_value']},     "
                f"Delta = {delta_color}{delta_value}%{RESET}")
        print(f" ")

process_file('source.xlsx')
