# Imports
import pandas as pd
import streamlit as st
from io import BytesIO
from pycaret.classification import load_model, predict_model
from sklearn.pipeline import Pipeline
import joblib  # Para carregar o pipeline do sklearn

# Configuração da página
st.set_page_config(page_title='PyCaret', layout="wide",
                   initial_sidebar_state='expanded')

# Função para converter DataFrame para CSV


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# Função para converter o DataFrame para Excel


@st.cache_data
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

# Função principal da aplicação


def main():
    # Título da aplicação
    st.write("## Escorando o modelo gerado no PyCaret ou Scikit-learn")
    st.markdown("---")

    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader(
        "Bank Credit Dataset", type=['csv', 'ftr'])

    # Seletor de modelo
    st.sidebar.write("## Escolha o modelo")
    model_choice = st.sidebar.selectbox("Escolha o modelo que deseja utilizar",
                                        options=["LightGBM (PyCaret)", "Regressão Logística (sklearn)"])

    # Verifica se há conteúdo carregado na aplicação
    if data_file_1 is not None:
        df_credit = pd.read_feather(data_file_1)
        df_credit = df_credit.sample(50000)

        # Se a escolha for LightGBM, use o modelo do PyCaret
        if model_choice == "LightGBM (PyCaret)":
            model_saved = load_model('model_final')  # Arquivo do LightGBM
            predict = predict_model(model_saved, data=df_credit)

        # Se a escolha for Regressão Logística, use o pipeline do sklearn
        elif model_choice == "Regressão Logística (sklearn)":
            # Carregar o pipeline de regressão logística
            # Carregue o pipeline correto
            pipeline = joblib.load('model_regressao_logistica.pkl')

            # Fazendo a previsão com o pipeline (sklearn)
            predict = pipeline.predict(df_credit)  # Use o predict do sklearn

            # Como `predict` retorna um array, converta para DataFrame para facilitar
            predict = pd.DataFrame(predict, columns=['Previsão'])

        # Convertendo para Excel e permitindo o download
        df_xlsx = to_excel(predict)
        st.download_button(label='📥 Download', data=df_xlsx,
                           file_name='predict.xlsx')


# Iniciando a aplicação
if __name__ == '__main__':
    main()
