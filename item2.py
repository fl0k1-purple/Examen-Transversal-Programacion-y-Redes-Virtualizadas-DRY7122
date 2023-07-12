import urllib.parse
import requests

global api_key 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
api_key = "ulWjE3md8vRY3F4a5KNxoipUAhnHIrVi"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "S":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "S":
        break
    url = main_api + urllib.parse.urlencode({"key" : api_key, "from" : orig, "to" : dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A sucessful route call.\n")
        print("=============================================")
        print("Direcciones desde " + (orig) + " hacia " + (dest))
        print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
        print("Distancia en Kilómetros: " + str(round(int(json_data["route"]["distance"] * 1.609),2)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.609) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Código de Estado: " + str(json_status) + "; Entrada inválida en una o ambas ubicaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Código de Estado: " + str(json_status) + "; Entrada faltante en una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Para Código de Estado: " + str(json_status) + "; Refiérase a:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")