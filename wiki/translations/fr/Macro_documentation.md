# Macro documentation/fr



## Description

Toutes les macros doivent être correctement documentées de la même manière que les [commandes Gui](Gui_Command/fr.md) le sont. Elles doivent avoir leur propre page wiki et être répertoriées dans l\'une des catégories de la[Liste des Macros](Macros_recipes/fr.md).

La page [Liste des Macros](Macros_recipes/fr.md) contient une sélection de macros créées par des utilisateurs expérimentés, qui peuvent être installées directement à partir de l\'utilitaire [Gestionnaire d\'Addon](Addon_Manager/fr.md).

Voir le [Modèle GuiCommand](GuiCommand_model/fr.md) et les pages de macros comme les [Macro Loft](Macro_Loft/fr.md) et [Macro Site From Contours](Macro_Site_From_Contours/fr.md) pour voir comment documenter les macros. Au moins deux sections doivent être incluses, une section **Description** avec des informations générales sur l'utilisation et une section **Script** pour contenir le code réel de la macro. D\'autres sections peuvent être incluses si nécessaire pour expliquer plus en détail l\'utilisation de la macro.

Si une macro fournit une fonctionnalité bien définie et est bien documentée, elle pourrait éventuellement être incluse dans un [atelier](Workbenches/fr.md) nouveau ou déjà existant.

## Nouvelle page pour une macro 

Créez une nouvelle page pour la macro en commençant par le mot `Macro_`, par exemple, `Macro_Excellent_Modification`. Le lien peut être utilisé sans trait de soulignement sous la forme `<nowiki>[Macro Site From Contours](Macro_Excellent_Modification/fr.md)</nowiki>`, ce qui s\'affiche [Macro Excellent Modification](Macro_Excellent_Modification/fr.md). Les espaces sont automatiquement convertis en traits de soulignement.

Dans la nouvelle page, vous devez utiliser le [Template:Macro](Template:Macro.md) en haut, avec un minimum d\'informations:

{{Macro
|Name=Macro Excellent Modification
|Description=This macro does excellent things on existing shapes
|Author=your username
|Date=2018-11-30
}}

Vous pouvez ajouter une icône personnalisée si elle ne porte pas le même nom que la macro. Vous pouvez également ajouter d\'autres champs d\'information.

{{Macro
|Name=Macro Excellent Modification
|Icon=Macro_custom_icon.svg
|Description=This macro does excellent things on existing shapes
|Author=your username
|Date=2018-11-30
|Version=3.14516
|SeeAlso=[[Macro Regular Modification]]
}}

Lors de la traduction de la page, utilisez un modèle localisé. Vous devez spécifier le nom avec le code de langue à deux lettres (`/fr`, `/it`, `/de`) et vous devez indiquer l\'icône explicitement

{{Macro/fr
|Name=Macro Excellent Modification translated
|Icon=Macro_Excellent_Modification.svg
|Description=(Translated description)
|Author=your username
|Date=2018-11-30
}}

ou utilisez le champ `Translate`

{{Macro/fr
|Name=Macro Excellent Modification
|Translate=Macro Excellent Modification translated
|Description=(Translated description)
|Author=your username
|Date=2018-11-30
}}

-   Utilisez la page [:Special:Upload](:Special:Upload.md) pour télécharger votre icône personnalisée aux formats [SVG](SVG/fr.md) ou PNG. Elle devrait avoir le même nom que la macro.
-   Sinon, l\'icône Icon=Text-x-python.svg <img alt="" src=images/Text-x-python.svg  style="width:32px;"> par défaut sera utilisée.
-   Pour les macros utilisée en ligne de commande dans la console Python de FreeCAD utilisez Icon=Text_console_python.png <img alt="" src=images/Text_console_python.png  style="width:32px;">.
-   pour les exemples de vidéo, utilisez ce squelette d\'icône <img alt="" src=images/Text_Video_Movie.png  style="width:32px;"> et remplissez le pour obtenir ex: <img alt="" src=images/Macro_crank_simul.png  style="width:32px;"> et sauvez le avec le même nom que votre macro.

