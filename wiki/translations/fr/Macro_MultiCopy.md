# Macro MultiCopy/fr
{{Macro
|Name=Macro MultiCopy
|Icon=MultiCopy-reduced.png
|Description=MultiCopy permet la duplication (copier-coller) de plusieurs objets FreeCAD qui peuvent être étiquetés séquentiellement et de manière personnalisée.
|Author=Melwyncarlo
|Date=2021-03-18
|Version=1.0.1
|FCVersion={{VersionPlus/fr|0.17}}
|Download=[https://github.com/melwyncarlo/MultiCopy/blob/main/MultiCopy.zip?raw=true MultiCopy.zip]
|Links=[https://github.com/melwyncarlo/MultiCopy Github personnel- MultiCopy]<br>[https://github.com/FreeCAD/FreeCAD-macros/tree/master/Conversion Github FC - MultiCopy]<br>[https://forum.freecadweb.org/viewtopic.php?f=22&t=56753 FC Forum - MultiCopy]
}}

## Description

**\'MultiCopy**\' est une macro créée et destinée à être utilisée dans l\'application FreeCAD. MultiCopy permet la duplication (copier-coller) de plusieurs objets FreeCAD qui peuvent être étiquetés séquentiellement et de manière personnalisée.

![](images/MultiCopy-reduced.png )    Voici l\'icône **MultiCopy Macro**.

La macro MultiCopy peut être téléchargée en utilisant le [Gestionnaire d\'addons](Std_AddonMgr/fr.md) intégré au logiciel FreeCAD.

####  Caractéristiques principales 

-   Deux méthodes de saisie : par la souris ou par le clavier (commandes de collage de code).
-   Méthodes de copie standard et de copie simple prises en charge
-   Duplication dans deux documents différents
-   Suppression des objets sélectionnés après la duplication
-   Duplication avec ou sans dépendances
-   Ajout de séparateurs d\'étiquettes personnalisés
-   Ajout d\'une numérotation supplémentaire aux étiquettes
-   Types de numérotation : Chiffres ordinaires, chiffres romains majuscules/minuscules et caractères alphabétiques majuscules/minuscules.
-   Des \"commandes de collage de code\" uniques qui permettent la duplication multiple de manière procédurale ainsi que dans des boucles imbriquées.
-   Les deux méthodes CUI et GUI disponibles

\[\[<File:Macro_MultiCopy_Main_Dialog.png%7Cframe%7Ccenter%7Calt=Macro_MultiCopy_Main_Dialog.png>\|


<div style="text-align: center">

Légende : boîte de dialogue principale de la macro MultiCopy


</div>

\]\]

## Installation

####  Linux

MultiCopy peut être installé manuellement, de manière similaire à l\'installation de Windows, ou en utilisant le terminal de commande et ses commandes pertinentes, comme indiqué dans le fichier [INSTALL](https://raw.githubusercontent.com/melwyncarlo/MultiCopy/main/INSTALL.sh).

Par défaut, le terminal de commande Linux peut être lancé en appuyant simultanément sur les touches suivantes du clavier :

**Control** + **Alt** + **T**

####  Windows

MultiCopy peut être installé à l\'aide des deux étapes suivantes :

1.  Téléchargez le fichier [MultiCopy.zip](https://github.com/melwyncarlo/MultiCopy/blob/main/MultiCopy.zip?raw=true) file.
2.  Extrayez le contenu du fichier ZIP dans l\'emplacement du répertoire de la macro utilisateur de FreeCAD.

Par défaut, le répertoire de la macro utilisateur de FreeCAD doit être situé à :

C:/Users/User_Name/AppData/Roaming/FreeCAD/Macro

##  Utilisation - Méthode GUI 

MultiCopy peut être chargé en effectuant les étapes suivantes :

1.  Lancez l\'application **FreeCAD**.
2.  Allez dans **Macro → Macros ...**.
3.  Cliquez sur l\'onglet **Macros utilisateur** dans la boîte de dialogue contextuelle.
4.  Sélectionnez **MultiCopy.FCMacro**.
5.  Cliquez sur **Execute**.

Avant de charger la macro MultiCopy, sélectionnez d\'abord un ou plusieurs objets dans le doccument FreeCAD actif, puis chargez la macro. Ensuite, suivez les instructions de la boîte de dialogue, remplissez les entrées requises, et cliquez sur le bouton \'Paste\'. En cas d\'erreur ou d\'avertissement, vous en serez automatiquement informé. Si vous rencontrez une erreur inattendue, communiquez-la en mentionnant la version de FreeCAD, en retraçant les étapes suivies et en précisant si un résultat a été généré (et dans quelle mesure).

##  Utilisation - Méthode CUI (console Python) 

Avant d\'exécuter l\'opération MultiCopy, sélectionnez d\'abord un ou plusieurs objets dans le document FreeCAD actif.

###  Pour lancer la boîte de dialogue GUI: 


```python
import MultiCopy

MultiCopy.Launch()
```

###  Pour effectuer l\'opération sur le terminal: 

La commande MultiCopy est la suivante :


```python
Run (paste_code, copy_type=True, delete_selection=False, paste_document_label=None)
```

Les paramètres de la commande MultiCopy sont les suivants :

    1. Name              : paste_code
       Type              : String
       Is Optional       : False
       Description       : The paste code commands string.
                           For indentations, use \'\\t\'.
                           For line breaks, use \'\\n\'.

    2. Name              : copy_type
       Type              : Boolean or String or Integer
       Is Optional       : True
       Description       : The copy operation mode.
       Acceptable Values : 'Standard', 'Simple', 
                           True, False, 
                           1, 2
       Default Value     : True

    3. Name              : delete_selection
       Type              : Boolean
       Is Optional       : True
       Description       : If true, the selected objects are 
                           deleted after the MultiCopy operation.
       Default Value     : False

    4. Name              : paste_document_label
       Type              : String or FreeCAD.Document
       Is Optional       : True
       Description       : The label of the document to paste to, 
                           or the document object itself.
       Default Value     : FreeCAD.ActiveDocument

####  Exemple 1: 

Pour coller les objets sélectionnés dans le document actuellement actif comme une copie standard, et pour ne pas supprimer les sélections après l\'opération.


```python
import MultiCopy

some_paste_code_commands = 'from 1 to 2 :\n\t[1] = SomeName_{n#}'
MultiCopy.Run(some_paste_code_commands)
```

####  Exemple 2: 

Pour coller les objets sélectionnés dans un autre document comme une simple copie, et pour supprimer les sélections après l\'opération.


```python
import MultiCopy

some_paste_code_commands = 'from 1 to 2 :\n\t[1] = SomeName_{n#}'
MultiCopy.Run(some_paste_code_commands, True, True, 'SomeDocumentLabel')
```

##  Commandes de collage de code 

\[\[<File:Macro_MultiCopy_Commands.png%7Cframe%7Ccenter%7Calt=Macro_MultiCopy_Commands.png>\|


<div style="text-align: center">

Légende : Liste des commandes de code à coller de la macro MultiCopy


</div>

\]\]

Les deux commandes récurrentes dans leur forme générique sont les suivantes :

1.  from ... to ... :
2.  [...] = ...

Pendant la saisie des Commandes de code de collage dans la zone de texte de saisie concernée, il y a **trois** indications sous forme de bandes colorées situées en bas de la zone de texte :

1.  **Noir** indique que la zone de texte est focalisée, et que l\'utilisateur est en train d\'y saisir les commandes du code à coller.
2.  **Rouge** indique que la zone de texte est en dehors de la focalisation, et que les commandes entrées par l\'utilisateur sont SYNTAXIQUEMENT INCORRECTES.
3.  **Vert** indique que la zone de texte est hors focus et que les commandes saisies par l\'utilisateur sont SYNTAXIQUEMENT CORRECTES.

####  Exemple 1 

    from 1 to 3 :
         [1] = {1}-Something_{n#}

Les valeurs **1** et **3** représentent la plage de duplication où les deux valeurs sont INCLUSIVES. La première valeur (de) doit toujours être INFÉRIEURE OU ÉGALE à la deuxième valeur (à). Les valeurs (ensemble) peuvent prendre la forme de l\'un des cinq types de numérotation (**Vérifiez \'Caractéristiques principales**\').

[1] représente le **premier objet** d\'une liste supposée d\'objets sélectionnés par l\'utilisateur.
{1} représente le **nom de l\'étiquette** du premier objet.
{n#} représente une **étiquette de numérotation** du type \'Numériques ordinaires\'\'. (on y reviendra, plus tard)

**REMARQUEZ** que des **retraits de tabulation** corrects sont cruciaux pour les commandes ; ils ne peuvent pas être remplacés par des espaces.

Les crochets ne sont utilisés que pour les commandes du deuxième type générique. Les crochets **\[** et **\]** se trouvent toujours à gauche de la commande ; tandis que les parenthèses **{** et **}** se trouvent toujours à droite de la commande.

Laissons le nom de l\'étiquette originale du premier objet être **Corps**. Ensuite, les commandes ci-dessus produiraient un ensemble d\'objets dupliqués (du premier objet), chacun étiqueté comme suit :

    Body-Something_1
    Body-Something_2
    Body-Something_3

####  Représentation de l\'objet 

Soit **i** un i-ème objet arbitraire d\'une liste supposée d\'objets sélectionnés par l\'utilisateur.
[i] représente le **i-ième objet** sans dépendances (par défaut).
[i|0] représente le **i-ième objet** sans dépendances (autre forme).
[i|1] représente le **i-ième objet** AVEC des dépendances incluses.

####  Les étiquettes de numérotation 

code\>{n#} ou {N#} sont du type \"Chiffres ordinaires\".
{R#} ou {ru#} ou {RU#} sont du type \"Chiffres romains majuscules\".
{r#} ou {rl#} ou {RL#} sont du type \"Chiffres romains minuscules\".
{A#} ou {au#} ou {AU#} sont du type \"Alphabet majuscule\".
{a#} ou {al#} ou {AL#} sont de type \"Alphabet minuscule\".

Une étiquette de numérotation peut avoir deux options supplémentaires :

1.  {n#X} Padding (de chiffres \'X\').
2.  {n#X|i1} Assignation d\'un niveau de boucle imbriquée (à une boucle étiquetée \'i1\')

Dans le cas d\'une affectation de niveau de boucle imbriquée SANS remplissage, faites :

1.  {n#0|i1} OU
2.  {n#|i1}

####  Exemple 2 

    from 1 to 2 : i1 :
         from a to b : i2 :
              [1|1] = Pasted-{1}-{n#3|i1}-{AU#0|i2}

Ici, les objets sont collés ainsi que les dépendances. L\'étiquette \'Chiffre ordinaire\' a un padding de \'3\', et l\'étiquette \'Alphabet majuscule\' a un padding de \'0\'.

**NOTEZ** comment la boucle \'from-to\' utilise l\'alphabet en minuscules ; mais l\'étiquette sera sortie en majuscules.
Les commandes ci-dessus produiraient un ensemble d\'objets dupliqués (du premier objet) chacun étiqueté comme suit :

    Pasted-Body-001-A
    Pasted-Body-001-B
    Pasted-Body-002-A
    Pasted-Body-002-B

\[\[<File:Macro_MultiCopy_Input_Signal.png%7Cframe%7Ccenter%7Calt=Macro_MultiCopy_Input_Signal.png>\|


<div style="text-align: center">

Légende : macro MultiCopy \'Commandes de code à coller\'.
Indication pour ENTREE


</div>

\]\]

\[\[<File:Macro_MultiCopy_Incorrect_Signal.png%7Cframe%7Ccenter%7Calt=Macro_MultiCopy_Incorrect_Signal.png>\|


<div style="text-align: center">

Légende : macro MultiCopy \'Commandes de code à coller\'
Indication pour INCORRECT


</div>

\]\]

\[\[<File:Macro_MultiCopy_Correct_Signal.png%7Cframe%7Ccenter%7Calt=Macro_MultiCopy_Correct_Signal.png>\|


<div style="text-align: center">

Légende : macro MultiCopy \'Commandes de code à coller\'
Indication pour CORRECT


</div>

\]\]

##  Remarques

   
  \(1\)   Il y a quelques inévitables conflits d\'appellation entre les chiffres romains et les caractères alphabétiques, par exemple : c, v, i, x, etc.
  \(2\)   Par conception, les chiffres romains ont la priorité sur les caractères alphabétiques.
  \(3\)   Les dépendances ne s\'appliquent qu\'à la \"copie standard\" ; leur application à la \"copie simple\" sera automatiquement ignorée.
          
   

## Script


{{MacroCode|code=

__Title__         = "MultiCopy"
__Author__        = "Melwyncarlo"
__Version__       = "1.0.1"
__Date__          = "2021-03-18"
__Comment__       = "MultiCopy allows the duplication (copy and paste) of "\
                    "multiple FreeCAD objects that can be labelled sequentially "\
                    "and in a custom manner."
__Web__           = "https://github.com/melwyncarlo/MultiCopy"
__Wiki__          = "http://www.freecadweb.org/wiki/index.php?title=Macro_MultiCopy"
__Icon__          = "MultiCopy_UI_Files/MultiCopy.svg"
__Help__          = "Select one or more FreeCAD objects, then click on the "\
                    "MultiCopy button/macro, and follow the instructions in the dialog box."
__Status__        = "stable"
__Requires__      = "Freecad >= v0.17"
__Communication__ = "https://github.com/melwyncarlo/MultiCopy/issues"
__Files__         = "MultiCopy_UI_Files/MultiCopy_Main_Dialog.ui, "\
                    "MultiCopy_UI_Files/MultiCopy_Commands_Dialog.ui, "\
                    "MultiCopy_UI_Files/mc_d_imgs.gif, "\
                    "MultiCopy_UI_Files/MultiCopy.svg"



#  OS: Ubuntu 18.04.5 LTS
#  Word size of OS: 64-bit
#  Word size of FreeCAD: 64-bit
#  Version: 0.18.4.
#  Build type: Release
#  Python version: 3.6.8
#  Qt version: 5.9.5
#  Coin version: 4.0.0a
#  OCC version: 7.3.0
#  Locale: English/UnitedKingdom (en_GB)

#  OS: Ubuntu 18.04.5 LTS (LXDE/Lubuntu)
#  Word size of OS  : 64-bit
#  Word size of FreeCAD: 64-bit
#  Version: 0.19
#  Build type: Release
#  Branch: unknown
#  Hash: 32200b604d421c4dad527fe587a7d047cf953b4f
#  Python version: 3.6.9
#  Qt version: 5.9.5
#  Coin versio: 4.0.0a
#  OCC version: 7.3.0
#  Locale: English/UnitedKingdom (en_GB)



}}


{{Codeextralink|https://raw.githubusercontent.com/melwyncarlo/MultiCopy/main/MultiCopy.FCMacro}}

## Liens

\[1\] [Dépôt Github de MultiCopy](https://github.com/melwyncarlo/MultiCopy)
\[2\] [Dépôt Github des macros FreeCAD - MultiCopy](https://github.com/FreeCAD/FreeCAD-macros/tree/master/Conversion)
\[3\] [Page de discussion du forum FreeCAD - MultiCopy](https://forum.freecadweb.org/viewtopic.php?f=22&t=56753)



---
⏵ [documentation index](../README.md) > Macro MultiCopy/fr
