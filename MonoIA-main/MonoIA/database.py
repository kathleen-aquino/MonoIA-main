import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('clientes.db')
cursor = conexao.cursor()

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    fatura REAL NOT NULL,
    senha REAL NOT NULL,
    limite REAL NOT NULL,
    bloqueio TEXT NOT NULL,
    parcela TEXT NOT NULL
)
""")

# Inserção dos registros
dados_clientes = [
    ('440.851.123-29', 'Fernanda Gomes', 1200.50, 1234, 5000.00, 'N', '3x'),
    ('491.189.148-77', 'Alice Borges', 800.00, 5678, 3000.00, 'N', '2x'),
    ('113.287.543-82', 'Wanda Monteiro', 950.75, 4321, 4000.00, 'N', '4x'),
    ('546.748.779-37', 'Vitor Hugo Araujo', 1500.00, 8765, 6000.00, 'N', '5x'),
    ('608.750.777-70', 'Beto Cardoso', 700.25, 1111, 2500.00, 'N', '1x'),
    ('792.493.529-71', 'Juliana Reis', 1763.63, 7193, 15.000, 'S', '9X'),
]

cursor.executemany("""
    INSERT INTO clientes (cpf, nome, fatura, senha, limite, bloqueio, parcela)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(cpf) DO NOTHING
""", dados_clientes)


# Salva e fecha o banco
conexao.commit()
conexao.close()

print("Tabela criada e registros inseridos com sucesso!")