[Template:Macro](Template:Macro.md) mettra les informations sur l\'utilisation et l\'installation des macros dans chaque page.

<img alt="" src=images/Macro_Recipes_MacroHowToInstall.png  style="width:200px;"> 
*Les liens [Comment installer une macro](How_to_install_macros/fr.md) et [créer une barre d'outils](Customize_Toolbars/fr.md) se trouvent dans l'infobox de chaque page de macro*

### Ajouter la documentation sur la macro 

-   Tout comme une [Gui Command](Gui_Command/fr.md), expliquez ce que fait la macro, ses entrées, sorties, options et limitations, etc.
-   Inclure une icône personnalisée au format [SVG](SVG/fr.md) ou PNG pour votre macro afin que les autres utilisateurs puissent l'inclure dans une barre d'outils personnalisée.
-   Ajoutez une ou plusieurs images pour clarifier l\'utilisation de votre outil.
-   Si la macro effectue une tâche complexe, envisagez d\'ajouter un fichier GIF animé pour présenter ses fonctionnalités. L\'image GIF doit avoir une taille maximale de 500 x 500 pixels. Si le GIF est plus grand, l\'animation peut ne pas fonctionner. Ne redimensionnez pas le GIF car le wiki ne lira pas les GIF redimensionnés.
-   Mentionnez les macros et les ateliers associés qui complètent la fonction de cet outil.
-   Mentionnez la version de FreeCAD utilisée pour créer la macro. Ces informations peuvent être recueillies à partir de **Aide → À propos de FreeCAD → Copier dans le presse-papiers**.

:   Lorsque cette information est collée, elle ressemble à ceci


```python
OS: Ubuntu 18.04.1 LTS
Word size of OS: 64-bit
Word size of FreeCAD: 64-bit
Version: 0.18.15302 (Git)
Build type: Release
Branch: master
Hash: 2e03d2f298677b8212c22cbbc3cb20b7c80eabb5
Python version: 2.7.15rc1
Qt version: 4.8.7
Coin version: 4.0.0a
OCC version: 7.3.0
Locale: English/UnitedStates (en_US)
```

Envisagez d\'ajouter ces informations dans un bloc de commentaires à l\'intérieur du code de la macro.

### Ajouter le code de la macro 

Dans la section **Script**, utilisez [Template:MacroCode](Template:MacroCode.md) pour placer le code de la macro dans la page. Cela créera un bloc de texte utilisant la police de caractères monospace, qui préservera les espaces essentiels pour [Python](Python/fr.md).

Si le bloc de code contient les caractères {{ }} (double accolade fermante et accolade ouvrante) ou {{!}} (barre verticale), les balises <nowiki> ... </nowiki> peuvent être ajoutées explicitement pour permettre l\'affichage de ces symboles spéciaux.

Ce [Template:MacroCode](Template:MacroCode.md) génère essentiellement un bloc de balises HTML <pre> ... </pre> de sorte que celles-ci peuvent être utilisées directement au lieu d\'utiliser le modèle. Le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) recherchera le plus gros bloc de ce type et l\'utilisera pour le corps de la macro.

{{MacroCode|code=

«Your code should be here»

}}

Ou si elle comprend la barre verticale {{!}}.

{{MacroCode|code=
<nowiki>

«Your code should be here»

</nowiki>
}}

Ou

<pre>

«Your code should be here»

</pre>

Ajouter les informations d\'en-tête avant votre code réel.

{{MacroCode|code=
__Title__="Title_Of_macro"
__Author__ = "User_Name"
__Version__ = "00.11"
__Date__    = "2015-07-25"
__Comment__ = "This is the comment of the macro"
__Web__ = "http://forum.freecadweb.org/viewtopic.php?f=3&t=7384"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_Title_Of_macro"
__Icon__  = "/usr/lib/freecad/Mod/plugins/icons/Title_Of_macro"
__IconW__  = "C:/Documents and Settings/YourUserName/Application Data/FreeCAD"
__Help__ = "start the macro and follow the instructions"
__Status__ = "stable"
__Requires__ = "freecad 0.14.3706"
__Communication__ = "http://www.freecadweb.org/wiki/index.php?title=User:User_Name" 

«Your code should be here»
}}

À partir de FreeCAD 0.17, ces informations sont utilisées par le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) qui télécharge la macro à partir du dépôt [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros).

