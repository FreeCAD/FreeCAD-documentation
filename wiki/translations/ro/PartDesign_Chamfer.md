# PartDesign Chamfer/ro
---
- GuiCommand:   Name: PartDesign Chamfer   Workbenches: [MenuLocation: Part Design - Chamfer   SeeAlso: [[Part Chamfer|Chamfer Part](PartDesign_Workbench___PartDesign]],_Complete.md)---


</div>




<div class="mw-translate-fuzzy">

### Descriere

## Introducere

Acest instrument utilizează **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)** pe muchiile selecționate ale unui obiect. Un element nou **Chamfer** (urmat de un număr secvențial dacă nu este primul element **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein](_PartDesign_Chamfer/fr.md)** creat în document) este adăugat în arborescența proiectului.
<img alt="Pièce chanfreinée" src=images/PartDesign_Chamfer_fr_01.png  style="width:480px;">




</div>

The <img alt="" src=images/PartDesign_Chamfer.svg  style="width:24px;"> **PartDesign Chamfer** tool creates chamfers on the selected edges of an object. It adds a **Chamfer** object to the document with its corresponding representation in the [Tree view](Tree_view.md).



+++
| ![Sélection des arêtes avant de démarrer la commande.](images/PartDesign_Chamfer-01.png ) ![Réglage de la dimension du chanfrein dans les paramètres de chanfrein.](images/PartDesign_Chamfer-02.png ) ![Un élément Chamfer est ajouté dans l\'arborescence Projet.](images/PartDesign_Chamfer-03.png ) | ### Usage                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1.                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2.                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 3.                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | ### PartDesign Chamfer VS. Part Chamfer  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | -                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | -                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | -                                                                              |
+++

## Utilizare

Selecționați una, sau mai multe muchii ale unui obiect apoi porniți instrumentul fie prin click pe iconiță **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [Chanfrein](_PartDesign_Chamfer/fr.md)** din bara de instrumente, fie din meniu **Affichage → Atelier → Part Design**.
Pentru un lanț de muchii tangente una pe alta, este necesară selectarea numai a uneia dintre margini. **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, se va propaga automat în lungul lanțului .
Pentru a-l modifica **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)** după crearea sa, double-cliquer pe intrarea sa în **Vue Combinée → Projet →** pe **Chamfer** pentru a modifica, sau faceți click butonul dreapta, și selecționați **Modifier le chanfrein**.
==Opțiuni==

### Vizualizarea combinată → Sarcini 

