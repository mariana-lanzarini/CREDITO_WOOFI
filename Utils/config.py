from webdriver_manager.chrome import ChromeDriverManager
import shutil
from dataclasses import dataclass
@dataclass
class Config:
    MODO_DEV : bool = True #False = fase de testes  
    #credenciais
    login_woofi:str = "richard@colbiz.io"
    senha_woofi:str = "TU6e8Sg8"
    url_woofi:str = "https://portal.woo-fi.com/login"


    remetente:str = "svc.rpaextratos@melnick.com.br"
    senha_remetente:str = "%LFcnXqs4R&y9?+L"
    destinatario:str = "mariana@colbiz.io"
    @staticmethod
    def get_chrome_driver_path():
        # Tenta achar no PATH
        path = shutil.which("chromedriver")
        if path:
            return path
        else:
            # Usa webdriver_manager para baixar/gerenciar
            return ChromeDriverManager().install()
        