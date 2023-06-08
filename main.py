import pandas as pd
from helpers.crearTabla import crearTabla

tablaArboles = pd.read_csv("./data/Siembras.csv")

yarumal = tablaArboles.query('Ciudad=="Yarumal"')
santaFe = tablaArboles.query('Ciudad=="Santa Fe de Antioquia"')
caucasia = tablaArboles.query('Ciudad=="Caucasia"')
belmira = tablaArboles.query('Ciudad=="Belmira"')
bello = tablaArboles.query('Ciudad=="Bello"')
caramanta = tablaArboles.query('Ciudad=="Caramanta"')

yarumalFiltro = tablaArboles.query('Ciudad=="Yarumal" and Vereda=="Mallarino"')
santaFeFiltro = tablaArboles.query('Ciudad=="Santa Fe de Antioquia" and Arboles>250')
belmiraFiltro = tablaArboles.query('Ciudad=="Belmira" and Vereda=="Rio Arriba" or Vereda=="La Salazar"')
belloFiltro = tablaArboles.query('Ciudad=="Bello" and Vereda=="Quitasol"')
caramantaFiltro = tablaArboles.query('Ciudad=="Caramanta" and Arboles>100')

#crearTabla(yarumal, "Yarumal")
#crearTabla(santaFe, "Santa Fe de Antioquia")
#crearTabla(caucasia, "Caucasia")
#crearTabla(belmira, "Belmira")
#crearTabla(bello, "Bello")
#crearTabla(caramanta, "Caramanta")

#crearTabla(yarumalFiltro, "YarumalFiltro")
#crearTabla(santaFeFiltro, "SantaFedeAntioquiaFiltro")
#crearTabla(belmiraFiltro, "BelmiraFiltro")
#crearTabla(belloFiltro, "BelloFiltro")
#crearTabla(caramantaFiltro, "CaramantaFiltro")