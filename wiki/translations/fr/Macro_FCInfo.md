# Macro FCInfo/fr
{{Macro/fr
|Name=Macro FCInfo
|Name/fr=Macro FCInfo
|Icon=FCInfo.png
|Description=Donne des informations sur la forme sélectionnée et peut afficher une conversion de la longueur, de l'inclinaison (degrés, radians, grades, pourcentage), de la surface, du volume et du poids dans différentes unités (métriques et impériales). La macro fonctionne désormais aussi pour les éléments d'une esquisse en mode édition.
<br />[https://gist.github.com/mario52a/6afc64081c4eb8be3b93 Version française]
|Author=Mario52
|Download=[https://wiki.freecad.org/images/5/53/FCInfo.png Icône de la barre d'outils]
|Version=1.30
|Date=2025/01/02
|FCVersion=Toutes
|SeeAlso=[Arch Prendre des cotes](Arch_Survey/fr.md), [Macro SimpleProperties](Macro_SimpleProperties/fr.md), [Macro FCInfoGlass](Macro_FCInfoGlass/fr.md)
}}

## Description

Donne des informations sur la forme sélectionnée et peut afficher une conversion de la longueur, de l\'inclinaison (degrés, radians, grades, pourcentage), de la surface, du volume et du poids dans différentes unités (métriques et impériales). La macro fonctionne désormais aussi pour les éléments d\'une esquisse en mode édition.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/c6dd9eabe1ae67d0baf235d672faa75dfd927ad6/FCInfo_en_Ver_1-30-rmu_Docked.FCMacro}}

<img alt="" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*



## Utilisation

Sélectionnez un objet et lancez l\'application, ou lancez d\'abord l\'application puis sélectionnez un objet. L\'objet est analysé et une boîte de dialogue s\'ouvre avec les informations recueillies. A chaque nouvelle sélection, l\'unité de longueur est remise à **mm** et l\'unité d\'angle à **degrés décimaux**. <img alt="Fenêtre supérieure" src=images/Macro_FCInfo_06.png  style="width:900px;">






### Secteur 1 : Document 

![FCInfo Document](images/Macro_FCInfo_Document_00.png )

-   Nom du document
-   Label et nom interne de l\'objet
-   Nom interne de l\'objet
-   Nom du sous-élément et type de l\'objet
-   Type de l\'objet

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_001_Document** pour cacher la boîte)*.



### Secteur 2 : Coordonnées au point cliqué 

![FCInfo Coordinate](images/Macro_FCInfo_Coordinate_click_mouse_00.png )

-   Coordonnées X,Y et Z, cliquez sur la souris
-   Le **button** crée un point, un axe, un plan, copie un axe vectoriel à partir de **FreeCAD.Vector(-24.0, 240.0, 7.0)**.

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_002_Coordinate_Mouse** pour cacher la boîte)*.



### Secteur 3 : Couleur au point 

![FCInfo Color_on_point](images/Macro_FCInfo_Color_on_point_00.png )

-   Couleur du point cliqué.
    -   valeur de 0.0 à 1.0

