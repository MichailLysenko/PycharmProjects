#Inflacja	Pożyczka
#Przed		12000
#Styczeń
inflacja_1 = 1.592824484	#11845,92824
#Luty
inflacja_2 = -0.4535091012	#11671,0662
#Marzec
inflacja_3 = 2.324671717	#11522,85337
#Kwiecień
inflacja_4 = 1.261254407	#11363,77154
#Maj
inflacja_5 = 1.782526286	#11209,06115
#Czerwiec
inflacja_6 = 2.329384541	#11058,84232
#Lipiec
inflacja_7 = 1.502229842	#10900,33353
#Sierpień
inflacja_8 = 1.782526286	#10743,77614
#Wrzesień
inflacja_9 = 2.328848994	#10591,4861
#Październik
inflacja_10 = 0.6169213482	#10423,40991
#Listopad
inflacja_11 = 2.352295886	#10269,90089
#Grudzień
inflacja_12 = 0.3377795452	#10098,46645
#Styczeń
inflacja_13 = 1.577035247	#9936,983976
#Luty
inflacja_14 = -0.2927814426	#9759,401966
#Marzec
inflacja_15 = 2.48619659	#9604,020297
#Kwiecień
inflacja_16 = 0.2671103178	#9430,168126
#Maj
inflacja_17 = 1.417952672	#9264,886489
#Czerwiec
inflacja_18 = 1.054243267	#9096,188242
#Lipiec
inflacja_19 = 1.480520104	#8930,151288
#Sierpnień
inflacja_20 = 1.577035247	#8764,212635
#Wrzesień
inflacja_21 = -0.07742069031	#8585,557724
#Październik
inflacja_22 = 1.165733399	#8415,362011
#Listopad
inflacja_23 = -0.4041867176	#8233,565935
#Grudzień
inflacja_24 = 1.499708521	#8064,439807

