from crypto.symmetric_crypto import encrypt_aes
from crypto.asymmetric_crypto import encrypt_key
from crypto.digital_signature import sign_data


def enviar_contrato(contrato, public_key_B, private_key_A):

    encrypted_doc, aes_key, iv = encrypt_aes(contrato)

    encrypted_key = encrypt_key(public_key_B, aes_key)

    assinatura = sign_data(private_key_A, encrypted_doc)

    pacote = {
        "doc": encrypted_doc,
        "key": encrypted_key,
        "iv": iv,
        "signature": assinatura
    }

    return pacote