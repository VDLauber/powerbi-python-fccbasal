import pandas as pd
from faker import Faker
import random

atividades = {
    "Nenhum",
    "Moderado",
    "Ativo",
    "Atleta"
}

def gerar_dados(n_registros):
    fake = Faker("pt_BR")
    registros = []

    for i in range(n_registros):
        nome = fake.name()
        idade = random.randint(18, 80)
        genero = random.choice(["Masculino", "Feminino"])
        peso = round(random.uniform(50, 100), 1)
        altura = random.randint(150, 200)
        nivel = random.choice(list(atividades))

        dados = {
            "Nome": nome,
            "Idade": idade,
            "Gênero": genero,
            "Peso (kg)": peso,
            "Altura (cm)": altura,
            "Nível de atividade física": nivel
        }

        registros.append(dados)

    df = pd.DataFrame(registros)
    df.to_excel("dados_automatizados.xlsx", index=False)
    print(f"{n_registros} registros gerados e salvos em 'dados_automatizados.xlsx'.")

gerar_dados(200)