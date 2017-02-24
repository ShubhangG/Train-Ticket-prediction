import pandas as pd
import pickle as pk
import numpy as np

df = pd.read_csv("EVERYTHING.csv", usecols=['bookingStatus', 'status1Day', 'status1Month', 'status1Week', 'status2Days'])

df.dropna(how='any', inplace=True)

df['status1Day'] = df['status1Day'].str.rstrip(to_strip= "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
df['status1Week'] = df['status1Week'].str.rstrip(to_strip= "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
df['status1Month'] = df['status1Month'].str.rstrip(to_strip= "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
df['status2Days'] = df['status2Days'].str.rstrip(to_strip= "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
df['bookingStatus'] = df['bookingStatus'].str.rstrip(to_strip= "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


#Remove all RAC and make them 0
df['status1Day'].replace(regex=True, inplace=True, to_replace=r'[^W/L\d\s,].*', value= r'0')
df['status2Days'].replace(regex=True, inplace=True, to_replace=r'[^W/L\d\s,].*', value=r'0')
df['status1Week'].replace(regex=True, inplace=True, to_replace=r'[^W/L\d\s,].*', value=r'0')
df['status1Month'].replace(regex=True, inplace=True, to_replace=r'[^W/L\d\s,].*', value=r'0')
df['bookingStatus'].replace(regex=True, inplace=True, to_replace=r'[^W/L\d\s,].*', value=r'0')


#The 5 following lines replace all letters of the alphabet with nothing and spaces with backslash.
df['status1Day'].replace(regex=True, inplace=True, to_replace=[r'[a-zA-Z/]', r'\s' ], value=[r'', r'/'])
df['status2Days'].replace(regex=True, inplace=True, to_replace=[r'[a-zA-Z/]', r'\s' ], value=[r'', r'/'])
df['status1Week'].replace(regex=True, inplace=True, to_replace=[r'[a-zA-Z/]', r'\s' ], value=[r'', r'/'])
df['status1Month'].replace(regex=True, inplace=True, to_replace=[r'[a-zA-Z/]', r'\s' ], value=[r'', r'/'])
df['bookingStatus'].replace(regex=True, inplace=True, to_replace=[r'[a-zA-Z/]', r'\s' ], value=[r'', r'/'])


#These 5 following lines strip from the left hand side all numbers until it hits a non digit
df['status1Day'] = df['status1Day'].str.lstrip(to_strip= "123456789,")
df['status1Week'] = df['status1Week'].str.lstrip(to_strip= "123456789,")
df['status1Month'] = df['status1Month'].str.lstrip(to_strip= "123456789,")
df['status2Days'] = df['status2Days'].str.lstrip(to_strip= "123456789,")
df['bookingStatus'] = df['bookingStatus'].str.lstrip(to_strip= "123456789,")


#These commands below now remove every non digit from these columns
df['status1Day'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')
df['status2Days'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')
df['status1Week'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')
df['status1Month'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')
df['bookingStatus'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')

df.replace(r'\s+|^$', 0, regex=True, inplace=True)

df['status1Day'] = df['status1Day'].astype(int,  raise_on_error=False)
df['status1Week'] = df['status1Week'].astype(int)
df['status1Month'] = df['status1Month'].astype(int)
df['status2Days'] = df['status2Days'].astype(int)
df['bookingStatus'] = df['bookingStatus'].astype(int)


#Write to csv
#df.to_csv("features_Anand.csv", index=False)
df.to_csv("features.csv", index=False)