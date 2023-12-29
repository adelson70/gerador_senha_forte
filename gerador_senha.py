# Bibliotecas
from random import sample
from random import shuffle as embaralhar
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
    senha = ''

    senha += ("".join(sample(letras_min,3)))
    senha += ("".join(sample(letras_mais,3)))
    senha += ("".join(sample(nums,3)))
    senha += ("".join(sample(char_spe,3)))

    senha = list(senha)

    embaralhar(senha)

    str_senha = "".join(senha)

    return str_senha
    
# Função que irá atualizar a label onde irá aparecer a senha
def atualizar_label(label, info):
    label.config(text=info)

    # Configurar evento de clique para permitir seleção e cópia
    label.bind("<Button-1>", lambda event: label.clipboard_clear())
    label.bind("<ButtonRelease-1>", lambda event: label.clipboard_append(info))

# Função que ira chamar a função de gerar a senha e depois de atualizar a label
def gerar(root):
    senha = gerar_senha()
    label = root
    atualizar_label(label,senha)
    
    # Ira copiar a senha para area de transferencia
    label.clipboard_clear()
    label.clipboard_append(senha)

    messagebox.showinfo(f'Senha Copiada',f'A senha {senha} foi copiada para a área de transferência!')

# Função para ajustar a janela principal conforme o conteudo que estiver nela
def ajustar_janela_ao_conteudo(root):
    root.update_idletasks()  # Atualiza a geometria da janela
    largura = root.winfo_reqwidth()  # Largura requisitada pelo conteúdo
    altura = root.winfo_reqheight()  # Altura requisitada pelo conteúdo

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula a posição para centralizar a janela
    x_pos = (largura_tela - largura) // 2
    y_pos = (altura_tela - altura) // 2

    # Define a geometria da janela
    root.geometry(f"{largura+200}x{altura}+{x_pos-50}+{y_pos-120}")


# Janela principal da aplicação
janela = tk.Tk()
janela.title('Gerador de Senha Forte')

# Fontes personalizadas
fonte_titulo = Font(family="Segoe UI", size=15, weight="bold")
fonte_senha = Font(family="Segoe UI", size=23, weight="bold")
fonte_botao = Font(family="Segoe UI", size=14, weight="bold")

# Label do titulo do programa
tk.Label(janela,text='Gerador de Senha Forte!', font=fonte_titulo).pack(pady=10)


# Label onde ficará a senha gerada
label_senha = tk.Label(janela, text='', font=fonte_senha, cursor="arrow")
label_senha.pack(pady=10)

# Botão para chamar a função que gera a senha e atualiza a label
tk.Button(janela, text='Gerar Senha', command=lambda: gerar(label_senha), font=fonte_botao).pack(pady=10)

ajustar_janela_ao_conteudo(janela)
janela.mainloop()