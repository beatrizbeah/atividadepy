def calculadora():
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  operador = input("Digite a operação (+, -, *, /): ")

  if operador == '+':
    resultado = num1 + num2
  elif operador == '-':
    resultado = num1 - num2
  elif operador == '*':
    resultado = num1 * num2
  elif operador == '/':
    if num2 == 0:
      print("Divisão por zero não é permitida.")
    else:
      resultado = num1 / num2
  else:
    print("Operador inválido.")

  if 'resultado' in locals():
    print("Resultado:", resultado)

calculadora()