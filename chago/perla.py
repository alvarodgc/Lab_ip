# Welcome to your Python project!
class Patron:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email 
        self.phone = phone

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name= name


    






Patron1 = Patron ("ana","ana@gmail.com", "4921233504")
Patron2 = Patron ("luis","luis@gmail.com", "82833838")



print("\nObjeto Patron1")
print("Nombre: " + Patron1.get_name())
Patron1.set_name("Ana Maria")
print("Nombre: " + Patron1.get_name())
print("Email: "+ Patron1.email)
print("Phone: "+ Patron1.phone)


print("\nObjeto Patron2")
print("Nombre: "+ Patron2.name)
print("Email: "+ Patron2.email)
print("Phone: "+ Patron2.phone)



