# inheritance
class Parent1:
    def assign_1(self,str1):
        self.str1=str1
    def show_1(self):
        return self.str1
class Parent2:
    def assign_2(self,str2):
        self.str2=str2
    def show_2(self):
        return self.str2
class Child(Parent1,Parent2):
    def assign_3(self,str3):
        self.str3=str3
    def show_3(self):
        return self.str3
d1 =Child()
d1.assign_1("hi baby")
d1.assign_2("yo babyy")
d1.assign_3("hiii bababy")
d1.show_1()
print(d1.show_2())
print(d1.show_3())