-   Line Edit affiche la valeur de la couleur dans différents formats : {{LineEdit|"3435973887" , "#cccccc" , "0xcccccc" , "204,204,204" , "(0.8,0.8,0.8)"}}
    -   **3435973887** : mode RVBA Entier non signé (format dans les préférences de FreeCAD) Alpha = 255
    -   **#cccccc** : mode RVB hexadécimal (Qt : `setStyleSheet("color : #cccccc")`)
    -   **0xcccc** : mode RVB hexadécimal (Python : `hex(0xcccccc`)
    -   \"**204,204,204** \" : RVB décimale : mode RVB (Qt : `setStyleSheet(u "QLineEdit {"background-color : rgb(204, 204, 204)} ;")`)
    -   **(0.8,0.8,0.8)** : RVB flottant : mode RVB format float de 0.0 à 1.0
    -   (Le nombre de décimales dépend de l\'option *\"x (Décimales)\"*)

-    {{CheckBox|Sub.Objet}}: change la couleur de l\'objet ou du sous-objet sélectionné. Si cette case est activée {{CheckBox|TRUE|Sub.Objet}} la face ou le sous-objet sélectionné est modifié ou dupliqué. Si elle n\'est pas activée (par défaut) l\'objet est modifié (couleur) ou dupliqué.

-    **Coul. Obj**: change la couleur de la forme ou de la face selon le choix. Dans le cas d\'un objet Mesh ou Points, l\'objet complet est coloré.

-    **Dupl. Obj**: duplique la face ou l\'objet selon l\'option choisie. Dans le cas d\'un objet Mesh ou Points, l\'objet complet est coloré. Dupliquer un objet Mesh conserve l\'original et crée une forme solide. Dupliquer un objet Points conserve l\'original et crée une copie.

-    {{SpinBox|0}}: degré de transparence de la face ou de l\'objet sélectionné en fonction de l\'option choisie **0 = opaque** , **100 = transparent**

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_003_Color** pour cacher la Box)*.



### Secteur 4 : Composants Mesh 

![FCInfo Composant Mesh](images/Componant_Mesh_v_1-28.png )

Si la sélection est un objet maillé, une nouvelle fenêtre ***\"Components\"*** est affichée et donne :

-   Edges : nombre d\'arêtes {{LineEdit|9561}}.
-   Faces : nombre de faces {{LineEdit|6374}}.
-   Points : nombre de points {{LineEdit|3189}}.

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_004_Object_Mesh** pour cacher la Boîte)*


### Secteur 5 : Unités 

![FCInfo Units](images/Macro_FCInfo_Units_00.png )

-    {{ComboBox|mm}} : si l\'objet est un périmètre de face, la longueur de l\'objet est affichée. La taille de l\'unité peut être sélectionnée :
    km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique

-   Length of the object : longueur de l\'objet ou périmètre de la face {{LineEdit|10.0 mm}}.

-   Si l\'objet est un cercle, une seconde lineEdit **Rayon :** s\'ouvre et affiche le rayon et le diamètre du cercle {{LineEdit|2.0 mm (dia. 4.0 mm)}}.

-   Perimeter of the shape (12). Périmètre de l\'objet et nombre de subObject (Edges) contenus dans l\'objet {{LineEdit|120.0 mm}}.

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_005_Value_Unit** pour cacher la boîte)*



### Secteur 6 : Inclinaison 

![FCInfo Inclination](images/Macro_FCInfo_Inclination_00.png )

-   **Inclinaison de l\'objet** peut être affiché en :
    -   degré décimal, ex : {{LineEdit|174.831872611°}}
    -   degré minute seconde, ex : {{LineEdit|174° 49' 54.741401''}}
    -   radian, ex : {{LineEdit|3.05139181449 rad}}
    -   grade, ex : {{LineEdit|194.257636235 gon}}
    -   pourcent, ex : 30° = {{LineEdit|57.74%}}
-   **Inclinaisons dans les plans XY, YZ, ZX** et leurs coordonnées
-   **Direction objet**, {{LineEdit|Vector (0.0, 0.0, -10.0)}} donne la direction de l\'objet. Le calcul est : coord_1 - coord_2 = direction (ou inverse)
    -   
        **Direction**
        
        ce bouton crée une ligne en direction de l\'objet.
-   **ValueAt(0)**, {{LineEdit|Vector (0.0, 0.0, 10.0)}} renvoie le vecteur 3D correspondant à une valeur de paramètre.
    -   
        **ValueAt(0)**
        
        ce bouton crée une ligne dans la direction ValueAt de l\'objet.
-   **NormalAt(0,0)**, {{LineEdit|Vector (0.0, 0.0, 1.0)}} renvoie le vecteur 3D correspondant à une valeur de paramètre.
    -   
        **NormalAt(0,0)**
        
        ce bouton crée une ligne dans la direction NormalAt de l\'objet.

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_006_Inclination** pour cacher la boîte)*



### Secteur 7 : Surface et volume 

![FCInfo Surface and Volume](images/Macro_FCInfo_Surface_and_Volume_00.png )

-   Surface de la forme affichée, la taille de l\'unité peut être sélectionnée. {{LineEdit|600.0 mm2}}
-   Surface de la face affichée, la taille de l\'unité peut être sélectionnée. {{LineEdit|0.0 mm2}}
-   Volume de la forme affiché, la taille de l\'unité peut être sélectionnée. {{LineEdit|1000.0 mm3}}
-   Unité, choisissez votre unité.
-   L\'unité de grandeur {{ComboBox|gram}} peut être choisie :
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg , gr (grain), dr (drachme), oz (once), oz t (once de troy),
    lb t (livre de troy), lb (livre av), st (stone), qtr (quart), cwt (hundredweight), tonneau fr, ct.
-   Poids de la forme affichée, unité de masse sélectionnable. {{LineEdit|2.7 g}}
-   Densité de la matière en **kg par dm3** {{LineEdit|2.7000 kg (by dm3)}}
-   Matériel {{ComboBox|Metal Nickel (Ni),8.27,10.0,adapt Price}}
    -   Au démarrage, la macro chercher le fichier **FCInfo_material.txt**, si le fichier n\'existe pas, un fichier FCInfo_material.txt est créé.
    -   Le fichier est créé avec 10 types de matériaux enregistrés dans ce format.
        -   **Intitulé du matériau , Densité en dm3 , Prix par dm3 , texte info sur choix**
        -   *(4 champs séparés par des virgules)*
        -   Liquid Water (H2o),1,10.0,adapt Price
        -   Mater Beton,2.4,10.0,adapt Price
        -   Metal Aluminium (Al),2.7,10.0,adapt Price
        -   Metal Copper (Cu),8.96,10.0,adapt Price
        -   Metal Gold (Au),19.3,10.0,Gratis
        -   Metal Iron (Fe),7.87,10.0,adapt Price
        -   Metal Lead (Pb),11.35,10.0,adapt Price
        -   Metal Magnesium (Mg),1.43,10.0,adapt Price
        -   Metal Nickel (Ni),8.27,10.0,adapt Price
        -   Metal Pewter (Sn),7.29,10.0,adapt Price
        -   Metal Platinum (Pt),21.45,10.0,adapt Price
        -   Metal Silver (Ag),10.5,10.0,adapt Price
        -   Metal Sodium (Na),0.97,10.0,adapt Price
        -   Metal Titanium (Ti),4.4,10.0,adapt Price
        -   Metal Zinc (Zn),7.1,10.0,adapt Price
        -   Wood Beechwood,0.8,10.0,adapt Price
        -   Wood MDF,0.75,10.0,adapt Price
        -   Wood Mahogany,0.6,10.0,adapt Price
        -   Wood Oak,0.7,10.0,adapt Price
        -   Wood White pine,0.4,10.0,adapt Price
-   Nouveau matériau ou édition {{LineEdit|Metal Nickel (Ni),8.27,10.0,adapt Price}}
    -   vous pouvez modifier ou éditer un nouveau matériau dans ce format :

    -   **Title, Density on dm3, Price on dm3, text info on choice**

    -   *(4 champs séparés par des virgules)*

    -   *vous pouvez également éditer le fichier dans votre éditeur préféré en respectant le format spécifique*

    -   vous pouvez enregistrer le fichier dans un chemin souhaité avec la variable : **seTMaterialSavePathName**

    -   *par défaut le fichier est créé dans le chemin de la macro*

    -   
        **Effacer 6/17**
        
        : supprime le champ affiché

    -   
        **Sauve**
        
        : enregistre la modification ou le nouveau matériau

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_007_Surface_and_Volume** pour cacher la boîte)*.



### Secteur 8 : Coût 

![FCInfo Cost](images/Macro_FCInfo_Cost_00.png )

-   Coût total : coût total de l\'objet sélectionné


{{LineEdit|0.027 Eu}}

-   Prix (kg/dm3) : prix du matériau choisi (*Metal Aluminium (Al),2.7,***10.0***,adapt Price*)


{{SpinBox|10,0000 Eu (par Kg)}}

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_008_Cost_And_Price** pour cacher la boîte)*.



### Secteur 9 : Boîte englobante 

![FCInfo BoundBox](images/Macro_FCInfo_BoundBox_00.png )

-   La boîte englobante donne les dimensions limites de la forme.
    -   longueur X maximale : {{LineEdit|10.0 mm}}

    -   longueur Y maximale : {{LineEdit|10.0 mm}}

    -   longueur Z maximale : {{LineEdit|10.0 mm}}

    -   Diagonale : longueur de la diagonale {{LineEdit|17.3205 mm}}

    -   
        **Tracing**
        
        : crée 6 rectangles aux dimensions de la boîte englobante

    -   
        **Volume**
        
        : crée un volume aux dimensions de la boîte englobante

    -   
        {{CheckBox|Text Dim.}}
        
        : crée la dimension du triangle *(boundbox)*

    -   Si {{CheckBox|TRUE|Text Dim.}} est coché, la dimension de la spinbox du texte {{SpinBox|3,000}} est opérationnelle pour donner votre valeur *(3.0 par défaut)*

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_009_BoundBox** pour cacher la boîte)*.



### Secteur 10 : Centre 

![FCInfo Center of\...](images/Macro_FCInfo_Center_of_00.png )

-   Centre de la forme et ces coordonnées XYZ
-   Centre de masse et ces coordonnées XYZ
-   Les **Boutons** créent sur un point, un axe, un plan, copie un axe vectoriel sous forme de **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(voir Secteur 13)*

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_010_Center_Mass** pour cacher la boîte)*.



### Secteur 11 : Centre d\'inertie 

![FCInfo Inertia](images/Macro_FCInfo_Inertia_00.png )

-   Moment d\'inertie et ces coordonnées longueur et poids
-   Le bouton crée sur le point, l\'axe, le plan, copier l\'axe vectoriel sous forme **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(voir Secteur 13)*
    -   action ligne 1 : {{LineEdit|x1}}, {{LineEdit|y1}}, {{LineEdit|z1}}, {{LineEdit|0.0}}
    -   action ligne 2 : {{LineEdit|x2}}, {{LineEdit|y2}}, {{LineEdit|z2}}, {{LineEdit|0.0}}
    -   action ligne 3 : {{LineEdit|x3}}, {{LineEdit|y3}}, {{LineEdit|z3}}, {{LineEdit|0.0}}
    -   action ligne 4 diagonale : {{LineEdit|x1}}, {{LineEdit|y2}}, {{LineEdit|z3}}

idem le poids

-   Determinant 1 : {{LineEdit|4629629629629.633}} calcule le déterminant de la matrice, en [valeur scientifique](https://fr.wikipedia.org/wiki/Notation_scientifique)
-   Determinant 2 : {{LineEdit|4629629629629.6328125}} calcule le déterminant de la matrice, en valeur décimale

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_011_Inertia** pour cacher la boîte)*.



### Secteur 12 : Feuille de calcul 

![FCInfo Disabled](images/Macro_FCInfo_Disabled_module_00.png )

-   La case à cocher {{CheckBox|Disabled module}} permet de rechercher ou non tous les détails de l\'objet. Si elle n\'est pas cochée, seule la valeur principale est affichée.
-   Sommets et détails de la forme (compt_Edge), (compt_Faces), (compt_Vector de la Face)
-   200 lignes maximum dans le tableau, s\'il y a plus de 200 lignes il apparaît **(!+ 200)** et le nombre de lignes
-   Si l\'objet comporte de nombreux objets, le temps est long et la recherche est répétée à chaque clic de souris. La fonction d\'écriture dans la feuille de calcul incluse, diminue le temps d\'affichage pour cela elle est désactivée par défaut
-   Les détails complets peuvent être sauvegardés par le bouton **Save** dans un fichier au format CSV et peuvent être visualisés dans le tableur avec le bouton **Read** ou par un tableur externe comme [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) ou autre

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_012_SpreadSheet** pour cacher la boîte)*.



### Secteur 13 : Création d\'une feuille de calcul 

![FCInfo SpreedSheet](images/Macro_FCInfo_SpreedSheet_00.png )

-    **SpreadSheet**: crée une nouvelle feuille de calcul dans un document

-    {{LineEdit|SpreadSheet}}: la feuille de calcul courante. Si la feuille de calcul n\'existe pas, une feuille de calcul est créée

-    **Refresh**: rafraîchir la liste des feuilles de calcul dans le document

-    {{ComboBox|-}}: le(s) tableur(s) présent(s) dans le document

-    **Read**: lire les données d\'une feuille de calcul sauvegardée *.FCInfo* ou txt, asc, csv

-    **Save**: sauvegarde les données sur disque sous la forme sélectionnée ci-dessous *\'.FCInfo* ou txt, asc, csv

-    {{RadioButton|TRUE|Tabulation}}: le séparateur est la tabulation (par défaut)

-    {{RadioButton|Comma}}: le séparateur est la virgule

-    {{RadioButton|Semicolon}}: le séparateur est le point-virgule

-    {{RadioButton|Space}}: le séparateur est l\'espace

Option pour **sauvegarder** ou **lire** la feuille de calcul avec différents séparateurs, Tabulation, Virgule, Point-virgule, Espace
La tabulation est le séparateur pour l\'\[Spreadsheet_Workbench/fr\|atelier Spreadsheet\] de FreeCAD
Le nombre de ces quatre séparateurs est calculé pour aider en cas d\'inconnu
Les VIRGULES étaient les anciens séparateurs de la macro FCInfo (01.16 et avant)
Depuis la version 01.17, pour être compatible avec le tableur FreeCAD, la TABULATION est le séparateur par défaut
Si vous voulez convertir votre ancienne feuille de calcul FCInfo : ouvrez-la dans FCInfo et enregistrez-la avec l\'option Tabulation cochée.
*(vous pouvez cocher à {{false}} la variable **switch_setVisible_GBox_013_SpreadSheet_Creation** pour cacher la boîte)*\'.



### Secteur 14 : Principales commandes 

![FCInfo Main](images/Macro_FCInfo_Main_00.png )

-    {{CheckBox|Info}}: si cette case est cochée, les informations sont affichées dans la vue rapport

-    {{CheckBox|Point}}: si cette case est cochée, un point est créé dans la forme de coordonnées affichée : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Axis}}: si cette case est cochée, un axe est créé dans la forme de coordonnées affichée.

-    {{CheckBox|Axis}}: si cette case est cochée, un axe est créé dans le formulaire de coordonnées affiché : **FreeCAD.Vector(-24.0, 240.0, 7.0)**.

-    {{CheckBox|Plan}}: si cette case est cochée, un plan d\'axe est créé dans le formulaire de coordonnées affiché : **FreeCAD.Vector(-24.0, 240.0, 7.0)**.

-    {{RadioButton|Clip-B0}}: aucun presse-papier

-    {{RadioButton|Clip-B1}}: si cette case est cochée, les coordonnées sont copiées dans le clipBoard Forme : **FreeCAD.Vector(X.0, Y.0, Z.0)** Modèle FreeCAD

-    {{RadioButton|Clip-B2}}: si cette case est cochée, les coordonnées sont copiées dans le clipBoard Form : **X, Y, Z** avec séparateur virgule

-    {{RadioButton|Clip-B3}}: si cette case est cochée, les coordonnées sont copiées dans le clipBoard Form : **X Y Z** tel quel avec séparateur d\'espace

-    {{CheckBox|Left/Right}}: si cette case n\'est pas cochée, les macros de la fenêtre sont affichées à droite (par défaut). Si elle est cochée, les macros de la fenêtre sont affichées à gauche.

Si l\'option est 1 mode fly *(User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**seTPositionFlyRightLeft**)* ce bouton n\'est pas visible.

-    {{SpinBox|4 (Decimales)}}: donne le nombre de décimales affichées

-    {{SpinBox|12 (Dim. texte)}}: donne la dimension du texte dans la macro

-    **Forum**: pointe vers le fil du forum FCInfo *(vous devez être connecté à internet)*.

-    **Wiki**: pointe vers le Wiki FCInfo *(vous devez être connecté à internet)*

-    **Ref**: rafraîchir l\'affichage des données dans la vue du rapport

-    **Ref**: rafraîchir l\'affichage des données dans la vue rapport

-    **Exit**: sortir correctement de la macro *(ne pas utiliser la croix rouge de la fenêtre)*

*(vous pouvez mettre à {{false}} la variable **switch_setVisible_GBox_014_Main_Tools** pour cacher la boîte)*.

Une fois la macro lancée, la macro reste active et la fenêtre reste visible. Il faut quitter la macro par la touche **Quitte**. Si vous quittez par la petite croix, la fenêtre disparaît et la macro reste en mémoire, les données continuent de s\'afficher dans la *vue rapport* de FreeCAD. Vous devrez quitter FreeCAD pour vider la mémoire.


<center>

Image:Macro_FCInfo_04.png\|Dockée à droite, Image:Macro FCInfo 05.png\|ou à gauche avec la Vue combinée et accessible par un onglet, ou non dockée, au choix.


</center>




## Options



### Les unités utilisées 



#### Unités de longueur : 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.



#### Unités d\'angle : 

1.  **degré décimal**, ex : 174.831872611°
2.  degré minute seconde, ex : 174° 49\' 54.741401\'\'
3.  radian, ex : 3.05139181449 rad
4.  grade, ex : 194.257636235 gon ou gr
5.  pourcent, ex : 30° = 57.74%

Compréhension de l\'affichage des angles dans FCInfo.


<center>

Image:Macro FCInfo 02.png\|Compréhension de l\'affichage des angles dans FCInfo Image:Macro FCInfo 03.gif\|Compréhension de l\'affichage des angles en pourcentage dans FCInfo
Cliquez deux fois sur l\'image pour voir l\'animation (l\'image doit être en plein écran)


</center>






#### Unités de masse : 

ton, quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct



#### Configuration de FCInfo 

-   Emplacement : **Outils \> Editer les paramètres \> \*Paramètre utilisateur:BaseApp/Préférences/Macros/FCMmacros/FCInfo/**
-   **switchNotInfoOnBeginning** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Affiche ou non ce texte d\'information lors de l\'exécution de la macro
        -   \[{{false}}\] = afficher cette information

        -   
            {{true}}
            
            = cette information n\'est pas affichée au début de l\'exécution de la macro
-   **switchVersionSearch** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Recherche si une nouvelle version existe lors de l\'exécution de la macro
-   **switchWarning** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Affiche ou non la fenêtre d\'avertissement en cas de mauvaise sélection
-   **switchCreatePoint** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Cocher la case Créer un point
-   **switchCreateAxis** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Cocher la case Créer un axe
-   **switchCreatePlane** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Cocher la case Créer un plan
-   **switchDisplayInfoObject** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Cocher la case info
-   **switchClearDisplayReportView** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Si switchClearDisplayReportView est {{true}} le vue rapport est effacée
-   **seTWidgetPosition** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Cocher la case Position du widget à gauche/droite
    -   Si seTWidgetPosition \[{{false}}\] : si seTPositionFlyRightLeft = 2 = ancré à droite
    -   Si seTWidgetPosition {{true}} : if seTPositionFlyRightLeft = 3 = ancré à gauche
    -   si elle vaut 1, la fenêtre de la macro n\'est pas ancrée
-   **switchBoundBoxCreateText** **\#** SetBool {{true}} ou \[{{false}}\]
    -   Créer la dimension texte de la case a cocher
-   **seTBoundBoxTextHeigth** **\#**\' seTBoundBoxTextHeigth = 3.0
    -   Donne la hauteur de la dimension du texte (indépendamment de la valeur seTTextHeigthValue)
-   **seTBoundBoxTextArround** **\#** seTBoundBoxTextArround = 3
    -   Donne l\'arrondi des dimensions du texte (indépendant de seTDecimalValue)
-   **seTMemoClipBoard** **\#** SetInt \[0\], 1, 2, 3
    -   Donne une valeur \[0\], 1, 2, 3 presse-papier
        -   \[0\] = désactiver le presse-papier
        -   1 = la chaîne de données est mémorisée dans : FreeCAD.Vector( X, Y, Z )
        -   2 = la chaîne de données est mémorisée dans : X, Y, Z
        -   3 = la chaîne de données est mémorisée sous la forme de : X Y Z
-   **seTTextHeigthValue** **\#** SetInt 11
    -   Donne une valeur de hauteur de texte de la macro
-   **seTDecimalValue** **\#** SetInt 4
    -   Indique le nombre de décimales affichées
    -   Si le nombre est -1, la valeur des décimales totale est affichée)
-   **seTMaterialCurrentIndex** **\#**\' SetInt 0
    -   Définit l\'index de la boîte combinée
-   **seTMaterialFileName** **\#** SetString FCInfo_material.txt
    -   Nom du fichier du matériau
-   **seTMaterialSavePathName** **\#** SetString C:\\N- \\N- \\N- \\N- \\N- \\N- \\NMacro\\NFCINfo_material.txt
    -   Nom du chemin d\'accès au fichier du matériau
-   **seTMaterialPrice** **\#**\' SetFloat
    -   Prix du matériau par Kg
-   **seTMaterialSuffixDevise** **\#** SetString
    -   Devise de la monnaie
-   **seTMaterialSuffixCost** **\#**\' seTMaterialSuffixCost
    -   Coût du dispositif de suffixe
-   **seTMaterialCost** **\#**\' SetFloat
    -   Coût du matériau
-   **seTDensiteValue** **\#** SetFloat 1.0
    -   Donne la valeur de la densite
-   **seTDensiteDecimalNumber** **\#** SetInt 4
    -   Indique le nombre de décimales pour la valeur de la densite
-   **seTDensiteSingleStep** **\#** SetFloat 1.0
    -   Donne le pas pour un clic, par défaut 1.0 (possible 0.01 ou \...)
-   **seTDensiteSuffixChain** **\#** SetString kg (by dm3)
    -   Choisir votre chaîne de suffixe
-   **seTPositionFlyRightLeft** **\#**\' SetInt 2
    -   Choisir votre position, Fly, \[Right\], Left
        -   \[1\] = la fenêtre macro est non dockée
        -   \[2\] = la fenêtre macro est positionnée à droite
        -   3 ou autre = la fenêtre macro est positionnée à gauche
-   **seTIndexUnitWeight** **\#**\' SetInt
    -   Définit l\'unité Poids de l\'index
-   **seTUnitSymbolMicro** **\#**\' U
    -   Définit le symbole Micro
-   **seTUnitSymbolCube** **\#**\' 3
    -   Définit le symbole Cube
-   **seTUnitSymbolCarre** **\#**\' 2
    -   Définit le symbole Square
-   **seTIndexUnitLength** **\#**\' SetInt
    -   Définit l\'unité de longueur de l\'index
-   **setBSplineToByArcValue** **\#** SetFloat 0.00001
    -   Définit l\'unité de coupe de la BSpline pour saisir le rayon sur le point donné
-   **setMeshTopologyValue** **\#** SetFloat 0.1
    -   Définit l\'unité de création de la maille à la forme
-   **switchBSplineCreateCircleConstructorAxis** **\#**SetBool {{true}} ou \[{{false}}\]
    -   Affiche l\'axe des cercles (arcs) pour créer la B-spline
-   **switchBSplineCreateCircleConstructor** **\#**SetBool {{true}} ou \[{{false}}\]
    -   Affiche les créateurs de cercles pour créer la B-spline
-   **switchCreateLineDiVatNatOnClick** **\#**SetBool {{true}} ou \[{{false}}\]
    -   Créer l\'information de la ligne au point (0,0,0) ou au point cliqué par la souris (x,y,z) si c\'est {{true}}
    -   Si c\'est {{true}}, un \'\*\' est affiché devant le texte. EX : \'\*Direction\'

*(section GroupBox)* vous permet de n\'afficher que la ou les section(s) souhaitées (uniquement visuelles) {{False}} ou {{True}}.

Tous les calculs sont fait sans tenir conte de cette option

-   section GroupBox begin
    -   **switch_setVisible_GBox_001_Document** = True (1)
    -   **switch_setVisible_GBox_002_Coordinate_Mouse** = True (1)
    -   **switch_setVisible_GBox_003_Color** = True (1)
    -   **switch_setVisible_GBox_004_Object_Mesh** = True (1)
    -   **switch_setVisible_GBox_005_Value_Unit** = True (1)
    -   **switch_setVisible_GBox_006_Inclination** = True (1)
    -   **switch_setVisible_GBox_007_Surface_and_Volume** = True (1)
    -   **switch_setVisible_GBox_008_Cost_And_Price** = True (1)
    -   **switch_setVisible_GBox_009_BoundBox** = True (1)
    -   **switch_setVisible_GBox_010_Center_Mass** = True (1)
    -   **switch_setVisible_GBox_011_Inertia** = True (1)
    -   **switch_setVisible_GBox_012_SpreadSheet** = True (1)
    -   **switch_setVisible_GBox_013_SpreadSheet_Creation** = True (1)
    -   **switch_setVisible_GBox_014_Main_Tools** = True (1)
-   section GroupBox end

## Script

Copiez le contenu de la macro dans un fichier nommé \"FCInfo.FCMacro\"

-   Windows : habituellement **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**.
-   Ubuntu : habituellement **\" /home/your_user_name/.FreeCAD \"**.

Ou, directement dans l\'interface de FreeCAD.
Les icônes doivent se trouver dans le même répertoire que la macro.
Télécharger les images en vous positionnant sur les icônes <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> puis faites clic droit de la souris \"Enregistrer l\'image sous\" (ne pas modifier le nom)
**PS : le code est trop long pour être contenu dans la page du wiki (pour le moment les pages du wiki n\'acceptent que 64 KB). Le code de la macro a été placé dans le forum**

Téléchargez le fichier FCInfo **docké à droite**


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|Dernière version de Macro_FCInfo}}

(Ou **[sur le forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)** )
**PS :** cette macro utilise la fonction **getSelection()** et la liste des objets commence à 1 ex: pour un cube **Edge1 à Edge12** (arêtes) et le code qui liste les arêtes dans la console Python commence à 0 ex: pour un cube **Edge\[0\] à Edge\[11\]**
Cette différence est tout à fait normale, le compteur de la liste/tableau dans OpenCascade commence toujours à **1 et pas à 0**.

### Limitations

Toujours utiliser le bouton **Exit**. Si vous quittez le programme sans passer par le bouton **Exit**, le programme reste en mémoire et continue à s\'exécuter et l\'affichage continue dans le \"rapport de visualisation\". Vous devez quitter FreeCAD pour l'effacer de la mémoire.
Seuls les 200 premiers éléments de l'objet sont visibles dans le tableau. Si il y a plus de 200 éléments dans l'objet, un signal sera affiché par **(! +200)**. La liste complète des données est visible dans le fichier sauvegardé par le bouton **Save**.

Si la fenêtre de la macro n\'est pas visible au lancement, regardez en bas de la fenêtre :

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 

en projet :
~~lecture du fichier directement dans un tableau.~~ fait
~~correspondances des \"Edges\" et de leurs coordonnées~~ fait
~~association d\'une substance à sa masse volumique~~
~~inclinaison sur l\'élément plutôt que sur l\'objet global~~ fait
~~incrustation à droite dans l\'interface de FreeCAD~~ fait

## Version

ver \"1.30\" 2025/01/02 : effacé toutes les références à PySide PySide2 et QtWidgets modifé (Qt) Save file


```python
#
import PySide2
from PySide2 import QtGui , QtCore, QtWidgets
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QTableWidget, QApplication
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

            OpenName, Filter = PySide2.QtWidgets.QFileDialog.getOpenFileName(None, u"Read a txt file", setPathLatestDirectory, "*.FCInfo *.csv *.asc *.txt;;FCInfo (*.FCInfo);;Cvs (*.csv);;Ascii (*.asc);;TXT (*.txt);;(*.*);;(*)")#PySide2
