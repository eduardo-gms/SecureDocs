from crypto.key_generator import gerar_chaves
from services.sender import enviar_contrato
from services.receiver import receber_contrato

# gerar chaves
gerar_chaves("empresaA")
gerar_chaves("empresaB")

with open("contratos/contrato.txt", "rb") as f:
    contrato = f.read()

pacote = enviar_contrato(contrato)

contrato_recuperado = receber_contrato(pacote)

with open("contratos/contrato_recebido.txt", "wb") as f:
    f.write(contrato_recuperado)

print("Contrato recebido com sucesso")