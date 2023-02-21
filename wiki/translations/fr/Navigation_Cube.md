# Navigation Cube/fr
{{TOCright}}

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

-    **[Orthographique](Std_OrthographicCamera/fr.md)**: passe à une vue orthographique.

-    **[Perspective](Std_PerspectiveCamera/fr.md)**: permet d\'obtenir une vue en perspective.

-    **[Isometrique](Std_ViewIsometric/fr.md)**: permet de passer à une vue isométrique.

-    **[Ajuster le zoom](Std_ViewFitAll/fr.md)**: effectue un zoom et un panoramique de la caméra de façon à ce que tous les objets visibles tiennent dans la vue.



## Personnalisation



### Déplacement du cube de navigation 

L\'ensemble du cube de navigation peut être déplacé en appuyant sur la souris n\'importe où sur le cube principal et en la faisant glisser. La structure ne commencera à se déplacer que lorsque le curseur aura dépassé l\'un des bords du cube principal.



### Préférences

Le cube de navigation est contrôlé par plusieurs préférences : **Édition → Préférences... → Affichage → Navigation → Cube de navigation**. Voir [Réglage des préférences](Preferences_Editor/fr#Navigation.md).



### Paramètres avancés 

Certains paramètres avancés du cube de navigation ne peuvent pas être modifiés dans l\'[éditeur de préférences](Preferences_Editor/fr#Navigation.md). Ces paramètres peuvent être définis manuellement dans l\'[éditeur de paramàtres](Std_DlgParameter/fr.md) ou via l\'[atelier externe CubeMenu](Interface_Customization/fr#Menu_Cube.md). Les modifications seront visibles lorsqu\'une nouvelle vue 3D sera créée (avec [Std Nouveau](Std_New/fr.md), [Std Ouvrir](Std_Open/fr.md) ou [Std Créer une nouvelle vue](Std_ViewCreate/fr.md)).

Pour définir manuellement les couleurs :

1.  Démarrez l\'<img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> l\'[éditeur de paramàtres](Std_DlgParameter/fr.md).
2.  Dans le panneau de gauche, allez dans **BaseApp → Preferences → NaviCube**.
3.  Cliquez avec le bouton droit de la souris sur le panneau de droite et sélectionnez **New unsigned item** dans le menu contextuel.
4.  Saisissez le nom de l\'une de ces couleurs :
    -   
        **BorderColor**
        
        : les lignes séparant les faces du cube, la valeur par défaut est {{Value|4281479730}} (hex: {{Value|ff323232}}).

    -   
        **ButtonColor**
        
        : tous les éléments autour du cube, la valeur par défaut est {{Value|2162354671}} (hex: {{Value|80e2e9ef}}).

    -   
        **FrontColor**
        
        : toutes les faces du cube, la valeur par défaut est {{Value|3236096495}} (hex: {{Value|c0e2e9ef}}).

    -   
        **HiliteColor**
        
        : la face du cube ou de la flèche qui est actuellement en surbrillance, la valeur par défaut est {{Value|4289389311}} (hex: {{Value|ffaae2ff}}).

    -   
        **TextColor**
        
        : le texte sur les faces du cube, la valeur par défaut est {{Value|4278190080}} (hex: {{Value|ff000000}}).
5.  La valeur de la couleur doit être saisie sous la forme d\'un nombre entier non signé de 32 bits. Traduit au format hexadécimal, ce nombre entier a la forme {{Value|AARRGGBB}}. Où {{Value|AA}} représente le canal alpha (une mesure de la transparence) et les trois autres paires de chiffres représentent le rouge, le vert et le bleu. Pour convertir une valeur hexadécimale en un nombre entier non signé, vous pouvez utiliser la [console Python](Python_console/fr.md) en entrant par exemple {{Incode|int("ff323232", 16)}}, ou un service en ligne tel que [celui-ci](https://cryptii.com/pipes/integer-encoder).
6.  Définissez éventuellement d\'autres couleurs.
7.  Appuyez sur le bouton **Fermer**.

Pour définir manuellement la largeur de la bordure :

1.  Démarrez l\'<img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> l\'[éditeur de paramàtres](Std_DlgParameter/fr.md).
2.  Dans le panneau de gauche, allez dans **BaseApp → Preferences → NaviCube**.
3.  Cliquez avec le bouton droit de la souris sur le panneau de droite et sélectionnez **New float item** dans le menu contextuel.
4.  Saisissez le nom **BorderWidth**, {{Value|default is 1.1}}.
5.  Saisissez la largeur.
6.  Appuyez sur le bouton **Fermer**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/fr
