# Quem não te segue de volta no Instagram?

Uma aplicação [web](https://nao-seguidores-instagram.streamlit.app/) interativa feita em **Python** e **Streamlit** que cruza os dados do seu Instagram para revelar exatamente quais perfis você segue, mas que não te seguem de volta. 

## Funcionalidades

- **Suporte a contas grandes:** Permite o upload de múltiplos arquivos de seguidores (`followers_1.json`, `followers_2.json`, etc.), contornando a divisão de arquivos que o Instagram faz para contas com muitos seguidores.
- **Linha do tempo:** Os resultados são exibidos ordenados cronologicamente (dos mais recentes para os mais antigos), mostrando a data exata em que você começou a seguir a pessoa.
- **Geração de Links:** Cria links diretos para o perfil das pessoas que não te seguem, facilitando a visualização e a ação (dar unfollow, se desejar).
- **Processamento local e seguro:** O aplicativo roda localmente na sua máquina. Seus dados do Instagram não são enviados para nenhum banco de dados externo.

## Como obter seus dados do Instagram (JSON)

Para que o aplicativo funcione, você precisa exportar seus dados de conexão diretamente do Instagram no formato **JSON**:

1. Pelo celular ou PC, vá em **Configurações e atividade** (ícone de 3 risquinhos).
2. Clique em **Conta Meta** (ou Centro de Contas) e depois em **Suas informações e permissões**.
3. Clique em **Baixar suas informações** -> **Baixar ou transferir informações**.
4. Selecione seu perfil do Instagram e escolha **Algumas de suas informações**.
5. Na lista, marque apenas a opção **Seguidores e seguindo** e clique em Avançar.
6. **MUITO IMPORTANTE:** Escolha "Baixar no dispositivo" e altere o Formato de HTML para **JSON**.
7. Altere o Intervalo de datas para **Desde o início**.
8. Solicite o download. O Instagram pode levar alguns minutos (ou horas) para preparar o arquivo. Você receberá um e-mail quando estiver pronto.
9. Baixe e extraia o arquivo ZIP fornecido pelo Instagram.
10. Navegue pelas pastas extraídas até encontrar os arquivos `following.json` e `followers_1.json` (pode haver mais de um arquivo de followers).
11. Faça o upload desses arquivos na interface do Streamlit!

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (Interface Web)
- Biblioteca `json` e `datetime` (Nativas do Python)
