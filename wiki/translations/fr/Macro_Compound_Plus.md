# Macro Compound Plus/fr
{{Macro/fr
|Name=Macro Compound Plus
|Description = Commande Draft définie dans une petite macro pour l'exemple de fil 2D: travailler avec les fichiers DXF. La macro détecte: Ligne, Arc, Cercle, Ellipse, BSplineCurve et reproduit le fil DXF dans un objet Draft. Le texte est converti en ShapeString.
|Author=Mario52
|Version=00.05
|Date=2024-11-11
|FCVersion= 0.21.2 et plus
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Compound_Plus.png ToolBar Icon]
}}

## Description

Commande Draft définie dans une petite macro pour l\'exemple de fil 2D: travaille avec les fichiers DXF. La macro détecte: Ligne, Arc, Cercle, Ellipse, BSplineCurve et reproduit le fil DXF dans un objet Draft. Le texte est converti en ShapeString.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/7be361a8c489deec918f664fdcfc4394/raw/2d12268123cbd38a3fba10fff1c7f35837cd3325/Macro_Compound_Plus.FCMacro}}



## Utilisation

![Macro_Compound_Plus_00](images/Macro_Compound_Plus_00.png )

### Choix

-    **<img src="images/Part_Compound.svg" width=16px> Compound I**Type I \[1 + 1 = 1\] : créez un composé unique de tous les objets sélectionnés sans historique.

-    **<img src="images/Part_Compound.svg" width=16px> Compound II**Type II \[1 + 1 = A (1 + 1)\] : Créez un composé de tous les objets sélectionnés avec l\'historique de tous les objets. Idem \"**Menu → Part → Make compound**\".

### {{CheckBox}} Couleur de l\'option 

S\'il {{CheckBox}} est vérifiée, la couleur de l\'objet à travailler sont colorées (bord, sommet)

-    **{{ColoredText|#ff0000|<img src="images/Workbench_Image.svg" width=16px> Color** }}: Donne une couleur à l\'objet. (Rouge par défaut 255, 0, 0)

### Outils

-   LineEdit: affiche (Index de police/nombre de police) le chemin et le nom de la police.

-    **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)**: convertir le texte <img alt="" src=images/Draft_Text.svg  style="width:16px;"> en une chaîne de forme <img alt="" src=images/Draft_ShapeString.svg  style="width:16px;"> (La hauteur du texte converti est respectée mais le résultat visuel peut ne pas être respecté, voir la propriété Vue combinée pour confirmer). (A) est la hauteur de la valeur automatique du texte.

    -   
        {{SpinBox|0,00 Auto}}
        
        : Si spinbox est égal à 0.0, la hauteur de la VALEUR du texte est respectée. Si différent de 0.0, le **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** se change en mode manuel **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (M)**.

-    **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**: Cette commande convertit le fil en une ligne avec des coordonnées. (ex: un composé rétrogradé n\'a pas de coordonnées, cette fonction crée une ligne avec les coordonnées comme ligne de dépouille et reproduit le fil DXF dans un objet dépouille sont détectées: ligne, arc, cercle, ellipse, BSplineCurve.

    -   
        {{SpinBox|0,00 Auto}}
        
        : Donne une épaisseur du fil. Si spinbox est égal à 0.0, la hauteur de la VALEUR du texte est respectée, si différent de 0.0, le **<img src="images/Draft_Line.svg" width=16px> Convert Wire (A)** se change en mode manuel **Convert Wire (M)**.

-    {{CheckBox|<img src="images/Draft_BezCurve.svg" width=16px> BezierCurve}}: Par défaut, le BezierCurve détecté est <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;">, s\'il est coché, le BezierCurve est cubique <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> et le bouton change {{CheckBox|TRUE|<img src="images/Draft_CubicBezCurve.svg" width=16px> Cubic BezierCurve}}

-    {{RadioButton|TRUE|<img src="images/Std_DrawStyleFlatLines.svg" width=16px> FlatLines}}: les objets créés sont des FlatLines.

-    {{RadioButton|<img src="images/Std_DrawStyleWireFrame.svg" width=16px> Wireframe}}: Les objets créés sont Wireframe.

-    {{RadioButton|<img src="images/Std_DrawStylePoints.svg" width=16px> Points}}: Les objets créés sont des Points.

-    **[<img src=images/Draft_Upgrade.svg style="width:16px"> UpGrade**: UpGrade

-    **[<img src=images/Draft_Downgrade.svg style="width:16px"> DownGrade**: DownGrade

### Pour le composé I et le bord de conversion 

Cette section fonctionne uniquement avec les outils **<img src="images/Part_Compound.svg" width=16px> Compound I
**, **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** et **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**

-    {{RadioButton|TRUE|None}}: Tous les objets d\'origine restent tels quels.

-    {{RadioButton|Hidden original objest(s)}}: Masque les objets originaux.

-    {{RadioButton|Delete original objest(s)}}: supprime les objets originaux.

### Forcer sur une forme: Ligne 

Si l\'objet ligne, arc ou cercle n\'est pas reconnu (comme forme dans un objet 3D de volume), cette section force la création d\'une ligne, d\'un arc ou d\'un cercle.

aucune vérification n\'est effectuée, cette section plateau permet de créer une forme 2D demandée (Draft) en fonction des données fournies

-    {{RadioButton|TRUE|<img src="images/Draft_Line.svg" width=16px> Lines}}: pour créer une ligne.

-    {{RadioButton|<img src="images/Draft_Arc.svg" width=16px> Arc}}: pour créer un arc.

-    {{RadioButton|<img src="images/Draft_Circle.svg" width=16px> Circle}}: pour créer un cercle

-    **<img src="images/Draft_Line.svg" width=16px> Force on : Line**: Bouton Force

### Commande

-   Barre de progression

-    **Reset**: réinitialiser la macro

-    **Quit**: Quittez la macro, bye

-    **Help**:afficher la page wiki dans le navigateur FreeCAD

## Script

L\' icône pour votre barre d\'outils ![](images/Macro_Compound_Plus.png ) a copier dans votre répertoire de macros.

[Comment créer une barre d\'outils](Customize_Toolbars/fr.md), [Comment installer une macro](How_to_install_macros/fr.md)

Le script sur github [Macro_Compound_Plus.FCMacro](https://gist.github.com/mario52a/7be361a8c489deec918f664fdcfc4394)

## Liens

Mes macros sur [Github](https://gist.github.com/mario52a)

## Version

-   11/11/2024 ver 0.05 : retour à **PySide** et remplacé **WebGui**par **webbrowser**
-   15/08/2020 ver 0.04: ajout de la section \"Forcer la forme\" si non détectée, créer Ligne, Arc et Cercle sur forcé
-   14/05/2020 ver 00.03: mise à niveau pySide2 et Qt5 et (police matPlotLib) et convertir Cercle, Arc, Ellipse, BezierCurve
-   24/01/2018 ver 00.02: sup \"import PyQt4\"
-   21/11/2016 ver 00.01:



---
⏵ [documentation index](../README.md) > Macro Compound Plus/fr
