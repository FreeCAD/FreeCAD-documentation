---
- GuiCommand:/fr
   Name:Path Waterline
   Name/fr:Path Lignes de niveau
   MenuLocation:Path → Waterline
   Workbenches:[Path](Path_Workbench/fr.md)
   Version:0.19
---

# Path Waterline/fr

## Description

Cet outil crée une nouvelle opération Lignes de niveau. A partir de 0.19_pre, l\'opération Lignes de niveau fonctionne sur l\'ensemble du modèle pour générer le G-code de la tâche. Actuellement, dans les paramètres de l\'opération, il n\'y a pas de fonctionnalité pour sélectionner des zones, des faces ou des régions spécifiques du modèle.

L\'opération Lignes de niveau a deux algorithmes : OCL Drop Cutter et Experimental.

-   L\'algorithme OCL Drop Cutter s\'interface avec OCL.pyd, un module Open Source tiers intitulé [OpenCamLib](OpenCamLib/fr.md) qui génère des chemins d\'outils à partir d\'un modèle 3D. OpenCamLib n\'est pas intégré directement dans FreeCAD.
-   L\'algorithme expérimental utilise la classe intégrée Path.Area().

**Remarque :** Pour utiliser l\'opération Lignes de niveau, vous devez :

1.  Installer correctement [OpenCamLib](OpenCamLib/fr.md).
2.  Activez les [Fonctions expérimentales](Path_experimental/fr.md) de l\'atelier Path.
3.  Vérifiez **Édition → Préférences... → Path → Advanced → Enable OCL dependent features**.

## Utilisation

Les instructions d\'utilisation pour plusieurs variantes de [Path Lignes de niveau](Path_Waterline/fr.md) sont présentées ici.

#### Opération de base 

1.  Appuyez sur l\'icône **<img src="images/Path_Waterline.svg" width=24px> [Waterline](Path_Waterline/fr.md)** ou sélectionnez l\'outil [Waterline](Path_Waterline/fr.md) dans le menu **Path**.
2.  Sélectionnez le contrôleur d\'outil pour l\'opération dans la fenêtre contextuelle de dialogue du contrôleur d\'outil.
3.  Ajustez les profondeurs d\'opération selon les besoins dans l\'onglet Profondeurs : Profondeur de début, Profondeur de fin, Descente.
4.  Effectuez des ajustements dans l\'onglet Heights si nécessaire.
5.  Configurez les paramètres dans l\'onglet Operations en fonction de l\'algorithme sélectionné :
    1.  OCL Dropcutter
        1.  Choisissez la BoundBox : Stock ou BaseBoundBox.
        2.  Définissez le mode de calque : passe unique ou multi-pas.
        3.  Définissez l\'intervalle d\'échantillonnage utilisé pour l\'analyse OCL.
    2.  Expérimental
        1.  Choisissez la BoundBox : Stock ou BaseBoundBox.
        2.  Définissez le mode de calque : passe unique ou multi-pas.
        3.  Définissez le motif de coupe si vous souhaitez effacer chaque couche.
        4.  Définissez l\'ajustement des limites (allocation de matière).
6.  Si vous souhaitez prévisualiser le résultat avant d\'accepter les paramètres, cliquez sur Apply
7.  Cliquez sur le bouton **OK** pour confirmer et générer des chemins.

Pour obtenir des effets différents ou plus complexes, définissez des propriétés d\'opération supplémentaires dans l\'onglet Data de la vue Propriétés pour l\'opération.

##### Remarques sur l\'algorithme expérimental 

-   Il ne gère pas correctement les surplombs.
-   Il ne renvoie que les chemins pour une fraise de type fraise en bout (outil).
-   Il peut ne pas capturer correctement toutes les caractéristiques intérieures.
-   C\'est juste ça, expérimental, et pas prêt pour l\'intégration grand public. Veuillez inspecter les chemins avec le **<img src="images/Path_Simulator.svg" width=16px> [Path Simulateur d'usinage](Path_Simulator/fr.md)** ou d\'autres outils d\'inspection g-code tiers, avant de couper avec votre machine.

