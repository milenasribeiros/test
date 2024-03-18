def inverter (string):
    string_invertida = ""

    for i in range(len(string) -1, -1, -1):
        string_invertida += string[i]
    return string_invertida

programa = input("Insira uma string: ")

string_invertida = inverter(programa)
print("String inserida: ", programa)
print("String invertida: ", string_invertida)