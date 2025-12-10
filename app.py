from flask import Flask, request
import os # Importamos el módulo OS para leer variables de entorno

# 1. CONFIGURACIÓN 
VERIFY_TOKEN = "JulianaMu" 

app = Flask(__name__)

# --- RUTA DE VERIFICACIÓN (GET) ---
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
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    
    # LOG DE DEPURACIÓN: Imprime los datos que Meta te está enviando
    print("DATOS RECIBIDOS:", data)
    
    print("¡Conexión POST exitosa! El puerto está abierto.")
    return "OK", 200 

# --- INICIO DEL SERVIDOR ---
if __name__ == "__main__":
    # La variable 'PORT' se lee del entorno (será 10000 en Render)
    # Si no está definida (si lo corres localmente), usa 5000 por defecto
    port = int(os.environ.get("PORT", 5000)) 
    
    print(f"Iniciando servidor en puerto {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)