```

remplacé et changé la commande par


```python
#
import PySide
try:
    from PySide import QtWidgets
    from PySide.QtWidgets import *
except Exception:
    None
from PySide import QtGui , QtCore
from PySide.QtGui import *
from PySide.QtCore import *

            OpenName, Filter = QFileDialog.getOpenFileName(None, u"Read a txt file", setPathLatestDirectory, "*.FCInfo *.csv *.asc *.txt;;FCInfo (*.FCInfo);;Cvs (*.csv);;Ascii (*.asc);;TXT (*.txt);;(*.*);;(*)")#PySide

```

ver \"1.29b\" 2024/05/10 **PySide2** modifier l\'inertie \" MatrixX1\*uniteM en (MatrixX1\*uniteM) \" et ajouter l\'inertie à l\'interface

-   [Calcul du moment d\'inertie](https://forum.freecad.org/viewtopic.php?p=713935#p713935)
-   [Moment d\'inertie - FCInfo macro](https://forum.freecad.org/viewtopic.php?t=64653)

ver 1.29 2024/05/06 **french** version **fr PySide6** par sylvainbx <https://gist.github.com/sylvainbx/af09a30be3e1427de56305825331fb29> merci sylvainbx

ver 1.28b 1.28c 2023/10/30 orthographe

ver 1.28 01/09/2023 modifié le nom des variables, possibilité de masquer chaque secteur, sauvegarder les données directement dans le document, le rayon de la surface, ajouter un bouton webWiki et webForum

ver 1.27 2023/06/30 optimiser la feuille de style, corriger la position gauche/droite et restaurer la vue après l\'édition du sketcher 
```python
            self.PB_00_Decrement.setStyleSheet("background-color: white; border:2px solid rgb(215, 10, 22);")      # bord white and red
