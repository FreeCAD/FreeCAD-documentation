# TechDraw Preferences/fr
## Introduction

Les préférences pour l\'[atelier TechDraw](TechDraw_Workbench/fr.md) se trouvent dans l\'[Editeur de préférences](Preferences_Editor/fr.md), **Édition → Préférences → TechDraw**.

Tous les paramètres de préférences avec des étiquettes en *italiques* sont des valeurs par défaut pour les nouveaux objets de dessin. Ils n\'ont aucun effet sur les objets existants.



## Général

<img alt="Préférences générales" src=images/TechDraw_PreferencesGeneral.png  style="width:350px;">



### Mises à jour du dessin 

-   **Mettre à jour avec la 3D** : si les pages sont mises à jour ou non chaque fois que le modèle 3D est modifié. Il s\'agit d\'un paramètre de règle globale.
-   **Autoriser le remplacement de page** : indique si la propriété **[KeepUpdated](TechDraw_PageDefault/fr#Propri.C3.A9t.C3.A9s.md)** d\'une page peut remplacer le paramètre global **Mettre à jour avec la 3D**. Il s\'agit d\'un paramètre de règle globale.
-   **Garder la page à jour** : permet de synchroniser les pages de dessin avec les modifications du modèle 3D *en temps réel*. Cela peut ralentir le temps de réponse.
-   **Distribuer automatiquement les vues secondaires** : distribue automatiquement les vues secondaires pour les [groupes de projection](TechDraw_ProjectionGroup/fr.md).



### Étiquettes

-   **Police d\'annotation** : nom de la police par défaut pour les étiquettes. La police est également utilisée pour les nouvelles [cotes](#Cotes.md), sa modification n\'a aucun effet sur les cotes existantes.
-   **Taille des étiquettes** : taille par défaut pour les étiquettes.

### Conventions

-   **Convention de projection** : si les [groupes de projection](TechDraw_ProjectionGroup/fr.md) utilisent la projection du premier angle (européen) ou du troisième angle (américain). Voir [projection multivue](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews) pour une explication.
-   **Style des lignes cachées** : le style à utiliser pour les lignes cachées.



### Fichiers

-   **Modèle par défaut** : fichier [modèle](TechDraw_Templates/fr.md) par défaut pour les nouvelles pages.
-   **Répertoire des modèles** : répertoire de démarrage du bouton de la barre d\'outils **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insérer une page à l'aide d'un modèle](TechDraw_PageTemplate/fr.md)**.
-   **Fichier des motifs hachurés** : fichier par défaut [SVG](SVG/fr.md) ou [bitmap](bitmap/fr.md) pour [hachures](TechDraw_Hatch/fr.md).
-   **Fichier des groupes de lignes** : fichier alternatif pour les définitions personnelles des [Groupes de lignes](TechDraw_LineGroup/fr.md).
-   **Répertoire de Soudage** : répertoire par défaut du bouton de la barre d\'outils **[<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Symbole de soudure](TechDraw_WeldSymbol.md)**.
-   **Fichier PAT** : fichier de définition de modèle PAT par défaut pour [hachures géométriques](TechDraw_GeometricHatch/fr.md).
-   **Nom du motif** : nom du motif PAT par défaut.



### Grille

-   **Afficher la grille** : paramètre par défaut de Show Grid pour les nouvelles pages. {{Version/fr|0.20}}
-   **Espacement de la grille** : distance par défaut entre les lignes de la grille pour les nouvelles pages. {{Version/fr|0.20}}



## Échelle

<img alt="Préférences d\'Échelle" src=images/TechDraw_PreferencesScale.png  style="width:350px;">



### Échelle 

-   **Échelle de la page** : échelle par défaut pour les nouvelles pages.
-   **Afficher le type d\'échelle** : échelle par défaut pour les nouvelles vues.
-   **Échelle personnalisée** : échelle par défaut pour les vues si **Afficher le type d\'échelle** est *Personnalisé*.



### Ajustements de la taille 

-   **Échelle des sommets** : échelle des points [vertex](Glossary/fr#V.md). Multiplicateur de la largeur des lignes.
-   **Échelle des marques centrales** : taille des marques centrales. Multiplicateur des tailles des sommets.
-   **Modifier les balises du modèle** : taille des poignées des balises du [modèle](TechDraw_Templates/fr.md) en mm (points verts).
-   **Échelle des symboles de soudage** : multiplicateur de la taille des [Symboles de soudure](TechDraw_WeldSymbol/fr.md).



## Cotes

<img alt="Préférences de Dimensions" src=images/TechDraw_PreferencesDimensions.png  style="width:350px;">

-   **Standard et style** : norme à utiliser pour les valeurs des cotes. La différence entre les normes est indiquée dans l\'image : ![\|500px\|Différences entre les differentes normes prises en charge. ([Image source](images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png ).

:   

    :   ISO Oriented - dessine selon la norme ISO 129-1, le texte est tourné pour être parallèle à la tangente de la ligne de cote.
    :   ISO Referencing - dessine conformément à la norme ISO 129-1, le texte est toujours horizontal, au-dessus de la ligne de référence la plus courte possible.
    :   ASME Inlined - dessine selon la norme ASME Y14.5M, le texte est horizontal, inséré dans une rupture dans la ligne de cote ou l\'arc.
    :   ASME Referencing - dessine selon la norme ASME Y14.5M, le texte est horizontal, une courte ligne de référence est attachée au centre vertical d\'un côté.

-   **Utiliser les paramètres système pour les décimals** : utilise le nombre de décimales des [préférences générales](Preferences_Editor/fr#Unit.C3.A9s.md).
-   **Afficher les unités**: ajoute l\'unité (mm, in, etc.) aux valeurs de cote.
-   **Nombre de décimales** : nombre de décimales si **Utiliser les paramètres système pour les décimals** n\'est pas sélectionné et si **Format des cotes** n\'est pas spécifié.
-   **Format des cotes** : format personnalisé pour le texte des cotes. Utilise le [spécification du format printf](https://fr.wikipedia.org/wiki/Printf).
-   **Taille de la police** : taille de police pour le texte de cote.
-   **Échelle du texte de tolérance** : réglage de la taille de la police de tolérance. Multiplicateur de **Taille de la police**.
-   **Symbole de diamètre** : caractère utilisé pour indiquer les dimensions des diamètres.
-   **Style des flèches** : style de pointe des flèches pour les dimensions.
-   **Taille des flèches** : taille de la pointe des flèches des dimensions.
-   **Facteur d\'écart d\'extension - ISO** : écart entre le point de dimension et le début des lignes d\'extension pour les dimensions ISO. {{Version/fr|0.21}}
-   **Facteur d\'écart d\'extension - ASME** : écart entre le point de cote et le début des lignes d\'extension pour les cotes ASME. {{Version/fr|0.21}}
-   **Espacement des lignes - ISO** : écart entre la ligne de cote et le texte de la cote pour les dimensions ISO. {{Version/fr|0.21}}

## Annotation

<img alt="Préférences d\'Annotation" src=images/TechDraw_PreferencesAnnotation.png  style="width:350px;">

-   **Norme des lignes de coupe** : standard à utiliser pour tracer des lignes de section dans les [vues en coupe](TechDraw_SectionView/fr.md).
-   **Style des lignes de coupe** : style pour les lignes de coupe.
-   **Marques des lignes de la vue en coupe complexe** : affiche des marques aux changements de direction sur les lignes des [Vues en coupe complexe](TechDraw_ComplexSection/fr.md). {{Version/fr|0.21}}
-   **Motif des vue en coupe** : motif pour la section coupée. Les options sont les suivantes :
    -   *Caché* : pas de surface visible.
    -   *Couleur pleine* : la surface prend la couleur définie pour **Section Face**
    -   *Hachure SVG* : la surface est [hachurée](TechDraw_Hatch/fr.md).
    -   *Hachure PAT* : la surface est [géométriquement hachurée](TechDraw_GeometricHatch/fr.md).
-   **Largeurs des lignes** : [groupe de lignes](TechDraw_LineGroup/fr.md) pour définir les largeurs de ligne par défaut.
-   **Forme du contour pour les vues détaillées** : forme de contour pour les [vues détaillées](TechDraw_DetailView/fr.md).
-   **Style de la ligne de la forme de contour des vues détaillées** : style de la ligne de la forme de contour des [vues détaillées](TechDraw_DetailView/fr.md).
-   **Style des lignes centrales** : style par défaut pour les [lignes centrales des faces](TechDraw_FaceCenterLine/fr.md).
-   **Forme des infobulles** : forme des [infobulles](TechDraw_Balloon/fr.md).
-   **Extrémité des infobulles** : style par défaut pour des extrémités des infobulles.
-   **Longueur horizontale de la ligne des infobulles** : longueur horizontale de la ligne des infobulles.
-   **Triangle orthogonal de l\'infobulle** : si **Extrémité des infobulles** est mis à *Triangle*, le triangle ne peut avoir une direction verticale ou horizontale que lorsque l\'infobulle est déplacé.
-   **Ligne de référence horizontale auto** : force le dernier segment de la [ligne de référence](TechDraw_LeaderLine/fr.md) à être horizontal.
-   **Afficher les marques des centres** : affiche les marques des centres des arcs dans les vues.
-   **Imprimer les marques des centres** : affiche les marques des centres des arcs sur la version imprimable.



## Couleurs

<img alt="Préférences de Couleurs" src=images/TechDraw_PreferencesColors.png  style="width:350px;">

Configuration des couleurs par défaut pour les nouvelles pages:

-   **Normal** : couleur des lignes normales.
-   **Préselectionnés** : couleur des présélections. Couleur utilisée pour mettre en surbrillance les objets lorsque vous passez la souris dessus.
-   **Sélection** : couleur des objets sélectionnés.
-   **Arrière-plan** : couleur d\'arrière-plan autour des pages.
-   **Dimension** : couleur des lignes de cote et du texte.
-   **Ligne centrale** : couleur des [lignes centrales de faces](TechDraw_FaceCenterLine/fr.md).
-   **Couleur des contours des vues détaillées** : couleur des lignes pour la forme des contours des [vues détaillées](TechDraw_DetailView/fr.md).
-   **Couleur des grilles** : couleur pour toutes les grilles de page. {{Version/fr|0.20}}
-   **Lignes cachées** : couleur de la ligne cachée. Cette couleur sera utilisée pour toutes sortes de [lignes cachées](#Param.C3.A8tres_HLR.md).
-   **Vues en coupe** : couleur de la surface des [vues en coupe](TechDraw_SectionView/fr.md). Utilisé uniquement si le paramètre **Motif des vue en coupe** est réglé sur *Couleur pleine*.
-   **Lignes des vues en coupe** : couleur de la ligne des [vues en coupe](TechDraw_SectionView/fr.md).
-   **Hachure** : couleur de l\'image des [hachures par motifs](TechDraw_Hatch/fr.md).
-   **Hachure géometrique** : couleur du motif des [hachures géométriques](TechDraw_GeometricHatch/fr.md).
-   **Sommet** : couleur des [vertices](Glossary/fr#V.md) (sommets) sélectionnables dans les vues.
-   **Lignes de référence** : couleur des nouvelles [lignes de référence](TechDraw_LeaderLine/fr.md).
-   **Faces transparentes** : si coché, les faces des objets seront transparentes. Sinon, la couleur définie sera utilisée pour les faces.
-   **Clair sur sombre** : si coché, le texte et les lignes auront une couleur claire. A utiliser si **Couleur de la page** est sombre. Les faces transparentes ou de couleur claire sont recommandées avec cette option. {{Version/fr|0.21}}
-   **Monochrome** : si coché, la couleur définie sera utilisée pour tout le texte et toutes les lignes. {{Version/fr|0.21}}
-   **Couleur de la page** : couleur du fond de la page. {{Version/fr|0.21}}



## Lignes cachées 

<img alt="Préférences de Lignes cachées" src=images/TechDraw_PreferencesHLR.png  style="width:350px;">

Version anglaise de la GUI, HLR pour *hidden line removal* (suppression des lignes cachées).

-   **Utiliser l\'approximation du polygone** : utilise une approximation pour trouver les lignes cachées. C\'est rapide, mais le résultat est une collection de courtes lignes droites.
-   **Afficher les lignes dures** : affiche les bords durs et les contours (les lignes visibles sont toujours affichées)
-   **Afficher les lignes de transition**: affiche les lignes lisses. Une ligne lisse est une ligne indiquant un changement entre des surfaces tangentes, comme dans la transition d\'une surface plane à un [congé](https://fr.wikipedia.org/wiki/Arrondi_et_cong%C3%A9).
-   **Afficher les lignes de couture** : affiche les lignes de couture. Une ligne de couture est une frontière entre les faces.
-   **Afficher les lignes isoparamétriques** : affiche les lignes ISO. ISO signifie «isoparamétrique». [Voici une description (en anglais)](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) des lignes isoparamétriques (en fait des courbes).
-   **Dénombrement ISO** : nombre de lignes ISO par bord de face.



## Avancé

<img alt="Préférences de Avancé" src=images/TechDraw_PreferencesAdvanced.png  style="width:350px;">

-   **Détecter les faces** : si cette case est cochée, TechDraw tentera de créer des faces en utilisant les segments de ligne renvoyés par l\'algorithme de suppression de ligne cachée. Les faces doivent être détectés pour utiliser les [hachures](TechDraw_Hatching/fr.md), mais il peut y avoir une dégradation des performances pour les modèles complexes.
-   **Afficher les arêtes de coupe** : met en surbrillance la bordure de la section coupée dans les [vues en coupe](TechDraw_SectionView/fr.md).
-   **Rapport d\'avancement** : messages d\'avancement lors de la construction de la Géométrie de la vue. {{Version/fr|0.21}}
-   **Utiliser le nouvel algorithme de recherche de face** : si coché, le nouvel algorithme de recherche de face sera utilisé à la place de l\'algorithme d\'origine. {{Version/fr|0.21}}
-   **Corriger automatiquement les références des cotes** : si coché, une tentative est faite pour mettre à jour les références des cotes lorsque le modèle change. {{Version/fr|0.21}}
-   **Unir avant d\'effectuer une vue en coupe** : effectue une opération de fusion sur la ou les formes d\'entrée avant le traitement de la vue en coupe.
-   **Montrer les objets 2D isolés** : inclut des objets 2D dans les projections, par exemple les esquisses isolées.
-   **Autoriser des arêtes inhabituelles** : inclut des arêtes avec une géométrie inattendue dans les résultats, par ex. longueurs nulles.
-   **Section de débogage** : affiche les résultats intermédiaires pendant un traitement des vues en coupe.
-   **Détail de débogage** : affiche les résultats intermédiaires pendant un traitement des vues détailllées.
-   **Passes pour supprimer les chevauchements d\'arêtes** : nombre de tentatives de suppression des chevauchements d\'arêtes renvoyées par l\'algorithme de suppression des lignes cachées. Une valeur de 0 indique qu\'il n\'y a pas de nettoyage. Les valeurs supérieures à 2 ne sont généralement pas productives. Chaque tentative augmente le temps nécessaire à la production du dessin. {{Version/fr|0.21}}
-   **Sélection autour des bords** : taille de la zone de sélection autour des bords. L\'unité de focalisation est d\'environ 0,1 mm, en fonction de votre zoom en cours.
-   **Sélection autour des marques centrales** : zone de sélection autour des marques centrales. L\'unité de focalisation est d\'environ 0,1 mm, en fonction de votre zoom en cours. La valeur par défaut est 10. Les valeurs comprises entre 20 et 30 facilitent considérablement la sélection des bords. Les valeurs élevées entraînent des chevauchements avec d\'autres éléments du dessin.
-   **Style des extrémités de ligne** : réglage de la forme des extrémités des lignes. Explication des options: [pen cap styles](https://doc.qt.io/qt-5/qt.html#PenCapStyle-enum)
-   **Taille maximum des tuiles de hachures SVG** : La limite des tuiles SVG d\'une taille de 64x64 pixels utilisées pour hachurer une seule face. Pour des mises à l\'échelle importantes, il se peut que l\'on obtienne une erreur concernant le nombre trop élevé de tuiles SVG, il faut alors augmenter le nombre maximum de tuiles.
-   **Nombre maximum de segments des hachures PAT** : nombre maximal de segments de hachures utilisés pour hachurer une face avec un motif PAT.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/fr
