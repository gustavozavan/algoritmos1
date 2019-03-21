idade = input("Digite sua idade: ")
idade = int(idade)

if( idade < 0):
    print("Idade Inválida")
elif( idade < 3 ):
  print("Bebê detectado!")
elif ( idade < 12):
  print("Criança")
elif ( idade < 18 ):
  print("Adolescente")
elif ( idade < 60 ):
  print("Adulto")
else:
  print("Melhor Idade :D")
