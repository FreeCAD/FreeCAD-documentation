# TechDraw Preferences/fr







{{TOCright}}

## Introduction

Les préférences pour l\'[Atelier TechDraw](TechDraw_Workbench/fr.md) se trouvent dans l\'[Editeur de préférences](Preferences_Editor/fr.md), **Edition → Préférences → TechDraw**.

Tous les paramètres de préférences avec des étiquettes \\ italiques\'\' sont des valeurs par défaut pour les nouveaux objets de dessin. Ils n\'ont aucun effet sur les objets existants.

## Généralités

<img alt="Préférences générales" src=images/TechDraw_PreferencesGeneral.png  style="width:350px;">

### Mises à jour de dessin 


{{Version/fr|0.19}}

-   **Update With 3D**: si les pages sont mises à jour ou non chaque fois que le modèle 3D est modifié. Il s\'agit d\'un paramètre de politique globale.
-   **Allow Page Override**: Indique si la propriété \'\' \'[Keep Update](TechDraw_PageDefault/fr#_Propriétés.md) d\'une page peut remplacer le paramètre global **Update With 3D**. Il s\'agit d\'un paramètre de politique globale.
-   **Keep Page Up To Date**: permet de synchroniser les pages de dessin avec les modifications du modèle 3D *en temps réel*. Cela peut ralentir le temps de réponse.
-   **Auto-distribute Secondary Views**: distribue automatiquement les vues secondaires pour [groupes de projection](TechDraw_ProjectionGroup/fr.md).

### Étiquettes

