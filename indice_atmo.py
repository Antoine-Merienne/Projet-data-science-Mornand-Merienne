def atmo(mesure_polluants):

    '''
    Cette fonction calcule l'indice Atmo associé à la mesure de polluants.\n
    L'argument "mesure_polluants est une liste comprenant 5 valeurs mesures de polluants suivants :\n
    Abbréviation | Nom | Standard\n
    PM2.5 |Particules fines < 2.5 microns | Moyenne journalière\n
    PM10 |Particules fines < 10 microns| Moyenne journalière\n
    NO2 | Dioxyde d'azote | Maximum horaire journalier\n
    O3 | Ozone | Maximum horaire journalier\n
    SO2 | Dioxyde de soufre | Maximum horaire journalier\n

    Remarque : l'argument d'entrée doit correspondre dans l'odre aux mesures des polluants susmentionnés
    '''

    valeurs_intermediaires = [0,0,0,0,0]

    #Tableau de référence issue de la législation des bornes supéreures de chaque catégorie de qualité de l'aire
    #Pour plus d'information consulter https://www.atmo-france.org/sites/federation/files/medias/documents/2022-04/guide_calcul_nouvel_indice_ATMO_VF_version14decembre2020.pdf
    tableau_ref = [
        [10,20,25,50,75],
        [20,40,50,100,150],
        [20,90,120,230,340],
        [50,100,130,240,380],
        [100,200,350,500,750]
    ]
    
    #On assigne à chaque mesure de qualité de l'air une valeur entre 0 et 4 en fonction de la catégorie associée
    for i in range(len(mesure_polluants)):
        if mesure_polluants[i] > tableau_ref[i][4] :
            valeurs_intermediaires[i] = 5
        else:
            for j in range(4):
                if tableau_ref[i][j] <= mesure_polluants[i] <= tableau_ref[i][j+1] :
                    valeurs_intermediaires[i] = j

    #On ne garde que le maximum des valeurs calculées
    match max(valeurs_intermediaires) :
        case 0 :
            valeur_indice = "bon"

        case 1 :
            valeur_indice = "moyen"

        case 2 :
            valeur_indice = "dégradé"

        case 3 :
            valeur_indice = "mauvais"

        case 4 :
            valeur_indice = "très mauvais"

        case 5 :
            valeur_indice = "extrêmement mauvais"
        
        case _:
            valeur_indice = "indéterminé"
    
    return valeur_indice

def iqa(mesure_polluants_iqa):
    
    '''
    Cette fonction calcule l'indice IQA associé à la mesure de polluants.\n
    L'argument "mesure_polluants_iqa est une liste comprenant 5 valeurs mesures de polluants suivants :\n
    Abbréviation | Nom | Standard\n
    O3 | Ozone | Moyenne horaire journalière\n
    PM2.5 |Particules fines < 2.5 microns | Moyenne horaire heures\n
    SO2 | Dioxyde de soufre | Maximum horaire journalier\n
    NO2 | Dioxyde d'azote | Moyenne horaire journalier\n
    CO |Monoxyde de carbone | Moyenne horaire journalière\n

    Remarque : l'argument d'entrée doit correspondre dans l'odre aux mesures des polluants susmentionnés
    '''

    valeurs_ref = [82,35,200,213,30]
    valeurs_indice = [50*mesure_polluants_iqa[i]/valeurs_ref[i] for i in range(5)]

    return max(valeurs_indice)