import random

class Operator:
    def __init__(self, name, hourly_wage_usd):
        self.name = name
        self.work_hours = 0
        self.on_leave = False
        self.hourly_wage_usd = hourly_wage_usd
        self.daily_salary = 0
        self.monthly_salary = 0
        self.production_count = 0

    def calculate_total_work_hours(self):
        return self.work_hours  # Operatörün toplam çalışma saati

    def calculate_efficiency(self):
        if self.work_hours == 0:
            return 0
        else:
            return self.production_count / self.work_hours

class ShiftSchedule:
    def __init__(self):
        self.operators = []

    def add_operator(self, name, hourly_wage_usd):
        operator = Operator(name, hourly_wage_usd)
        self.operators.append(operator)

    def calculate_salary(self, usd_to_try_exchange_rate=32.5):  # 1 doların TL karşılığı
        days = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']
        shifts = ['Sabah Vardiyası', 'Akşam Vardiyası']

        num_operators = len(self.operators)
        num_leave_per_day = num_operators // len(days)

        for day in days:
            # Operatörleri karıştır
            random.shuffle(self.operators)

            # İzin kullanacak operatörleri seç
            operators_on_leave = random.sample(self.operators, num_leave_per_day)
            for operator in operators_on_leave:
                operator.on_leave = True
                print(f"{day} günü {operator.name} izin kullanacak.")

            for operator in self.operators:
                # İzin kullanacak operatörleri pas geç
                if operator in operators_on_leave:
                    continue

                shift = random.choice(shifts)
                print(f"{day} günü {operator.name} {shift} olarak atandı.")
                # Çalışanlara günlük maaş ödenir
                if day != 'Cumartesi' and day != 'Pazar':
                    if shift == 'Sabah Vardiyası':
                        daily_salary = operator.hourly_wage_usd * 8 * usd_to_try_exchange_rate
                    else:
                        daily_salary = operator.hourly_wage_usd * 8 * usd_to_try_exchange_rate
                    operator.daily_salary += daily_salary
                    operator.work_hours += 8  # Her bir vardiya 8 saat olduğu için
                    print(f"{operator.name} için günlük maaş: ₺{daily_salary:.2f}")
                    
                    # Operatörün günlük üretim adedini al
                    while True:
                        try:
                            production_count = int(input(f"{operator.name} için günlük üretim adedi: "))
                            if production_count < 0:
                                raise ValueError("Üretim adedi negatif olamaz. Lütfen pozitif bir değer girin.")
                            break
                        except ValueError as ve:
                            print(ve)
                    operator.production_count += production_count  # Operatörün toplam üretim adedine ekle

            # İzin kullanacak operatörlerin izinini sıfırla
            for operator in operators_on_leave:
                operator.on_leave = False

        print("\nAylık Maaşlar, Toplam Çalışma Saatleri ve Verimlilik:")
        self.calculate_monthly_salary()
        self.calculate_total_work_hours()
        self.calculate_efficiency()

    def calculate_monthly_salary(self):
        for operator in self.operators:
            operator.monthly_salary = operator.daily_salary * 20  # 20 iş günü var varsayıldı
            print(f"{operator.name}: ₺{operator.monthly_salary:.2f}")

    def calculate_total_work_hours(self):
        for operator in self.operators:
            total_work_hours = operator.calculate_total_work_hours()
            print(f"{operator.name} Toplam Çalışma Saati: {total_work_hours} saat")

    def calculate_efficiency(self):
        for operator in self.operators:
            efficiency = operator.calculate_efficiency()
            print(f"{operator.name} Verimlilik: {efficiency:.2f} adet/saat")


def main():
    schedule = ShiftSchedule()

    # Operatörleri ekleyin ve saatlik ücretleri dolar olarak belirleyin
    schedule.add_operator("Ahmet", 15)   # Ahmet'in saatlik ücreti $15
    schedule.add_operator("Berat", 12)   # Berat'in saatlik ücreti $12
    schedule.add_operator("Ceylin", 13)  # Ceylin'in saatlik ücreti $13
    schedule.add_operator("Deniz", 14)   # Deniz'in saatlik ücreti $14
    schedule.add_operator("Elif", 16)    # Elif'in saatlik ücreti $16
    schedule.add_operator("Faruk", 11)   # Faruk'un saatlik ücreti $11
    schedule.add_operator("Gökhan", 17)  # Gökhan'ın saatlik ücreti $17
    schedule.add_operator("Hakan", 14)   # Hakan'ın saatlik ücreti $14
    # Yeni operatörler ekle ve saatlik ücretleri dolar olarak belirleyin
    schedule.add_operator("İbrahim", 18) # İbrahim'in saatlik ücreti $18
    schedule.add_operator("Jale", 15)     # Jale'in saatlik ücreti $15
    schedule.add_operator("Kadir", 16)    # Kadir'in
    schedule.calculate_salary(usd_to_try_exchange_rate=32.5)


if __name__ == "__main__":
    main()
