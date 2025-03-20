# Módulo 38 - Credit Scoring para Cartão de Crédito

[Projeto04_streamlit.mov.webm.webm](https://github.com/user-attachments/assets/6e306288-2402-47ac-a09b-e0d12b19571b)

Este projeto tem como objetivo desenvolver um modelo de credit scoring para avaliar o risco na concessão de cartões de crédito. Para isso, utilizamos a biblioteca PyCaret para automatizar o fluxo de machine learning, implementando o algoritmo LightGBM para criar um pipeline robusto e eficiente.

## Fluxo de Trabalho

1. **Carregamento dos dados**: O pipeline recebe um arquivo de dados no formato `.ftr` contendo as informações dos clientes.
2. **Processamento e Previsão**: O modelo realiza as previsões de risco de crédito.
3. **Geração de Resultados**: Após o processamento, um arquivo **Excel** é gerado com duas colunas adicionais:
   - `prediction_label`: Previsão binária (0 para baixo risco, 1 para alto risco).
   - `prediction_score`: Probabilidade associada à previsão, expressando a confiança da previsão.
