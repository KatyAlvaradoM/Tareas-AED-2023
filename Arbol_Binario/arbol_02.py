

class Nodo: #creando la clase
    def __init__(self, nombre=None, id=None, left=None, rigth=None): #creación del constructor
        self.nombre= nombre                                        #creación de los atributos de la clase
        self.id= id
        self.left= left                                            #punteros (LEFT, RIGHT)
        
        
    def __str__(self):                                             #para convertir el objeto en cadena
        return "%s %s" %(self.id, self.nombre)
    
class arbol:
    def __init__(self):
        self.raiz = None
        
    def agregar(self, elemento):
        if self.raiz== None: 
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.id) >= int(aux.id): 
                    aux= aux.right
                else:
                    aux = aux.left
            if int(elemento.id) >= int(padre.id):
                padre.right = elemento
            else:
                padre.left = elemento



# creando método preorden
def preorden(self, elemento):
    if elemento != None:
        print(elemento)
        self.preorden(elemento.left)
        self.preorden(elemento.right)


# creando método postorden
def postorden(self, elemento):
    if elemento != None:
        self.postorden(elemento.left)
        self.postorden(elemento.right)
        print(elemento)
        

# creando método inorden
def inorden(self, elemento):
    if elemento != None:
        self.inorden(elemento.left)
        print(elemento)
        self.inorden(elemento.right)
        

def getRaiz(self):
    return self.raiz




                

if __name__ == "__main__":
    ab = arbol()
    
    while(True):
        print("\n _________OPCIONES___________")
        print("\n   1.- AGREGAR\n"+
            "   2.- PREORDEN\n"+
        "   3.- POSTORDEN\n"+
        "   4.- INORDEN")
        
        print("\n")
        
        num = input("Digite una opcion: ")
       # print("\n")
        if num == "1":
            id = input("\n ingrese el id: ")
            nombre = input("ingrese el nombre: ")
            nod = Nodo(id, nombre)
            ab.agregar(nod)
        elif num == "2":
            print("\n   _________________PREORDEN_________________")  
            ab.preorden(ab.getRaiz())
        elif num == "3":
            print("\n   _________________POSORDEN_________________")  
            ab.postorden(ab.getRaiz())
        elif num == "4":
            print("\n   _________________INORDEN_________________")  
            ab.inorden(ab.getRaiz())