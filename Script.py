import pandas as pd 
from sqlalchemy import create_engine
import urllib  


#Database Configuration 

Server='ACER-PC' 
Database='Sales_DW' 
Driver='SQL SERVER'

params = urllib.parse.quote_plus(
    f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


