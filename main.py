import time
class Student:
    def __init__(self, name, pri, rokiw, ozinkyzamis, height): 
        self.name = name
        self.pri = pri
        self.rokiw = rokiw
        self.ozinkyzamis = ozinkyzamis
        self.height = height

    def updt_name(self, new_name):
        self.name = new_name

    def updt_pri(self, new_pri):
        self.pri = new_pri

    def updt_ozinkyzamis(self, new_ozinkyzamis):
        self.ozinkyzamis= new_ozinkyzamis

    def updt_height(self, new_height):
        self.height = new_height

    def updt_rokiw(self, new_rokiw):
        self.rokiw = new_rokiw

    def disstu(self):
        print("Імя: студента:")
        print(f"Імя {self.name}")
        print(f"Прізвище: {self.pri}")
        print(f"Років: {self.rokiw}")
        print(f"Оцінки за місяць: {self.ozinkyzamis}")
        print(f"Зріст: {self.height}")



student1 = Student("walter", "white", "9", "12", 110)
student1.disstu()

time.sleep(1)
print("              ")
student1.updt_name("Walter")
student1.updt_pri("Sigma")
student1.updt_rokiw(12)
student1.updt_ozinkyzamis(9)
student1.updt_height("290")
student1.disstu()
