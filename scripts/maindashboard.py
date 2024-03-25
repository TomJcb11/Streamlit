import streamlit as st 
import psycopg2
import pandas as pd

def color_cells(val):
    if val in ['f', 'oui']:
        color = 'red' 
    elif val in ['v','non']:
        color = 'green'
    else :
        color = 'black'
    return 'color: %s' % color


def Showtable(table):
    st.header(f"Affichage de la table {table}")
    conn = psycopg2.connect(
        host="db",
        dbname="postgres",
        user="postgres",
        password="example",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table};")
    #data est le dataframe qui contient les données de la table c'est sur lui que vont se baser les manipulations suivantes
    data=pd.DataFrame(cur.fetchall(),columns=[desc[0] for desc in cur.description])
    with st.sidebar:
        # Choix de la colonne une seule fois
        selected_column = st.radio("Choisissez une colonne", data.columns)

    # Créez des onglets pour chaque valeur unique dans la colonne sélectionnée
    tabs = st.tabs([str(value) for value in sorted(data[selected_column].unique())])

    for i, tab in enumerate(tabs):
        with tab:
            # Stockez la valeur sélectionnée dans la session_state pour chaque onglet
            st.session_state[f'selected_value_{i}'] = sorted(data[selected_column].unique())[i]

    # Sélectionnez les colonnes à afficher
    stock = st.multiselect("Select columns", data.columns, [data.columns[0], data.columns[1], data.columns[2], data.columns[3]])
    


    # Affichez les données pour la valeur sélectionnée et les colonnes sélectionnées en dehors de la barre latérale
    for i, tab in enumerate(tabs):
        with tab:
            styled_data = data[data[selected_column] == st.session_state[f'selected_value_{i}']][stock].style.map(color_cells)
            # Fonction pour colorer les cellules en fonction d'une condition
            st.dataframe(styled_data)

            









def ShowEachTable():
    """je veux créer un dataframe pour chaque table de la base de données et les afficher dans un onglet différent de l'application streamlit """
    conn = psycopg2.connect(
        host="db",
        dbname="postgres",
        user="postgres",
        password="example",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")

    # Initialisez st.session_state si nécessaire
    if "table_name" not in st.session_state:
        st.session_state.table_name = None

    with st.sidebar:  # afficher un bouton pour chaque table
        st.header("Tables")
        for table in cur.fetchall():
                    if st.button(table[0].capitalize()):
                        # Mettez à jour st.session_state lorsque le bouton est cliqué
                        st.session_state.table_name = table[0]

    # Affichez la table en dehors de la barre latérale si un bouton a été cliqué
    if st.session_state.table_name is not None:
        Showtable(st.session_state.table_name)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    cur.close()
    conn.close()

ShowEachTable()