import pandas as pd 
import numpy as np 
import streamlit as st


##config pestaña
st.set_page_config(layout='centered',page_title='A team fan page',page_icon=':heart:')

##config columnas
t1, t2 = st.columns([0.3,0.7])
t1.image('casa.jpg')
t2.title('A team headquarters')
t2.markdown('Since 2019 | youre in for a good laugh')

##secciones
steps= st.tabs(['Amapola','Amadeo','Ana','Arturo','Bootcamp activities'])
with steps[0]:
    st.write('Amapola: The newest and happiest member')
    st.image('Amapola.png',width=180)

    data={'Actividades Favoritas': ['Ir al Parque','Morder'],'Tutor Favorito': ['Ana','Arturo']}
    df=pd.DataFrame(data)
    st.dataframe(df)

with steps[1]:
    st.write('Amadeo: The sweetest and cuddliest boy')
    st.image('Amadeo.jpg',width=180)

with steps[2]:

    left, middle, right = st.columns([0.5,0.3,0.3])
    left.button('BioIng')
    middle.button('Travel')
    right.button('English')
    middle.button('French')
    left.button('Work')
   
    if right.button('Ballet', type='primary'):
        st.write('Love/hate story')
        st.image('ballet.png',width=200)

with steps[3]: 
    st.selectbox('Pick an option', ['Musician','Finance Bro', 'Basket and swag' ])  

with steps[4]: 
    camp_df= pd.read_csv('Campanhas.csv',encoding='latin-1',sep=';')
    camp= st.selectbox('Escoge un ID de Campaña', camp_df['ID_Campana'], help= 'Muestra las campañas existentes')
    met_df=pd.read_csv('Metricas.csv',encoding='latin-1',sep=';')

    m1,m2,m3= st.columns([1,1,1])

    id1= met_df[(met_df['ID_Campana']== camp)]
    id2= met_df[(met_df['ID_Campana']== camp)]

    m1.write('Metricas filtradas')
    m1.metric(label='Métrica 1',value=sum(id1['Conversiones']), delta=str(sum(id1['Rebotes']))+' Total de rebotes',delta_color='inverse')
    m2.metric(label='Métrica 2',value=np.mean(id1['Clics']), delta=str(np.mean(id1['Impresiones']))+' Promedios',delta_color='inverse')






