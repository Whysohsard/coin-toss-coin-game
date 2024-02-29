from flask import Flask, render_template
import random

app = Flask(__name__)

facts_list = ["Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
              "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
              "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."]

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a><br><a href="/yazi_tura">Yazı Tura Oyna!</a>'

@app.route("/rastgele_gercek")
def rastgele_gercek():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/yazi_tura")
def yazi_tura():
    result = "Yazı" if random.choice([True, False]) else "Tura"
    return f'<h2>Yazı Tura Sonucu: {result}</h2>'

app.run(debug=True)
