import requests, lxml.html as lh, pandas as pd,json

#this file should only really be run if an update to the list of flights is needed
#i debated even adding this file however it is how i ended up getting the different airport codes

url ='https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States'
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
tr_elements_slice = tr_elements[7:]
col=[]
i=0
for t in tr_elements_slice[0]:
    i+=1
    name=t.text_content()
    col.append((name,[]))
for j in range(1,len(tr_elements_slice)):
    T=tr_elements_slice[j]
    if len(T)!=7:
        break
    i=0
    for t in T.iterchildren():
        data=t.text_content() 
        if i>0:
            try:
                data=int(data)
            except:
                pass
        col[i][1].append(data)
        i+=1
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
df = df[['IATA','Airport']]
df = df.apply(lambda x: x.str.strip())
df.replace('', None,inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True) 
df.sort_values('Airport',inplace=True)
df = df.iloc[1:,:]
df.set_index('IATA',inplace=True)
airportcodes = df.to_dict()
with open('airportcodes.txt', 'w') as f:
    f.write(json.dumps(airportcodes['Airport']))
f.close()