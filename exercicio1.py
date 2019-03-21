print("""
***Cadastro de Alunos***

1 - Cadastrar
2 - Alterar
3 - Excluir
4 - Consultar
5 - Imprimir Relatório
""")

escolha=input("Escolha a opção desejada: ")
escolha=int(escolha)
if(escolha==1):
    print("Você escolheu CADASTRAR aluno")
elif(escolha==2):
    print("Você escolheu ALTERAR cadastro do aluno!")
elif(escolha==3):
    print("Você escolheu EXCLUIR cadastro do aluno!")
elif(escolha==4):
    print("Você escolheu CONSULTAR cadastro do aluno!")
elif(escolha==5):
    print("Você escolheu IMPRIMIR RELATÓRIO do cadastro de alunos!")
else:
  print("Opção Inválida")
