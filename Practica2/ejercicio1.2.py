import csv

if __name__ == "__main__":
    # We use try-except statements to properly handle errors, as in case the
    # input file does not exist in the directory.
    try:
        # We open the .csv file loading the filds separated by a ; delimiter:
        csv_archivo_locales = open("Locales.csv", encoding="utf8", errors='ignore')
        entrada_locales = csv.reader(csv_archivo_locales, delimiter=";")

        # We skip the first line before saving the results into a list for later
        # processing by using the next() statement. The reason why we do not use
        # the line_num function is because we would need to include it in a loop
        # and read file line by line whereas this way, with just two instructions
        # we get the same result:
        next(entrada_locales, None)
        lista_locales = list(entrada_locales)

        # List that will contain the result:
        agrupadas = []
        # Dictionary to keep the relation of neighborhood ID and its name, and
        # the number of locals whose main entry address differs from its official
        # address:
        barrios_dic = {}

        # For each local in the list of locals, we check if it is already in the
        # dictionary to increase its counter. Otherwise, we create a new entry in
        # the dictionary and set the counter to 1:
        for local in lista_locales:
            if local[16] != local[25]:
                entry = local[3] + ',' + local[4]

                if entry in barrios_dic:
                    barrios_dic[entry] += 1
                else:
                    barrios_dic[entry] = 1

        # Now we get the key (neighborhood ID + neighborhood name) and its attached
        # value (counter). To split the key into the two different fields it is
        # containing, we use the split() function and store the fields in a
        # small list also with the counter value:
        for key, value in barrios_dic.items():
            lista_barrios = []
            info_barrio = key.split(',')

            for i in info_barrio:
                lista_barrios.append(i)
            lista_barrios.append(value)

            # Finally, we store the mini-list containing the requested information
            # for each neighborhood in a list of neighborhoods:
            agrupadas.append(lista_barrios)

        # We open the output file to store the data retrieved:
        csvFileObj = open("Agrupadas.csv", "w")
        csvWriter = csv.writer(csvFileObj, delimiter=";")

        # For each row in the final list, we write it to the CSV output file:
        for row in agrupadas:
            csvWriter.writerow(row)

        print ("The file has been successfully created.")

        # We close the opened CSV file:
        csvFileObj.close()

    except IOError:
        print("The file does not exist.")
