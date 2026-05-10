import sqlite3
import os

# Isso descobre a pasta onde o seu projeto está guardado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "clientes.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def update_client_field(cpf, field, new_value):
    allowed_fields = ['nome', 'fatura', 'senha', 'limite', 'bloqueio', 'parcela']
    if field not in allowed_fields:
        return False

    conn = get_db_connection()
    try:
        cursor = conn.execute(f'UPDATE clientes SET {field} = ? WHERE cpf = ?', (new_value, cpf))
        conn.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
        return False
    finally:
        conn.close()

def read_client(cpf):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,)).fetchone()
    conn.close()
    return user

# --- NOVA FUNÇÃO DE DELETAR ---
def delete_client(cpf):
    conn = get_db_connection()
    try:
        cursor = conn.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        return False
    finally:
        conn.close()