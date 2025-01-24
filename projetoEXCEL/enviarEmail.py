import yagmail
import os

def enviarEmail(arquivo):
    sender_email = 'gabbr00203@gmail.com'  # Coloque seu e-mail diretamente
    app_password = 'mzpd alir gmop uzxn'
    receiver_email = 'jgabrielnr31@gmail.com'

    yag = yagmail.SMTP(user=sender_email, password=app_password)

    try:
        yag.send(
            to=receiver_email,
            subject="HORA EXTRA",
            contents="Planilha de horas extras em anexo",
            attachments=arquivo
        )
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")