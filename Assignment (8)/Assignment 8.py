def find(endLetter):
    for x in Pokemon_Dictionary:
        if endLetter == Pokemon_Dictionary[x][0] and Pokemon_Dictionary[x] not in current_Pokemons:
            current_Pokemons.append(x)
            find(Pokemon_Dictionary[x][1])
        else:
            break
Pokemons = open("Assignment 8 Pokemon List.txt","r",encoding='UTF8')
Pokemon_Dictionary = {}
Max_Pokemons = []
for a in Pokemons:
    for b in a.split():
        Pokemon_Dictionary[b] = [b[0],b[-1]]
for a in Pokemon_Dictionary:
    current_Pokemons = [a]
    find(Pokemon_Dictionary[a][1])
    if len(Max_Pokemons) < len(current_Pokemons):
        Max_Pokemons = current_Pokemons