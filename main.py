
import pandas as pd
from calculos import calcular_zpr

def carregar_dados(arquivo):
    """Carrega a planilha Excel e retorna os dados."""
    try:
        dados = pd.ExcelFile(arquivo)
        return dados
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

def main():
    """Função principal do programa."""
    arquivo = "data.xlsx"  # Nome do arquivo Excel
    dados = carregar_dados(arquivo)
    
    if dados:
        # Carregar a aba principal
        aba_principal = dados.parse("Gerenciamento de risco")
        
        # Definir quantas ZPRs serão utilizadas
        qtd_zpr = int(aba_principal.iloc[5, 1])  # Supondo que o valor esteja na célula correta
        
        # Executar cálculos
        resultados = calcular_zpr(qtd_zpr, dados)
        
        # Exibir resultados (pode ser salvo ou exibido em interface futuramente)
        print("Resultados das ZPRs:", resultados)

if __name__ == "__main__":
    main()
