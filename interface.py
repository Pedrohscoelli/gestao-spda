import tkinter as tk
from tkinter import ttk
import webbrowser

def abrir_link():
    webbrowser.open("http://www.inpe.br/webelat/homepage/")

def atualizar_ks1(*args):
    try:
        w = float(entrada_w.get()) if entrada_w.get() else 0
        ks1 = 0.12 * w
        label_ks1_valor.config(text=f"{ks1:.4f}")
    except ValueError:
        label_ks1_valor.config(text="Erro")

def criar_interface():
    global entrada_w, label_ks1_valor

    root = tk.Tk()
    root.title("Gerenciamento de Risco - SPDA")
    root.geometry("650x800")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Gerenciamento de Risco do SPDA - Memorial de Cálculo", 
              font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(frame, text="Dados do Cliente", font=("Arial", 12, "bold")).grid(row=1, column=0, columnspan=2, pady=5)

    campos_cliente = ["Nome do Cliente:", "Endereço:", "Edificação (tag):"]
    for i, texto in enumerate(campos_cliente, start=2):
        ttk.Label(frame, text=texto).grid(row=i, column=0, sticky=tk.W)
        ttk.Entry(frame, width=40).grid(row=i, column=1, pady=5)

    ttk.Label(frame, text="Características da Estrutura e Meio Ambiente", 
              font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=5)

    label_ng = tk.Label(frame, text="Densidade de Descargas Atmosféricas (Ng) (Acesse aqui):", fg="black", cursor="hand2")
    label_ng.grid(row=6, column=0, sticky=tk.W)
    label_ng.bind("<Button-1>", lambda e: abrir_link())
    ttk.Entry(frame, width=40).grid(row=6, column=1, pady=5)

    campos_dimensoes = ["Comprimento (L):", "Largura (W):", "Altura (H):", "Altura da Proeminência (Hp):"]
    entradas_dimensoes = []
    for i, texto in enumerate(campos_dimensoes, start=7):
        ttk.Label(frame, text=texto).grid(row=i, column=0, sticky=tk.W)
        entrada = ttk.Entry(frame, width=40)
        entrada.grid(row=i, column=1, pady=5)
        entradas_dimensoes.append(entrada)

    entrada_w = entradas_dimensoes[1]  # Campo da largura (W)
    entrada_w.bind("<KeyRelease>", atualizar_ks1)

    tabelas = {
        "Fator de localização da estrutura (Tabela A.1)(Cd):": 
        ["Nenhuma", "Cercada por objetos mais altos", 
            "Cercada por objetos da mesma altura ou mais baixos", "Isolada sem outros objetos próximos", 
            "Isolada no topo de uma colina"],
        "Sistema de Proteção contra Descargas Atmosféricas (Tabela B.2) (Pb):": 
        ["Sem SPDA", "SPDA Classe IV", "SPDA Classe III", 
            "SPDA Classe II", "SPDA Classe I", "SPDA Classe I + estrutura metálica contínua", 
            "Cobertura metálica com proteção completa"],
        "Ligação Equipotencial (Tabela B.7) (Peb):": 
        ["Sem DPS", "Classe III - IV", "Classe II", "Classe I", "NOTA 4"]
    }

    linha = 12
    for label_texto, opcoes in tabelas.items():
        ttk.Label(frame, text=label_texto).grid(row=linha, column=0, sticky="w")
        ttk.Combobox(frame, values=opcoes, state="readonly", width=37).grid(row=linha, column=1, pady=5)
        linha += 1

    # Exibição do resultado Ks1
    ttk.Label(frame, text="Blindagem Espacial Externa (Equacionamento B.5) (Ks1):").grid(row=linha, column=0, sticky=tk.W)
    label_ks1_valor = ttk.Label(frame, text="0.00", font=("Arial", 10, "bold"))
    label_ks1_valor.grid(row=linha, column=1, sticky=tk.W)
    linha += 1

    # Adicionando o título "Linha de Energia ¹" na sequência correta
    ttk.Label(frame, text="Linha de Energia ¹", 
              font=("Arial", 12, "bold")).grid(row=linha, column=0, columnspan=2, pady=10)
    linha += 1



    ttk.Button(frame, text="Continuar", command=lambda: print("...Aguarde...")).grid(row=linha, column=0, columnspan=2, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    criar_interface()
