# Navigation Cube/fr
## Introduction

Le **cube de navigation** donne des informations visuelles sur l\'orientation de la caméra dans la [vue 3D](3D_view/fr.md) en cours et peut être utilisé pour la modifier. Par défaut, il est visible et se trouve dans le coin supérieur droit de la vue.

![](images/Navigation_Cube_Example.png )

Le cube de navigation se compose de plusieurs parties :

-   Le [cube principal](#Cube_principal.md)
-   Six [flèches directionnelles](#Fl.C3.A8ches_directionnelles.md).
-   Le [bouton de vue inversée](#Bouton_de_vue_invers.C3.A9e.md). (en haut à droite) {{Version/fr|0.20}}
-   Le [menu du mini-cube](#Menu_du_mini-cube.md) (en bas à droite)
-   Les indicateurs des axes X, Y et Z

Toutes les composantes, à l\'exception des indicateurs d\'axe, peuvent être cliquées.



## Utilisation



### Cube principal 

Le cube principal possède 26 faces : 6 faces principales, 12 faces à bords rectangulaires ({{Version/fr|0.20}}) et 8 faces d\'angle. En cliquant sur l\'une d\'entre elles, la caméra sera réorientée de manière à ce que sa direction soit perpendiculaire à la face sélectionnée.



### Flèches directionnelles 

Il existe six flèches directionnelles : quatre flèches triangulaires et deux flèches courbes. En cliquant sur l\'une des flèches triangulaires, vous ferez pivoter la [vue 3D](3D_view/fr.md) autour d\'une ligne perpendiculaire à la direction de la flèche. Si vous cliquez sur une flèche courbe, la [vue 3D](3D_view/fr.md) tournera autour de la direction de la flèche.



### Bouton de vue inversée 

En cliquant sur le bouton rond dans le coin supérieur droit du cube de navigation, vous ferez pivoter la [vue 3D](3D_view/fr.md) de 180 degrés autour de l\'axe vertical de la vue.



### Menu du mini-cube 

En cliquant sur le petit cube dans le coin inférieur droit du cube de navigation, un menu s\'affiche avec les options suivantes :

-    **<img src="images/Std_OrthographicCamera.svg" width=16px> [Orthographique](Std_OrthographicCamera/fr.md)**: passe à une vue orthographique.

-    **<img src="images/Std_PerspectiveCamera.svg" width=16px> [Perspective](Std_PerspectiveCamera/fr.md)**: permet d\'obtenir une vue en perspective.

-    **<img src="images/Std_ViewIsometric.svg" width=16px> [Isométrique](Std_ViewIsometric/fr.md)**: permet de passer à une vue isométrique.

-    **<img src="images/Std_ViewFitAll.svg" width=16px> [Ajuster le zoom](Std_ViewFitAll/fr.md)**: effectue un zoom et un panoramique de la caméra de façon à ce que tous les objets visibles tiennent dans la vue.

-    **Cube de navigation mobile**: si cette case ({{Version/fr|0.21}}) est cochée, l\'ensemble du cube de navigation peut être déplacé en maintenant le bouton gauche de la souris enfoncé n\'importe où sur le cube principal et en le faisant glisser. Cela permet de déplacer temporairement le cube. Les [paramètres avancés](#Paramètres_avancés.md) OffsetX et OffsetY peuvent être utilisés pour repositionner le cube de façon permanente, voir ci-dessous.



## Personnalisation



### Préférences

Le cube de navigation est contrôlé par plusieurs préférences : **Édition → Préférences... → Affichage → Navigation → Cube de navigation**. Voir [Réglage des préférences](Preferences_Editor/fr#Navigation.md).



### Paramètres avancés 

Certains paramètres avancés du cube de navigation ne peuvent pas être modifiés dans l\'[éditeur de préférences](Preferences_Editor/fr#Navigation.md). Ces paramètres peuvent être définis manuellement dans l\'[éditeur de paramètres](Std_DlgParameter/fr.md).

Pour définir manuellement les couleurs :

1.  Démarrez l\'<img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [éditeur de paramètres](Std_DlgParameter/fr.md).
2.  Dans le panneau de gauche, allez dans **BaseApp → Preferences → NaviCube**.
3.  Cliquez avec le bouton droit de la souris sur le panneau de droite et sélectionnez **Nouvel élément type non signé** dans le menu contextuel.
4.  Saisissez le nom de l\'une de ces couleurs :
    -   
        **BaseColor**
        
        : la couleur de base de tous les éléments, la valeur par défaut est {{Value|3806916544}} (hex : {{Value|e2e8efc0}}). Cette couleur peut également être définie dans l\'[éditeur de préférences](Preferences_Editor/fr#Navigation.md). {{Version/fr|0.21}}

    -   
        **EmphaseColor**
        
        : la couleur des textes et des lignes, la valeur par défaut dépend de la **BaseColor**. Elle est soit noire : {{Value|255}} (hex : {{Value|000000ff}}), soit blanc : {{Value|4294967295}} (hex : {{Value|ffffff}}). {{Version/fr|0.21}}

    -   
        **HiliteColor**
        
        : la couleur utilisée pour mettre en évidence les faces et les boutons, la valeur par défaut est {{Value|2867003391}} (hex : {{Value|aae2ff}}).
5.  La valeur de la couleur doit être saisie sous la forme d\'un nombre entier non signé de 32 bits. Traduit au format hexadécimal, ce nombre entier a la forme {{Value|RRGGBBAA}}. Où {{Value|AA}} représente le canal alpha (une mesure de la transparence) et les trois autres paires de chiffres représentent le rouge, le vert et le bleu. Pour convertir une valeur hexadécimale en un nombre entier non signé, vous pouvez utiliser la [console Python](Python_console/fr.md) en entrant par exemple {{Incode|int("323232ff", 16)}} ou un service en ligne tel que [celui-ci](https://cryptii.com/pipes/integer-encoder).
6.  Vous pouvez définir d\'autres couleurs.
7.  Appuyez sur le bouton **Fermer**.

Le tableau ci-dessous énumère les autres paramètres avancés du cube de navigation qui peuvent être définis de la même manière. Utilisez les informations de la colonne **Type** pour créer un nouvel élément correct à l\'étape 3.

+++++
| Nom         | Description                                                                                                                              | Type     | Défaut  |
+=============+==========================================================================================================================================+==========+=========+
| BorderWidth | La largeur des bords du cube et des bordures autour des boutons en pixels.                                                               | Flottant | 1.1     |
+++++
| ChamferSize | La taille des arêtes et des coins en tant que facteur de la taille du cube. Les valeurs doivent être comprises entre 0.05 et 0.18.       | Flottant | 0.12    |
|             |                                                                                                                                          |          |         |
|             |                                                                                                                           |          |         |
|             | {{Version/fr|0.21}}                                                                                                                      |          |         |
|             |                                                                                                                                       |          |         |
+++++
| FontStretch | La largeur de la police est exprimée en pourcentage de la largeur par défaut. Utilisez 0 ou 100 pour la largeur de police par défaut.    | Entier   | 0       |
+++++
| FontWeight  | Le poids de la police. Des valeurs élevées rendent la police plus gras. L\'effet peut dépendre de la police. La valeur par défaut est 0. | Entier   | 0       |
+++++
| FontZoom    | La taille des étiquettes :                                                                                                               | Flottant | 0.3     |
|             |                                                                                                                                          |          |         |
|             | -                                                                                                                         |          |         |
|             |     {{Value|FontZoom &#61; 1.0}}                                                                                                         |          |         |
|             |                                                                                                                                       |          |         |
|             |     : chaque étiquette doit être aussi grande que possible.                                                                              |          |         |
|             |                                                                                                                                          |          |         |
|             | -                                                                                                                         |          |         |
|             |     {{Value|0.0 < FontZoom < 1.0}}                                                                                                       |          |         |
|             |                                                                                                                                       |          |         |
|             |     : idem mais en limitant la taille maximale de la police.                                                                             |          |         |
|             |                                                                                                                                          |          |         |
|             | -                                                                                                                         |          |         |
|             |     {{Value|FontZoom &#61; 0.0}}                                                                                                         |          |         |
|             |                                                                                                                                       |          |         |
|             |     : idem mais en utilisant la même taille de police pour tout.                                                                         |          |         |
|             |                                                                                                                                          |          |         |
|             | -                                                                                                                         |          |         |
|             |     {{Value|FontZoom < 0.0}}                                                                                                             |          |         |
|             |                                                                                                                                       |          |         |
|             |     : la même taille de police pour tout, mais à échelle réduite.                                                                        |          |         |
|             |                                                                                                                                          |          |         |
|             |                                                                                                                           |          |         |
|             | {{Version/fr|0.21}}                                                                                                                      |          |         |
|             |                                                                                                                                       |          |         |
+++++
| OffsetX     | Le décalage du cube dans la direction des X par rapport à la position de son coin en pixels.                                             | Entier   | 0       |
+++++
| OffsetY     | Le décalage du cube dans la direction des Y par rapport à la position de son coin en pixels.                                             | Entier   | 0       |
+++++
| ShowCS      | Affiche le système de coordonnées (les indicateurs des axes X, Y et Z).                                                                  | Booléen  | Vrai    |
+++++
| TextBottom  | Le texte sur la face inférieure du cube. La valeur par défaut doit être traduite.                                                        | Chaîne   | DESSOUS |
+++++
| TextFront   | Le texte de la face avant du cube. Idem.                                                                                                 | Chaîne   | DEVANT  |
+++++
| TextLeft    | Le texte de la face gauche du cube. Idem.                                                                                                | Chaîne   | GAUCHE  |
+++++
| TextRear    | Le texte de la face arrière du cube. Idem.                                                                                               | Chaîne   | ARRIÈRE |
+++++
| TextRight   | Le texte de la face droite du cube. Idem.                                                                                                | Chaîne   | DROITE  |
+++++
| TextTop     | Le texte de la face supérieure du cube. Idem                                                                                             | Chaîne   | DESSUS  |
+++++



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/fr
