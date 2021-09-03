---
- GuiCommand:   Name:PartDesign Chamfer   Workbenches:[MenuLocation:Part Design → Chamfer   SeeAlso:[[Part Chamfer|Chamfer Part](PartDesign_Workbench___PartDesign]],_Complete.md)---


</div>


<div class="mw-translate-fuzzy">

### Descriere

## Introducere

Acest instrument utilizează **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)** pe muchiile selecționate ale unui obiect. Un element nou **Chamfer** (urmat de un număr secvențial dacă nu este primul element **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein](_PartDesign_Chamfer/fr.md)** creat în document) este adăugat în arborescența proiectului.
<img alt="Pièce chanfreinée" src=images/PartDesign_Chamfer_fr_01.png  style="width:480px;">




</div>

This tool creates chamfers on the selected edges of an object. A new separate Chamfer entry (followed by a consecutive number if there are already existing chamfers in the document) is created in the Project tree.


<div class="mw-translate-fuzzy">

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| ![Sélection des arêtes avant de démarrer la commande.](images/PartDesign_Chamfer-01.png ) ![Réglage de la dimension du chanfrein dans les paramètres de chanfrein.](images/PartDesign_Chamfer-02.png ) ![Un élément Chamfer est ajouté dans l\'arborescence Projet.](images/PartDesign_Chamfer-03.png ) | ### Usage                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1.                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2.                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 3.                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | ### PartDesign Chamfer VS. Part Chamfer  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | -                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | -                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | -                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

## Utilizare

Selecționați una, sau mai multe muchii ale unui obiect apoi porniți instrumentul fie prin click pe iconiță **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein](_PartDesign_Chamfer/fr.md)** din bara de instrumente, fie din meniu **Affichage → Atelier → Part Design**.
Pentru un lanț de muchii tangente una pe alta, este necesară selectarea numai a uneia dintre margini. **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, se va propaga automat în lungul lanțului .
Pentru a-l modifica **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)** după crearea sa, double-cliquer pe intrarea sa în **Vue Combinée → Projet →** pe **Chamfer** pentru a modifica, sau faceți click butonul dreapta, și selecționați **Modifier le chanfrein**.
==Opțiuni==

### Vizualizarea combinată → Sarcini 

<img src=images/PartDesign_Chamfer.png style="width:240px\|left](IMAGE:PartDesign_Chamfer_fr_05.png.md) {{TitreTache|[16px"> Paramètres du chanfrein}}


{{OngletTache|Size}}

: Réglez la dimension du **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, en saisissant une valeur, ou en cliquant sur les flèches haut et bas. Un aperçu en temps réel est affiché dans la fenêtre 3D.
Cliquez sur **OK** pour valider.

Șanfrenul va avea întodeauna unghiul la 45°.

Lățimea maximă a șanfrenului trebuie să fie inferior celei mai micii fațetee 
==Proprietăți==

### Vue combinée → Chamfer → Vue 

<img alt="" src=images/PartDesign_Chamfer_fr_03.png‎  style="width:240px;"> {{PartOngletVue/fr}}
===Vue combinée → Chamfer → Données===
<img alt="" src=images/PartDesign_Chamfer_fr_04.png  style="width:240px;"> {{TitreProprietes|Base}}


{{ProprieteDonnees|Label}}

: Nom de l\'objet (modifiable à volonté).


{{ProprieteDonnees|Placement}}

