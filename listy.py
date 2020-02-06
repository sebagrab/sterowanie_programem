countries = ["FR" , 'US','DE']
countries[1] = 'GB'
print(countries[1])
countries.append('PL')
countries.insert(2,'ES')
countries.remove('DE')
countries.sort()
countries.reverse()
#pobiera i usuwa z listy
print(countries.pop(2))
#na ktorej pozycji znajduje sie de
print(countries.index('ES'))

#kopiowanie listy tylko ndanie nazyw
countriesCopy = countries
countriesCopy.clear()
#kopiowanie listy
countriesCopy = countries.copy()
print(countries)

Tax = (4,7,8,23)
print(Tax[2])
print(Tax)
print(Tax.index(7))
print(Tax.index(8))
print(max(Tax))

TaxList = list(Tax)
print(TaxList)
TaxList.append(30)

a=1
b=10
(a,b)=(b,a)
print ('a=',a,"\tb b=",b)

#dicionary
CountryLeaders ={'PL':'Duda', 'US':"tramp"}
print(CountryLeaders)
print(CountryLeaders['US'])
CountryLeaders['DE']='merkel'
print(CountryLeaders.keys())
print(CountryLeaders.values())

print(CountryLeaders.popitem())
print(CountryLeaders.setdefault('FR','Marcon'))
NewLeaders= {'RU':"Putin","DE":"inny"}
CountryLeaders.update(NewLeaders)
print(CountryLeaders)