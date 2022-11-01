from tkinter.tix import DisplayStyle
import requests
import json
import pandas as pd
import schedule
import time
from datetime import datetime

def resultado_eleicoes():
    dataPresidents = requests.get(
        "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"
    )
    json_dataPresidents = json.loads(dataPresidents.content)

    canditado = []
    partido = []
    votos = []
    porcentagem = []

    for informacoes in json_dataPresidents["cand"]:
        if (
            informacoes["seq"] in['1', '2', '3', '4']
        ):
            canditado.append(informacoes["nm"])
            votos.append(informacoes["vap"])
            porcentagem.append(informacoes["pvap"])

    df_eleicaoPresidents = pd.DataFrame(
        list(
            zip(
                canditado,
                votos,
                porcentagem,
            )
        ),
        columns=["Canditado", "N° de Votos", "porcentagem"],
    )

    dataGorvernators = requests.get(
        "https://resultados.tse.jus.br/oficial/ele2022/547/dados-simplificados/pe/pe-c0003-e000547-r.json"
    )
    json_dataGorvernators = json.loads(dataGorvernators.content)

    canditado = []
    partido = []
    votos = []
    porcentagem = []

    for informacoes in json_dataGorvernators["cand"]:
        if (
            informacoes["seq"] in['1', '2', '3', '4']
        ):
            canditado.append(informacoes["nm"])
            votos.append(informacoes["vap"])
            porcentagem.append(informacoes["pvap"])

    df_eleicaoGovernator = pd.DataFrame(
        list(
            zip(
                canditado,
                votos,
                porcentagem,
            )
        ),
        columns=["Canditado", "N° de Votos", "porcentagem"],
    )
    print()
    print(f'===== TOTAL DE URNAS APURADAS: {json_dataGorvernators["psi"]}% =====')
    print()
    print('=============== APURAÇÃO PRESIDENCIAL ================')
    print()
    print(df_eleicaoPresidents)
    print()
    print('============== APURAÇÃO GOVERNO DE PE ===============')
    print()
    print(df_eleicaoGovernator)
    print()
    print()

resultado_eleicoes()
schedule.every(10).seconds.do(resultado_eleicoes)

while True:
    schedule.run_pending()
    time.sleep(1)