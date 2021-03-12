from datetime import datetime
import pandas as pd


data = pd.read_excel('mwFellowship.xlsx',engine='openpyxl')

schedules = data.to_dict('records')

# date processing
current_data = datetime.now().date()
year, week_num, day_of_week = current_data.isocalendar()


for schedule in schedules:
    if schedule['Week'] == week_num:
        text_msg =pd.DataFrame.from_dict(schedule, orient='index')
        #text_msg =pd.DataFrame(schedule, index=['first'])
        print (text_msg)

