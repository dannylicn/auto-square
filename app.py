import pandas as pd

df = pd.DataFrame({'name':['A','B','C','D','E','F','G','H','I','J','K','L'],
                  'type':[0,0,1,1,1,2,2,2,2,2,2,3],
                   'level':[None, None,1,2,3,None, None, None, None, None, None,None],
                  'pl':[100,150,200,100,300,50,150,-200,100,100,-150,100],
                  'transfer':[0,0,0,0,0,0,0,0,0,0,0,0],
                  'parent':[None, 'C','A','C','D','A','B','D','E','D','E','J']})

total = df['pl'].sum()
half = total/2
avg = total/12
mininum, maxum = 0,200

df_transfer = pd.DataFrame(columns=['from','to','value'])
df.sort_values(by='type', ascending=False, inplace=True)
for i, row in df.iterrows():
    arr = []
    arr.append(row['name']) 
    print(row['name'])
    if avg>=maxum:
        threshold=maxum
    else:
        threshold=50
    print(f'total:{total},threshold:{threshold}')
    while len(arr)>0:
        name = arr[0]
        parent = df.loc[df['name']==name,'parent'].values[0]
        pl = df.loc[df['name']==name,'pl'].values[0]
        arr.pop(0)
        if parent != None:
            if ',' in parent:
                p1,p2 = parent.split(',')
                arr.append(p1)
                arr.append(p2)
                if df.loc[df['name']==p1,'pl'].values[0]>=df.loc[df['name']==p2,'pl'].values[0]:
                    parent = p1
                else:
                    parent = p2
            else:
                arr.append(parent)
        if pl>0 and pl<200:
            pass
#             print(f'{name}:pass')
        if pl<0 and parent !=None:
            ask = threshold - pl 
            df.loc[df['name']==name,'pl']=ask+pl
            df.loc[df['name']==parent,'pl']=df.loc[df['name']==parent,'pl'].values[0]-ask
            new_row = {'from':parent,'to':name,'value':ask}
            df_transfer = df_transfer.append(new_row, ignore_index=True)
        if pl>200 and parent !=None:
            offer = pl-threshold
            df.loc[df['name']==name,'pl']=pl-offer
            df.loc[df['name']==parent,'pl']=df.loc[df['name']==parent,'pl'].values[0]+ offer
            new_row = {'from':name,'to':parent,'value':offer}
            df_transfer = df_transfer.append(new_row, ignore_index=True)

df.sort_values(by=['type','pl'], ascending=True, inplace=True)