[240px\|left](IMAGE:PartDesign_Chamfer_fr_05.png.md) {{TitleTasks|[<img src=images/PartDesign_Chamfer.png style="width:16px"> Paramètres du chanfrein}}


{{OngletTache|Size}}

: Réglez la dimension du **[16px|text-top=Chanfrein|link=PartDesign_Chamfer/fr](File:PartDesign_Chamfer.png.md) [chanfrein](_PartDesign_Chamfer/fr.md)**, en saisissant une valeur, ou en cliquant sur les flèches haut et bas. Un aperçu en temps réel est affiché dans la fenêtre 3D.
Cliquez sur **OK** pour valider.

Șanfrenul va avea întodeauna unghiul la 45°.

Lățimea maximă a șanfrenului trebuie să fie inferior celei mai micii fațetee 
==Proprietăți==

### Vue combinée → Chamfer → Vue 

<img alt="" src=images/PartDesign_Chamfer_fr_03.png‎  style="width:240px;"> {{PartOngletVue/fr}}
===Vue combinée → Chamfer → Données===
<img alt="" src=images/PartDesign_Chamfer_fr_04.png  style="width:240px;"> {{TitleProperty|Base}}


{{ProprieteDonnees|Label}}

: Nom de l\'objet (modifiable à volonté).


{{ProprieteDonnees|Placement}}

: \[(**0,00 0,00 1,00**);**0,00**;(**0,00 0,00 0,00**)\], donne l\'ensemble des données **Axis, Angle**, et, **Position** ci dessous.
Si vous sélectionnez, le titre **Placement** <img alt="Options Placement" src=images/Tache_Placement_01_fr_00.png  style="width:256px;">, un bouton avec **trois petits points** s\'affiche, en cliquant sur ce bouton **''' ... '''**, vous avez accès à la fenêtre d\'options **[Tâche Placement](Tasks_Placement/fr.md)**.

-    {{ProprieteDonnees|Angle}}: Angle de rotation par rapport aux coordonnées **X, Y, Z**

-    {{ProprieteDonnees|Axis}}: Sélection de l\'axe(s) de rotation de travail **X, Y**, ou **Z**.
    Par exemple : nous déterminons un {{ProprieteDonnees|Angle}} de **15°**, nous spécifions une valeur de **1,0 pour x** et **2,0 pour y**, cette configuration, aura pour effet, une rotation finale de la pièce qui sera de, \"**15° dans l\'axe x** \" et \"**30° dans l\'axe y** \". (Défaut, **Z = 1 = actif**)

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

### Add a chamfer 

1.  Optionally [activate](PartDesign_Body#Active_status.md) the Body to chamfer.
2.  There are several ways to select edges to chamfer:
    -   Select one or more edges of the Body individually.
    -   Select one or more faces of the Body to select all their edges.
    -   Select a feature (usually the last feature) of the Body to select all its edges. <small>(v0.20)</small> 
3.  For a chain of tangentially connected edges only a single edge needs to be selected, the chamfer will propagate along the chain.
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_Chamfer.svg" width=16px> [Chamfer](PartDesign_Chamfer.md)** button.
    -   Select the **Part Design → Apply a dress-up feature → <img src="images/PartDesign_Chamfer.svg" width=16px> Chamfer** option from the menu.
5.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
6.  The **Chamfer parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.

### Edit a chamfer 

1.  Do one of the following:
    -   Double-click the Chamfer object in the [Tree view](Tree_view.md)
    -   Right-click the Chamfer object in the [Tree view](Tree_view.md) and select **Edit Chamfer** from the context menu.
2.  The **Chamfer parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Options

-   To add edges do one of the following:
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following:
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following:
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Specify a chamfer **Type**:
    -   
        **Equal distance**
        
        : One distance is used to place both chamfer edges.

    -   
        **Two distances**
        
        : Two distances are used to place the chamfer edges.

    -   
        **Distance and angle**
        
        : A distance is used to place one chamfer edge, the placement of the other chamfer edge is defined by the angle of the chamfer.
-   Press the **<img src="images/PartDesign_Flip_Direction.svg" width=16px> Flip direction** button to flip the direction of the chamfer (deactivated for **Equal distance**).
-   Set the **Size** of the chamfer.
-   Set the **Size2** of the chamfer (only available if **Two distances** is selected).
-   Set the **Angle** of the chamfer (only available if **Distance and angle** is selected).
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Notes

-   PartDesign Chamfer should not be confused with [Part Chamfer](Part_Chamfer.md). Unless you know what you are doing, [Part Chamfer](Part_Chamfer.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).
-   Chamfers cannot completely consume the adjacent faces.

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign Chamfer object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Base|LinkSub**: Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**: If `True` the chamfered shape of the additive/subtractive parent feature will be used when the chamfer object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the chamfer itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Chamfer}}

-    **Chamfer Type|Enumeration**: The chamfer type: {{value|Equal distance}} (default), {{value|Two distances}} or {{value|Distance and Angle}}.

-    **Size|QuantityConstraint**: The first chamfer distance. The default is {{value|1 mm}}.

-    **Size2|QuantityConstraint**: The second chamfer distance. Only used if **Chamfer Type** is {{Value|Two distances}}. The default is {{value|1 mm}}.

-    **Angle|Angle**: The chamfer angle. Only used if **Chamfer Type** is {{Value|Distance and Angle}}. The default is {{value|45 °}}.

-    **Flip Direction|Bool**: If `True` the direction of the chamfer is flipped. Not used if **Chamfer Type** is {{Value|Equal distance}}. The default is `False`.

-    **Use All Edges|Bool**: If `True` all edges of the feature are chamfered, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).

## Known issues 

See [PartDesign Fillet](PartDesign_Fillet#Known_issues.md).


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/ro
