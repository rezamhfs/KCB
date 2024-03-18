from kanren.facts import Relation, facts
from kanren.core import var, run, conde

def get_sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))


if __name__ == '__main__':
    parent = Relation()
    facts(parent, ("Homer", "Bart"),
          ("Homer", "Lisa"),
          ("Abe", "Homer"))
    x = var()
    output = run(1, x, parent(x, "Lisa"))
    print("\nNama ayah Bart:", output[0])
    
    # Example of defining sibling (sibling) using a new relation
    sibling = Relation()
    facts(sibling, ("Bart", "Lisa"),
          ("Lisa", "Bart"),
          ("Lisa", "Agung"))
    

    brother = run(0, x, sibling(x, "Lisa"))
    print("\nNama saudara laki-laki Lisa:", brother[0])
    
    sister = run(0, x, sibling(x, "Bart"))
    print("\nNama saudara perempuan Bart:", sister[0])

    # Example of defining siblings using an existing relation (parent)
    siblings = run(0, x, get_sibling("Lisa", x))
    siblings = [x for x in siblings if x != "Lisa"]
    print("\nNama saudara Lisa:")
    for item in siblings:
        print(item)
