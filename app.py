import streamlit as st
from extrair import extrair_usuarios
import json
from datetime import datetime

st.set_page_config(page_title="Quem não me segue de volta?", page_icon="🕵️", layout="centered")

st.title("🕵️ Quem não te segue de volta?")
st.write("Descubra quais contas você segue no Instagram, mas que não te seguem de volta.")

with st.expander("Como baixar seus dados do Instagram em JSON?"):
    st.markdown("""
    1. No Instagram vá em **Configurações e atividade (3 risquinhos)**.
    2. Clique em **Conta Meta** e depois em **Suas informações e permissões**.
    3. Clique em **Exportar suas informações** -> **Criar exportação**.
    4. Selecione seu perfil e escolha **Exportar para dispositivo**.
    5. Em personalizar informações, selecione apenas **"Seguidores e seguindo"**.
    6. Em intervalo de datas, mude para **"Desde o início"**.
    7. Em formato selecione **JSON**.
    9. Então clique em **Iniciar exportação** e aguarde o Instagram gerar o arquivo (pode demorar alguns minutos).
    10. Quando o arquivo estiver pronto, baixe e extraia do arquivo ZIP.
    11. Dentro da pasta extraída, você encontrará os arquivos **`following.json`** e **`followers_1.json`** (se tiver muitos seguidores, pode haver mais arquivos followers) 
    12. Faça o upload de **TODOS** os arquivos followers em seguidores e do following em seguindo.
    """)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Seguidores")
    arquivos_followers = st.file_uploader(
        "Faça upload dos arquivos followers.json", 
        type=['json'], 
        accept_multiple_files=True
    )

with col2:
    st.subheader("2. Seguindo")
    arquivos_following = st.file_uploader(
        "Faça upload do arquivo following.json", 
        type=['json'] 
    )

if arquivos_followers and arquivos_following:
    try:
        dict_followers = {}
        dict_following = {}
        
        for arquivo in arquivos_followers:
            conteudo = arquivo.getvalue()
            dados = json.loads(conteudo)
            novos_usuarios = extrair_usuarios(dados)
            for usuario, tempo in novos_usuarios.items():
                dict_followers[usuario] = max(dict_followers.get(usuario, 0), tempo)
            
        conteudo = arquivos_following.getvalue()
        dados = json.loads(conteudo)
        novos_usuarios = extrair_usuarios(dados)
        for usuario, tempo in novos_usuarios.items():
            dict_following[usuario] = max(dict_following.get(usuario, 0), tempo)
        
        apenas_nomes_nao_seguem = set(dict_following.keys()) - set(dict_followers.keys())
        
        lista_nao_seguem = [(usuario, dict_following[usuario]) for usuario in apenas_nomes_nao_seguem]
        
        lista_nao_seguem.sort(key=lambda x: x[1], reverse=True)
        
        st.divider()
        st.subheader("📊 Resultados")
        
        col_metric1, col_metric2, col_metric3 = st.columns(3)
        col_metric2.metric("Te seguem", len(dict_followers))
        col_metric1.metric("Você segue", len(dict_following))
        col_metric3.metric("Não te seguem de volta", len(lista_nao_seguem))
        
        if len(lista_nao_seguem) > 0:
            st.warning("Algumas contas desativadas podem aparacer como seguindo, mas não aparecem te seguindo.")
            
            lista_formatada = ""
            for usuario, timestamp in lista_nao_seguem:
                data_legivel = "Data desconhecida"
                if timestamp > 0:
                    data_legivel = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y')
                
                lista_formatada += f"- [@{usuario}](https://instagram.com/{usuario}) *(Seguido em: {data_legivel})*\n"
                
            with st.container(height=400):
                st.markdown(lista_formatada)
        else:
            st.success("Todo mundo que você segue te segue de volta!")
            st.balloons()
            
    except Exception as e:
        st.error(f"Erro ao processar os arquivos. Certifique-se de que são os arquivos JSON corretos. Erro técnico: {e}")