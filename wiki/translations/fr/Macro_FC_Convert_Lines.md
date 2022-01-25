# Macro FC Convert Lines/fr
{{Macro/fr
|Name=Macro FC Convert Lines
|Icon=Macro_FCConvertLines.png
|Description=Cette macro  convertit un objet ligne, fil en une ligne de Tirets ou Tiret-Points ou Tiret-Point-Points avec les dimensions données.
|Author=mario52
|Version=00.07b
|Date=2020-11-09
|FCVersion=Toute
|Download=[https://www.freecadweb.org/wiki/images/e/e2/Macro_FCConvertLines.png ToolBar Icon]
}}

## Description

Cette macro convertit un objet ligne, fil en une ligne de Tirets ou Tiret-Points ou Tiret-Point-Points, Zig-Zag ou dessinée à la main avec des dimensions voulues. {{Codeextralink|https://gist.githubusercontent.com/mario52a/3d719574089a5f9044ec/raw/812769b6b296a1da2e9c8cd8153ad7266fe80f8d/Macro_FCConvertLines.FCMacro}}

<img alt="" src=images/Macro_FCConvertLines_00.png  style="width:400px;"> 
*Lignes converties en Tiret, Tiret-Point, Tiret-Point-Point*

## Utilisation

Copiez la macro dans votre répertoire de macros et lancez la macro FCConvertLines Gui ![FCConvertLines Gui](images/Macro_FCConvertLines_01.png )  Première section :

Cut line (Cochée par défaut) ![FCConvertLines](images/Macro_FCConvertLines_02.png )

-   Selectionnez une ou plusieurs lignes dans la vue 3D
-   **SpinBox** : cette boîte de dialogue sert a entrer le nombre de coupure du ou des lignes sélectionnées ou coupure avec une longueur déterminée \... (Par défaut nombre de coupures ici suffixe affiché \"x Cut\")
-   **Create L.** : si cette case a cocher est cochée les lignes sont créées
-   **Dimension** : si cette case a cocher est cochée le nombre entré est considéré comme une longueur le suffixe change alors en \"x.000 Dim\" et accepte 3 décimales
-   **Bicolor** : si cette case a cocher est cochée la couleur des lignes change alternativement en rouge puis blanche. Si cette case n\'est pas cochée la couleur des lignes dépendra de la couleur choisie avec le bouton **Color**
-   **Points** : si cette case a cocher est cochée un point est créé en suivant les spécifications entrées dans la boîte de dialogue de coupure ou dimension la couleur est définie par la case à cocher bicolor ou les options déterminées \"Options lines\"
-   les options **Options lines** sont disponibles




Seconde section :

Type de ligne : Dash ![FCConvertLines](images/Macro_FCConvertLines_03.png )

-   L\'écran affichant les images dans le bas de la macro change en ligne Dash
-   Sélectionnez une ou plusieurs couleurs dans la vue 3D
-   **Line A** : dimension du trait (voir **A** dans l\'écran)
-   **Space B** : dimension de l\'espace (voir **B** dans l\'écran)
-   Les lignes sont créées suivant la configuration spécifiée dans le menu **Options lines**




Troisième section :

Type de ligne : DashDot ![FCConvertLines](images/Macro_FCConvertLines_04.png )

-   L\'écran affichant les images dans le bas de la macro change en ligne DashDot
-   Sélectionnez une ou plusieurs lignes dan la vue 3D
-   **Line A** : dimension du premier tiret (voir **A** dans l\'écran)
-   **Space B** : dimension du premier espace (voir **B** dans l\'écran) (peut être différent de D)
-   **Line 2 C** : dimension du deuxième tiret (voir **C** dans l\'écran)
-   **Space 2 D** : dimension du deuxième espace (voir **D** dans l\'écran) (peut être différent de B)
-   Les lignes sont créées suivant la configuration spécifiée dans le menu Options lines




Quatrième section :

Type de ligne : DashDotDot ![FCConvertLines](images/Macro_FCConvertLines_05.png )

-   L\'écran affichant les images dans le bas de la macro change en ligne DashDotDot
-   Sélectionnez une ou plusieurs lignes dan la vue 3D
-   **Line A** : dimension du premier tiret (voir **A** dans l\'écran)
-   **Space B** : dimension du premier tiret (voir **B** dans l\'écran)
-   **Line 2 C** : dimension du deuxième tiret (voir **C** dans l\'écran)
-   **Space 2 D** : dimension du deuxième espace (voir **D** dans l\'écran)
-   Les lignes sont créées suivant la configuration spécifiée dans le menu Options lines




Cinquième section :

Type de ligne ligne : ZigZag ![FCConvertLines](images/Macro_FCConvertLines_06.png ) L\'écran affichant les images dans le bas de la macro change en ligne ZigZag

-   Cette option crée une ligne
-   **Number heads** : nombre de têtes totales sur la ligne
-   ****_____140.0_____**** : La longueur totale de la ligne est calculée et affichée dans cet écran en temps réel
-   **Begin A** : dimension du début de la ligne jusque le début de la première tête, même chose pour la fin de la ligne (voir **A** dans l\'écran)
-   **Dimension B** : dimension entre la fin et le début de deux têtes (voir **B** dans l\'écran)
-   **Gap C** : dimension de la largeur de la tête (voir **C** dans l\'écran)
-   **Height D** : hauteur de la tête (voir **D** dans l\'écran)
-   **Number E** : nombre de têtes contiguës (voir **E** dans l\'écran)
-   Les lignes sont créées suivant la configuration spécifiée dans le menu \"Options lines\" et \"Plan\"




Sixième section :

Type de ligne : Hand ![FCConvertLines](images/Macro_FCConvertLines_07.png )

-   Une ligne est créée
-   **Length A** : La longueur totale de la ligne (voir **A** dans l\'écran)
-   **Height B** : Hauteur de la ligne (voir **B** dans l\'écran)
-   **Wave** : Compression ou décompression de la vague (voir **Wave** dans l\'écran)
-   Les lignes sont créées suivant la configuration spécifiée dans le menu \"Options lines\" et \"Plan\"




Septième section :

Options line : ![FCConvertLines](images/Macro_FCConvertLines_08.png ) Cette option est disponible pour tous les types de lignes

-    **__2,00 Width__**: dimension de l\'épaisseur de(s) ligne(s)

-    **__2,00 Point S__**: dimension de la grosseur des points de(s) ligne(s)

-    **Color**: couleur de(s) ligne(s) ce bouton prends la couleur sélectionnée (si le checkbox \"Bicolor\" du menu \"Cut line\" est coché cette option ne fonctionnera pas)




Huitième section :

Option Plane

Cette option est uniquement disponible pour les types de lignes **\"ZigZag\"** et **\"Hand\"** ![FCConvertLines](images/Macro_FCConvertLines_09.png )

-   **XY** : Plan XY
-   **YZ** : Plan YZ
-   **XZ** : Plan XZ




Neuvième section :

Les Boutons ![FCConvertLines](images/Macro_FCConvertLines_10.png ) 

-    **Save type**: une configuration de ligne peut être sauvée dans un fichier (un fichier par configuration de ligne). Un entête est automatiquement prédéterminé suivant l\'option de type de ligne choisi (exemple : le type Dash est sauvé, dans la boîte de dialogue de sauvegarde du fichier s\'affiche \"Dash\_.FCConvertL\" vous pouvez par exemple modifier en \"Dash\_my\_config\_10.FCConvertL\" ou ce que vous voulez\... cette méthode permet de lister dans l\'ordre les configurations de même type)

-    **Load type**: charge une configuration et règle tous les paramètres sauvés pendant la sauvegarde

-    **Name type line________________**: nom donné à la configuration ce nom est sauvé dans le fichier

-    **Reset**: règle tous les paramètre à leur état d\'origine

-    **Create Comp**: ce bouton crée un composé de tous les objets traités (dix lignes créées = un composé)

-    **Create**: ce bouton crée les lignes individuelles (dix lignes traitées = dix lignes créées)

-    **Quit**: quitte la macro




## Les fichiers images à télécharger 

Les fichiers sont à copier dans votre répertoire de macros (10 fichiers images)

**L\'icône pour votre barre d\'outils** ![Macro\_FCConvertLines](images/Macro_FCConvertLines.png )  **Title** ![ConvertLines\_Title](images/Macro_FCConvertLines_Title.png )  **Line Dash** : ![ConvertLines\_Dash](images/Macro_FCConvertLines_Dash.png )  **Line DashDot** : ![ConvertLines Dash dot](images/Macro_FCConvertLines_DashDot.png_‎ )  **Line DashDotDot** : ![ConvertLines Dash dot dot](images/Macro_FCConvertLines_DashDotDot.png )  **Line Zigzag** : ![ConvertLines\_Zigzag](images/Macro_FCConvertLines_Zigzag.png )  **Line Hand** : ![ConvertLines\_Hand](images/Macro_FCConvertLines_Hand.png )  **View** :  ![ConvrtLines\_View-front](images/Macro_FCConvrtLines_View-front.png ) ![ConvrtLines\_View-right](images/Macro_FCConvrtLines_View-right.png ) ![ConvrtLines\_View-right](images/Macro_FCConvrtLines_View-top.png ) 

## Script

Copiez la macro **Macro\_FCConvertLines.FCMacro** dans votre répertoire de macros

Le script sur Gist [Macro\_FCConvertLines.FCMacro](https://gist.github.com/mario52a/3d719574089a5f9044ec)

ToolBar icon ![](images/Macro_FCConvertLines.png )

**Macro\_FCConvertLines.FCMacro**

## Exemples

Exemple dot, dash dot, dash dot, dash dot dot [center\|500px ](File:Macro_FCConvertLines_11b.png.md)  Exemple hand, zigzag [center\|500px ](File:Macro_FCConvertLines_11.png.md)  Exemple hand [center\|500px ](File:Macro_FCConvertLines_012.png.md)  Exemple hand (manuel) peut créer un belle sinusoïde ou une ligne totalement anarchique [center\|500px ](File:Macro_FCConvertLines_013.png.md) 

Exemple de conversion d\'un objet ShapeString en objet Sketch (la conversion de courbes n\'est pas (encore) possible) d\'un Shape en Sketch

![](images/ShapeString_To_Sketch.gif )




## Version

ver 00.07b 09/11/2020 correct bug \# (ajoute recompute() pour corriger)\# Cannot compute Inventor representation for the shape of Shape. Et Line avec Label

ver 00.07 13/05/2017 correction du bug après un changement de dimension cause création \"Alternate \....\" la dimension des lignes ne change pas et reste sur les dimensions calculées pour une création alternative et ne correspond plus aux dimensions voulues.

ver 00.06 20/02/2017 correction sur la précision restituée dans une coupure (remplacé \"numberOfPoints = longueur\" par \"numberOfPoints = (longueur + 1)\")

ver 00.05 11/01/2017 remplacé la méthode de recherche sur le chemin des macros (maintenant directement dans les préférences)

ver 00.04 05/09/2016 setPointSize(8.0)

ver 00.02 18/02/2016

ver 00.01 19/01/2016

ver 00.00 19/01/2016



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FC Convert Lines/fr
