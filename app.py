from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import certifi

app = Flask(__name__)

def obtener_valor_dolar():
    url = 'https://www.bcv.org.ve/'
    response = requests.get(url, timeout=30, verify=certifi.where())
    valor_redondeado = 'Error al obtener el valor'

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        dolar_element = soup.find(id='dolar')

        if dolar_element:
            valorresultadodolar = dolar_element.get_text(strip=True)
            valorresultadodolar = valorresultadodolar.replace(',', '.')
            valorresultadodolar = ''.join(c for c in valorresultadodolar if c.isdigit() or c == '.')

            try:
                valor = float(valorresultadodolar)
                valor_redondeado = round(valor, 2)
            except ValueError:
                valor_redondeado = 'Error al convertir el valor'
        else:
            valor_redondeado = 'Elemento no encontrado'
    else:
        valor_redondeado = 'Error al obtener la página'

    return valor_redondeado

@app.route('/')
def index():
    valor_dolar = obtener_valor_dolar()
    return render_template('index.html', valor_dolar=valor_dolar)

if __name__ == '__main__':
    app.run(debug=True)
