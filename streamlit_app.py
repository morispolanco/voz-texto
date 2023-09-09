import streamlit as st
import whisper

st.sidebar.title('Transcriptor de Voz a Texto')
api_key = st.sidebar.text_input('Ingrese su API Key de OpenAI')

if api_key:
    model = whisper.load_model('base')

    st.title('Transcriptor de Voz a Texto')

    if st.button('Escuchar'):
        with st.spinner('Escuchando...'):
            audio = whisper.record(microphone=True)
            transcription = model.transcribe(audio, api_key=api_key)['text']
        
        st.write(transcription)
else:
    st.warning('Por favor ingrese su API Key de OpenAI')
