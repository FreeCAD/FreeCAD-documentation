# PartDesign Preferences/fr
## Introduction

L\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md) et l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) utilisent les mêmes préférences. Elles se trouvent dans l\'[éditeur de préférences](Preferences_Editor/fr.md). Dans le menu, sélectionnez **Édition → Préférences...** puis **<img src="images/Preferences-part_design.svg" width=16px> Part/PartDesign**.Ce groupe n\'est disponible que si l\'un des ateliers a été chargé dans la session FreeCAD en cours.

Certaines préférences avancées ne peuvent être modifiées que dans l\'[éditeur de paramètres](Std_DlgParameter/fr.md). Voir [Réglage fin](Fine-tuning/fr#Atelier_PartDesign.md).

Cette page a été mise à jour pour la version 1.0.



## Préférences disponibles 

Il y a trois pages : [Général](#Général.md), [Vue des formes](#Vue_des_formes.md) et [Apparence des formes](#Apparence_des_formes.md).



### Général

<img alt="" src=images/Preferences_PartDesign_Page_General.png  style="width:400px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                                               | Description                                                                                                                                                                       |
+===================================================================================================+===================================================================================================================================================================================+
|                                                                                    | Si coché, le [B-Rep](https://fr.wikipedia.org/wiki/B-Rep) du modèle est [validé](Part_CheckGeometry/fr.md) après les [opérations booléennes](Part_Boolean/fr.md). |
| **Vérifier les modèles automatiquement après une opération booléenne**                |                                                                                                                                                                                   |
|                                                                                                |                                                                                                                                                                                   |
+++
|                                                                                    | Si coché, le modèle est [affiné](Part_RefineShape/fr.md) après les [opérations booléennes](Part_Boolean/fr.md).                                                   |
| **Affiner les modèles automatiquement après une opération booléenne**                 |                                                                                                                                                                                   |
|                                                                                                |                                                                                                                                                                                   |
+++
|                                                                                    | Si coché, le modèle est [affiné](Part_RefineShape/fr.md) après les modifications apportées aux esquisses sources des objets.                                              |
| **Affiner automatiquement le modèle après une opération d'esquisse**                  |                                                                                                                                                                                   |
|                                                                                                |                                                                                                                                                                                   |
+++
|                                                                                    | Si la case est cochée, les corps peuvent avoir plusieurs solides. {{Version/fr|1.0}}                                                                                |
| **Autoriser plusieurs solides dans un corps de PartDesign par défaut (expérimental)** |                                                                                                                                                                                   |
|                                                                                                |                                                                                                                                                                                   |
+++



### Vue des formes 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_view.png  style="width:400px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                   | Description                                                                                                                                                                                                                             |
+=======================================================================+=========================================================================================================================================================================================================================================+
|                                                        | La [déviation linéaire](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) maximale des objets [tesselés](#Tesselation.md) par rapport à leur surface.            |
| **L'écart maximal suivant la  boîte englobant le modèle** |                                                                                                                                                                                                                                         |
|                                                                    |                                                                                                                                                                                                                                         |
+++
|                                                        | La [déviation angulaire](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) maximale d\'une section d\'un objet [tesselé](#Tesselation.md) à la section suivante. |
| **Déviation angulaire maximale**                          |                                                                                                                                                                                                                                         |
|                                                                    |                                                                                                                                                                                                                                         |
+++



### Apparence des formes 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_appearance.png  style="width:400px;">

Une explication des couleurs peut être trouvée [ici](Part_ColorPerFace/fr#Utilisation.md).

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                        | Description                                                                                                                                                                                                                                                              |
+============================================================+==========================================================================================================================================================================================================================================================================+
|                                             | La couleur diffuse pour les nouvelles formes. Si l\'option **Aléatoire** est définie, une couleur aléatoire est utilisée à la place.                                                                                                           |
| **Couleur des formes**                         |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur ambiante pour les nouvelles formes. {{Version/fr|1.0}}                                                                                                                                                                                          |
| **Couleur ambiante des formes**                |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur émissive pour les nouvelles formes. {{Version/fr|1.0}}                                                                                                                                                                                          |
| **Couleur émissive des formes**                |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur spéculaire pour les nouvelles formes. {{Version/fr|1.0}}                                                                                                                                                                                        |
| **Couleur spéculaire des formes**              |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La transparence pour les nouvelles formes. {{Version/fr|0.21}}                                                                                                                                                                                             |
| **Transparence des formes**                    |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La brillance des nouvelles formes. {{Version/fr|1.0}}                                                                                                                                                                                                      |
| **Brillance des formes**                       |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur des lignes pour les nouvelles formes.                                                                                                                                                                                                                         |
| **Couleur des traits**                         |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La largeur de ligne pour les nouvelles formes.                                                                                                                                                                                                                           |
| **Largeur des lignes**                         |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur des nouveaux [sommets](Glossary/fr#Vertex.md).                                                                                                                                                                                                        |
| **Couleurs des sommets**                       |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La taille des nouveaux [sommets](Glossary/fr#Vertex.md).                                                                                                                                                                                                         |
| **Taille des sommets**                         |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur des [boîtes englobantes](Property_editor/fr#Vue.md) dans la vue 3D.                                                                                                                                                                                   |
| **Couleur des boîtes englobantes**             |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La taille de la police des [boîtes englobantes](Property_editor/fr#Vue.md) dans la vue 3D. {{Version/fr|1.0}}                                                                                                                                      |
| **Taille de la police des boîtes englobantes** |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | Si cette case cochée, la couleur du côté intérieur des faces sera la même que celle du côté extérieur. Si cette case n\'est pas cochée, la [couleur du rétroéclairage](Preferences_Editor/fr#Vue_3D.md), si elle est activée ou le noir sera utilisé à la place. |
| **Rendu des deux côtés**                       |                                                                                                                                                                                                                                                                          |
|                                                         |                                                                                                                                                                                                                                                                          |
+++
|                                             | La couleur du texte pour les annotations du document.                                                                                                                                                                                                                    |
| **Couleur du texte**                           |                                                                                                                                                                                                                                                                          |
|                                                         | Actuellement, ces annotations ne peuvent être ajoutées qu\'en utilisant la [console Python](Python_console/fr.md) :                                                                                                                                              |
|                                                            |                                                                                                                                                                                                                                                                          |
|                                                            | obj = App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                                                                         |
+++



## Tesselation

Afin d\'afficher efficacement un objet, sa surface est [téssélée](https://en.wikipedia.org/wiki/Tessellation_(computer_graphics)), elle est affichée avec quelques petites déviations par rapport à sa surface réelle. Cela s\'applique non seulement aux modèles PartDesign, mais aussi à d\'autres objets dans FreeCAD.

La limite inférieure pour le tesselation est de 0,01%. Si vous voulez vraiment passer plus de temps, vous pouvez réduire encore la limite inférieure en ouvrant l\'[éditeur de propriétés](Std_DlgParameter/fr.md).

Dans l\'éditeur de paramètres, naviguez vers **BaseApp → Preferences → Mod → Part**, faites un clic droit sur **MeshDeviation** et choisissez **Changer la valeur** dans le menu contextuel. Réglez la valeur sur la tessellation minimale de votre choix. N\'oubliez pas que la valeur est en %, c\'est-à-dire que pour une valeur de 0,005%, vous devez entrer {{Value|0.00005}}. La plus petite valeur possible est {{Value|1e-7}}. Notez que dans le [réglage des préférences](Preferences_Editor/fr.md), vous verrez toujours 0,01% même si vous avez défini une valeur inférieure.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/fr
