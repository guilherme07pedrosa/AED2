def contar_substrings(texto, padrao):
    tamanho_texto = len(texto)
    tamanho_padrao = len(padrao)
    
    #  tabela de programação dinâmica para armazenar as contagens parciais
    dp = [[0] * (tamanho_padrao + 1) for _ in range(tamanho_texto + 1)]
    
    #  primeira coluna da tabela com 1 (para contar substrings vazias)
    for i in range(tamanho_texto + 1):
        dp[i][0] = 1
    
    # Preenchimento  da tabela usando programação dinâmica
    for i in range(1, tamanho_texto + 1):
        for j in range(1, tamanho_padrao + 1):
            dp[i][j] = dp[i - 1][j]
            if texto[i - 1] == padrao[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    
    # O valor na última célula da tabela (dp[tamanho_texto][tamanho_padrao]) contém o número de ocorrências
    return dp[tamanho_texto][tamanho_padrao]



#Prorgama principal

n=int(input("\nEntre com o numero de casos de testes: "))
for i in range (n):
    string=str(input("\n Digite o texto: "))
    substring=str(input("\n Digite o padrão"))
    resultado=int(input("\n Digite a quantidade de de vezes que o padrao deve ser encontrado no texto"))
    if contar_substrings(string, substring)==resultado:
        print("\nY")
    
    else :
        print("\nN")