### Ajouter le code d\'une macro en dehors du wiki 

Si votre macro est trop grosse et dépasse 64 Ko, elle ne pourra pas être hébergée sur le wiki. Dans ce cas, utilisez le [Template:Codeextralink](Template:Codeextralink.md) avec un lien vers l\'adresse Web de la page du code brut (page texte du code).

Exemple :

{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/e16ad9ea7b38c0c47e42aa3019be01dd1267a620/FCInfo_en_Ver_1-20_Docked.FCMacro}}

Ce qui sera affiché comme : {{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/e16ad9ea7b38c0c47e42aa3019be01dd1267a620/FCInfo_en_Ver_1-20_Docked.FCMacro}}

Ce modèle doit être placé au début de la page de macro, dans la section **Description**. Il doit s\'agir du premier bloc de code de la page pour que du [Gestionnaire d\'Addon](Addon_Manager/fr.md) <img alt="" src=images/AddonManager.svg  style="width:24px;"> puisse le détecter automatiquement et l\'importer. Voir [Macro CirclePlus](Macro_CirclePlus/fr.md) pour un exemple d\'utilisation.


{{ColoredParagraph|'''PS:''' En cas de mise à jour dans GitHub le chemin du code brut est modifié, ne pas oublier de modifier le lien dans le modèle Codeextralink.}}

## Ajouter une nouvelle macro au dépôt du wiki 

Utilisez le template [Template:MacroLink](Template:MacroLink.md) pour inclure une ligne dans la catégorie appropriée de la [Liste des Macros](Macros_recipes/fr.md). Créez une nouvelle catégorie si nécessaire.


```python
<nowiki>
* {{MacroLink|Macro_Excellent_Modification|Macro Excellent Modification```: the macro described in a short sentence.
</nowiki>
}}

-   Le premier argument est le nom de la macro page dans le wiki.
-   Le deuxième argument est le texte affiché, qui peut être différent du nom de la page. Cela créera un lien vers le premier argument, montrant le deuxième argument comme texte.
-   Une courte description de la macro vient après les deux points.

Vous pouvez également utiliser le paramètre facultatif Icon= pour spécifier le fichier image qui sera placé au début de la ligne. L\'icône doit être un fichier [SVG](SVG/fr.md) ou PNG, et doit porter le même nom que votre macro. Si ce paramètre n\'est pas spécifié, l\'icône par défaut <img alt="" src=images/Text-x-python.svg  style="width:24px;"> sera utilisée pour le script [Python](Python/fr.md). 
```python
<nowiki>
* {{MacroLink|Icon=Macro_Excellent_Modification.svg|Macro_Excellent_Modification|Macro Excellent Modification```: the macro described in a short sentence.
</nowiki>
}}

Pour localiser ce modèle, utilisez le lien de langue approprié dans le premier argument. 
```python
<nowiki>
* {{MacroLink|Macro_Excellent_Modification/fr|Macro Excellent Modification```: (translated description)
</nowiki>
}}

## Ajouter une nouvelle macro au dépôt central 

Pour rendre une macro installable à partir du [Gestionnaire d\'Addon](Addon_Manager/fr.md), elle doit être incluse dans le dépôt central [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros).

Pour y inclure la macro, elle doit d'abord être examinée par la communauté FreeCAD du sous-forum [Python scripting and macros](https://forum.freecadweb.org/viewforum.php?f=22). Une fois que cela est fait, le dépôt des FreeCAD-macros doit être divisé, la nouvelle macro doit être incluse dans une branche, puis la branche doit être poussée et fusionnée dans le dépôt en amont.

[Category:Macros](Category:Macros.md) [Category:User Documentation](Category:User_Documentation.md)
