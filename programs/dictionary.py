anime = { 
    'Naruto':'Naruto',
    'Luffy':'One Piece',
    'Ichigo':'Bleach'
}
anime.update({'Bakugo':'My Hero Academia'})
#print(anime[input("Enter the anime character: ")])
print(anime.get(input("Enter the anime character: ")))
#print(anime.keys())
#print(anime.values())
print(anime.items())
a = anime.pop('Luffy')
print(a)
print(anime)
b = anime.popitem()
print(b)
print(anime)
anime.clear()
print(anime)