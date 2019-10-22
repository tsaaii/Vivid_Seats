import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
engine = create_engine('sqlite:///data.db', echo=True)
with open('App/data.db', 'r') as file:
    data_df = pd.read_csv('App/data.csv',dtype={'Event_ID': int,'Section':str,'Quantity':int,'Price':int,'ROW':str,'Availability':str})
    print(data_df,data_df.columns)
data_df.to_sql('vivid_data',con=engine,index=False,index_label=None,if_exists='replace')