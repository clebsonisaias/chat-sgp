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
    headers = {
        "Authorization": "Bearer 949c987c-a80b-4182-a833-e6ac3818ed30",
        "Content-Type": "application/json"
    }
    payload = {
        "cpfcnpj": cpf_cnpj
    }

    resposta = requests.post(url, json=payload, headers=headers)
    return resposta.json()
