# Bibliotecas
from random import sample
from tkinter import messagebox
import tkinter as tk
from tkinter.font import Font
import string

# Caracteres que vão compor a senha
letras_minusculas = string.ascii_lowercase
letras_maiuscula = string.ascii_uppercase
numeros = [str(n) for n in range(0,10)]
especiais = ['!','@','#','$','%','&','*']

# Função que ira gerar a senha
def gerar_senha(
        letras_min=letras_minusculas,
        letras_mais=letras_maiuscula,
        nums=numeros,
        char_spe=especiais
):
    senha = []

    senha.append("".join(sample(letras_min,3)))
    senha.append("".join(sample(letras_mais,3)))
    senha.append("".join(sample(nums,2)))
    senha.append("".join(sample(char_spe,2)))

    senha_str = "".join(senha)
    return senha_str

# Função que ira atualizar a label onde ira aparecer a senha
def atualizar_label(label,info):
    label.config(text=info)
    label.update()

# Função que ira chamar a função de gerar a senha e depois de atualizar a label
def gerar(root):
    senha = gerar_senha()

    label = root
    atualizar_label(label,senha)


# Janela principal da aplicação
janela = tk.Tk()
janela.title('Gerador de Senha Forte')

# Label do titulo do programa
tk.Label(janela,text='Gerador de Senha Forte!').pack(pady=10)


# Label onde ficara a senha gerada
label_senha = tk.Label(janela,text='')
label_senha.pack(pady=10)

# Botão para chamar a função que gera a senha e atualiza a label
tk.Button(janela, text='Gerar Senha', command=lambda: gerar(label_senha)).pack(pady=10)

janela.mainloop()