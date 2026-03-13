from crypto.key_generator import gerar_chaves
from services.sender import enviar_contrato
from services.receiver import receber_contrato
from cryptography.hazmat.primitives import serialization

# gerar chaves
gerar_chaves("empresaA")
gerar_chaves("empresaB")

def carregar_chave_privada(caminho):
    with open(caminho, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

def carregar_chave_publica(caminho):
    with open(caminho, "rb") as key_file:
        return serialization.load_pem_public_key(
            key_file.read()
        )

# Carregando chaves em memória
private_key_A = carregar_chave_privada("keys/empresaA_private.pem")
public_key_A = carregar_chave_publica("keys/empresaA_public.pem")
private_key_B = carregar_chave_privada("keys/empresaB_private.pem")
public_key_B = carregar_chave_publica("keys/empresaB_public.pem")

with open("contratos/contrato.txt", "rb") as f:
    contrato = f.read()

# Fluxo da criptografia simétrica AES para o documento
# e proteção da chave AES com RSA e OAEP acontecem no envio
pacote = enviar_contrato(contrato, public_key_B, private_key_A)
#pacote["doc"] = pacote["doc"] + b"1" #Simulação de alteração do documento para testar a integridade

# Garantia de autenticidade através da assinatura digital RSA com PSS e decifração
contrato_recuperado = receber_contrato(pacote, private_key_B, public_key_A)

with open("contratos/contrato_recebido.txt", "wb") as f:
    f.write(contrato_recuperado)

if contrato == contrato_recuperado:
    print("Sucesso na integridade: O contrato recuperado é idêntico ao original.")
else:
    print("Falha na integridade: Os contratos são diferentes.")

print("Contrato processado com sucesso.")