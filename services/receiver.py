from crypto.asymmetric_crypto import decrypt_key
from crypto.symmetric_crypto import decrypt_aes
from crypto.digital_signature import verify_signature
from cryptography.exceptions import InvalidSignature
import sys


def receber_contrato(pacote, private_key_B, public_key_A):

    try:
        # Garantia de autenticidade através da assinatura digital RSA com PSS
        verify_signature(public_key_A, pacote["signature"], pacote["doc"])
    except InvalidSignature:
        print("Alerta de possível fraude: a assinatura do documento é inválida!")
        sys.exit(1)

    aes_key = decrypt_key(private_key_B, pacote["key"])

    contrato = decrypt_aes(
        pacote["doc"],
        aes_key,
        pacote["iv"]
    )

    return contrato