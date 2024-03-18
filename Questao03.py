import json

def calcular_faturamento(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    menor_valor = min(data["faturamento"])
    maior_valor = max(data["faturamento"])

    
    dias_faturamento = [valor for valor in data["faturamento"] if valor > 0]
    media_mensal = sum(dias_faturamento) / len(dias_faturamento)


    dias_acima_da_media = sum(1 for valor in dias_faturamento if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media


json_file = "Faturamento.json"


menor, maior, dias_acima_media = calcular_faturamento(json_file)


print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)