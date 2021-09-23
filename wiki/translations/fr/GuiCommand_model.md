---
- GuiCommand:/fr
   Name:Base ExampleCommandModel
   Name/fr:Modèle GuiCommand
   Icon:
   MenuLocation:Menu → Sousmenu → Texte de menu pour la commande 
   Workbenches:[Nom de l'atelier](Workbench_Name/fr.md)
   Shortcut:**F** **C**
   Version:0.19
   SeeAlso:
---

## Description

tant que la page est en construction, ajouter le template [Template:UnfinishedDocu](Template:UnfinishedDocu.md) en haut de la page le modèle en mettant le code ****.

Dans ce premier paragraphe, donnez une brève description de ce que fait la commande. La description peut faire référence à d\'autres ateliers tels que <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Atelier Sketcher ](Sketcher_Workbench/fr.md). (*Note de l\'éditeur:* L\'image fait 24px, pas 16px)

N\'oubliez pas d\'utiliser [Template:Version/fr](Template:Version/fr.md), [Template:VersionMinus/fr](Template:VersionMinus/fr.md), [Template:VersionPlus/fr](Template:VersionPlus/fr.md) et [Template:Obsolete/fr](Template:Obsolete/fr.md) le cas échéant.

Par exemple: La fonctionnalité pour utiliser `App::Link` {{Version/fr|0.19}} permet la liaison entre les sous-ensembles, etc\....

Ajoutez une image si possible et suivez les instructions dans [WikiPages\#Graphics](WikiPages#Graphics.md) (page en Anglais). Exemple tiré de [Part Balayage](Part_Sweep/fr.md) : ![](images/Part_Sweep_simple.png ) *Facultatif : ajoutez une légende sous l'image pour expliquer le fonctionnement de l'outil.*

La fermeture et l'ouverture des balises de traduction doivent entourer les images et d'autres éléments fixes, s'ils ne nécessitent pas de traduction. La légende doit toujours être traduite.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande:
    -   Appuyez sur le bouton **<img src="images/Std_Open.svg" width=16px> [Base ExampleCommandModel](GuiCommand_model/fr.md)**. (*Note de l\'éditeur:* Ceci utilise le modèle [Template:Button](Template:Button.md), il est nécessaire de créer un lien vers la commande comme indiqué dans cet exemple)
    -   Sélectionnez l\'option **Menu → Sous-menu → <img src="images/Std_Open.svg" width=16px> Texte du menu de la commande** dans le menu. (*Note de l\'éditeur:* Ceci utilise le modèle [Template: MenuCommand](Template:_MenuCommand.md))
    -   Sélectionnez l\'option **Submenu → <img src="images/Std_Open.svg" width=16px> Texte du menu de la commande** dans le menu contextuel [Vue en arborescence](Tree_view/fr.md) ou [Vue 3D](3D_view/fr.md). (*Note de l\'éditeur:* Ceci utilise également le modèle [Template:MenuCommand](Template:MenuCommand.md), toutes les commandes ne sont pas accessibles à partir d\'un menu contextuel)
    -   Utilisez le raccourci clavier **F** puis **C** ou **Ctrl** + **Z**. (*Note de l\'éditeur:* Ceci utilise le modèle [Template:KEY](Template:KEY.md), toutes les commandes n\'ont pas de raccourci clavier)
2.  Étapes détaillées au besoin. Certaines étapes peuvent nécessiter **Keyboard** pressions tandis que d\'autres peuvent nécessiter l\'utilisation de la souris pour cliquer sur un **Button**.
3.  D\'autres commandes peuvent devoir être référencées / utilisées. Pensez à créer un lien vers leurs pages wiki avec leurs icônes **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** ou **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.
4.  Définissez les options et appuyez sur **OK**.

## Options

-   Optionnel. Énumérez les options de commande ici. Découvrez deux exemples, **<img src="images/Draft_Line.svg" width=16px> [Draft Ligne](Draft_Line/fr.md)** et **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.

## Exemple

Optionnel.

## Remarques

-   Optionnel. Utilisez une liste à puces s\'il y a plusieurs éléments. Vous pouvez également mentionner les limitations ici.

## Propriétés

### Données


{{TitleProperty|Property Group}}

-    {{PropertyData/fr|Property Name 1}}: Description de la propriété

### Vue


{{TitleProperty|Property Group}}

-    {{PropertyView/fr|Property Name 2}}: Description de la propriété

## Script

Voir aussi : [:Category:API/fr](:Category:API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil ExampleCommandModel peut être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Object = makeExampleCommandModel(Data1, Data2)
```

-   Créer un `Object` utilisant `Data1` et `Data2`.

Exemple :


```python
import FreeCAD, Base

Model = Base.makeExampleCommandModel(FreeCAD.Data1, FreeCAD.Data2)
```

## Autre

Optionnel.

## Bloc sélectionnable 


<languages/>

<translate>



{{GuiCommand
|Name=Base ExampleCommandModel
|Icon= 
|MenuLocation=Menu → Submenu → Menu text for the command
|Workbenches=[Workbench](Workbench_Name.md)
|Shortcut=**F** **C**
|Version=0.19
|SeeAlso= 
}}

== Description ==

While the page is under construction, add the [[Template:UnfinishedDocu]] template at the top of the page by simply typing: ''''''

In this first paragraph give a short description of what the command does. The description can refer to other workbenches such as the <img src="images/Workbench_Sketcher.svg" width=24px> [Sketcher Workbench](Sketcher_Workbench.md). (''Editor note:'' The image is 24px, not 16px)

Remember to use [[Template:Version]], [[Template:VersionMinus]], [[Template:VersionPlus]] and [[Template:Obsolete]] when applicable.

For example: The feature to utilize `App::Link` <small>(v0.19)</small>  allows linking between sub-assemblies etc...

Add an image if possible, and please follow the guidelines in [Part Sweep](WikiPages#Graphics]]. Example taken from [[Part_Sweep.md):
</translate>
![](images/)
<translate>
*Optional: add a caption below the image to explain what the tool does*

Closing and opening translate tags should surround images, and other fixed elements, if they don't need to be translated. The caption should always be translated.

== Usage ==

# There are several ways to invoke the command: 
#* Press the **<img src="images/Std_Open.svg" width=16px> [Base ExampleCommandModel](GuiCommand_model.md)** button. (''Editor note:'' This uses the [[Template:Button]] template, it is necessary to link to the command as shown in this example)
#* Select the **Menu → Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the menu. (''Editor note:'' This uses the [[Template:MenuCommand]] template)
#* Select the **Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu. (''Editor note:'' This also uses the [[Template:MenuCommand]] template, not all commands can be accessed from a context menu)
#* Use the keyboard shortcut **F** then **C** or **Ctrl**+**Z**. (''Editor note:'' This uses the [[Template:KEY]] template, not all commands have a keyboard shortcut)
# Detailed steps as needed. Some steps may need **Keyboard** presses while others may require using the mouse to click on a **Button**.
# Other commands may need to be referenced/used. Consider linking to their wiki pages along with their icons **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** or **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)**.
# Set options and press **OK**.

== Options ==

* Optional. List the command options here. Check out two examples, **<img src="images/Draft_Line.svg" width=16px> [Draft Line](Draft_Line.md)** and **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)**.

== Example ==

Optional.

== Notes ==

* Optional. Use a bullet list if there are multiple items. You can also mention limitations here.

== Properties ==

=== Data ===

{{TitleProperty|Property Group}}

* **Property Name 1**: Description of the property

=== View ===

{{TitleProperty|Property Group}}

* **Property Name 2**: Description of the property

== Scripting ==

See also: [FreeCAD Scripting Basics](:Category:API]] and [[FreeCAD_Scripting_Basics.md).

The ExampleCommandModel tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

</translate>
```python
Object = makeExampleCommandModel(Data1, Data2)
```
<translate>

* Creates an `Object` using `Data1` and `Data2`.

Example:

</translate>
```python
import FreeCAD, Base

Model = Base.makeExampleCommandModel(FreeCAD.Data1, FreeCAD.Data2)
```
<translate>

== Other ==

Optional.




</translate>
{{Workbench Tools navi}} 






{{Workbench Tools navi

}} 

[Category:Wiki:Example](Category:Wiki:Example.md)
