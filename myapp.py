import streamlit as st
import pandas as pd
from PIL import Image

# Load sidebar image
sidebar_image = Image.open("shield.png")  # Replace with your shield image file

# Sidebar with shield image
st.sidebar.image(sidebar_image, caption="Sécurité IoT", use_container_width=True)

# Class Mapping Table (renamed to "Type d'Attaque")
st.sidebar.write("### Type d'Attaque")
class_mapping = {
    0: "ARP_poisioning",
    1: "DDOS_Slowloris",
    2: "DOS_SYN_Hping",
    3: "Metasploit_Brute_Force_SSH",
    4: "NMAP_FIN_SCAN",
    5: "NMAP_OS_DETECTION",
    6: "NMAP_TCP_scan",
    7: "NMAP_UDP_SCAN",
    8: "NMAP_XMAS_TREE_SCAN",
    9: "Normal"
}
class_mapping_df = pd.DataFrame(list(class_mapping.items()), columns=["Code", "Classe"])
st.sidebar.table(class_mapping_df)

# Title and general description
st.title("Système de Détection d'Attaques IoT")
st.write("""
### Bienvenue dans le Système de Détection d'Attaques IoT !
Cet outil prédit le type d'attaque dans un réseau IoT en fonction des caractéristiques du trafic réseau.
Vous pouvez suivre les étapes suivantes pour utiliser cette application :
1. Téléchargez un fichier CSV contenant les features nécessaires.
2. Consultez le type d'attaque dans la barre latérale.
3. Obtenez les prédictions basées sur vos données.
""")

# Section 1: Upload CSV
st.header("📂 Charger votre fichier CSV")
uploaded_file = st.file_uploader("Téléchargez votre fichier CSV avec les features requises", type=["csv"])
if uploaded_file:
    try:
        input_data = pd.read_csv(uploaded_file)
        st.success("✅ Fichier chargé avec succès ! Voici un aperçu des données :")
        st.write(input_data.head())

        # Placeholder for predictions (to be added later)
        st.info("Les prédictions apparaîtront ici une fois que toutes les étapes sont validées.")
    except Exception as e:
        st.error(f"⚠️ Une erreur s'est produite lors du chargement du fichier : {e}")
else:
    st.warning("⚠️ Veuillez télécharger un fichier CSV pour continuer.")

# Footer
st.markdown("---")
st.markdown("Propulsé par **Streamlit** | Conçu pour l'analyse de sécurité IoT")
