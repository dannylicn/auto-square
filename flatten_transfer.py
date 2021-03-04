import pandas as pd

# import sample data
df_transfer = pd.DataFrame({'from':[],
                            'to':[],
                            'value':[]})

# swith from, to column by comparing the from, to alphabetically
for i, row in df_transfer.iterrows():
    if row['from']>row['to']:
        df_transfer.loc[i,'from'] = row['to']
        df_transfer.loc[i,'to'] = row['from']
        df_transfer.loc[i,'value'] = - df_transfer.loc[i,'value']

# group up
df_transfer = df_transfer.groupby(by=["from",'to'],as_index=False).sum()

# swith from, to if transfer value is negtive 
for i, row in df_transfer.iterrows():
    if row['value']<0:
        df_transfer.loc[i,'from'] = row['to']
        df_transfer.loc[i,'to'] = row['from']
        df_transfer.loc[i,'value'] = - df_transfer.loc[i,'value']

# sum up the total transfer
df_transfer['value'].sum()