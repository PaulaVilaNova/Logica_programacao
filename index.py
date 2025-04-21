# nome =input("nome do herói:")
nome = "paula"
XPs = 9056

if 0 <= XPs <= 1000:
    nivel = "Ferro"  
elif 1001 <= XPs < 2000:
    nivel = "Bronze"
elif 2001 <= XPs < 5000:
    nivel = "Prata"
elif 5001 <= XPs < 7000:
    nivel = "Ouro"
elif 7001 <= XPs < 8000:
    nivel = "Platina"
elif 8001 <= XPs < 9000:
    nivel = "Ascendente"
elif 9001 <= XPs < 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print("O Herói de nome",nome,"está no nível de", nivel)