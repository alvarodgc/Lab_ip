from flask import Flask
from flask import jsonify

app= Flask(
    __name__,
    static_folder="static",
    static_url_path=""
)


@app.get('/')
def inicio():
    return app.send_static_file('index.html')

@app.get("/api/config")
def obtener_configuracion():
    datos = {
        "titulo": "Panel de Periféricos",
        "boton": "Ingresar",
        "enlace": {
            "texto": "Ver datos Json",
            "url": "/api/config"
        },
        "imagen": {
            "src": "/images/logo.png",
            "alt": "Ingenieria de software"
        },
        "menu": ["Inicio", "Formulario", "Ayuda"]
    }
    return jsonify(datos)

if __name__ == "__main__":
    app.run(debug=True)


