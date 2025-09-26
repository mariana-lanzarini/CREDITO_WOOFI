from Utils.config import Config
from woofi.woofi_navegacao import woofiNavegacao
print("iniciando o driver")
driver = woofiNavegacao.abrirWoofi()
woofiNavegacao.logarWoofi(driver)
woofiNavegacao.verficarValor(driver)