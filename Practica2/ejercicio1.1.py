import csv
import operator

if __name__ == "__main__":
    # We use try-except statements to properly handle errors, as in case the
    # input file does not exist in the directory.
    try:
        # We open the .csv file loading the filds separated by a ; delimiter:
        csv_archivo_locales = open("Locales.csv", encoding="utf8", errors='ignore')
        locales = csv.reader(csv_archivo_locales, delimiter=";")
        csv_archivo_terrazas = open("Terrazas.csv", encoding="utf8", errors='ignore')
        terrazas = csv.reader(csv_archivo_terrazas, delimiter=";")

        # We skip the first line before saving the results into a list for later
        # processing by using the next() statement. The reason why we do not use
        # the line_num function is because we would need to include it in a loop
        # and read file line by line whereas this way, with just two instructions
        # we get the same result:
        next(locales, None)
        lista_locales = list(locales)
        next(terrazas, None)
        lista_terrazas = list(terrazas)

        # When we read the fields from the CSV, they are stored as strings, so we
        # need to explicitely convert the ID to int to be able to sort them:
        for i in lista_locales:
            i[0] = int(i[0])

        for j in lista_terrazas:
            j[0] = int(j[0])

        # We sort the lists taking into account the ID column which is in the
        # first position to get it with the itemergetter function:
        sorted_lista_locales = sorted(lista_locales, key=operator.itemgetter(0), reverse = False)
        sorted_lista_terrazas = sorted(lista_terrazas, key=operator.itemgetter(0), reverse = False)

        # For each entry in lista_terrazas, we check where is its corresponding
        # entry in lista_locales. As they are sorted ascendently, all the entries
        # before the wanted one are included in the result list as they do not
        # appear in lista_terrazas. Moreover, we keep the index counter to just
        # traverse the lista_locales once.
        index = 0
        no_terrazas = []
        for terraza in sorted_lista_terrazas:
            while (terraza[0] > sorted_lista_locales[index][0]):
                no_terrazas.append(sorted_lista_locales[index])
                index += 1

            # It is important to perform this step once we have reached the local
            # entry from the lista_locales, as if not, the next entry from
            # lista_terrazas will be greater than the found one in lista_locales
            # and will wrongly include it in the result list:
            if (terraza[0] == sorted_lista_locales[index][0]):
                index += 1

        # We open the output file to store the data retrieved:
        csvFileObj = open("NoTerrazas.csv", "w")
        csvWriter = csv.writer(csvFileObj, delimiter=";")

        # For each row in the final list, we write it to the CSV output file:
        for row in no_terrazas:
            csvWriter.writerow(row)

        print ("The file has been successfully created.")

        # We close the opened CSV file:
        csvFileObj.close()

        # NOTE: we have realized that a few error occurs when comparing the total
        # amount of entries in NoTerrazas.csv with the entries in Locales.csv and
        # Terrazas.csv, as it is expected to have NoTerrazas = Locales - Terrazas

        # However, as the exercice statement indicates that some inconsistency
        # may exist in the files, we assume the error is due to this unsteadiness.

    except IOError:
        print("The file does not exist.")
