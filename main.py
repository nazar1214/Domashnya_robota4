class Student:
    def __init__(self, name, pri, rokiw, ozinkyzamis, height):
        self.name = name
        self.pri = pri
        self.rokiw = rokiw
        self.ozinkyzamis = ozinkyzamis
        self.height = height

    def new_name(self, new_name):
        self.new_name = new_name

    def new_pri(self, new_pri):
        self.new_pri = new_pri

    def new_ozinkyzamis(self, new_ozinkyzamis):
        self.new_ozinkyzamis= new_ozinkyzamis

    def new_height(self, new_height):
        self.new_height = new_height

    def new_rokiw(self, new_rokiw):
        self.new_rokiw = new_rokiw

    def disstu(self):
        print("Імя студента:")
        print(f"Імя {self.name}")
        print(f"Прізвище: {self.pri}")
        print(f"Років: {self.rokiw}")
        print(f"Оцінки за місяць: {self.ozinkyzamis}")
        print(f"Зріст: {self.height}")



student1 = Student("walter", "white", "9", "13", 110)
student1.disstu()

student1.new_name("Jane")
student1.new_pri("Smith")
student1.new_rokiw(12)
student1.new_ozinkyzamis(9)
student1.new_height("9'11")
student1.disstu()
