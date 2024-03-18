from kanren.facts import Relation, facts
from kanren.core import var, run, conde

def get_sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

if __name__ == '__main__':

    #relasi ayah
    parent = Relation()
    facts(parent, ("Slamet", "Amin"),
            ("Slamet", "Anang"),
            ("Amin", "Badu"),
            ("Amin", "Budi"),
            ("Anang", "Didi"),
            ("Anang", "Dadi"))
    x = var()
    output = run(1, x, parent(x, "Budi"))
    print("Nama ayah Budi:", output[0])
    
    # relasi
    grandpa = Relation()
    facts(grandpa, ("Slamet","Badu"),
          ("Slamet","Budi"),
          ("Slamet","Didi"),
          ("Slamet","Dadi"))
   
    kakek = run(1,x, grandpa(x,"Badu"))
    print ("Kakek Badu : ", kakek[0])


    # # Example of defining siblings using an existing relation (parent)
    siblings = run(0, x, get_sibling("Slamet", x))
    siblings = [x for x in siblings if x != "Slamet"]
    print("\nNama Cucu Slamet:")
    for item in siblings:
        print(item)



#TAMBAHAN 
from kanren.facts import Relation, facts
from kanren.core import var, run
parent = Relation()
facts(parent, ("Slamet", "Amin"),
("Slamet", "Anang"),
("Amin", "Badu"),
("Amin", "Budi"),
("Anang", "Didi"),
("Anang", "Dadi"))
x = var()
child = "Amin"
ayah = run(2, x, parent(child, x))
print("\nNama ayah " + child + ": ")
for item in ayah:
    print(item)

