def format_date(string):
    liste_jour_heure = string.split(" ")
    date_liste  = liste_jour_heure[0].split("/")
    liste_ordonnee = date_liste[::-1]
    return liste_ordonnee

def format_date(string):
    liste_jour_heure = string.split(" ")
    jour = liste_jour_heure[0].replace('/','-')
    return jour

def filtre_mesure_minuit(df):
    # Convertir la colonne date_UTC au format datetime
    from pandas import to_datetime
    df['date_UTC'] = to_datetime(df['date_UTC'], format='%Y%m%d%H%M%S', errors='coerce')
    
    # Filtrer les lignes correspondant à minuit (heure, minute et seconde égales à 0)
    df_minuit = df[(df['date_UTC'].dt.hour == 0) & 
                   (df['date_UTC'].dt.minute == 0) & 
                   (df['date_UTC'].dt.second == 0)]
    
    return df_minuit
