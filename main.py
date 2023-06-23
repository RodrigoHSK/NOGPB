from flask import Flask, render_template, request, redirect
import datetime
import io
import pandas as pd

app = Flask(__name__)

data_path = "data/dados.txt"
servidores = ["Rodrigo Henrique Schernovski", "Leonardo da Silva Valenga"]
diligencias = ["Intimação", "Intimação pessoal", "Fiscalização de IAT", "Velada"]
niveis = range(1,6)

#header = ["servidor", "diligencia", "nivel", "SEI", "IPL", "data"]

@app.route('/')
def index():
    df = pd.read_csv(data_path, sep = ',',header = 0, index_col=0)
    entradas = list(df.to_numpy())
    return render_template("index.html", servidores = servidores, diligencias = diligencias, niveis = niveis, entradas = entradas)


@app.route('/update-file/', methods=['POST'])
def test():
    data_path = "data/dados.txt"
    if request.method == 'POST':
        df = pd.read_csv(data_path, sep = ',',header = 0, index_col=0)
        data = dict()
        data['servidor'] = request.form.get('servidor')
        data['diligencia'] = request.form.get('diligencia')
        data['nivel'] = request.form.get('nivel')
        data["SEI"] = request.form.get('SEI')
        data["IPL"] = request.form.get('IPL')
        data["data"] = datetime.datetime.today().strftime('%d/%m/%Y')
        serie = pd.Series(data)
        df = df._append(serie, ignore_index = True)
        df.to_csv(data_path, sep = ',', encoding='utf-8')

    return redirect("/")

# @app.route("/forward/", methods=['GET', 'POST'])
# def move_forward():
#     #Moving forward code
#     entradas = list()
#     data = dict()
#     data['servidor'] = "Rodrigo Henrique Schernovski"
#     data['diligencias'] = 10
#     data['creditos'] = 40
#     data['diligenciasT'] = 20
#     data['creditosT'] = 280
#     data["data"] = "21/06/2023"
#     entradas.append(data)

#     data = dict()
#     data['servidor'] = "Leonardo da Silva Valenga"
#     data['diligencias'] = 9
#     data['creditos'] = 50
#     data['diligenciasT'] = 25
#     data['creditosT'] = 300
#     data["data"] = "21/06/2023"

#     entradas.append(data)
    

#     return render_template('base.html', entradas = entradas)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
