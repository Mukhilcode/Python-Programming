# Map()
l=[1,2,3,4,5,6]
#square of the each element in the lis
def square(l):
    for i in l:
        print(i**2)
square(l)        
list(map(lambda x:x**2,l))

## odd or even

L=[21,3,5,2,56,76]
list(map(lambda x:"even" if x%2==0 else 'odd',L))


users= [{
    "house": "Gryffindor",
    "pet": "Hedwig",
    "wand": "Holly, phoenix feather"
},
{
    "house": "findor",
    "pet": "wig",
    "wand": "Hol, feather"
},
{
    "house": "Gry",
    "pet": "Heg",
    "wand": "Molly, phoenixr"
}] 

list(map(lambda users: users['house'],users))