``` remplacé par 
```python
            self.PB_00_Decrement.setStyleSheet("QPushButton {background-color: white; border:2px solid rgb(215, 10, 22)};")      # bord white and red
```

-   ver 1.26c 2022/04/19 mise à niveau Erreur BSpline avec Gear Bspline=Line

-   ver 1.26b 20/02/2022 mise à jour pour détecter BSpline dans SubObject

-   ver 1.26 06/02/2022 ajouter des informations sur les objets Mesh et Points, décoder les couleurs, dupliquer un objet ou un sous-objet, mémoriser le dernier chemin et d\'autres options de préférences.

-   ver 1.25e 18/12/2021 ajouter l\'info détaillée à BSpline (ToByArcs) et l\'info \"sel\[0\].TypeId\".
-   ver 1.25d 12/12/2021 \-\--
-   ver 1.25c 12/12/2021 correction de \"strAround((\" par \"str(Around(\" et autres petits \...
-   ver 1.25b 11/12/2021 correction erreur dans changement/modification nouveau matériel et réorganisation
-   ver 1.25 10/12/2021 PySide2 et ajout de matériel comboBox
-   Ver 1.24 02/12/2021 Ajout de [adjustedGlobalPlacement](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852) modifié par edwilliams16 pour le placement avec Body, traçage boundbox.
-   ver 1.23cb 25/11/2021 delete **\"import Sketcher \* \"** create conflict with \"**open(OpenName, \"r\")**\' ? ??

Ajout de 
```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 13/12/2021 petite correction champ matériel décommanter le \"\'try\...Except\" !!!
-   ver 1.25c, 12/12/2021 petite correction nouveau matériel
-   ver 1.23b, 20/11/2021 petite correction, ajout de l\'info texte au début de la macro et ordonner le code texte.
-   ver 1.23 , 19/11/2021 inclut l\'icône dans la macro, le nombre de décimales affichées, la hauteur du texte, configure les options dans les Préférences de Freecad, corrige les infos pour les éléments de l\'esquisse en mode édition.
-   ver 1.22 , 12/11/2020 : maintenant la macro est totalement désinstallée en utilisant :


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` et j\'ai ajouté la possibilité d\'afficher ou non la fenêtre \"Message d\'erreur\" \"Faux\" par défaut, si vous voulez activer la fenêtre d\'avertissement allez à : 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" remplacé caractères micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"
-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu remplacé tous les caractères au dessus de 127 in ex: \"°\" en chr(176)) #degree
-   ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"
-   ver 1.21 , 16/04/2019 optimisation pour Py 3\... Qt 5\...
-   ver 1.20 , 29/01/2018 optimisation
-   ver 1.19 , 20/01/2018 mise en place d\'une case à cocher pour activer ou désactiver le module spreadSheet, le module ralenti la macro si l\'objet sélectionné est \"compliqué\". Optimisation.
-   ver 1.18 , 19/12/2017 \....
-   ver 1.17c , 14/12/2017 création de plans avec las mêmes coordonnées d\'un projet dans un autre projet et remplacement de \"FCInfo\" by \"\_\_title\_\_\"
-   ver 1.17b , 13/12/2017 petite correction remplascé FCTreeView to FCInfo
-   ver 1.17 , 12/12/2017 ajout et mise à jour de la section Moment of inertia mm et kg par pinq [FCMacro and moment of inertia of assembly](https://forum.freecadweb.org/viewtopic.php?t=23888), et création de plans, axes, point, et ajout de l\'option sépateur pour le spreadsheet
-   ver 1.16 , 21/06/2017 ajout du contrôle de la hauteur des caractères (here PointSize 8) et checkbox pour la position de la fenêtre à gauche ou à droite
-   ver 1.16 , 21/06/2017 ajout d\'un contrôle sur la hauteur des caractères affichés, ajout d\'une case à cocher pour positionner la macro à gauche ou droite et nouveau code de recherche de chemin de l\'emplacement des macros.
-   ver 1.15 , 19/12/2015 suppression de l\'option PyQt4 [voir la cause](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541) , ajout d\'un checkBox pour éditer ou non les infos dans la vue rapport
-   ver 1.14 , 04/08/2014 PyQt4 et PySide, correction des tooltips qui ne s\'affichaient plus a cause de PySide, ajout de \"fg\" et d\'une décimale dans la densité
-   ver 1.13 , 27/07/2014 remplacement FCInfo_fr_Ver_1-12_Docked.FCMacro avec FCInfo_fr_Ver_1-13_Docked.FCMacro accepte PyQt4 et PySide
-   ver 1.12 , 10/03/2014 ajout de tooltips sur les boutons.
-   ver 1.11 , 04/03/2014 ajout de µm, nm, pm, fm, µg, ng, pg, pour-cent, correction de la grandeur carat ~~\"cd\"~~ en **\"ct\"**, affichage du label et du nom interne, correction du calcul des angles XY YZ ZX fonctionnait bien sur un objet simple mais donnait une valeur erronée sur une pièce composée (prenait d\'autres coordonnées ! découvert en comparant le tableau et les coordonnées affichées dans la section Inclinaisons), fenêtre volante ou dockable n\'importe où dans FreeCAD
-   ver 1.10b, 19/11/2013 boutons à l\'extérieur du scrollbar et blocage des dimensions de la fenêtre
-   ver 1.10 , 18/11/2013 ajout d\'une \"scrollbar\" pour diminuer la dimension de la fenêtre
-   ver 1.08b 10/11/2013 correction d\'erreur d\'affichage de la surface des faces listées dans le tableau et remplacement des \"**print**\" par \"**App.Console.PrintMessage**\"
-   ~~ver 1.09 , 04/11/2013 fonctionne parfaitement sur Windows et Linux (cause de l\'erreur les caractères : ² ³ ° \"ordinal not in range(128)\")~~
-   ver 1.08 , 24/10/2013 correction de l\'affichage dans le fichier des \"Faces\" et \"Edges\" haut dessus de 100 objets
-   ver 1.07 , 11/10/2013 correspondance des \"Faces\" et de leurs coordonnées.
-   ver 1.06 , 22/09/2013 correspondances des \"Edges\" et de leurs coordonnées, inclinaison sur l\'élément plutôt que sur l\'objet global
-   ver 1.05 , 17/09/2013 ajout d\'un icône pour le tableur, conversion en tonneau fr, affichage des dimensions hors tout à la place des coordonnées.
-   ver 1.04 , 11/09/2013: lecture du fichier et affichage directement dans un tableau
-   ver 1.03 , 09/09/2013: affichage plus clair dans Vue rapport et remplacement par \"typeObject = sel\[0\].Shape.ShapeType\"
-   ver 1.02 , 7/09/2013 : petites mises au point
-   ver 1.00 , 6/09/2013



## Liens

Voir aussi : <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch Prise de cotes](Arch_Survey/fr.md)

Vous pouvez faire part de vos commentaires sur le forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Ici un autre post traitant de [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)



---
⏵ [documentation index](../README.md) > Macro FCInfo/fr
