# PartDesign Preferences/fr
{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md) et l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) utilisent les mêmes préférences. Elles se trouvent dans la section <img alt="" src=images/Preferences-part_design.svg  style="width:24px;"> **Part design** de l\'éditeur de préférences [Réglage des préférences](Preferences_Editor/fr.md). Cette section ne sera disponible que si l\'un des ateliers a été chargé dans la session FreeCAD en cours.

## Préférences disponibles 

Il y a trois onglets : Général, Vue de la forme et Apparence de la forme.

### Général

Dans l\'onglet *Général*, vous pouvez spécifier les éléments suivants:

+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nom                                                                                | Description                                                                                                                                                                      |
+====================================================================================+==================================================================================================================================================================================+
|                                                                     | Si coché, le [BRep](https://fr.wikipedia.org/wiki/B-Rep) du modèle est [validé](Part_CheckGeometry/fr.md) après les [opérations booléennes](Part_Boolean/fr.md). |
| **Vérifier les modèles automatiquement après une opération booléenne** |                                                                                                                                                                                  |
|                                                                                 |                                                                                                                                                                                  |
+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                     | Si coché, le modèle est [affiné](Part_RefineShape/fr.md) après les [opérations booléennes](Part_Boolean.md).                                                     |
| **Affiner les modèles automatiquement après une opération booléenne**  |                                                                                                                                                                                  |
|                                                                                 |                                                                                                                                                                                  |
+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                     | Si coché, le modèle est [affiné](Part_RefineShape/fr.md) après les modifications apportées aux esquisses sources des objets.                                             |
| **Affiner automatiquement le modèle après une opération d'esquisse**   |                                                                                                                                                                                  |
|                                                                                 |                                                                                                                                                                                  |
+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_General.png )

### Vue de la forme 

Dans l\'onglet *Vue de la forme*, vous pouvez spécifier les éléments suivants:

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nom                                                                   | Description                                                                                                                                                                                                                          |
+=======================================================================+======================================================================================================================================================================================================================================+
|                                                        | Déviation maximale [déviation linéaire](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) des objets [tesselés](#Tesselation.md) par rapport à leur surface.  |
| **L'écart maximal suivant la  boîte englobant le modèle** |                                                                                                                                                                                                                                      |
|                                                                    |                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                        | Déviation [angulaire maximale](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) d\'une section d\'un objet [tesselé](#Tesselation.md) à la section suivante. |
| **Déviation angulaire maximale**                          |                                                                                                                                                                                                                                      |
|                                                                    |                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Apparence de la forme 

Dans l\'onglet *Apparence de la forme*, vous pouvez spécifier les éléments suivants:

+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Nom                                            | Description                                                                                                                                                                                                                                                                     |
+================================================+=================================================================================================================================================================================================================================================================================+
|                                 | Couleur des nouvelles formes. Si l\'option **Random** est définie, une couleur aléatoire est utilisée à la place.                                                                                                                                     |
| **Couleur de la forme**            |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Couleur de ligne pour les nouvelles formes.                                                                                                                                                                                                                                     |
| **Couleur de trait**               |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Epaisseur de ligne pour les nouvelles formes.                                                                                                                                                                                                                                   |
| **Épaisseur de ligne**             |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Couleur des nouveaux [vertices](Glossary/fr#Vertex.md) (sommet)                                                                                                                                                                                                         |
| **Couleur de sommet**              |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Taille des nouveaux [vertices](Glossary/fr#Vertex.md)                                                                                                                                                                                                                   |
| **Taille de sommet**               |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Couleur des [bounding boxes](Property_editor/fr#Vue.md) dans la vue 3D.                                                                                                                                                                                                 |
| **Couleur de la boîte englobante** |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Si coché, la couleur de la face intérieure des faces sera la même que celle de la face extérieure. Si cette case n\'est pas cochée, la couleur [Couleur du rétroéclairage](Preferences_Editor/fr#Vue_3D.md), si elle est activée ou le noir seront utilisés à la place. |
| **Two-side rendering**             |                                                                                                                                                                                                                                                                                 |
|                                             |                                                                                                                                                                                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Couleur du texte pour les annotations du document. Il n\'existe actuellement aucun dialogue permettant d\'ajouter des annotations aux documents. Les annotations ne peuvent être ajoutées qu\'en utilisant la console Python avec cette commande :                              |
| **Couleur du texte**               |                                                                                                                                                                                                                                                                                 |
|                                             | obj=App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                                                                                  |
|                                                |                                                                                                                                                                                                                                                                                 |
|                                                | Cette console est affichée à l\'aide du menu **Affichage → Panneaux → Console Python**.                                                                                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

## Tesselation

Afin d\'afficher efficacement un objet, sa surface est [téssélée](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)): il est montré avec de petits écarts par rapport à sa surface réelle. Cela s\'applique non seulement aux modèles PartDesign, mais également aux autres objets de FreeCAD.

La limite inférieure pour le tesselation est de 0,01%. Si vous voulez vraiment passer plus de temps, vous pouvez réduire encore la limite inférieure en ouvrant le menu **Outils → Éditer paramètres**. Ceci ouvre l\'éditeur de paramètres dans lequel vous accédez à **BaseApp → Preferences → Mod → Part**.

Cliquez avec le bouton droit de la souris sur **Mesh deviation** dans le menu contextuel **Change value**. Définissez la valeur sur la tesselation minimale de votre choix. Veuillez garder à l'esprit que la valeur est en %, c'est-à-dire que pour une valeur de 0,005%, vous devez entrer \"0,00005\". La plus petite valeur possible est 1e-7. **Remarque:** dans le menu Préférences, vous verrez toujours 0,01% même si vous définissez une valeur inférieure.





{{PartDesign Tools navi

}} 

[Category:Preferences](Category:Preferences.md)

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/fr
