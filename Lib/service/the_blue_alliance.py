import requests
import streamlit as st

AUTH_KEY = "C6OI1pNbzua4AYNdBbdGXFxQPdO6UKWO9YvcFtUW8V55D7ozXx23GPNMUWXFkRhY"

def get_teams(event_code):
    try:
        url = f"https://www.thebluealliance.com/api/v3/event/{event_code}/teams/simple"
        headres = {"X-TBA-Auth-Key": AUTH_KEY}
        response = requests.get(url, headers=headres)
        
        if response.status_code == 200:
            return response.json()  
        
        return None
    
    except Exception as e:
        st.error(f'Hubo un error desconocido: {e}')
        st.info("Informar a Mario")
        
    except requests.HTTPError as eh:
        st.error(f'Hubo un error en la petición HTTP: {eh}')
        st.info("Informar a Mario")
    
    except requests.ConnectionError as ec:
        st.error(f'Hubo un error en la conexión: {ec}')
        st.info("Informar a Mario")
    
    except requests.Timeout as et:
        st.error(f'Hubo un error de tiempo de espera: {et}')
        st.info("Informar a Mario")
        
    except requests.RequestException as er:
        st.error(f'Hubo un error en la petición: {er}')
        st.info("Informar a Mario")
    
    except requests.exceptions as ee:
        st.error(f'Hubo un error en la petición: {ee}')
        st.info("Informar a Mario")

def get_schedule(event_code):
    try:
        url = "https://www.thebluealliance.com/api/v3/event/{event_code}/matches/simple"
        headres = {"X-TBA-Auth-Key": AUTH_KEY}
        response = requests.get(url, headers=headres)
        
        if response.status_code == 200:
            return response.json()
        
        return None
    
    except Exception as e:
        st.error(f'Hubo un error desconocido: {e}')
        st.info("Informar a Mario")
        
    except requests.HTTPError as eh:
        st.error(f'Hubo un error en la petición HTTP: {eh}')
        st.info("Informar a Mario")
    
    except requests.ConnectionError as ec:
        st.error(f'Hubo un error en la conexión: {ec}')
        st.info("Informar a Mario")
    
    except requests.Timeout as et:
        st.error(f'Hubo un error de tiempo de espera: {et}')
        st.info("Informar a Mario")
        
    except requests.RequestException as er:
        st.error(f'Hubo un error en la petición: {er}')
        st.info("Informar a Mario")
    
    except requests.exceptions as ee:
        st.error(f'Hubo un error en la petición: {ee}')
        st.info("Informar a Mario")