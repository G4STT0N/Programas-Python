import requests
import json

api_url = "http://ip-api.com/json/"

parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):
	res = requests.get(api_url+ip, data=data)
	api_json_res = json.loads(res.content)
	return api_json_res

if __name__ == '__main__':
	
	print()
	print()
	print('░██████╗░░░░██████╗░██╗████████╗░██████╗')
	print('██╔════╝░░░░██╔══██╗██║╚══██╔══╝██╔════╝')
	print('██║░░██╗░░░░██████╦╝██║░░░██║░░░╚█████╗░')
	print('██║░░╚██╗░░░██╔══██╗██║░░░██║░░░░╚═══██╗')
	print('╚██████╔╝██╗██████╦╝██║░░░██║░░░██████╔╝')
	print('░╚═════╝░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░')
	print()
	print()

	ip = input("Ingrese la dirección IP: ")
	
	par = parametros.split(",")
	for x in par:
		print(x.upper(), ":")
		print(ip_scraping(ip)[x])
		print("\n")
	