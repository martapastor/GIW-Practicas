import json
import math

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat= lat2 - lat1
    dlon= lon2 - lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia


def eventos_cercanos(latitud, longitud, max_distancia, json_doc):
    lista_eventos = json_doc["@graph"]

    # For every event in the list of events, we obtain its latitude and longitude
    # and calculate the distance in km using the given function.
    for loc in lista_eventos:
        if "location" in loc:
            lat = loc["location"]["latitude"]
            lon = loc["location"]["longitude"]
            dis = haversine(float(latitud), float(longitud), lat ,lon)

            # If the distance calculated is lower than our maximun distance wanted
            # then the activity is shown in the standard output:
            if dis <= float(max_distancia):
                print ("Titulo: " + loc["title"] + " " + "Inicio: " + loc["dtstart"] + " " + "Final: " + loc["dtend"] + " " + "URL: " + loc["link"] + "\n")


if __name__ == "__main__":
    # We use try-except statements to properly handle errors, as in case the
    # input file does not exist in the directory.
    try:
        # We open the .json file and properly load it in JSON format using the
        # json module for Python
        doc = open('Agenda.json', encoding="utf8")
        json_doc = json.loads(doc.read())

        lista_eventos = json_doc["@graph"]

        # We introduce the desired values to calculate from:
        miLat = input ("Mi latitud: \n")
        miLon = input ("Mi longitud: \n")
        distMax = input ("Distancia maxima que recorrer: \n")

        eventos_cercanos(miLat, miLon, distMax, json_doc)

        # We close the opened file:
        doc.close()

    except IOError:
        print("The file does not exist.")