#### Formes d\'outils (de coupe) disponibles 

Lorsque vous utilisez l\'algorithme ***OCL Dropcutter***, l\'opération Lignes de niveau utilise OpenCamLib \[OCL\] pour extraire les chemins de la base de la pièce. En tant que tel, une traduction d\'outil est nécessaire entre le contrôleur d\'outil FreeCAD et OCL afin de terminer l\'analyse avec la forme d\'outil (cutter) choisie. Ces formes d\'outils sont (doivent être) respectées et disponibles pour le Dropcutter OCL tant que les formes d\'outils intégrées sont utilisées, qu\'il s\'agisse d\'outils Legacy ou ToolBit:

-   Fraise en bout
-   Fraise à boule
-   Fraise en bout de nez
-   Chanfrein
-   Graveur

#### Remarques additionnelles 

-   Si vous choisissez d\'exécuter le simulateur de chemin, **<img src="images/_Path_Simulator.svg" width=16px> [Path Simulateur d'usinage](Path_Simulator/fr.md)** dans l\'atelier Path, vous pourriez ne pas voir d\'enlèvement de matière spécifique à la forme de l\'outil. Prudence donc. Un petit travail d\'essai utilisant de la mousse ou un autre matériau très peu dense est recommandé pour vérifier que les chemins sont corrects avec le contrôleur d\'outil sélectionné.
-   À compter de mai 2020, seule la fraise en bout dispose de tout type de test pour déterminer l\'exactitude de la traduction des paramètres de l\'outil FreeCAD vers OCL. Veuillez publier tout commentaire concernant une utilisation non-finale dans la section [Path/CAM](https://forum.freecadweb.org/viewforum.php?f=15) des forums FreeCAD.

## Propriétés

***Remarque***: toutes ces propriétés ne sont pas disponibles dans l\'éditeur de fenêtre de tâches. Certaines ne sont accessibles que dans l\'onglet Données du panneau Vue de propriétés pour cette opération.


{{TitleProperty|Base}}

Remarque : il est conseillé de ne pas modifier la propriété Placement des opérations de chemin. Déplacez ou faites pivoter le modèle de tâche de chemin selon vos besoins.

-    {{PropertyData/fr|Placement}}: placement global \[position et rotation\] de l\'objet - par rapport à l\'origine (ou à l\'origine du conteneur d\'objet parent)

    -   
        {{PropertyData/fr|Angle}}
        
        : Angle en degrés appliqué à la rotation de l\'objet autour de la valeur de la propriété Axis

    -   
        {{PropertyData/fr|Axis}}
        
        : Axe (un ou plusieurs) autour duquel faire pivoter l\'objet, défini dans les sous-propriétés : x, y, z

        -   
            {{PropertyData/fr|X}}
            
            : valeur de l\'axe x

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de l\'axe y

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de l\'axe z

    -   
        {{PropertyData/fr|Position}}
        
        : Position de l\'objet, définie dans les sous-propriétés : x, y, z - par rapport à l\'origine (ou à l\'origine du conteneur de l\'objet parent)

        -   
            {{PropertyData/fr|X}}
            
            : x valeur de distance

        -   
            {{PropertyData/fr|Y}}
            
            : valeur de distance y

        -   
            {{PropertyData/fr|Z}}
            
            : valeur de distance z

-    {{PropertyData/fr|Label}}: nom de l\'objet fourni par l\'utilisateur (UTF-8)


{{TitleProperty|Clearing Options}}

-    {{PropertyData/fr|Algorithm}}: bibliothèque à utiliser pour générer le chemin

-    {{PropertyData/fr|BoundBox}}: l\'opération doit-elle être limitée par l\'objet stock ou par la boîte englobante de l\'objet de base

