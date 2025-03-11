import streamlit as st

def main():
    try:
            
            
            
        pag = {
            "Eliga una App" : [
                st.Page(page='Lib\presentation\screens\Matches.py',title='Matches',url_path='Matches.py'),
                st.Page(page='Lib\presentation\screens\Pits.py',title='Pits',url_path='Pits.py'),
                st.Page(page='Lib\presentation\screens\Horarios.py',title='Horarios',url_path='Horarios.py'),
            ],
            "Checar registros" : [
                st.Page(page='Lib\presentation\screens\Registro.py',title='Registro',url_path='Registro.py'),
            ]
        }
        
        st.navigation(pages=pag,position="sidebar",expanded=False).run()
            
    except Exception as e:
        st.error(f'Hubo un error desconocido: {e}')
        st.info("Informar a Mario")
        
if __name__ == '__main__':
    main()