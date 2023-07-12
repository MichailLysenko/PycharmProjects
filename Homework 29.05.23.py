'''
	Inflacja	Pożyczka
Przed		12000
Styczeń	1,592824484	11845,92824
Luty	-0,4535091012	11671,0662
Marzec	2,324671717	11522,85337
Kwiecień	1,261254407	11363,77154
Maj	1,782526286	11209,06115
Czerwiec	2,329384541	11058,84232
Lipiec	1,502229842	10900,33353
Sierpnień	1,782526286	10743,77614
Wrzesień	2,328848994	10591,4861
Październik	0,6169213482	10423,40991
Listopad	2,352295886	10269,90089
Grudzień	0,3377795452	10098,46645
Styczeń	1,577035247	9936,983976
Luty	-0,2927814426	9759,401966
Marzec	2,48619659	9604,020297
Kwiecień	0,2671103178	9430,168126
Maj	1,417952672	9264,886489
Czerwiec	1,054243267	9096,188242
Lipiec	1,480520104	8930,151288
Sierpnień	1,577035247	8764,212635
Wrzesień	-0,07742069031	8585,557724
Październik	1,165733399	8415,362011
Listopad	-0,4041867176	8233,565935
Grudzień	1,499708521	8064,439807
Grudzień = 0.337779545187098 * Pozyczka
'''

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
formula_do_pierwszego_obliczenia = (1 + ((inflacja_1+oprocentowanie_kredytu)/1200)) * kwota_poczatkowa_kredytu - stala_wartosc_raty

'''
tabela_inflacji_wartosci
oprocentowanie_kredytu
stala_wartosc_raty
wartosc_zadluzenia_w_kazdym_miesiacu_przez_2_nadchodzace_lata
Pozostala_kwota_kredytu_1 = x
Pozostala_kwota_kredytu_2 = y
'''