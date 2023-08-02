---
- GuiCommand:
   Name: Path Waterline
   Name/fr: Path Lignes de niveau
   MenuLocation: Path -> Lignes de niveau
   Workbenches: Path_Workbench/fr
   Version: 0.19
---

# Path Waterline/fr

## Description

L\'outil <img alt="" src=images/Path_Waterline.svg  style="width:24px;"> [Lignes de niveau](Path_Waterline/fr.md) crée une nouvelle opération de lignes de niveau. A partir de 0.19_pre, l\'opération fonctionne sur l\'ensemble du modèle pour générer le G-code de la tâche. Actuellement, dans les paramètres de l\'opération, il n\'y a pas de fonctionnalité pour sélectionner des zones, des faces ou des régions spécifiques du modèle.

L\'opération Lignes de niveau a deux algorithmes : OCL Drop Cutter et Experimental.

-   L\'algorithme OCL Drop Cutter s\'interface avec OCL.pyd, un module Open Source tiers intitulé [OpenCamLib](OpenCamLib/fr.md) qui génère des chemins d\'outils à partir d\'un modèle 3D. OpenCamLib n\'est pas intégré directement dans FreeCAD.
-   L\'algorithme expérimental utilise la classe intégrée Path.Area().

**Remarque :** pour utiliser l\'opération Lignes de niveau, vous devez :

1.  Installer correctement [OpenCamLib](OpenCamLib/fr.md).
2.  Activez les [Fonctions expérimentales](Path_experimental/fr.md) de l\'atelier Path.
3.  Vérifiez **Édition → Préférences... → Path → Advanced → Enable OCL dependent features**.



## Utilisation

Les instructions d\'utilisation pour plusieurs variantes de [Path Lignes de niveau](Path_Waterline/fr.md) sont présentées ici.



#### Opération de base 

1.  Appuyer sur l\'icône **<img src="images/Path_Waterline.svg" width=24px> [Lignes de niveau](Path_Waterline/fr.md)** ou sélectionnez l\'outil [Lignes de niveau](Path_Waterline/fr.md) dans le menu **Path**.
2.  Sélectionner le contrôleur d\'outil pour l\'opération dans la fenêtre de dialogue du contrôleur d\'outil.
3.  Ajuster les profondeurs d\'opération selon les besoins dans l\'onglet Depths : Start Depth, Finish Depth, Step Down.
4.  Effectuer des ajustements dans l\'onglet Heights si nécessaire.
5.  Configurer les paramètres dans l\'onglet Operations en fonction de l\'algorithme sélectionné :
    1.  OCL Dropcutter
        1.  Choisir BoundBox : Stock ou BaseBoundBox.
        2.  Définir le mode de calque : Single-pass ou Multi-pas.
        3.  Définir l\'intervalle d\'échantillonnage utilisé pour l\'analyse OCL.
    2.  Expérimental
        1.  Choisir BoundBox : Stock ou BaseBoundBox.
        2.  Définir le mode de calque : Single-pass ou Multi-pas.
        3.  Définir le motif de coupe si vous souhaitez effacer chaque calque.
        4.  Définir l\'ajustement des limites (allocation de matière).
6.  Si vous souhaitez prévisualiser le résultat avant d\'accepter les paramètres, cliquez sur Apply
7.  Cliquez sur le bouton **OK** pour confirmer et générer des chemins.

Pour obtenir des effets différents ou plus complexes, définissez des propriétés d\'opération supplémentaires dans l\'onglet Data de la vue Propriétés pour l\'opération.



##### Remarques sur l\'algorithme expérimental 

-   Il ne gère pas correctement les surplombs.
-   Il ne renvoie que les chemins pour une fraise de type fraise en bout (outil).
-   Il peut ne pas capturer correctement toutes les caractéristiques intérieures.
-   C\'est juste ça, expérimental, et pas prêt pour l\'intégration grand public. Veuillez inspecter les chemins avec le **<img src="images/Path_Simulator.svg" width=16px> [Path Simulateur d'usinage](Path_Simulator/fr.md)** ou d\'autres outils d\'inspection g-code tiers, avant de couper avec votre machine.



#### Formes d\'outils (de coupe) disponibles 

Lorsque vous utilisez l\'algorithme ***OCL Dropcutter***, l\'opération Lignes de niveau utilise OpenCamLib \[OCL/fr\|OCL\] pour extraire les parcours de la base de la pièce. En tant que tel, une traduction d\'outil est nécessaire entre le contrôleur d\'outil FreeCAD et OCL afin de terminer l\'analyse avec la forme d\'outil (cutter) choisie. Ces formes d\'outils sont (doivent être) respectées et disponibles pour le Dropcutter OCL tant que les formes d\'outils intégrées sont utilisées, qu\'il s\'agisse d\'outils hérités ou d\'outils coupants :

