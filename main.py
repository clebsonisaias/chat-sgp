from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/consultar_cliente")
async def consultar_cliente(request: Request):
    dados = await request.json()
    cpf_cnpj = dados.get("cpf_cnpj")

    url = "https://citrn.sgp.net.br/api/ura/consultacliente/"
    headers = {
        "Authorization": "Bearer 949c987c-a80b-4182-a833-e6ac3818ed30",
        "Content-Type": "application/json"
    }
    payload = {
        "cpfcnpj": cpf_cnpj
    }

    resposta = requests.post(url, json=payload, headers=headers)
    return resposta.json()
