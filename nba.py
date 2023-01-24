import requests
url = "https://free-nba.p.rapidapi.com/players"
querystring = {"page":"0","per_page":"25"}
headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
'''Data= (response.text)
df = pd.DataFrame(Data)
Print(df)'''