-   Fraise en bout
-   Fraise à boule
-   Fraise en bout de nez
-   Chanfrein
-   Graveur



#### Remarques additionnelles 

-   Si vous choisissez d\'exécuter le simulateur de parcours, **<img src="images/_Path_Simulator.svg" width=16px> [Path Simulateur d'usinage](Path_Simulator/fr.md)** dans l\'atelier Path, vous pourriez ne pas voir d\'enlèvement de matière spécifique à la forme de l\'outil. Prudence donc. Un petit travail d\'essai utilisant de la mousse ou un autre matériau très peu dense est recommandé pour vérifier que les parcours sont corrects avec le contrôleur d\'outil sélectionné.
-   À compter de mai 2020, seule la fraise en bout dispose de tout type de test pour déterminer l\'exactitude de la traduction des paramètres de l\'outil FreeCAD vers OCL. Veuillez publier tout commentaire concernant une utilisation non-finale dans la section [Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) des forums FreeCAD.



## Propriétés

***Remarque***: toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    **Placement**: placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

    -   
        **Angle**
        
        : angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        **Axis**
        
        : axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés : X, Y, Z

        -   
            **X**
            
            : valeur de l\'axe X

        -   
            **Y**
            
            : valeur de l\'axe Y

        -   
            **Z**
            
            : valeur de l\'axe Z

    -   
        **Position**
        
        : Position de l\'objet, définie dans les sous-propriétés : X, Y, Z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent)

        -   
            **X**
            
            : valeur de distance X

        -   
            **Y**
            
            : valeur de distance Y

        -   
            **Z**
            
            : valeur de distance Z

-    **Label**: nom de l\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Clearing Options}}

-    **Algorithm**: bibliothèque à utiliser pour générer le parcours

-    **BoundBox**: détermine si l\'opération doit être limitée par l\'objet brut ou par la boîte englobante de l\'objet de base

-    **Clear Last Layer**: permet d\'effacer la dernière couche lors d\'une opération \"multi-passes\".

-    **Cut Mode**: direction dans laquelle le parcours d\'outil doit aller autour de la pièce : usinage en avalant (sens des aiguilles) ou usinage en opposition (sens inverse des aiguilles)

-    **Cut Pattern**: motif d\'effacement à utiliser

-    **Depth Offset**:

-    **Ignorer Outer Above**:

-    **Layer Mode**: mode de complétion de l\'opération: simple ou multi-passes

-    **Step Over**:


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour eviter les pinces et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Safe Height**: seuil supérieur duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    **Step Down**: abaissement incrémentiel de l\'outil.


{{TitleProperty|Path}}

-    **Active**: mettre à False pour empêcher l\'opération de générer du code.

-    **Base**: géométrie de base pour cette opération.

-    **Comment**: commentaire facultatif pour cette opération.

-    **Coolant Mode**:

-    **Cycle Time**:

-    **Tool Controller**: définit le contrôleur d\'outil utilisé dans l\'opération.

-    **User Label**: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Start Point}}

-    **Start Point**: point de départ personnalisé pour le chemin de cette opération.

    -   
        **X**
        
        : valeur de distance X.

    -   
        **Y**
        
        : valeur de distance Y.

    -   
        **Z**
        
        : valeur de distance Z.

-    **Use Start Point**: mis à True, si vous spécifiez manuellement un point de départ.



## Disposition de l\'éditeur de la fenêtre des tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.*

Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.



### Localisation de la base 

-   **Ajouter** : ajoute le(s) élément(s) sélectionné(s) qui doit(vent) être la(les) base(s) pour le(s) parcours.
-   **Enlever** : supprime le ou les éléments sélectionnés dans la liste de la géométrie de base.
-   **Réinitialiser** : efface tous les éléments de la liste de la géométrie de base.



### Profondeurs

-    **Start Depth**
    

-    **Final Depth**
    

-    **Step Down**
    



### Hauteurs

-    **Safe Height**
    

-    **Clearance Height**
    



### Opération

-    **Tool Controller**
    

-    **Coolant Mode**
    

-    **Algorithm**
    

-    **BoundBox**
    

-    **Layer Mode**
    

-    **Cut Pattern**\~

-    **Boundary Adjustment**\~

-    **Sample Interval**\~

\~ La visibilité change avec d\'autres paramètres.



## Ressources

-   Simulateur de G-code (parcours) : [NCViewer](https://ncviewer.com/)
-   Simulateur de G-code (parcours) : [CAMotics](https://www.camotics.org/)





{{Path Tools navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Waterline/fr
