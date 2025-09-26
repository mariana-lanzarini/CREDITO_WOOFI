import smtplib
from Utils.config import Config
from email.message import EmailMessage

class email:
    @staticmethod
    def enviarEmail(valor):
        """envia email se o valor do site for menor ou igual a 150"""
        try:
            remetente = Config.remetente
            destinatario = Config.destinatario
            senha = Config.senha_remetente
            assunto = """Aviso da conta Woo-fi"""
            corpo_email = f"""
            <html>
                <body>
                    <h1> AVISO </h1>
                    <p>Seu saldo na conta da Woo-fi é ${valor}, que está abaixo ou igual a $150
                    </p>
                </body>
            </html>
            """
            msg = EmailMessage()
            msg['From'] = remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto
            msg.set_content("Seu saldo está abaixo de $150.")
            msg.add_alternative(corpo_email, subtype='html')

            # Envia o e-mail
            with smtplib.SMTP('smtp.office365.com', 587) as smtp:
                smtp.starttls()
                smtp.login(remetente, senha)
                smtp.send_message(msg)
            print("email enviado com sucesso")
        except Exception as e:
            print("erro ao enviar o email")
            print(e)