: \[(**0,00 0,00 1,00**);**0,00**;(**0,00 0,00 0,00**)\], donne l\'ensemble des données **Axis, Angle**, et, **Position** ci dessous.
Si vous sélectionnez, le titre **Placement** <img alt="Options Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">, un bouton avec **trois petits points** s\'affiche, en cliquant sur ce bouton **''' ... '''**, vous avez accès à la fenêtre d\'options **[Tâche Placement](Tasks_Placement/fr.md)**.

-    {{ProprieteDonnees|Angle}}: Angle de rotation par rapport aux coordonnées **X, Y, Z**

-    {{ProprieteDonnees|Axis}}: Sélection de l\'axe(s) de rotation de travail **X, Y**, ou **Z**.
    Par exemple : nous déterminons un {{ProprieteDonnees|Angle}} de **15°**, nous spécifions une valeur de **1,0 pour x** et **2,0 pour y**, cette configuration, aura pour effet, une rotation finale de la pièce qui sera de, \"*\' 15° dans l\'axe x*\' \" et \"*\' 30° dans l\'axe y*\' \". (Défaut, **Z = 1 = actif**)

-    {{ProprieteDonnees|Position}}: Déplacement des coordonnées **X, Y, Z**, par rapport aux points d\'origine **0, 0, 0**.


{{ProprieteDonnees|Size}}

:Projet Donne la valeur au **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)** 

## Exemple


<center>

<File:PartDesign_Chamfer_fr_06.png>‎\|Sélectionnez l\'arête, ou les arêtes à **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfreiner](_PartDesign_Chamfer/fr.md)**, cliquez sur le bouton **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein](_PartDesign_Chamfer/fr.md)** entrez votre dimension, puis validez avec le bouton **OK**, <File:PartDesign_Chamfer_fr_01.png>‎\|le résultat final.


</center>



<center>

<File:PartDesign_Chamfer_fr_07.png>‎\|Une nouvelle icône s\'ajoute à l\'arborescence du projet, cette icône est totalement indépendante, et, est un objet supplémentaire.
Vous pouvez modifier le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)** en double cliquant dessus, ou faites clic droit sur l\'icône et cliquez sur **Modifier le chanfrein**, ou encore dans [Vue combinée → Chamfer → Données → Size](#Vue_combinée_→_Projet_→_Données.md).


</center>

== Comparaison Chanfrein Conception de Pièce et Chanfrein Pièce ==

**Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ne doit pas être confondu avec son équivalent de l\'atelier Part **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)****.
Bien qu\'ils partagent la même icône, ces outils sont différents, et s\'utilisent différemment.

### Voici quelques différences : 

-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** est *paramétrique*. Après l\'application d\'un **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, sa dimension peut être modifié ; ce n\'est pas le cas du **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)**.
-   Les arêtes doivent être sélectionnées avant de démarrer le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)**. Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)**, quant à lui, peut être lancé, puis, suivi de la sélection du solide, et, enfin des arêtes.
-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ajoute une entrée distincte dans l\'arborescence Projet. Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)** devient le parent de l\'objet auquel il a été appliqué.
-   Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** affiche un aperçu en temps réel de l\'application du chanfrein avant la validation de la fonction.
-   Le **![](images/)_[Chanfrein_Part](Part_Chamfer/fr.md)** supporte les dimensions variables (avec une dimension de départ, et, une dimension d\'arrivée). Le **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein PartDesign](_PartDesign_Chamfer/fr.md)** ne le permet pas.

 {{LesOutilsDeModificationsPartDesign}}


</div>

-   Select a single edge, multiple edges or a face on an object, then start the tool either by clicking the button **<img src="images/PartDesign_Chamfer.svg" width=24px> '''Chamfer'''** or using the menu **PartDesign → Apply a dress-up feature → Chamfer**. In case you selected a face all its edges are respected for chamfering.
-   In the appearing [Task panel](Task_panel.md) you can define the chamber in 3 ways:
    -   **Equal distance**: The chamfer edges are equally distanced from the body edge.
    -   **Two distances**: The distances of the chamfer edge to the body edge are specified. The distance direction can be flipped. <small>(v0.19)</small> 
    -   **Distance and angle**: One distances of the chamfer edge to the body edge is specified. The second chamfer edge is defined by the angle of the chamfer. The distance direction can be flipped. <small>(v0.19)</small> 
-   If you want to add more edges or faces click the **Add** button and select edges and/or the faces.
-   If you want to remove edges or faces
    -   either select the edge/face in the list of the dialog and press the **DEL** key. *Note*: Since there must be at least an edge for the feature, the last remaining edge or face in the list cannot be removed.
    -   or click the **Remove** button. All edges and faces being previously selected are highlighted in purple. Select the edge or the face to be removed.
-   Click **OK** to validate.
-   For a chain of edges tangential to one another, one single edge can be selected; the chamfer will propagate along the chain.
-   To edit the chamfer after the function has been validated, either double-click on the chamfer label in the Project tree, or right-click on it and select **Edit Chamfer**.

## PartDesign Chamfer vs. Part Chamfer 

**The PartDesign Chamfer is not to be confused with its [Part workbench counterpart](Part_Chamfer.md)**. Although they share the same icon, they are not the same, and are not used the same way. The main difference is that PartDesign Chamfer creates a separate Chamfer entry (followed by a sequential number if there are already existing chamfers) in the Project tree for the current body. The Part Chamfer becomes the parent of the object it was applied to.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
