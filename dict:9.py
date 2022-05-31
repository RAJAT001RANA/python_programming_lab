dct={'name':'rajat','sec':'f','rolln':39,'Name':'rajat'}
ls=[]
res=dict()
for key,val in dct.items():
    if val not in ls:
        ls.append(val) 
        res[key]=val
print(res)
