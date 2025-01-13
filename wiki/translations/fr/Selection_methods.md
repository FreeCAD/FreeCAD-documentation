# Selection methods/fr
## Présentation

Les [Méthodes de sélection](Selection_methods/fr.md) dans FreeCAD permettent de choisir des objets dans l\'[interface de FreeCAD](Interface/fr.md) tels que la [vue 3D](3D_view/fr.md), la [vue en arborescence](Tree_view/fr.md), la [fenêtre de sélection](Selection_view/fr.md) et d\'autres boîtes de dialogue. Certaines méthodes de sélection sont spécifiques à l\'atelier et sont documentées dans la documentation particulière de l\'atelier.



## Vue 3D 

Dans la [Vue 3D](3D_view/fr.md), il existe plusieurs façons de sélectionner des objets.



### Sélection simple 

La sélection simple avec la souris (par défaut clic gauche) et la présélection (survol) sont décrites dans la page [Navigation par la souris](Mouse_navigation/fr.md).



### Clics répétés 

Le premier clic sélectionne un sous-élément (sommet, arête ou face) de l\'objet sous la souris. Un deuxième clic sélectionne tout l\'objet.

Le troisième clic étend la sélection à son objet conteneur ([PartDesign Corps](PartDesign_Body/fr.md), [Std Part](Std_Part/fr.md) et autres). Des clics supplémentaires développent la sélection dans la chaîne de conteneurs.



### Commandes par sélection 

-   Pour sélectionner tous les objets : [Std Tout sélectionner](Std_SelectAll/fr.md).
-   Pour sélectionner par une boîte plusieurs objets principaux : [Std Sélection par boîte](Std_BoxSelection/fr.md).
-   Pour sélectionner plusieurs faces par une boîte : [Std Sélection d\'éléments par boîte](Std_BoxElementSelection/fr.md) ou [Part Sélection par boîte](Part_BoxSelection/fr.md).



## Fenêtre de sélection 

La [fenêtre de sélection](Selection_view/fr.md) affiche les noms des objets sélectionnés y compris leur nom complet dans un objet, par exemple `Unnamed#Body.Box001.Face17`.

Elle permet également d\'effectuer certaines actions comme [Std Affichage de la sélection](Std_ViewFitSelection/fr.md) et d\'envoyer l\'objet à la [Console Python](Python_console/fr.md).



### Exportation d\'objets 

*Cela devrait être dans la page [Fenêtre de sélection](Selection_view/fr.md).*

Sélectionnez un objet complexe, par exemple un [PartDesign Corps](PartDesign_Body/fr.md) ou [Std Part](Std_Part/fr.md), puis dans la [fenêtre de sélection](Selection_view/fr.md) sélectionnez à nouveau l\'objet puis appuyez sur **Ctrl** + **C** au clavier pour ouvrir la fenêtre de dialogue **Sélection des objets**. Cela permet de copier l\'objet sélectionné avec tous ou seulement certains des objets de dépendance de cet objet. Par exemple, pour un [Std Part](Std_Part/fr.md), les objets possibles à sélectionner incluent [Std Part](Std_Part/fr.md) lui-même, mais aussi son origine, ses trois axes de base (XYZ) et ses trois plans de base (XY, YZ, XZ).

Après avoir appuyé sur **OK**, les objets sélectionnés sont copiés en mémoire puis peuvent être collés dans le document pour dupliquer uniquement ces objets.

![](images/ObjectSelection.png )



*Fenêtre de dialogue de sélection d'objet lancée depuis la [fenêtre de sélection](Selection_view/fr.md).*



## Vue en arborescence 

Dans la [Vue en arborescence](Tree_view/fr.md), les éléments peuvent être sélectionnés ou désélectionnés, un par un, en maintenant la touche **Ctrl** et en cliquant avec la souris.

Une série d\'éléments peut être sélectionnée en cliquant sur le premier élément, en maintenant la touche **Maj** enfoncée et en cliquant sur le dernier élément.

La sélection d\'un seul élément affichera également ses propriétés dans l\'[éditeur de propriétés](Property_editor/fr.md).

Un double clic ouvrira le [panneau des tâches](Task_Panel/fr.md) associé contenant des actions. Veillez à fermer ce panneau de tâches avant de lancer une autre commande ou de passer à un autre poste de travail.

D\'autres méthodes sont disponibles en ouvrant le menu contextuel (clic droit) en fonction de l\'objet sélectionné ou de l\'atelier actif. Voir les informations dans la [Vue en arborescence](Tree_view/fr.md).



## Script

La sélection d\'objets est en soi une tâche graphique et n\'est donc disponible que lorsque l\'interface utilisateur graphique est chargée.

Ces méthodes peuvent être utilisées dans des [macros](Macros/fr.md) ou depuis la [Console Python](Python_console/fr.md).


```python
import FreeCADGui as Gui

Gui.Selection.addSelection
Gui.Selection.addSelectionGate
Gui.Selection.Filter
```

La méthode `addSelectionGate` empêche l\'utilisateur de sélectionner des objets non spécifiés dans la chaîne de sélection. Un symbole <img alt="" src=images/Button_invalid.svg  style="width:16px;"> apparaît lorsque le pointeur se trouve sur un élément ne faisant pas partie du groupe spécifié.


```python
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Edge")

#### or
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Face")

#### or
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Vertex")
```

Pour quitter la commande `SelectionGate()` :


```python
Gui.Selection.removeSelectionGate()
```

Voir la [Documentation du code source](Source_documentation/fr.md) et la [Std Documentation des modules Python](Std_PythonHelp/fr.md) pour plus d\'aide sur l\'utilisation de ces outils.



---
⏵ [documentation index](../README.md) > Selection methods/fr
