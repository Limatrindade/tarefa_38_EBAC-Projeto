# Módulo 38 - Projeto 04 -  Credit Scoring para Cartão de Crédito

[Projeto04_streamlit.mov.webm.webm](https://github.com/user-attachments/assets/6e306288-2402-47ac-a09b-e0d12b19571b)

Este projeto tem como objetivo desenvolver um modelo de **credit scoring** para avaliação de risco na concessão de cartões de crédito. Utilizamos a biblioteca **PyCaret** para automatizar o processo de machine learning, empregando o algoritmo **LightGBM** para gerar um pipeline eficiente.

## Fluxo de Trabalho

1. **Carregamento dos dados**: O pipeline recebe um arquivo de dados no formato `.ftr` contendo as informações dos clientes.
2. **Processamento e Previsão**: O modelo realiza as previsões de risco de crédito.
3. **Geração de Resultados**: Após o processamento, um arquivo **Excel** é gerado com duas colunas adicionais:
   - `prediction_label`: Previsão binária (0 para baixo risco, 1 para alto risco).
   - `prediction_score`: Probabilidade associada à previsão, expressando a confiança da previsão.

## Conteúdo

- `Mod38 - Projeto 04.ipynb`: Notebook com o código principal e explicações do processo de construção do modelo.
- ``app_pycaret.py``: Este arquivo contém o código para criar o aplicativo Streamlit com o deploy do projeto.
- `model_final.pkl`: Pipeline do modelo LightGBM treinado gerado pelo Pycaret.
- `model_regressao_logistica.pkl`: Pipeline do modelo de regressão logística treinado gerado pela biblioteca Joblib.
- ``sklearn.pipeline.pkl``: Pipeline do modelo de regressão logística treinado gerado pela biblioteca Pickle.
- `logs.log`: Arquivo de log com registros das etapas de execução do pipeline.
- `credit_scoring.zip`: Arquivo compactado contendo a base de dados original.
- `sample_credit_scoring.ftr`: Base de dados reduzida, contendo 100.000 registros utilizados para simulações.
- `requirements.txt`: Arquivo de texto contendo todas as bibliotecas que o projeto necessita para funcionar corretamente.
- `Projeto04_streamlit.mov.webm.webm`: Este vídeo apresenta o deploy criado com o aplicativo Streamlit.

Este repositório foi criado como parte do projeto 04 realizado no Módulo 38, com o objetivo de consolidar o aprendizado e fornecer um recurso para referência futura.

## Referências

Para mais informações sobre como utilizar as ferramentas e técnicas abordadas neste módulo, consulte a documentação oficial das seguintes bibliotecas:

- [Pandas](https://pandas.pydata.org/docs/)
- [Warnings](https://docs.python.org/3/library/warnings.html)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Pycaret](https://pycaret.gitbook.io/docs)
- [Streamlit](https://docs.streamlit.io/)
- [io](https://docs.python.org/3/library/io.html)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Joblib](https://joblib.readthedocs.io/en/stable/)
