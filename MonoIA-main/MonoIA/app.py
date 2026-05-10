from flask import Flask, request, jsonify
from flask_cors import CORS
import crud 
import re

app = Flask(__name__)
CORS(app)

CONHECIMENTO = {
    "fatura": ["fatura", "pagar", "fechou", "atraso", "total", "boleto", "quanto devo"],
    "limite": ["limite", "gastar", "aumentar", "disponivel", "credito", "teto"],
    "bloqueio": ["bloqueado", "bloqueio", "desbloquear", "funciona", "suspenso"],
    "parcela": ["parcela", "restam", "dividir", "parcelamento"],
    "senha": ["senha", "esqueci", "trocar", "acesso"]
}

def classificar_intencao(texto):
    texto = texto.lower()
    for categoria, palavras in CONHECIMENTO.items():
        if any(palavra in texto for palavra in palavras):
            return categoria
    return None

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    cpf = data.get("cpf")
    user = crud.read_client(cpf)
    if user:
        return jsonify({"status": "ok", "nome": user["nome"]})
    return jsonify({"status": "not_found"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensagem = data.get("message", "").lower()
    cpf_usuario = data.get("cpf", "")
    
    categoria = classificar_intencao(mensagem)
    
    # --- 1. LÓGICA DE DELEÇÃO (CRUD - DELETE) ---
    if "deletar" in mensagem or "excluir" in mensagem:
        return jsonify({"reply": "Você tem certeza que deseja excluir sua conta? Esta ação é permanente. Se sim, digite exatamente: **CONFIRMAR EXCLUSÃO**"})

    if "confirmar exclusão" in mensagem:
        if crud.delete_client(cpf_usuario):
            return jsonify({"reply": "Sua conta foi excluída com sucesso. O MonoIA sentirá sua falta! 🤖"})
        else:
            return jsonify({"reply": "Erro ao processar a exclusão ou conta não encontrada."})

    # --- 2. LÓGICA DE ATUALIZAÇÃO (CRUD - UPDATE) ---
    gatilhos_mudanca = ["mudar", "alterar", "atualizar", "para", "gostaria", "ajustar", "colocar"]
    if any(p in mensagem for p in gatilhos_mudanca):
        match_valor = re.search(r'(\d+(?:[\.,]\d+)?)', mensagem)
        if match_valor and categoria in ['fatura', 'limite']:
            valor_str = match_valor.group(1).replace(',', '.')
            novo_valor = float(valor_str)
            if crud.update_client_field(cpf_usuario, categoria, novo_valor):
                label = "fatura" if categoria == "fatura" else "limite"
                return jsonify({"reply": f"Entendido! Atualizei o valor da sua {label} para R$ {novo_valor:.2f} com sucesso."})

    # --- 3. LÓGICA DE CONSULTA (CRUD - READ) ---
    user_data = crud.read_client(cpf_usuario)
    if not user_data:
        return jsonify({"reply": "Sessão expirada ou conta inexistente. Por favor, faça login novamente."})

    respostas = {
        "fatura": f"Sua fatura atual é de R$ {user_data['fatura']:.2f}. Você pode gerar o boleto no app.",
        "limite": f"Seu limite disponível é de R$ {user_data['limite']:.2f}.",
        "bloqueio": f"Status do cartão: {'Bloqueado' if user_data['bloqueio'] == 'S' else 'Liberado'}.",
        "parcela": f"Você tem um parcelamento de {user_data['parcela']} ativo.",
        "senha": "A senha deve ser alterada no menu 'Segurança' com validação facial."
    }

    if categoria in respostas:
        return jsonify({"reply": respostas[categoria]})

    nome_curto = user_data['nome'].split()[0]
    return jsonify({"reply": f"Olá {nome_curto}! Como posso ajudar com sua fatura ou limite hoje?"})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5000)