oprocentowanie_kredytu = float(input('Podaj oprocentowanie kredytu: '))
kwota_poczatkowa_kredytu = float(input('Podaj kwote poczatkowa kredytu: '))
stala_wartosc_raty = float(input('Podaj stala wartosc raty: '))
print(f'oprocentowanie kredytu to: {oprocentowanie_kredytu}, kwota poczatkowa kredytu to: {kwota_poczatkowa_kredytu}, stala wartosc raty to: {stala_wartosc_raty}')
kwota_po_pierwszej_racie = (1 + ((inflacja_1+oprocentowanie_kredytu)/1200)) * kwota_poczatkowa_kredytu - stala_wartosc_raty
kwota_po_drugiej_racie = (1 + ((inflacja_2+oprocentowanie_kredytu)/1200)) * kwota_po_pierwszej_racie - stala_wartosc_raty
kwota_po_trzeciej_racie = (1 + ((inflacja_3+oprocentowanie_kredytu)/1200)) * kwota_po_drugiej_racie - stala_wartosc_raty
kwota_po_czwartej_racie = (1 + ((inflacja_4+oprocentowanie_kredytu)/1200)) * kwota_po_trzeciej_racie - stala_wartosc_raty
kwota_po_piatej_racie = (1 + ((inflacja_5+oprocentowanie_kredytu)/1200)) * kwota_po_czwartej_racie - stala_wartosc_raty
kwota_po_szostej_racie = (1 + ((inflacja_6+oprocentowanie_kredytu)/1200)) * kwota_po_piatej_racie - stala_wartosc_raty
kwota_po_siodmej_racie = (1 + ((inflacja_7+oprocentowanie_kredytu)/1200)) * kwota_po_szostej_racie - stala_wartosc_raty
kwota_po_osmej_racie = (1 + ((inflacja_8+oprocentowanie_kredytu)/1200)) * kwota_po_siodmej_racie - stala_wartosc_raty
kwota_po_dziewiatej_racie = (1 + ((inflacja_9+oprocentowanie_kredytu)/1200)) * kwota_po_osmej_racie - stala_wartosc_raty
kwota_po_dziesiatej_racie = (1 + ((inflacja_10+oprocentowanie_kredytu)/1200)) * kwota_po_dziewiatej_racie - stala_wartosc_raty
kwota_po_jedenastej_racie = (1 + ((inflacja_11+oprocentowanie_kredytu)/1200)) * kwota_po_dziesiatej_racie - stala_wartosc_raty
kwota_po_dwunastej_racie = (1 + ((inflacja_12+oprocentowanie_kredytu)/1200)) * kwota_po_jedenastej_racie - stala_wartosc_raty
kwota_po_trzynastej_racie = (1 + ((inflacja_13+oprocentowanie_kredytu)/1200)) * kwota_po_dwunastej_racie - stala_wartosc_raty
kwota_po_czternastej_racie = (1 + ((inflacja_14+oprocentowanie_kredytu)/1200)) * kwota_po_trzynastej_racie - stala_wartosc_raty
kwota_po_pietnastej_racie = (1 + ((inflacja_15+oprocentowanie_kredytu)/1200)) * kwota_po_czternastej_racie - stala_wartosc_raty
kwota_po_szesnastej_racie = (1 + ((inflacja_16+oprocentowanie_kredytu)/1200)) * kwota_po_pietnastej_racie - stala_wartosc_raty
kwota_po_siedemnastej_racie = (1 + ((inflacja_17+oprocentowanie_kredytu)/1200)) * kwota_po_szesnastej_racie - stala_wartosc_raty
kwota_po_osiemnastej_racie = (1 + ((inflacja_18+oprocentowanie_kredytu)/1200)) * kwota_po_siedemnastej_racie - stala_wartosc_raty
kwota_po_dziewietnastej_racie = (1 + ((inflacja_19+oprocentowanie_kredytu)/1200)) * kwota_po_osiemnastej_racie - stala_wartosc_raty
kwota_po_dwudziestej_racie = (1 + ((inflacja_20+oprocentowanie_kredytu)/1200)) * kwota_po_dziewietnastej_racie - stala_wartosc_raty
kwota_po_dwudziestej_pierwszej_racie = (1 + ((inflacja_21+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_racie - stala_wartosc_raty
kwota_po_dwudziestej_drugiej_racie = (1 + ((inflacja_22+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_pierwszej_racie - stala_wartosc_raty
kwota_po_dwudziestej_trzeciej_racie = (1 + ((inflacja_23+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_drugiej_racie - stala_wartosc_raty
kwota_po_dwudziestej_czwartej_racie = (1 + ((inflacja_24+oprocentowanie_kredytu)/1200)) * kwota_po_dwudziestej_trzeciej_racie - stala_wartosc_raty
print(f"Twoja pozostała kwota kredytu to {kwota_po_pierwszej_racie}, to {kwota_poczatkowa_kredytu - kwota_po_pierwszej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_drugiej_racie}, to {kwota_po_pierwszej_racie - kwota_po_drugiej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_trzeciej_racie}, to {kwota_po_drugiej_racie - kwota_po_trzeciej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_czwartej_racie}, to {kwota_po_trzeciej_racie - kwota_po_czwartej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_piatej_racie}, to {kwota_po_czwartej_racie - kwota_po_piatej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_szostej_racie}), to {kwota_po_piatej_racie - kwota_po_szostej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_siodmej_racie}, {kwota_po_szostej_racie - kwota_po_siodmej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_osmej_racie}, to {kwota_po_siodmej_racie - kwota_po_osmej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dziewiatej_racie}, to {kwota_po_osmej_racie - kwota_po_dziewiatej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dziesiatej_racie}, to {kwota_po_dziewiatej_racie - kwota_po_dziesiatej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_jedenastej_racie}, to {kwota_po_dziesiatej_racie - kwota_po_jedenastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwunastej_racie}, to {kwota_po_jedenastej_racie - kwota_po_dwunastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_trzynastej_racie}, to {kwota_po_dwunastej_racie - kwota_po_trzynastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_czternastej_racie}, to {kwota_po_trzynastej_racie - kwota_po_czternastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_pietnastej_racie}, to {kwota_po_czternastej_racie - kwota_po_pietnastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_szesnastej_racie}, to {kwota_po_pietnastej_racie - kwota_po_szesnastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_siedemnastej_racie}, to {kwota_po_szesnastej_racie - kwota_po_siedemnastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_osiemnastej_racie}, to {kwota_po_siedemnastej_racie - kwota_po_osiemnastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dziewietnastej_racie}, to {kwota_po_osiemnastej_racie - kwota_po_dziewietnastej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwudziestej_racie}, to {kwota_po_dziewietnastej_racie - kwota_po_dwudziestej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwudziestej_pierwszej_racie}, to {kwota_po_dwudziestej_racie - kwota_po_dwudziestej_pierwszej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwudziestej_drugiej_racie}, to {kwota_po_dwudziestej_pierwszej_racie - kwota_po_dwudziestej_drugiej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwudziestej_trzeciej_racie}, to {kwota_po_dwudziestej_drugiej_racie - kwota_po_dwudziestej_trzeciej_racie} mniej niż w poprzednim miesiącu.")
print(f"Twoja pozostała kwota kredytu to {kwota_po_dwudziestej_czwartej_racie}, to {kwota_po_dwudziestej_trzeciej_racie - kwota_po_dwudziestej_czwartej_racie} mniej niż w poprzednim miesiącu.")
