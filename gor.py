class DayError(Exception):
    pass

class MonthError(Exception):
    pass

b=True;
while b==True:
	try:
		date  = input("Введите дату рождения в ввиде ДД.ММ.ГГГГ: ")
		day = int(date[0:2])
		# print(day)
		month = int(date[3:5])
		# print(month)
		year = int(date[6:])
		# print(year)
		if day <= 0 or day > 31:
			raise DayError 
		if (month<1) or (month>31):
			raise MonthError
		if (year==1924)or(year==1936)or(year==1948)or(year==1960) or (year==1972)or(year==1984)or(year==1996)or(year==2008)or(year==2020):
			print("Ты Крыса")

		if (year==1925) or (year==1937)   or (year==1949) or	(year==1961) or (year==1973) or	(year==1985) or	(year==1997) or	(year==2009) or		(year==2021):
			print("Ты Бык")
		if (year==1926) or (year==1938)   or (year==1950)  or	(year==1962) or 	(year==1974) or		(year==1986) or		(year==1998) or	(year==2010) or		(year==2022):          
			print("Ты Тигр")
		if  (year==1927) or (year==1939)   or (year==1951)  or	(year==1963) or 	(year==1975) or		(year==1987) or		 (year==1999) or	(year==2011) or		(year==2023):
			print("Ты Кролик")
		if  (year==1928) or (year==1940)   or (year==1952)  or	(year==1964) or 	(year==1976) or		(year==1988) or		(year==2000) or	(year==2012) or		(year==2024):
			print("Ты Дракон")
		if  (year==1929) or (year==1941)   or (year==1953)  or	(year==1965) or 	(year==1977) or		(year==1989) or		(year==2001) or	(year==2013) or		(year==2025):
			print("Ты Змея")
		if  (year==1930) or (year==1942)   or (year==1954) or	(year==1966) or 	(year==1978) or		(year==1990) or	(year==2002) or	(year==2014) or		(year==2026):
			print("Ты Лошадь")
		if  (year==1931) or (year==1943)   or (year==1955) or	(year==1967) or 	(year==1979) or		(year==1991) or		(year==2003) or	(year==2015) or		(year==2027):
			print("Ты Коза")
		if  (year==1932) or (year==1944)   or (year==1956) or	(year==1968) or 	(year==1980) or		(year==1992) or		 (year==2004) or	(year==2016) or		(year==2028):
			print("Ты Обезьяна")
		if  (year==1933) or (year==1945)   or (year==1957) or	(year==1969) or 	(year==1981) or		(year==1993) or		(year==2005) or	(year==2017) or		(year==2029):
			print("Ты Петух")
		if  (year==1934) or (year==1946)   or (year==1958)  or	(year==1970) or 	(year==1982) or		(year==1994) or	 (year==2006) or	(year==2018) or		(year==2030):
			print("Ты Собака")
		if  (year==1935) or (year==1947)   or (year==1959) or	(year==1971) or 	(year==1983) or		(year==1995) or	(year==2007) or	(year==2019) or		(year==2031):
			print("Ты Свинья")
		break

	except ValueError:
			print("Введите дату в правильном формате")
	except DayError:
			print("Введите правильный день")
	except MonthError:
    		print("Введите правильный месяц")