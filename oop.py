class Kefir:
    def __init__(self, percent_fat, color,packaging,firm):
        self.percent_fat = percent_fat
        self.color = color
        self.country = "Дагестан"
        self.packaging = packaging
        self.firm = firm
        

    def ferment(self, time):
        return "Испортился" if time > 10 else "Все хорошо"

the_best_kefir_in_the_world = Kefir(120,"Серый","бутылка","Oldspice")
print(the_best_kefir_in_the_world.ferment(14))
print(the_best_kefir_in_the_world.percent_fat)
print(the_best_kefir_in_the_world.color)
print(the_best_kefir_in_the_world.country)
print(the_best_kefir_in_the_world.packaging)
print(the_best_kefir_in_the_world.firm)
kefir = Kefir(227,"Белый","пакет","Newvillage")
kefir.country = "Татарстан"
print()
print(kefir.ferment(14))
print(kefir.percent_fat)
print(kefir.color)
print(kefir.country)
print(kefir.packaging)
print(kefir.firm)
