import streamlit as st
import pandas as pd
import gspread as gs
import io
from oauth2client.service_account import ServiceAccountCredentials as sac
from google.oauth2 import service_account as sa
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload as mibd


#   API_sheets
#   Esta clase se encarga de manejar las peticiones a las hojas de calculo de google
#   id : str : id de la hoja de calculo
#   sheet : str : nombre de la hoja de calculo

class API_sheets:
    def __init__(self, id, sheet):
        self.id = id
        self.sheet = sheet
        self.cred = sac.from_json_keyfile_name(
            filename='Lib\service\google\Token.json',
            scopes=[
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        
    def get (self):
        try:
            
            client = gs.authorize(self.cred)
            
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            data = work.get_all_records()
            df = pd.DataFrame(data)
            
            return df
            
        except ModuleNotFoundError as modulo:
            st.error(f"Hubo un error en los requerimientos : {modulo}")
            st.error(f"Infromar al mario")
            
        except gs.exceptions.APIError as api:
            st.error(f"Hubo un error en el api : {api}")
            st.error(f"Infromar al mario")
            
        except FileNotFoundError as token :
            st.error(f"Token no encontrado o autorizado : {token}")
            st.error(f"Infromar al mario")
            
        except Exception as e :
            st.error(f"Hubo un error desconocido : {e}")
            st.error(f"Infromar al mario")
    
    def get_2 (self):
        try:
            url = f"https://docs.google.com/spreadsheets/d/{self.id}/export?format=csv"
            df = pd.read_csv(url)
            
            return df
        
        except Exception as e :
            st.error(f"Hubo un error desconocido : {e}")
            st.info("Informar al mario")
            
        except ModuleNotFoundError as modulo:
            st.error(f"Hubo un error en los requerimientos : {modulo}")
            st.info(f"Informar al mario")
            
    def push (self, data):
        try:
            
            client = gs.authorize(self.cred)
            work = client.open_by_key(self.id).get_worksheet(self.sheet)
            
            work.insert_rows(data,2)
            
        except ModuleNotFoundError as modulo:
            st.error(f"Hubo un error en los requerimientos : {modulo}")
            st.error(f"Infromar al mario")
            
        except gs.exceptions.APIError as api:
            st.error(f"Hubo un error en el api : {api}")
            st.error(f"Infromar al mario")
            
        except FileNotFoundError as token :
            st.error(f"Token no encontrado o autorizado : {token}")
            st.error(f"Infromar al mario")
            
        except Exception as e :
            st.error(f"Hubo un error desconocido : {e}")
            st.error(f"Infromar al mario")

#   API_drive
#   Esta clase se encarga de manejar las peticiones a Google Drive
#   SCOPES : list : permisos de la API
#   SERVICE_ACCOUNT_FILE : str : archivo de credenciales
#   creds : obj : credenciales
#   drive_service : obj : servicio de drive
class API_drive:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.SERVICE_ACCOUNT_FILE = 'Lib\service\google\Token.json'
        
        self.creds = sa.Credentials.from_service_account_file(
            filename=self.SERVICE_ACCOUNT_FILE,
            scopes=self.SCOPES
        )
        
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        
        
    def upload_file_to_drive(self,file_obj, file_name, folder_id=None):
        try:
            
            file_obj.seek(0)
            media = mibd(
                fd=file_obj,
                mimetype=file_obj.type,
                resumable=True
            )
            body = {"name": file_name}
            
            if folder_id:
                body["parents"] = [folder_id]
                
            file_response = self.drive_service.files().create(
                body=body,
                media_body=media,
                fields="id, webViewLink"
            ).execute()
            
            return file_response.get("webViewLink")
        
        except Exception as e:
            st.error(f"Hubo un error desconocido : {e}")
            st.info(f"Informar a Mario")
            
        except FileNotFoundError as token:
            st.error(f"Token no encontrado o autorizado : {token}")
            st.info(f"Informar a Mario")