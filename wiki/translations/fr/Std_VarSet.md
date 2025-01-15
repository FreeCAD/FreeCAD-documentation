---
 GuiCommand:
   Name: Std VarSet
   Name/fr: Std Jeu de variables
   Workbenches: Tous
   Version: 1.0
   SeeAlso: Spreadsheet_Workbench/fr, DynamicData_Workbench/fr
---

# Std VarSet/fr



## Description

La commande **Std Jeu de variables** crée un jeu de variables. Un jeu de variables est un ensemble de propriétés qui peuvent être utilisées comme variables dans les [expressions](Expressions/fr.md).

![](images/Std_VarSet_Dialog.png ) 
*La fenêtre de dialogue Ajouter une propriété*



## Utilisation

1.  Faites l\'une des choses suivantes :
    -   Pour créer un nouveau jeu de variables : appuyez sur le bouton **<img src="images/Std_VarSet.svg" width=16px> [Créer un jeu de variables](Std_VarSet/fr.md)**.
    -   Pour modifier un jeu de variables existant : double-cliquez sur l\'ensemble dans la [vue en arborescence](Tree_view/fr.md).
2.  La fenêtre de dialogue **Ajouter une propriété** s\'ouvre.
3.  Entrez un **Nom** pour la propriété.
    -   Le nom doit être unique pour le jeu de variables.
    -   Seuls les caractères alphanumériques et les traits de soulignement (`A` à `Z`, `a` à `z`, `0` à `9` et `_`) sont autorisés.
    -   Le premier caractère ne peut pas être un chiffre.
    -   FreeCAD utilise la convention [UpperCamelCase](https://fr.wikipedia.org/wiki/Camel_case) pour ses noms de propriétés, ce qui signifie que chaque mot commence par une lettre majuscule, et qu\'il n\'y a pas d\'espace ou de soulignement. Lorsque l\'éditeur de propriétés affiche un tel nom, des espaces sont insérés entre les mots, ce qui rend le nom plus facile à lire. Il est conseillé de suivre cette convention.
4.  Entrez un nom de **Groupe** pour la propriété ou sélectionnez un groupe dans la liste. Les noms de groupes ont les mêmes restrictions que les noms de propriétés.
5.  Sélectionnez le **Type** de la propriété dans la liste. Voir ci-dessous pour les [types les plus courants](#Types_de_propriétés_courantes.md).
6.  Entrez une **Valeur** pour la propriété. Cette entrée accepte les unités pour les propriétés qui ont des unités.
7.  Vous pouvez cocher la case **Ajouter un autre** si vous souhaitez ajouter d\'autres propriétés.
8.  Vous pouvez saisir un **tooltip** pour la propriété.
9.  Appuyez sur le bouton **OK**.
10. Si la case **Ajouter un autre** a été cochée, la fenêtre de dialogue s\'ouvre à nouveau et une nouvelle propriété peut être ajoutée.
11. Appuyez sur le bouton **Annuler** lorsque vous avez terminé.



## Types de propriétés courantes 

FreeCAD prend en charge de nombreux types de propriétés. Le tableau ci-dessous répertorie certains des types les plus courants. Voir [Propriétés personnalisées de FeaturePython](FeaturePython_Custom_Properties/fr.md) pour plus d\'informations.

++++
| Type de propriété                | Unité par défaut (le cas échéant) | Remarque                                                                                                                                    |
+==================================+===================================+=============================================================================================================================================+
|                   | ° (ou deg)                        |                                                                                                                                             |
| {{Incode|App::PropertyAngle}}    |                                   |                                                                                                                                             |
|                               |                                   |                                                                                                                                             |
++++
|                   |                                   |                                                                                                                              |
| {{Incode|App::PropertyBool}}     |                                   | `True`                                                                                                                                    |
|                               |                                   |                                                                                                                                          |
|                                  |                                   | ou `False`, peut être utilisé dans des [expressions conditionnelles](Expressions/fr#Expressions_conditionnelles.md) |
++++
|                   | mm                                |                                                                                                                                             |
| {{Incode|App::PropertyDistance}} |                                   |                                                                                                                                             |
|                               |                                   |                                                                                                                                             |
++++
|                   |                                   | Nombre décimal                                                                                                                              |
| {{Incode|App::PropertyFloat}}    |                                   |                                                                                                                                             |
|                               |                                   |                                                                                                                                             |
++++
|                   |                                   | Nombre entier                                                                                                                               |
| {{Incode|App::PropertyInteger}}  |                                   |                                                                                                                                             |
|                               |                                   |                                                                                                                                             |
++++
|                   | mm                                | Semblable à {{Incode|App::PropertyDistance}} mais ne peut pas être négatif                                                    |
| {{Incode|App::PropertyLength}}   |                                   |                                                                                                                                             |
|                               |                                   |                                                                                                                                             |
++++
|                   |                                   | Chaîne de caractères                                                                                                                        |
| {{Incode|App::PropertyString}}   |                                   |                                                                                                                                             |
|                               |                                   |                                                                                                                                             |
++++



## Remarques

-   Les propriétés peuvent également être ajoutées aux jeux de variables existants dans l\'[éditeur d\'expressions](Expressions/fr.md) en cochant la case \"Afficher les ensembles de variables\".
-   Une propriété peut être supprimée d\'un jeux de variables via le [menu contextuel](Property_editor/fr#Menu_contextuel.md) de l\'[éditeur de propriétés](Property_editor/fr#Menu_contextuel.md).
-   Un nom de groupe peut être modifié via le même menu.
-   La commande ne peut actuellement pas définir la liste des éléments autorisés d\'une propriété {{Incode|App::PropertyEnumeration}}. Cela peut être fait via le [code en Python](FeaturePython_Custom_Properties#App:_PropertyEnumeration.md) ou dans l\'éditeur de propriétés. Les étapes de cette dernière option sont les suivantes
    1.  Sélectionnez **Afficher les propriétés cachées** dans le menu contextuel de l\'éditeur de propriétés.
    2.  Développez le nœud de la propriété.
    3.  Cliquez sur le champ **Énumération**.
    4.  Cliquez sur le bouton **...** qui apparaît.
    5.  Entrez des valeurs dans la fenêtre de dialogue **Liste** qui s\'ouvre.
    6.  Appuyez sur le bouton **OK**.



## Script


```python
import FreeCAD as App

doc = App.ActiveDocument

var_set = doc.addObject("App::VarSet", "VarSetName")
var_set.addProperty("App::PropertyInteger", "MyNumber")  # Property is added to the Base group.
var_set.MyNumber = 123
var_set.addProperty("App::PropertyString", "MyText", group="SomeGroup", doc="Some tooltip information")
var_set.MyText = "Abc"

doc.recompute()
```



---
⏵ [documentation index](../README.md) > Std VarSet/fr