-   **Label Font** : nom de la police par défaut pour les étiquettes. La police est également utilisée pour les nouvelles [dimensions](TechDraw_Preferences/fr#Dimensions.md), sa modification n\'a aucun effet sur les dimensions existantes.
-   **Label Size** : taille par défaut pour les étiquettes.

### Conventions

-   **Projection Group Angle**: Si les [groupes de projection](TechDraw_ProjectionGroup/fr.md) utilisent la projection du premier ou du troisième angle. Voir [projection multivue](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews) pour une explication.
-   **Hidden Line Style**: Le style à utiliser pour les lignes cachées.

### Fichiers

-   **Default Template**: fichier de [modèle](TechDraw_Templates/fr.md) par défaut pour les nouvelles pages.
-   **Template Directory**: répertoire de démarrage du bouton de la barre d\'outils **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insérer une page à l'aide d'un modèle](TechDraw_PageTemplate/fr.md)**.
-   **Hatch Pattern File**: fichier par défaut [SVG](SVG/fr.md) ou [bitmap](bitmap/fr.md) pour [hachures](TechDraw_Hatch/fr.md).
-   **Line Group File**: fichier alternatif pour les définitions personnelles [Groupes de lignes](TechDraw_LineGroup/fr.md).
-   **Welding Directory**: répertoire par défaut du bouton de la barre d\'outils **<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Symbole de soudure](TechDraw_WeldSymbol.md)**. {{Version/fr|0.19}}
-   **PAT File**: fichier de définition de modèle PAT par défaut pour [hachures géométriques](TechDraw_GeometricHatch/fr.md).
-   **Pattern Name**: nom du motif PAT par défaut.

## Échelle

<img alt="Préférences d\'échelle" src=images/TechDraw_PreferencesScale.png  style="width:350px;">

### Échelle 

-   **Page Scale**: Échelle par défaut pour les nouvelles pages.
-   **View Scale Type**: Échelle par défaut pour les nouvelles vues.
-   **View Custom Scale**: Échelle par défaut pour les vues si **View Scale Type** est *Personnalisé*.

### Size Adjustments 

-   **Vertex Scale**: échelle des points [vertex](Glossary/fr#V.md). Multiplicateur de largeur de ligne.
-   **Center Mark Scale**: taille des marques centrales. Multiplicateur de taille de sommet.
-   **Template Edit Mark**: taille des poignées de clic du champ [Modèles](TechDraw_Templates/fr.md) en mm (points verts).
-   **Welding Symbol Scale**: multiplicateur de la taille des [Symboles de soudure](TechDraw_WeldSymbol/fr.md). {{Version/fr|0.19}}

## Dimensions

<img alt="Préférences dimensions" src=images/TechDraw_PreferencesDimensions.png  style="width:350px;">

### Dimensions 

-   **Standard and Style**: norme à utiliser pour les valeurs dimensionnelles. La différence entre les normes est indiquée dans l\'image: ![\|500px\|Différences entre les differentes normes prises en charge. ([Image source](images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png ).

:   

    :   ISO Oriented - dessine selon la norme ISO 129-1, le texte est tourné pour être parallèle à la tangente de la ligne de cote.
    :   ISO Referencing - dessine conformément à la norme ISO 129-1, le texte est toujours horizontal, au-dessus de la ligne de référence la plus courte possible.
    :   ASME Inlined - dessine selon la norme ASME Y14.5M, le texte est horizontal, inséré dans une rupture dans la ligne de cote ou l\'arc.
    :   ASME Referencing - dessine selon la norme ASME Y14.5M, le texte est horizontal, une courte ligne de référence est attachée au centre vertical d\'un côté.

-   **Use Global Decimals**: utilise le nombre de décimales des [préférences générales](Preferences_Editor/fr#Unit.C3.A9s.md).
-   **Show Units**: ajoute l\'unité (mm, in, etc.) aux valeurs de cote.
-   **Alternate Decimals**: nombre de décimales si **Use Global Decimals** n\'est pas utilisé.
-   **Default Format**: format personnalisé pour le texte de cote. Utilise le [spécification du format printf](https://fr.wikipedia.org/wiki/Printf).
-   **Font Size**: taille de police pour le texte de cote.
-   **Tolerance Text Scale**: réglage de la taille de la police de tolérance. Multiplicateur de dimension **[Taille de police](TechDraw_Preferences/fr#Dimensions_2.md)**.
-   **Diameter Symbol**: Caractère utilisé pour indiquer les dimensions du diamètre.
-   **Arrow Style**: style de pointe de flèche pour les dimensions.
-   **Arrow Size**: taille de la pointe de flèche des dimensions.

## Annotation

<img alt="Préférences générales" src=images/TechDraw_PreferencesAnnotation.png  style="width:350px;">

-   **Section Line Standard**: standard à utiliser pour tracer des lignes de section dans les [vues en coupe](TechDraw_SectionView/fr.md).
-   **Section Line Style**: style pour les lignes de coupe.
-   **Section Cut Surface**: style pour la section coupée. Les options sont les suivantes: {{Version/fr|0.19}}
    -   *Hide*: pas de surface visible.
    -   *Solid Color*: la surface prend la couleur définie pour **Section Face**
    -   *SVG Hatch*: la surface est [hachurée](TechDraw_Hatch/fr.md).
    -   *PAT Hatch*: la surface est [géométriquement hachurée](TechDraw_GeometricHatch/fr.md).
-   **Line Width Group**: [groupe de lignes](TechDraw_LineGroup/fr.md) pour définir les largeurs de ligne par défaut.
-   **Detail View Outline Shape**: forme de contour pour les [vues détaillées](TechDraw_DetailView/fr.md).
-   **Detail Highlight Style**: style de ligne de la forme de contour pour les [vues détaillées](TechDraw_DetailView/fr.md). {{Version/fr|0.19}}
-   **Center Line Style**: style par défaut pour les [médianes](TechDraw_FaceCenterLine/fr.md).
-   **Balloon Shape**: forme des [annotations bulle](TechDraw_Balloon/fr.md).
-   **Balloon Leader End**: style par défaut pour les extrémités de ligne de ligne de repère de ballon.
-   **Balloon Leader Kink Length**: longueur du coude de la ligne de repère du ballon.
-   **Balloon Orthogonal Triangle**: si **Balloon Leader End** est *Filled Triangle*, le triangle ne peut obtenir une direction verticale ou horizontale que lorsque le ballon est déplacé.
-   **Leader Line Auto Horizontal**: force le dernier segment [Ligne de référence](TechDraw_LeaderLine/fr.md) à être horizontal.
-   **Show Center Marks**: affiche les marques du centre de l\'arc dans les vues.
-   **Print Center Marks**: affiche les centres d\'arc dans la sortie imprimée.

## Couleurs

<img alt="Préférences des couleurs" src=images/TechDraw_Preferences_Colors.PNG  style="width:350px;">

Configuration des couleurs par défaut pour les nouvelles pages:

-   **Normal**: Couleur de ligne normale.
-   **Preselected**: Couleur de présélection. Couleur utilisée pour mettre en surbrillance les objets lorsque vous passez la souris dessus.
-   **Selected**: Couleur des objets sélectionnés.
-   **Background**: Couleur d\'arrière-plan autour des pages.
-   **Dimension**: Couleur des lignes de cote et du texte.
-   **Centerline**: Couleur pour une [ligne médiane à une face](TechDraw_FaceCenterLine/fr.md).
-   **Detail Highlight**: Couleur de ligne pour la forme de contour des [vues de détail](TechDraw_DetailView/fr.md). {{Version/fr|0.19}}
-   **Transparent Faces**: Si coché, les faces des objets seront transparentes. Sinon, la couleur définie sera utilisée pour les visages. {{Version/fr|0.19}}
-   **Hidden Line**: Couleur de la ligne cachée. Cette couleur sera utilisée pour toutes sortes de [lignes cachées](#Param.C3.A8tres_HLR.md).
-   **Section Face**: Couleur de la surface de coupe [vue des coupes](TechDraw_SectionView/fr.md). Utilisé uniquement si le paramètre **Section Cut Surface** est réglé sur *Solid Color*.
-   **Section Line**: Couleur de la ligne de coupe [vue des coupes](TechDraw_SectionView/fr.md).
-   **Hatch**: [Hachures par motifs](TechDraw_Hatch/fr.md) couleur de l\'image.
-   **Geometric Hatch**: [Hachures géométriques](TechDraw_GeometricHatch/fr.md) couleur du motif.
-   **Vertex**: Couleur des [vertices](Glossary/fr#V.md) sélectionnables dans les vues.
-   **Leaderline**: Couleur des nouveaux [lignes de rappel](TechDraw_LeaderLine/fr.md).

## HLR

<img alt="Préférences HLR" src=images/TechDraw_PreferencesHLR.png  style="width:350px;">

HLR pour *hidden line removal* (suppression des lignes cachées).

-   **Use Polygon Approximation**: utilise une approximation pour trouver les lignes cachées. C\'est rapide, mais le résultat est une collection de courtes lignes droites.
-   **Show Hard Lines**: affiche les bords durs et les contours (les lignes visibles sont toujours affichées)
-   **Show Smooth Lines**: affiche les lignes lisses. Une ligne lisse est une ligne indiquant un changement entre des surfaces tangentes, comme dans la transition d\'une surface plane à un congé [1](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Show Seam Lines**: afficher les lignes de couture. Une ligne de couture est une frontière entre les faces.
-   **Show UV ISO Lines**: affiche les lignes ISO. ISO signifie «isoparamétrique». [Voici une description](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) des lignes isoparamétriques (en fait des courbes).
-   **ISO Count**: nombre de lignes ISO par bord de face.

## Advanced

<img alt="Préférences avancées" src=images/TechDraw_PreferencesAdvanced.png  style="width:350px;">

-   **Detect Faces**: si cette case est cochée, TechDraw tentera de créer des visages en utilisant les segments de ligne renvoyés par l\'algorithme de suppression de ligne cachée. Les visages doivent être détectés pour utiliser [hachures](TechDraw_Hatching/fr.md), mais il peut y avoir une pénalité de performance dans les modèles complexes.
-   **Show Section Edges**: met en surbrillance la bordure de la section coupée dans [vues de section](TechDraw_SectionView/fr.md).
-   **Debug Section**: vide les résultats intermédiaires pendant un traitement de vue de section
-   **Debug Detail**: vide les résultats intermédiaires pendant un traitement de vue de détail
-   **Allow Crazy Edges**: inclut des arêtes avec une géométrie inattendue dans les résultats, par ex. longueurs nulles
-   **Fuse Before Section**: effectue une opération de fusion sur la ou les formes d\'entrée avant le traitement de la vue en coupe
-   **Show Loose 2D Geom**: inclut des objets 2D dans les projections, par ex. croquis lâches
-   **Edge Fuzz**: taille de la zone de sélection autour des bords. L\'unité de focalisation est d\'environ 0,1 mm, en fonction de votre zoom en cours.
-   **Mark Fuzz**: zone de sélection autour des marques centrales. L\'unité de focalisation est d\'environ 0,1 mm, en fonction de votre zoom en cours.
-   **Line End Cap Shape**: réglage de la forme de l\'extrémité de ligne. Explication des options: <https://doc.qt.io/qt-5/qt.html#PenCapStyle-enum>
-   **Max SVG Hatch Tiles**: limite des tuiles SVG d\'une taille de 64x64 pixels utilisées pour hachurer une seule face. Pour les grandes échelles, on peut obtenir une erreur sur de nombreuses tuiles SVG, puis il faut augmenter la limite de tuiles.
-   **Max PAT Hatch Segments**: nombre maximal de segments de hachures utilisés pour hachurer une face avec un motif PAT.

## Paramètres cachés 

**Remarque:** Depuis FreeCAD 0.19, tous les paramètres sont disponibles dans les boîtes de dialogue Préférences. Ce qui suit s\'applique uniquement aux versions de FreeCAD antérieures à 0,19:

Certains paramètres de préférences ne sont accessibles que via [Std Editeur des paramètres](Std_DlgParameter/fr.md), **Outils → Éditer paramètres**.

### Preferences/Mod/TechDraw/Decorations

-   **CenterMarkScale**: facteur d\'échelle par défaut pour CenterMarks
-   **ShowCenterMarks**: défaut `True`/`False`
-   **PrintCenterMarks**: `True`/`False` affiche CenterMarks lors de l\'impression {{Version/fr|0.19}}

### Préférences/Mod/TechDraw/Général

-   **DefaultScale**: réglage initial de de la page échelle {{Version/fr|0.19}}
-   **EdgeFuzz**: rayon de la sélection des bords
-   **MarkFuzz**: rayon de la sélection des CenterMarks
-   **SectionFuseFirst**: fusionne les objets source avant d\'effectuer la coupe de la section
-   **EdgeEndCap**: forme des extrémités des bords 0x00 FlatCap, 0x10 SquareCap, 0x20 RoundCap (Qt::PenCapStyle) {{Version/fr|0.19}}

### Préférences/Mod/TechDraw/Format

-   **SectionFormat**: section style de lignes 0-ASME 1-ISO

### Préférences/Mod/TechDraw/Standards

-   **RadiusAligned**: rayon format de dimension 0-ISO(aligné) 1-ASME(uniforme)





{{TechDraw Tools navi

}} 

[Category:Preferences](Category:Preferences.md)
