import requests

r = requests.get("https://s3.amazonaws.com/dolartoday/data.json")
valores = r.json()
valores_dolar = valores["USD"]
tasa_dolar = valores_dolar["sicad2"]


tipo_tasa_usd = input(
    "Seleccione el numero del tipo de tasa que desea aplicar:\n\
    1)Dolar today.\n\
    2)Sicad 1.\n\
    3)Sicad 2.\n\
    4)Bitcoin\n "
)

if tipo_tasa_usd == "2":
    tasa_dolar = valores_dolar["sicad1"]  # valor tasa de compra USD bdv

elif tipo_tasa_usd == "3":
    tasa_dolar = valores_dolar["sicad2"]  # valor tasa de venta USD bdv

elif tipo_tasa_usd == "4":
    tasa_dolar = valores_dolar["bitcoin_ref"]  # valor tasa de localbitcoin

elif tipo_tasa_usd == "1":
    tasa_dolar = valores_dolar["dolartoday"]



def conv_usd_to_bs(total_usd, tasa):
    total_bs = total_usd * tasa
    return total_bs




print(conv_usd_to_bs(1, tasa_dolar), "BsS")

##Lista de valores y nombres. Todos los valores de esta lista
##son de referencia y estan desactuailzados
##{
##
##    "_timestamp": {
##        "epoch": "1614646817",
##        "fecha": "Marzo 1, 2021 09:00 PM",
##        "fecha_corta": "Mar 1, 2021",
##        "fecha_corta2": "Mar 2021",
##        "fecha_nice": "Marzo 1, 2021",
##        "dia": "Lunes",
##        "dia_corta": "Lun"
##    },
##    "USD": {
##        "transferencia": 1873893.89,
##        "transfer_cucuta": 1873893.89,
##        "efectivo": 87750.00,
##        "efectivo_real": 87750.00,
##        "efectivo_cucuta": 87750.00,
##        "promedio": 1873893.89,
##        "promedio_real": 1865613.89,
##        "cencoex": 105467725.72,
##        "sicad1": 1719961.05,
##        "sicad2": 1865613.89,
##        "bitcoin_ref": 1719961.05,
##        "localbitcoin_ref": 1719961.05,
##        "dolartoday": 1873893.89
##    },
##    "EUR": {
##        "transferencia": 2042544.34,
##        "transfer_cucuta": 2042544.34,
##        "efectivo": 95647.50,
##        "efectivo_real": 95647.50,
##        "efectivo_cucuta": 95647.50,
##        "promedio": 2042544.34,
##        "promedio_real": 2033519.14,
##        "cencoex": 114959821.03,
##        "sicad1": 1874757.54,
##        "sicad2": 2033519.14,
##        "dolartoday": 2042544.34
##    },
##    "COL": {
##        "efectivo": 0.0400,
##        "transfer": 0.0400,
##        "compra": 0.0400,
##        "venta": 0.04
##    },
##    "GOLD": {
##        "rate": 1400
##    },
##    "USDVEF": {
##        "rate": 1
##    },
##    "USDCOL": {
##        "setfxsell": 3510.00,
##        "setfxbuy": 3030.00,
##        "rate": 4080.00,
##        "ratecash": 3196.00,
##        "ratetrm": 3510.00,
##        "trmfactor": 0.2,
##        "trmfactorcash": 0.06
##    },
##    "EURUSD": {
##        "rate": 1.09
##    },
##    "BCV": {
##        "fecha": "1522123200",
##        "fecha_nice": "Marzo 27, 2018",
##        "liquidez": "328.319.818.517",
##        "reservas": "9.444.000"
##    },
##    "MISC": {
##        "petroleo": "57,83",
##        "reservas": "9,4"
##    }
# }
