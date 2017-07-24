
#PV = Present Value = balance

#n = numero de parcelas = 12

#i = taxa de juros / 100 = a.a ou a.m (/12)

#pmt = ?

#PV / ((1 + (i/12))**n)-1 / ((1 + (i/12))**n)*i(/12)

pv = 4060
i = 0.04
n = 12

parteMeio = ((1 + i)**n)-1
parteBaixo = ((1 + i)**n)*i

pmt = (pv / parteMeio / parteBaixo)

print(round(pmt, 2))

print(pmt * 12)

