import requests
import json
url = "https://imdb-api.com/en/API/SearchMovie/k_jghn2nq5/inception%202010"
querystring = {"s":"KGF","r":"json","page":"1"}
headers = {
    #'x-rapidapi-host': 'movie-database-alternative.p.rapidapi.com',
    'x-rapidapi-key': 'k_jghn2nq5'
}
response=requests.request("GET",url,headers=headers,params=querystring)
data=json.loads((response.text))

''''
{
  "details":[
      {
          "name":"Harsha",s
          "phone":525252
      },
      {
          "name":"Harsha",s
          "phone":525252
      },
      {
          "name":"Harsha",s
          "phone":525252
      }
  ]
}

'''
result=data['results']
id=[]
title=[]
image=[]
details={}
for i in result:
    id.append(i["id"])
    title.append(i["title"])
    image.append(i["image"])

for i in result:
    details['id']=id
    details['titles']=title
    
    
print(id)
print(title)
print(image)
print(details)
