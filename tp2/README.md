Exemplo de utilização da ferramenta de deteção de idioma:
python3 i_predict_languague_now.py dicionario texts/de_lynch_wet.txt

Usar flag -A para o caso de se querer adicionar as palavras do texto ao dicionário quando a match for superior à percentagem dada. Exemplo:
python3 i_predict_languague_now.py dicionario texts/de_lynch_wet.txt -A 75
No caso do match ser superior a 75%, então as palavras do texto de_lynch_wet.txt são adicionadas ao dicionario

Exemplo de utilização da ferramenta de aprendizagem do dicionário:
parserPL < dics.txt
