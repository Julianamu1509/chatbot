from flask import Flask, request

# ⚠️ 1. CONFIGURACIÓN IMPORTANTE ⚠️
VERIFY_TOKEN = "JulianaMu" 
PUERTO_FLASK = 5000 

app = Flask(__name__)

# --- RUTA DE VERIFICACIÓN (GET) ---
# Meta usa esta ruta para verificar que el puerto esté abierto
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("Webhook verificado y puerto abierto ✅")
        return challenge, 200
    else:
        print("Token de verificación incorrecto ❌")
        return "Token de verificación incorrecto", 403

# --- RUTA DE RECEPCIÓN (POST) ---
# Meta usa esta ruta para enviar mensajes (lo probaremos después)
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("¡Conexión POST exitosa! El puerto está abierto.")
    # NO procesa ni responde, solo confirma que llegó
    return "OK", 200 

# --- INICIO DEL SERVIDOR ---
if __name__ == "__main__":
    print(f"Iniciando servidor en puerto {PUERTO_FLASK}...")
    app.run(host="0.0.0.0", port=PUERTO_FLASK, debug=True)