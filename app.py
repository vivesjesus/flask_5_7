from flask import Flask, render_template, abort, request, redirect,url_for
from flask_bootstrap import Bootstrap
from forms import formcalculadora, UploadPdfForm
from os import listdir, path, remove
from werkzeug.utils import secure_filename

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'




@app.route('/hola/<nombre>')
def saluda(nombre):
    return render_template("template1.html", nombre=nombre)


@app.route('/suma/<num1>/<num2>')
def suma(num1, num2):
    try:
        resultado = int(num1) + int(num2)
    except:
        abort(404)
    return render_template("template2.html", num1=num1, num2=num2,
                        resultado=resultado)


@app.route('/tabla/<numero>')
def tabla(numero):
    try:
        numero = int(numero)
    except:
        abort(404)
    return render_template("template3.html", num=numero)


@app.route('/enlaces')
def enlaces():
    enlaces = [{"url": "http://www.goole.es", "texto": "Google"},
                {"url": "http://www.twitter.com", "texto": "Twitter"},
                {"url": "http://www.facbook.com", "texto": "Facebook"}, ]
    return render_template("template4.html", enlaces=enlaces)


@app.route('/')
@app.route('/final')
def final():
    digimones = [
    {
        "name": "Koromon",
        "img": "https://digimon.shadowsmith.com/img/koromon.jpg",
        "level": "In Training"
    },
    {
        "name": "Tsunomon",
        "img": "https://digimon.shadowsmith.com/img/tsunomon.jpg",
        "level": "In Training"
    },
    {
        "name": "Yokomon",
        "img": "https://digimon.shadowsmith.com/img/yokomon.jpg",
        "level": "In Training"
    },
        {
        "name": "Agumon",
        "img": "https://digimon.shadowsmith.com/img/agumon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Gabumon",
        "img": "https://digimon.shadowsmith.com/img/gabumon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Biyomon",
        "img": "https://digimon.shadowsmith.com/img/biyomon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Tentomon",
        "img": "https://digimon.shadowsmith.com/img/tentomon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Palmon",
        "img": "https://digimon.shadowsmith.com/img/palmon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Gomamon",
        "img": "https://digimon.shadowsmith.com/img/gomamon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Patamon",
        "img": "https://digimon.shadowsmith.com/img/patamon.jpg",
        "level": "Rookie"
    },
    {
        "name": "Kuwagamon",
        "img": "https://digimon.shadowsmith.com/img/kuwagamon.jpg",
        "level": "Champion"
    },
    {
        "name": "Greymon",
        "img": "https://digimon.shadowsmith.com/img/greymon.jpg",
        "level": "Champion"
    }
]
    return render_template("templateFinal.html", digimones=digimones)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404

@app.route("/avion")
def avion ():
    return render_template("avion.html")

@app.route("/calculadora_post", methods=["get","post"])
def calculadora_post():
    form=formcalculadora(request.form)
    if form.validate_on_submit():
        num1=form.num1.data
        num2=form.num2.data
        operador=form.operador.data
        try:
            resultado=eval(str(num1)+operador+str(num2))
        except:
            return render_template("error.html",error="No puedo realizar la operación")

        return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)  
    else:
        return render_template("calculadora_post.html",form=form)       

@app.route("/uploadpdf", methods=["get","post"])
def uploadpdf():
    form=UploadPdfForm()
    msg=None
    if form.validate_on_submit():
        f=form.pdf.data
        filename= secure_filename (f.filename)
        f.save(app.root_path+"/static/pdf/"+ filename)
        msg=f"El fichero {filename} se ha subido existosamente"
        return redirect(url_for('ver_pdfs',msg=msg))
    else:
        return render_template("uploadpdf.html",form=form)       

@app.route("/ver_pdfs")
@app.route("/ver_pdfs/<string:msg>")
def ver_pdfs (msg=None):
    lista=[]
    for file in listdir(app.root_path+"/static/pdf/"):
        lista.append(file)
    
    return render_template("ver_pdfs.html",lista=lista,msg=msg)

#@app.route("/borrar_pdf")
@app.route("/borrar_pdf/<string:pdfBorrar>")
def borrar_pdf(pdfBorrar=None):
    msg=None
    ruta_base= path.dirname(__file__)
    ruta_pdf= path.join (ruta_base, "static/pdf",pdfBorrar)
    if path.exists(ruta_pdf):
        remove(ruta_pdf)
        msg=f"El fichero {pdfBorrar} se ha borrado existosamente"
    
    lista=[]
    for file in listdir(app.root_path+"/static/pdf/"):
        lista.append(file)
    
    return render_template("ver_pdfs.html",lista=lista, msg=msg)

if __name__ == '__main__':
	app.run(debug=True)