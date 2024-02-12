"""
Przykład działania:
python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
Z pliku in.csv:
drzwi,3,7,0
kanapka,12,5,1
pedzel,22,34,5
plakat,czerwony,8,kij

Ma wyjść plik out.csv:
gitara,3,7,0
kanapka,12,5,kubek
pedzel,17,34,5
plakat,czerwony,8,0
"""

import csv

file_read = []

with open ("file_lm_in.csv") as file_stream:
    for line in csv.reader(file_stream):
        file_read.append(file_stream)
        print(file_read)


with open ("file_lm_out.csv", "w") as file_stream:
    csv_writer = csv.writer(file_stream)
    csv_writer.writerows(file_read)

