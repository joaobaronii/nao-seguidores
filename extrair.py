def extrair_usuarios(dados_json):
    usuarios = {}
    
    def buscar(obj):
        if isinstance(obj, dict):
            if 'string_list_data' in obj and isinstance(obj['string_list_data'], list):
                for item in obj['string_list_data']:
                    usuario = None
                    tempo = item.get('timestamp', 0)
                    
                    if 'value' in item and item['value']:
                        usuario = item['value']
                    elif 'title' in obj and obj['title']:
                        usuario = obj['title']
                    elif 'href' in item:
                        url = item['href']
                        usuario = url.rstrip('/').split('/')[-1]
                        
                    if usuario:
                        if usuario in usuarios:
                            usuarios[usuario] = max(usuarios[usuario], tempo)
                        else:
                            usuarios[usuario] = tempo
            else:
                for valor in obj.values():
                    buscar(valor)
                    
        elif isinstance(obj, list):
            for item in obj:
                buscar(item)
                
    buscar(dados_json)
    return usuarios