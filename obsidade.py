import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Variáveis de Entrada (Antecedent)
atividade_fisica = ctrl.Antecedent(np.arange(0, 11, 1), 'atividade_fisica')
consumo_comida = ctrl.Antecedent(np.arange(0, 10001, 1), 'consumo_comida')  # Variação de 0 a 10000 Kcal

# Variável de Saída (Consequent)
obesidade = ctrl.Consequent(np.arange(0, 101, 1), 'peso')  # Variação de 0 a 100 KG

# Funções de Pertinência para atividade_fisica
atividade_fisica['sedentario'] = fuzz.trimf(atividade_fisica.universe, [0, 0, 5])
atividade_fisica['moderado'] = fuzz.trimf(atividade_fisica.universe, [0, 5, 10])
atividade_fisica['ativo'] = fuzz.trimf(atividade_fisica.universe, [5, 10, 10])

# Funções de Pertinência para consumo_comida
consumo_comida['pouco'] = fuzz.trimf(consumo_comida.universe, [0, 0, 3000])  # Variação de 0 a 3000 Kcal
consumo_comida['razoavel'] = fuzz.trimf(consumo_comida.universe, [1500, 3000, 4500])  # Variação de 1500 a 4500 Kcal
consumo_comida['bastante'] = fuzz.trimf(consumo_comida.universe, [3000, 6000, 10000])  # Variação de 3000 a 10000 Kcal

# Funções de Pertinência para obesidade
obesidade['leve'] = fuzz.trimf(obesidade.universe, [0, 0, 50])
obesidade['peso_medio'] = fuzz.trimf(obesidade.universe, [0, 50, 100])
obesidade['pesado'] = fuzz.trimf(obesidade.universe, [50, 100, 100])

# Visualizando as variáveis
atividade_fisica.view()
consumo_comida.view()
obesidade.view()

# Criando as regras
regra_1 = ctrl.Rule(atividade_fisica['sedentario'] & consumo_comida['bastante'], obesidade['pesado'])
regra_2 = ctrl.Rule(atividade_fisica['moderado'] & consumo_comida['razoavel'], obesidade['peso_medio'])
regra_3 = ctrl.Rule(atividade_fisica['ativo'] & consumo_comida['pouco'], obesidade['leve'])

# Controlador
controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])
sistema = ctrl.ControlSystemSimulation(controlador)

# Simulando
atividade = int(input('Atividade Física (0-10): '))
consumo = int(input('Consumo de comida (0-10000 Kcal): '))

sistema.input['atividade_fisica'] = atividade
sistema.input['consumo_comida'] = consumo

sistema.compute()

valorObesidade = sistema.output['peso']

print("\nAtividade Física: %d\nConsumo de comida: %d Kcal\nNível de Obesidade: %5.2f KG" % (
    atividade, consumo, valorObesidade))

atividade_fisica.view(sim=sistema)
consumo_comida.view(sim=sistema)
obesidade.view(sim=sistema)

plt.show()
