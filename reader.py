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
import sys
print(sys.argv)

file_read = []

with open ("in.csv") as file_stream:
    for line in csv.reader(file_stream):
        file_read.append(line)

print(file_read)
file_read[0][0] = 'gitara'
file_read[1][3] = 'kubek'
file_read[2][1] = '17'
file_read[3][3] = 'kij'
print(file_read)


with open ("out.csv", "w", newline='') as file_stream:
    csv_writer = csv.writer(file_stream, delimiter=",")
    csv_writer.writerows(file_read)


