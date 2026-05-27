import tkinter as tk
from p import Pessoa
from fichas import criar_ficha

usuarios = []
usuario_logado = None


# ---------------- FICHA (NOVA TELA) ----------------

def abrir_ficha(ficha):

    tela_ficha = tk.Toplevel(janela)
    tela_ficha.title("Ficha do Jogador")
    tela_ficha.geometry("800x600")
    tela_ficha.configure(bg="black")

    introducao = """
====================================================

Olá, Jogador! Seja bem vindo ao se jogo de gerenciamento financeiro.
Vamos ver se com sua habilidades de getão monetária, você conseguirá se virar nesse mundo em 1 ano!

====================================================
"""

    tk.Label(
        tela_ficha,
        text=introducao,
        bg="black",
        fg="lime",
        font=("Courier", 10),
        justify="left"
    ).pack(pady=10)

    tk.Label(
        tela_ficha,
        text=f"Jogador: {ficha['nome']}",
        bg="black",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        tela_ficha,
        text=f"Saldo: R$ {ficha['saldo']:.2f}",
        bg="black",
        fg="gold",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        tela_ficha,
        text=f"Inventário: {ficha['inventario']}",
        bg="black",
        fg="cyan"
    ).pack(pady=5)

    tk.Label(
        tela_ficha,
        text=f"Histórico:\n" + "\n".join(ficha["historico"]),
        bg="black",
        fg="white",
        justify="left"
    ).pack(pady=5)


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
    entrada_nome.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)


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

    global usuario_logado

    for p in usuarios:
        if p.nome == nome and p.verificar_senha(senha):

            resultado.config(
                text=f"Bem-vindo, {nome}!",
                fg="green"
            )

            entrada_nome.delete(0, tk.END)
            entrada_senha.delete(0, tk.END)

            usuario_logado = p

            fichas = criar_ficha(usuario_logado)

            abrir_ficha(fichas)  # <<< AQUI abre a nova tela

            return

    resultado.config(
        text="Nome ou senha incorretos!",
        fg="red"
    )
    entrada_nome.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)


# ---------------- JANELA PRINCIPAL ----------------

janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("1980x720")

titulo = tk.Label(janela, text="Sistema de Login", font=("Arial", 16))
titulo.pack(pady=10)

label_nome = tk.Label(janela, text="Nome")
label_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

label_senha = tk.Label(janela, text="Senha")
label_senha.pack()

entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

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

resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

janela.mainloop()