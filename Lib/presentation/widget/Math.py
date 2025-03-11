import streamlit as st 

def Autonomo(level_1,level2,level3,level4,p,n):
    try:
        
        l1 = 3
        l2 = 4
        l3 = 6
        l4 = 7
    
        processor =  6
        net = 4
        
        r_l1 = l1 * level_1
        r_l2 = l2 * level2
        r_l3 = l3 * level3
        r_l4 = l4 * level4
    
        rp = processor * p
        rn = net * n
    
        r = r_l1 + r_l2 + r_l3 + r_l4 + rp + rn
    
        return r
    
    except Exception as e:
        st.error(f"Hubo un error desconocido: {e}")
        st.error("Informar a Mario")
        
def TeleOp(level_1,level2,level3,level4,p,n):
    try:
        
        l1 = 2
        l2 = 3
        l3 = 4
        l4 = 5
    
        processor =  6
        net = 4
        
        r_l1 = l1 * level_1
        r_l2 = l2 * level2
        r_l3 = l3 * level3
        r_l4 = l4 * level4
    
        rp = processor * p
        rn = net * n
    
        r = r_l1 + r_l2 + r_l3 + r_l4 + rp + rn
    
        return r
    
    except Exception as e:
        st.error(f"Hubo un error desconocido: {e}")
        st.error("Informar a Mario")
        
def End_Game():
    try:
        
        s = st.selectbox("¿Donde se estaciona?",["No se estaciono","Intento pero no pudo","BARAGE ZONE","shallow CAGE","deep CAGE"],key='s --end')

        if s == 'No se estaciono':
            s = 0
        elif s == 'Intento pero no pudo':
            s = 2   
        elif s == 'BARAGE ZONE':
            s = 2
        elif s == 'shallow CAGE':
            s = 6
        elif s == 'deep CAGE':
            s = 12
        
        return s
    
    except Exception as e:
        st.error(f"Hubo un error desconocido: {e}")
        st.error("Informar a Mario")

def resu(Autnomo,TeleOp,End_Game):
    try:
        
        r = Autnomo + TeleOp + End_Game
        
        return r
        
    except Exception as e:
        st.error(f"Hubo un error desconocido: {e}")