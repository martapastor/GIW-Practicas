import csv
import operator

if __name__ == "__main__":
    # We use try-except statements to properly handle errors, as in case the
    # input file does not exist in the directory.
    try:
        # We open the .csv file loading the filds separated by a ; delimiter:
        csv_archivo_terrazas = open("Terrazas.csv", encoding="utf8", errors='ignore')
        terrazas = csv.reader(csv_archivo_terrazas, delimiter=";")

        # We skip the first line before saving the results into a list for later
        # processing by using the next() statement. The reason why we do not use
        # the line_num function is because we would need to include it in a loop
        # and read file line by line whereas this way, with just two instructions
        # we get the same result:
        next(terrazas, None)
        lista_terrazas = list(terrazas)

        # Dictionary to keep the relation of local banner text and the number of
        # locals whith the same banner name:
        terrazas_dic = {}

        # For each local in the list of locals, we check if it is already in the
        # dictionary to increase its counter. Otherwise, we create a new entry in
        # the dictionary and set the counter to 1:
        for terraza in lista_terrazas:
            entry = terraza[21]

            if entry in terrazas_dic:
                terrazas_dic[entry] += 1
            else:
                terrazas_dic[entry] = 1

        # Now we get the key (local banner text) and its attached value (counter).
        # Then we store both values in a mini-list which will be also store in a
        # list of lists (each of one of those lists containing the values banner
        # text and amount of times it is repeated among all the locals):
        lista_rotulos = []
        for key,value in terrazas_dic.items():
            lista_num_rotulos = []

            lista_num_rotulos.append(key)
            lista_num_rotulos.append(value)

            lista_rotulos.append(lista_num_rotulos)

        # We sort the list taking into account the counting column which is in
        # the second position to get it with the itemergetter function:
        sorted_list_rotulos = sorted(lista_rotulos, key=operator.itemgetter(1), reverse = True)

        # Finally, we store in the result list only the first 20 values, already
        # sorted in descented mode:
        top_repeticiones = []
        for i in range(0, 20):
            top_repeticiones.append(sorted_list_rotulos[i])

        # We open the output file to store the data retrieved:
        csvFileObj = open("TopRepeticiones.csv", "w")
        csvWriter = csv.writer(csvFileObj, delimiter=";")

        # For each row in the final list, we write it to the CSV output file:
        for row in top_repeticiones:
            csvWriter.writerow(row)

        print ("The file has been successfully created.")

        # We close the opened CSV file:
        csvFileObj.close()

    except IOError:
        print("The file does not exist.")
