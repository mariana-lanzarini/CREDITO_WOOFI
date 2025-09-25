from Utils.config import Config
from woofi.woofi_navegacao import woofiNavegacao
driver = woofiNavegacao.abrirWoofi()
woofiNavegacao.logarWoofi(driver)
woofiNavegacao.verficarValor(driver)