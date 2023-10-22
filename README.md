# LogicaFuzzy

Este repositório contém um modelo de lógica fuzzy desenvolvido em Python para estimar o nível de obesidade com base nos níveis de atividade física e no consumo de comida. O modelo utiliza a biblioteca scikit-fuzzy para implementar a lógica fuzzy e oferece uma solução intuitiva para a análise do comportamento do sistema.

# Pré-requisitos
- Python 3.x
- Biblioteca numpy
- Biblioteca scikit-fuzzy
- Biblioteca matplotlib

# Executando o Modelo
- Certifique-se de ter Python e as bibliotecas mencionadas instaladas em seu ambiente.
- Execute o arquivo main.py.
- O programa solicitará a entrada do usuário para Atividade Física (0-10) e Consumo de comida (0-10000 Kcal).
- O modelo calculará o nível de obesidade com base nas entradas fornecidas e exibirá o resultado.
# Variáveis de Entrada
- Atividade Física: Varia de 0 (sedentário) a 10 (altamente ativo).
- Consumo de Comida: Varia de 0 a 10000 Kcal.
# Variável de Saída
- Obesidade (Peso): Varia de 0 a 100 KG.
# Funções de Pertinência
## Atividade Física:
- sedentario, moderado e ativo.
## Consumo de Comida:
- pouco, razoavel e bastante.
## Obesidade:
- leve, peso_medio e pesado.
# Regras Fuzzy
- Se a atividade física é sedentário e o consumo de comida é bastante, então a obesidade é pesada.
- Se a atividade física é moderado e o consumo de comida é razoavel, então a obesidade é de peso médio.
- Se a atividade física é ativo e o consumo de comida é pouco, então a obesidade é leve.
