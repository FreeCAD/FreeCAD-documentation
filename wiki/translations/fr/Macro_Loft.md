# Macro Loft/fr
{{Macro/fr
|Name=Macro Loft
|Icon=FCCreaLoft.png
|Description=Crée un lissage avec les fils sélectionnés. Spécialement écrit pour un lissage facile avec des lignes générées par la [https://www.freecadweb.org/wiki/Macro_Texture Macro Texture] (mais peut convenir et être utilisé pour les lofts courants)
|Author=Mario52
|Version=00.04
|Date=2019-07-03
|Download=[https://www.freecadweb.org/wiki/images/2/29/FCCreaLoft.png ToolBar Icon]
|SeeAlso= [32px|FCTexture](File:FCTexture.png.md) [Macro_Texture](Macro_Texture/fr.md)
|FCVersion=All
}}

## Description

Macro spécialement écrite pour un lissage facile avec des lignes générées par la [Macro Texture](Macro_Texture/fr.md) (mais peut convenir et être utilisé pour les lissages courants)
{{Codeextralink|https://gist.githubusercontent.com/mario52a/c477f892233d6abe02df5e97af828ff4/raw/d633193c577e8257ef458b8c1824d1047c3c6613/Macro_FCCreaLoft.FCMacro}}

<img alt="" src=images/Texture_001_Logo.png  style="width:480px;"> 
*Texture_001_Logo*

## Utisation

Copiez la macro et son icône dans votre répertoire de macro habituelle.

-   ****Sort**** : Trie les données entrées dans la macro.
-   ****Reverse**** : Reverse l\'ordre des données dans la macro.
-   ****Reset** / **Upgrade****: Ce bouton a plusieurs fonctions:
    1.  Si aucune sélection n\'est faite avant l\'ouverture de la macro le bouton **Upgrade** est affiché.
        Sélectionnez les objets dans la vue 3D ou dans la vue combinée et cliquez sur ce bouton pour valider les sélections dans la macro, le bouton change alors en **Reset**.
    2.  Si un ou plusieurs objets sont sélectionnés avant l\'ouverture de la macro le bouton **Reset** est affiché.
        Tous les objets sélectionnés sont affichés dans la fenêtre de la macro.
        Après avoir fait un triage **Sort** ou un triage inverse **Reverse** des données affichées, ce bouton **Reset** est affiché, s\'il est utilisé, l\'ordre des données reprend son ordre d\'entrée original.
        Si vous cliquez dans la vue 3D pour désélectionner les objets ce bouton efface les données contenues dans la mémoire de la macro.
        Si vous ajoutez un ou plusieurs objet(s) dans votre liste ce bouton met à jour les données avec vos nouvelles entrées.
-   ****Select all**** : Selectionne tous les objets dans la vue 3D.
-   **SpinBox** : Ce SpinBox vous permet de \"sauter\" x lignes (Défaut 1 tous les objets sont traités).
-   ****Quit**** : Quitte la macro.
-   **CheckBox** Si la case à cocher est validée le travail est visible en temps réel si elle n\'est pas cochée seul la barre défilement est active (cette méthode est plus rapide) (Cochée par défaut).
-   ****Launch the Lofting**** : Lance le \"Lofting\" efface toutes les donnée dans la macro la remet à zéro. Le nombre de sélections est affiché dans le bouton et le nombre réel qui sera traité si le spinBox \"Jump\" a été utilisé.

### L\'interface

<img alt="FCCreaLoft002" src=images/Macro_FCCreaLoft_01.png  style="width:400px;"> 

## Script

L\'icone pour votre barre d\'outils <img alt="" src=images/FCCreaLoft.png  style="width:64px;">

Téléchargez la macro sur Gist [**Macro\_FCCreaLoft.FCMacro**](https://gist.github.com/mario52a/c477f892233d6abe02df5e97af828ff4)

## Liens

La discussion sur le forum [Texture](http://forum.freecadweb.org/viewtopic.php?f=24&t=5893&start=10)

La macro [Macro Texture](Macro_Texture/fr.md)

## Version

version 00.00 : 06/02/2016

ver 00.02 : 09/02/2016 : Ajout du bouton \"Select all\" et petite option affichée dans le bouton de lancement (nombre de sélections) et (nombre réel de lissages).

ver 00.03 : 09/02/2016 : minor (affichage sur le bouton Launch)

ver 00.04 : 03/07/2019 : adapté pour Python 3



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Loft/fr
