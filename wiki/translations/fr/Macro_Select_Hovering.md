# Macro Select Hovering/fr
{{Macro/fr
|Name=Macro Select Hovering
|Icon=Macro_Select_Hovering.png
|Description=Cette macro sélectionne au choix Face, Bord, Sommet juste en survolant la souris sur les objets.<br/>PS : pour désélectionner une face (ou autre) cliquez sur le bouton **Pause grab** et utiliser la procédure standard : CTRL + Click
|Author=Mario52
|Version=00.04
|Date=2024-01-11
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/d/d8/Macro_Select_Hovering.png Icône de la barre d'outils]
}}

## Description

Cette macro sélectionne au choix Face, Edge, Vertex se trouvant sous la souris.

![Macro Select Hovering](images/Select_Hovering00.gif )


{{Codeextralink|https://gist.githubusercontent.com/mario52a/7ebe6b3fd047441114d9d0e08ceddd63/raw/f9dea03a0327b48c76a7c3e9d7cd391b5093a8cf/Macro%2520Select%2520Hovering.FCMacro}}

![Macro Select Hovering](images/Macro_Select_Hovering_00.png )

PS : pour désélectionner une face (ou autre) cliquez sur le bouton **Pause grab** et utiliser la procédure standard : CTRL + Click



## Utilisation

Survoler l\'objet avec la souris.

#### Section Face 


{{CheckBox}}

Select Face → 3 nombre de face(s) {{LineEdit|300.0}} surface totale des sélections {{LineEdit|100.0}} surface de la dernière face sélectionnée

#### Section Edge 


{{CheckBox}}

Select Edge → 4 nombre de bord(s) sélectionné(s) {{LineEdit|40.0}} longueur totale des sélections {{LineEdit|10.0}} longueur de la dernière sélection

#### Section Vertex 


{{CheckBox}}

Select Vertex → 1 nombre de vertex

#### Section Main 

Le titre affiche l\'information de :

-   ( Obj: 1 ) : nombre d\'objet(s) sélectionné(s)
-   ( Sub: 8 ) : nombre de Sub objet(s) sélectionné(s)
-   ( Tot: 9 ) : Somme de Obj + Sub


{{LineEdit|Unnamed: Box. Face6 (1.34,2.64,10.0)}}

-   Affiche une petite info sur les objets sous le curseur


{{ComboBox|Unnamed: 1 : (8 sel.) (Obj. 1, Fa. 3, Ed. 4, Ve. 1) }}

-   Nom du document
-   8 sélections
-   Obj. 1 objet
-   Fa. 3 faces
-   Ed. 4 bords
-   Ve. 1 vertex
-   Si vous utilisez plusieurs documents la macro restaure uniquement la sélection dans le document ouvert (document actif)
-   L\'info-bulle affiche la liste du nom et du sous-objet du document travaillé.

![Info objects memorized displayed](images/Macro_Select_Hovering_01.png )


**Selected by Box**

-   si vous faites une sélection avec boîte englobante ce bouton sélectionne tous les objets dont la case de sélection est cochée
-   Autre utilité si vous avez coché l\'option sommet et que vous souhaitez sélectionner tous les sommets de l\'objet\... cliquez sur ce bouton


**Reset Data**

-   Reset all data efface toutes les données de la macro (pas le mémo)


**Reset Memo**

-   Reset the memo efface les données mémorisées


**Remove selection**

-   Désélectionne les objets du le document actuel

*(**PS:** si plusieurs documents sont ouverts, un clic de souris dans la vue 3D, désélectionne toutes les sélections dans tous les documents)*


**Quit**

-   Quit quitte la macro


**Pause grab/Refresh**

-   Pause la macro par exemple : désélectionnez plusieurs objets
-   après la pause, cliquez pour revenir sur la macro et mettre à jour toutes les informations dans la macro
-   Peut être utilisé pour mettre à niveau les sélections dans la macro (tous le temps)
-   Ex : plusieurs objets sont sélectionnés avant d\'exécuter la macro
-   La macro s\'adapte et détecte tout changement de document



### Icône

L\'icône doit être copiée dans le même répertoire que la macro.

l\'icône de la barre d\'outils ![Macro Select Hovering](images/Macro_Select_Hovering.png )

## Script

**Macro_Select_Hovering.FCMacro**


{{CodeDownload|https://gist.github.com/mario52a/7ebe6b3fd047441114d9d0e08ceddd63| Download latest version of the macro}}

## Version

ver 00.04 (11/01/2024) : ajout:

-   LineEdit info,
-   ComboBox memo selection,
-   Button Memo selection,
-   Button Selected by body
-   Button Reset Data
-   Button Reset Memo
-   Button Remove Selection

ver 00.03b (28/10/2020) : ajout parenthèses print**()** pour Python 3

ver 00.03 (26/12/2017) : replace test with (FreeCAD.ActiveDocument.getObject(obj), sub) == False)

ver 00.02 (26/12/2017) :

ver 00.01 (25/12/2017) :



## Lien

[Multiple face selection to convert a shape to a solid](https://forum.freecadweb.org/viewtopic.php?f=3&t=26370)



---
⏵ [documentation index](../README.md) > Macro Select Hovering/fr
