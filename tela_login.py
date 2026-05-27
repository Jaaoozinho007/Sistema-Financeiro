import tkinter as tk
from p import Pessoa

usuarios = []

# ---------------- CADASTRO ----------------

def cadastro():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if not nome or not senha:
        resultado.config(
            text="Preencha todos os campos!",
            fg="red"
        )
        return

    for p in usuarios:
        if p.nome == nome:
            resultado.config(
                text="Nome já cadastrado!",
                fg="red"
            )
            return

    novo_usuario = Pessoa(nome, senha)
    usuarios.append(novo_usuario)

    resultado.config(
        text="Usuário cadastrado com sucesso!",
        fg="green"
    )
    entrada_nome.delete(0,tk.END)
    entrada_senha.delete(0,tk.END)

# ---------------- LOGIN ----------------

def login():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if not nome or not senha:
        resultado.config(
            text="Preencha todos os campos!",
            fg="red"
        )
        return

    for p in usuarios:
        if p.nome == nome and p.verificar_senha(senha):
            resultado.config(
                text=f"Bem-vindo, {nome}!",
                fg="green"
            )
            return

    resultado.config(
        text="Nome ou senha incorretos!",
        fg="red"
    )
    entrada_nome.delete(0,tk.END)
    entrada_senha.delete(0,tk.END)


janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("1980x720")

# Título
titulo = tk.Label(janela, text="Sistema de Login", font=("Arial", 16))
titulo.pack(pady=10)

# Nome
label_nome = tk.Label(janela, text="Nome")
label_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

# Senha
label_senha = tk.Label(janela, text="Senha")
label_senha.pack()

entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

# Botões
botao_cadastro = tk.Button(
    janela,
    text="Cadastrar",
    command=cadastro
    
)
botao_cadastro.pack(pady=5)

botao_login = tk.Button(
    janela,
    text="Login",
    command=login
)
botao_login.pack(pady=5)

# Resultado
resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

# Inicia a interface
janela.mainloop()