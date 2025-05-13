from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Modelo para entrada do JSON
class ClienteRequest(BaseModel):
    cpf_cnpj: str

app = FastAPI()

@app.post("/consultar_cliente")
async def consultar_cliente(dados: ClienteRequest):
    cpf_cnpj = dados.cpf_cnpj

    url = "https://citrn.sgp.net.br/api/ura/consultacliente/"
    payload = {
        "cpfcnpj": cpf_cnpj,
        "token": "97c3f6d7-b9b9-4ca0-8231-ac2c68e1323b",
        "app": "gpt"
    }
    headers = {
        "Content-Type": "application/json"
    }

    resposta = requests.post(url, json=payload, headers=headers)
    return resposta.json()
