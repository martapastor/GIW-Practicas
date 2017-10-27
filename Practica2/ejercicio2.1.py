import json

if __name__ == "__main__":
    # We use try-except statements to properly handle errors, as in case the
    # input file does not exist in the directory.
    try:
        # We open the .json file and properly load it in JSON format using the
        # json module for Python
        doc = open('Agenda.json', encoding="utf8")
        json_doc = json.loads(doc.read())
        lista_eventos = json_doc["@graph"]

        try:
            # We open both the output files to store the data retrieved
            kids = open("Children.txt", "w", encoding="utf8")
            familias = open("Families.txt", "w", encoding="utf8")

            # For each entry in the list of events, we check if the field
            # "audience" corresponds to one of the ones we are looking for. If
            # it is the case, we add it to the correspondent output file:
            for evento in lista_eventos:
                if "audience" in evento:
                    if evento["audience"] == "Niños,Familias":
                        familias.write("Titulo: " + evento["title"] + " " + "Inicio: " + evento["dtstart"] + " " + "Final: " + evento["dtend"] + " " + "URL: " + evento["link"] + "\n")
                    elif evento["audience"] == "Niños":
                        kids.write("Titulo: " + evento["title"] + " " + "Inicio: " + evento["dtstart"] + " " + "Final: " + evento["dtend"] + " " + "URL: " + evento["link"] + "\n")

            print ("The files have been successfully created.")

            # We close every opened file:
            kids.close()
            familias.close()
            doc.close()

        except IOError:
            print ("The files could not be opened.")

    except IOError:
        print("The file does not exist.")