-    {{PropertyData/fr|Clear Last Layer}}: paramétrez pour effacer la dernière couche dans l\'opération \Multi-pass\.

-    {{PropertyData/fr|Cut Mode}}: La direction dans laquelle le parcours d\'outil doit aller autour de la pièce : Climb (ClockWise) ou Conventionnel (CounterClockWise)

-    {{PropertyData/fr|Cut Pattern}}: motif d\'effacement à utiliser

-    {{PropertyData/fr|Depth Offset}}:

-    {{PropertyData/fr|Ignorer Outer Above}}:

-    {{PropertyData/fr|Layer Mode}}: mode de complétion de l\'opération: simple ou multi-passes

-    {{PropertyData/fr|Step Over}}:


{{TitleProperty|Depth}}

-    {{PropertyData/fr|Clearance Height}}: hauteur nécessaire pour eviter les pinces et les obstructions.

-    {{PropertyData/fr|Final Depth}}: profondeur finale de l\'outil - valeur la plus basse de Z.

-    {{PropertyData/fr|Safe Height}}: seuil supérieur duquel les mouvements rapides sont autorisés.

-    {{PropertyData/fr|Start Depth}}: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    {{PropertyData/fr|Step Down}}: abaissement incrémentiel de l\'outil.


{{TitleProperty|Path}}

-    {{PropertyData/fr|Active}}: mettre à Falsepour empêcher l\'opération de générer du code.

-    {{PropertyData/fr|Base}}: géométrie de base pour cette opération.

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération.

-    {{PropertyData/fr|Coolant Mode}}:

-    **Cycle Time**:

-    {{PropertyData/fr|Tool Controller}}: définit le contrôleur d\'outil utilisé dans l\'opération.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur.


{{TitleProperty|Start Point}}

-    {{PropertyData/fr|Start Point}}: point de départ personnalisé pour le chemin de cette opération.

    -   
        {{PropertyData/fr|X}}
        
        : valeur de distance x.

    -   
        {{PropertyData/fr|Y}}
        
        : valeur de distance y.

    -   
        {{PropertyData/fr|Z}}
        
        : valeur de distance z.

-    {{PropertyData/fr|Use Start Point}}: Mis à True, si vous spécifiez manuellement un point de départ.

## Disposition de l\'éditeur de fenêtre de tâches 

*Les descriptions des paramètres sont fournies dans la liste des propriétés ci-dessus.* Cette section est simplement une représentation des paramètres de l'éditeur de fenêtres pour l'opération.

### Localisation de la base 

-   **Add** : ajoute les éléments sélectionnés qui doivent être la base du ou des chemins.
-   **Remove** : supprime le ou les éléments sélectionnés dans la liste emplacement de base.
-   **Edit** : efface tous les éléments de la liste d\'emplacement de base.

### Profondeurs

-    {{PropertyData/fr|Start Depth}}
    

-    {{PropertyData/fr|Final Depth}}
    

-    {{PropertyData/fr|Step Down}}
    

### Hauteurs

-    {{PropertyData/fr|Safe Height}}
    

-    {{PropertyData/fr|Clearance Height}}
    

### Opération

-    {{PropertyData/fr|Tool Controller}}
    

-    {{PropertyData/fr|Coolant Mode}}
    

-    {{PropertyData/fr|Algorithm}}
    

-    {{PropertyData/fr|BoundBox}}
    

-    {{PropertyData/fr|Layer Mode}}
    

-    {{PropertyData/fr|Cut Pattern}}\~

-    {{PropertyData/fr|Boundary Adjustment}}\~

-    {{PropertyData/fr|Sample Interval}}\~

\~ La visibilité change avec d\'autres paramètres.

## Ressources

-   Simulateur G-code(tracé): [NCViewer](https://ncviewer.com/)
-   Simulateur G-code(tracé): [CAMotics](https://www.camotics.org/)





{{Path Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Waterline/fr
