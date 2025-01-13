# TechDraw Preferences/fr
## Introduction

Les préférences pour l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [atelier TechDraw](TechDraw_Workbench/fr.md) se trouvent dans les [réglages des préférences](Preferences_Editor/fr.md). Dans le menu, sélectionnez **Édition → Préférences...** puis **<img src="images/Workbench_TechDraw.svg" width=16px> TechDraw**. Ce groupe n\'est disponible que si l\'atelier TechDraw a été chargé dans la session FreeCAD en cours.

Il y a sept pages : [Général](#Général.md), [Échelle](#Échelle.md), [Dimensions](#Dimensions.md), [Annotation](#Annotation.md), [Couleurs](#Couleurs.md), [Lignes cachées supprimées](#Lignes_cachées_supprimées.md) et [Avancé](#Avancé.md).

Tous les préférences avec des étiquettes en *italiques* sont des valeurs par défaut pour les nouveaux objets de dessin. Ils n\'ont aucun effet sur les objets existants.

Cette page a été mise à jour pour la version 1.0.



## Général

<img alt="Préférences générales" src=images/Preferences_TechDraw_Page_General.png  style="width:350px;">



### Mises à jour du dessin 

-   **Mettre à jour avec la 3D (règle globale)** : si les pages sont mises à jour ou non chaque fois que le modèle 3D est modifié.
-   **Autoriser le remplacement de pages (règle globale)** : indique si la propriété **[KeepUpdated](TechDraw_PageDefault/fr#Propri.C3.A9t.C3.A9s.md)** d\'une page peut remplacer le paramètre global **Mettre à jour avec la 3D**.
-   **Garder les pages à jour** : permet de synchroniser les pages de dessin avec les modifications du modèle 3D *en temps réel*. Cela peut ralentir le temps de réponse.
-   **Distribuer automatiquement les vues secondaires** : distribue automatiquement les vues secondaires pour les [groupes de projection](TechDraw_ProjectionGroup/fr.md).



### Étiquettes

-   **Police d\'annotation** : nom de la police par défaut pour les étiquettes. La police est également utilisée pour les nouvelles [cotes](#Cotes.md), sa modification n\'a aucun effet sur les cotes existantes.
-   **Taille des étiquettes** : taille par défaut pour les étiquettes.

### Conventions

-   **Convention de projection** : si les [groupes de projection](TechDraw_ProjectionGroup/fr.md) utilisent la projection du premier angle (européen) ou du troisième angle (américain). Voir [projection multivue](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews) pour une explication.
-   **Convention des lignes de coupes** : norme pour les lignes de coupes qui contrôle la position des flèches et des symboles ({{Version/fr|1.0}}). Les options sont :
    -   *ANSI*
    -   *ISO*



### Fichiers

-   **Répertoire du modèle par défaut** : répertoire du fichier [modèle](TechDraw_Templates/fr.md) par défaut pour les nouvelles pages.
-   **Répertoire des modèles** : répertoire de démarrage du bouton de la barre d\'outils **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insérer une page à l'aide d'un modèle](TechDraw_PageTemplate/fr.md)**.
-   **Répertoire des fichiers à motif hachuré** : répertoire des fichiers par défaut [SVG](SVG/fr.md) ou [bitmap](bitmap/fr.md) pour des [hachures](TechDraw_Hatch/fr.md).
-   **Répertoire du fichier des groupes de lignes** : répertoire du fichier alternatif pour les définitions personnelles des [Groupes de lignes](TechDraw_LineGroup/fr.md).
-   **Répertoire pour les symboles de soudure** : répertoire par défaut du bouton de la barre d\'outils **[<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Symbole de soudure](TechDraw_WeldSymbol.md)**.
-   **Répertoire du fichier PAT** : répertoire du fichier de définition de modèle PAT par défaut pour des [hachures géométriques](TechDraw_GeometricHatch/fr.md).
-   **Nom du motif** : nom du motif PAT par défaut.
-   **Répertoire des symboles** : répertoire alternatif pour la recherche de fichiers de symboles SVG.



### Grille

-   **Afficher la grille** : paramètre par défaut de Afficher la grille pour les nouvelles pages.
-   **Espacement de la grille** : distance par défaut entre les lignes de la grille pour les nouvelles pages.



### Sélection

-   **Activer le mode de sélection multiple** : si cette option est cochée, le fait de cliquer sans **Ctrl** n\'efface pas la sélection existante. {{Version/fr|1.0}}



### Vues par défaut 

-   **Utiliser la direction de la caméra 3D** : si cette option est cochée, la direction de la caméra 3D (ou la normale d\'une face sélectionnée) sera utilisée comme direction de la vue. Si cette case n\'est pas cochée, les vues seront créées comme des vues de face. {{Version/fr|1.0}}
-   **Toujours afficher les étiquettes** : si cette option est cochée, les étiquettes des vues seront affichées même lorsque les images sont supprimées. {{Version/fr|1.0}}



### Aimantation

-   **Aimanter les vues à l\'alignement** : si cette option est cochée, les vues seront alignées lorsqu\'elles seront déplacées. {{Version/fr|1.0}}
-   **Coefficient d\'aimantation des vues** : tolérance pour l\'aimantation des vues. Si une vue est dans cette fraction de taille de vue de l\'alignement parfait, elle s\'aimantera. {{Version/fr|1.0}}



## Échelle

<img alt="Préférences d\'Échelle" src=images/Preferences_TechDraw_Page_Scale.png  style="width:350px;">



### Échelle 

-   **Échelle de la page** : échelle par défaut pour les nouvelles pages.
-   **Afficher le type d\'échelle** : échelle par défaut pour les nouvelles vues.
-   **Échelle personnalisée** : échelle par défaut pour les vues si **Afficher le type d\'échelle** est *Personnalisé*.



### Ajustements de la taille 

-   **Échelle des sommets** : échelle des points [vertex](Glossary/fr#V.md). Multiplicateur de la largeur des lignes.
-   **Échelle des marques centrales** : taille des marques centrales. Multiplicateur des tailles des sommets.
-   **Modifier les balises du modèle** : taille des poignées des balises du [modèle](TechDraw_Templates/fr.md) en mm (points verts).
-   **Échelle des symboles de soudage** : multiplicateur de la taille des [symboles de soudure](TechDraw_WeldSymbol/fr.md).



## Cotes

<img alt="Préférences de Cotes" src=images/Preferences_TechDraw_Page_Dimensions.png  style="width:350px;">



### Cotes 

-   **Standard et style** : norme à utiliser pour les valeurs des cotes. Les différences entre les normes sont indiquées dans l\'image : ![\|500px\|Différences entre les differentes normes prises en charge. ([Image source](images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png ).

:   

    :   ISO Oriented - dessine selon la norme ISO 129-1, le texte est tourné pour être parallèle à la tangente de la ligne de cote.
    :   ISO Referencing - dessine conformément à la norme ISO 129-1, le texte est toujours horizontal, au-dessus de la ligne de repère la plus courte possible.
    :   ASME Inlined - dessine selon la norme ASME Y14.5M, le texte est horizontal, inséré dans une rupture dans la ligne de cote ou l\'arc.
    :   ASME Referencing - dessine selon la norme ASME Y14.5M, le texte est horizontal, une courte ligne de repère est attachée au centre vertical d\'un côté.

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



### Outils

-   **Outils de cotation** : sélectionnez le type d\'outils de cotation pour la barre d\'outils. Quel que soit votre choix, tous les outils sont toujours disponibles dans le menu et par le biais de raccourcis. Les options sont les suivantes : {{Version/fr|1.0}}
    -   *Outil unique* : un [seul outil](TechDraw_Dimension/fr.md) pour toutes les cotations dans la barre d\'outils : Distance, Distance X/Y, Angle, Rayon. (d\'autres outils dans la liste déroulante).
    -   *Outils séparés* : outils distincts pour chaque outil de cotation.
    -   *Les deux* : vous aurez à la fois l\'outil unique et les outils séparés.
-   **Mode pour les diamètres/rayons de l\'outil de cotation** : lorsque vous utilisez l\'outil de [cotation](TechDraw_Dimension/fr.md), vous pouvez choisir comment traiter les cercles et les arcs : {{Version/fr|1.0}}
    -   *Automatique* : l\'outil appliquera le rayon aux arcs et le diamètre aux cercles.
    -   *Diamètre* : l\'outil appliquera le diamètre à tous les cercles.
    -   *Rayon* : l\'outil appliquera le rayon à tous les cercles.



## Annotations

<img alt="Préférences de Annotations" src=images/Preferences_TechDraw_Page_Annotation.png  style="width:350px;">



### Annotations 

-   **Motif des vue en coupe** : motif pour la section coupée. Les options sont les suivantes :
    -   *Caché* : pas de surface visible.
    -   *Couleur pleine* : la surface prend la couleur définie pour **Section Face**
    -   *Hachure SVG* : la surface est [hachurée](TechDraw_Hatch/fr.md).
    -   *Hachure PAT* : la surface est [géométriquement hachurée](TechDraw_GeometricHatch/fr.md).
-   **Afficher la ligne de coupe dans la vue source** : si cette option est cochée, l\'annotation de la coupe sera dessinée dans la vue source. Si la case n\'est pas cochée, aucune ligne de coupe, aucune flèche et aucun symbole ne seront affichés dans la vue source. {{Version/fr|1.0}}
-   **Inclure la ligne de coupe dans l\'annotation de la section** : si cette option est cochée, la ligne de coupe sera dessinée sur la vue source. Si la case n\'est pas cochée, seuls les marques de changement, les flèches et les symboles seront affichés. {{Version/fr|1.0}}
-   **Marques des lignes des vues en coupe complexe** : affiche des marques aux changements de direction sur les lignes des [vues en coupe complexe](TechDraw_ComplexSection/fr.md). {{Version/fr|0.21}}
-   **Forme du contour pour les vues détaillées** : forme du contour pour les [vues détaillées](TechDraw_DetailView/fr.md). Les options sont :
    -   *Cercle*
    -   *Carré*
-   **Afficher l\'ajustement des vues détaillées** : cette case à cocher permet d\'afficher ou non le contour d\'une vue détaillée. {{Version/fr|1.0}}
-   **Afficher une surbrillance autour des zones de détail** : cette case à cocher permet d\'afficher ou non une surbrillance autour de la zone de détail dans la vue source du détail. {{Version/fr|1.0}}
-   **Forme des infobulles** : forme des [infobulles](TechDraw_Balloon/fr.md).
-   **Extrémité des infobulles** : style par défaut pour des extrémités des infobulles, voir [Propriétés des infobulles](TechDraw_Balloon/fr#Propriétés.md).
-   **Longueur horizontale de la ligne des infobulles** : longueur horizontale de la ligne des infobulles.
-   **Infobulle en forme de triangle rectangle** : si **Extrémité des infobulles** est mis à *Triangle*, le triangle ne peut avoir une direction verticale ou horizontale que lorsque l\'infobulle est déplacé.
-   **Ligne de repère horizontale automatique** : force le dernier segment de la [ligne de repère](TechDraw_LeaderLine/fr.md) à être horizontal.
-   **Type de rupture de la vue interrompue** : type de rupture par défaut utilisé pour indiquer les [vues interrompues](TechDraw_BrokenView/fr.md) : {{Version/fr|1.0}}
    -   *Aucune ligne d\'interruption*
    -   *Lignes en zigzag*
    -   *Lignes simples*
-   **Afficher les marques des centres** : affiche les marques de centre d\'arc dans les vues.
-   **Imprimer les marques des centres** : affiche les centres des arcs à l\'impression.



### Lignes

-   **Norme des lignes** : norme à utiliser pour tracer des lignes de section dans les [vues en coupe](TechDraw_SectionView/fr.md).
-   **Largeur des lignes dans un groupe** : un [groupe de lignes](TechDraw_LineGroup/fr.md) utilisé pour définir les épaisseurs de lignes.
-   **Style des lignes cachées** : style des lignes cachées. {{Version/fr|1.0}}
-   **Style de ligne de section** : style des lignes de section.
-   **Style des mises en surbrillance des détails** : style des lignes de la forme du contour pour les [vues détaillées](TechDraw_DetailView/fr.md).
-   **Style des lignes centrales** : style par défaut pour les [lignes centrales](TechDraw_FaceCenterLine/fr.md).
-   **Style des lignes d\'interruption** : style par défaut des lignes utilisées pour indiquer les [vues interrompues](TechDraw_BrokenView/fr.md). {{Version/fr|1.0}}
-   **Style des extrémités des lignes** : la valeur par défaut (ronde) devrait presque toujours être le bon choix. Les extrémités plates ou carrées sont utiles si vous prévoyez d\'utiliser un dessin comme guide de coupe 1:1.



## Couleurs

<img alt="Préférences de Couleurs" src=images/Preferences_TechDraw_Page_Colors.png  style="width:350px;">

Configuration des couleurs par défaut pour les nouvelles pages:

-   **Normal** : couleur des lignes normales.
-   **Préselectionnés** : couleur des présélections. Couleur utilisée pour mettre en surbrillance les objets lorsque vous passez la souris dessus.
-   **Sélection** : couleur des objets sélectionnés.
-   **Arrière-plan** : couleur d\'arrière-plan autour des pages.
-   **Dimension** : couleur des lignes de cote et du texte.
-   **Ligne centrale** : couleur des [lignes centrales de faces](TechDraw_FaceCenterLine/fr.md).
-   **Couleur des contours des vues détaillées** : couleur des lignes pour la forme des contours des [vues détaillées](TechDraw_DetailView/fr.md).
-   **Couleur des grilles** : couleur pour toutes les grilles de page.
-   **Soulignement du modèle** : couleur pour le soulignement qui marque les textes modifiables dans les modèles. {{Version/fr|1.0}}
-   **Lignes cachées** : couleur de la ligne cachée. Cette couleur sera utilisée pour toutes sortes de [lignes cachées](#Param.C3.A8tres_HLR.md).
-   **Vues en coupe** : couleur de la surface des [vues en coupe](TechDraw_SectionView/fr.md). Utilisé uniquement si le paramètre **Motif des vue en coupe** est réglé sur *Couleur pleine*.
-   **Lignes des vues en coupe** : couleur de la ligne des [vues en coupe](TechDraw_SectionView/fr.md).
-   **Hachure** : couleur de l\'image des [hachures par motifs](TechDraw_Hatch/fr.md).
-   **Hachure géométrique** : couleur du motif des [hachures géométriques](TechDraw_GeometricHatch/fr.md).
-   **Sommet** : couleur des [vertices](Glossary/fr#V.md) (sommets) sélectionnables dans les vues.
-   **Lignes de référence** : couleur des nouvelles [lignes de référence](TechDraw_LeaderLine/fr.md).
-   **Faces transparentes** : si cette option est cochée, les faces des objets seront transparentes. Sinon, la couleur définie sera utilisée pour les faces.
-   **Clair sur sombre** : si cette option est cochée, le texte et les lignes auront une couleur claire. A utiliser si **Couleur de la page** est sombre. Les faces transparentes ou de couleur claire sont recommandées avec cette option. {{Version/fr|0.21}}
-   **Monochrome** : si cette option est cochée, la couleur définie sera utilisée pour tout le texte et toutes les lignes. {{Version/fr|0.21}}
-   **Couleur de la page** : couleur du fond de la page. {{Version/fr|0.21}}



## Lignes cachées supprimées 

<img alt="Préférences de Lignes cachées supprimées" src=images/Preferences_TechDraw_Page_HLR.png  style="width:350px;">

Version anglaise de la GUI, HLR pour *hidden line removal* (lignes cachées supprimées).

-   **Utiliser l\'approximation du polygone** : utilise une approximation pour trouver les lignes cachées. C\'est rapide, mais le résultat est une collection de courtes lignes droites.
-   **Afficher les lignes dures** : affiche les arêtes et les contours (les lignes visibles sont toujours affichées)
-   **Afficher les lignes de transition**: affiche les lignes de transition. Une ligne de transition est une ligne indiquant un changement entre des surfaces tangentes, comme dans la transition d\'une surface plane à un [congé](https://fr.wikipedia.org/wiki/Arrondi_et_cong%C3%A9).
-   **Afficher les lignes de couture** : affiche les lignes de couture. Une ligne de couture est une frontière entre les faces.
-   **Afficher les lignes isoparamétriques** : affiche les lignes ISO. ISO signifie *isoparamétrique*. [Voici une description (en anglais)](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html) des lignes isoparamétriques (en fait des courbes).
-   **Nombre de lignes isoparamétriques à afficher** : nombre de lignes isoparamétriques par arête de face.



## Avancé

<img alt="Préférences de Avancé" src=images/Preferences_TechDraw_Page_Advanced.png  style="width:350px;">

-   **Détecter les faces** : si cette option est cochée, TechDraw tentera de créer des faces en utilisant les segments de ligne renvoyés par l\'algorithme de suppression de ligne cachée. Les faces doivent être détectés pour utiliser les [hachures](TechDraw_Hatching/fr.md), mais il peut y avoir une dégradation des performances pour les modèles complexes.
-   **Rapport d\'avancement** : messages d\'avancement lors de la construction de la Géométrie de la vue. {{Version/fr|0.21}}
-   **Utiliser le nouvel algorithme de recherche de face** : si cette option est cochée, le nouvel algorithme de recherche de face sera utilisé à la place de l\'algorithme d\'origine. {{Version/fr|0.21}}
-   **Corriger automatiquement les références des cotes** : si cette option est cochée, une tentative est faite pour mettre à jour les références des cotes lorsque le modèle change. {{Version/fr|0.21}}
-   **Afficher les arêtes des coupes** : met en évidence les arêtes des coupes dans les [vues en coupe](TechDraw_SectionView/fr.md).
-   **Unir avant d\'effectuer une vue en coupe** : effectue une opération de fusion sur la ou les formes d\'entrée avant le traitement de la vue en coupe.
-   **Basculer d\'atelier d\'un double-clic** : si cette option est cochée, un double-clic sur une page de l\'arborescence fera basculer automatiquement vers TechDraw et la page sera rendue visible. {{Version/fr|1.1}}
-   **Autoriser des arêtes inhabituelles** : inclut des arêtes avec une géométrie inattendue dans les résultats, par ex. longueurs nulles.
-   **Valider les formes** : si cette option est cochée, les formes saisies seront vérifiées de la présence d\'erreurs avant d\'être utilisées et les formes invalides seront ignorées. Cela peut être plus lent mais peut éviter des plantages. {{Version/fr|1.1}}
-   **Débogage des vues en coupe** : affiche les résultats intermédiaires pendant un traitement des vues en coupe.
-   **Débogage des mauvaises formes** : si cette option est cochée, les formes qui ont échoué à la validation seront sauvegardées en tant que fichiers B-rep pour une analyse ultérieure. {{Version/fr|1.1}}
-   **Débogage des vues détaillées** : affiche les résultats intermédiaires pendant un traitement des vues détailllées.
-   **Passes pour supprimer les chevauchements d\'arêtes** : nombre de tentatives de suppression des chevauchements d\'arêtes renvoyées par l\'algorithme de suppression des lignes cachées. Une valeur de 0 indique qu\'il n\'y a pas de suppression. Les valeurs supérieures à 2 ne sont généralement pas productives. Chaque tentative augmente le temps nécessaire à la production du dessin. {{Version/fr|0.21}}
-   **Zone de sélection autour des bords** : taille de la zone de sélection autour des bords. L\'unité de focalisation est d\'environ 0,1 mm, en fonction de votre zoom en cours.
-   **Zone de sélection autour des marques centrales** : zone de sélection autour des marques centrales. L\'unité de focalisation est d\'environ 0,1 mm, en fonction de votre zoom en cours. La valeur par défaut est 10. Les valeurs comprises entre 20 et 30 facilitent considérablement la sélection des bords. Les valeurs élevées entraînent des chevauchements avec d\'autres éléments du dessin.
-   **Taille maximum des tuiles de hachures SVG** : limite des tuiles SVG d\'une taille de 64x64 pixels utilisées pour hachurer une seule face. Pour des mises à l\'échelle importantes, il se peut que l\'on obtienne une erreur concernant le nombre trop élevé de tuiles SVG, il faut alors augmenter le nombre maximum de tuiles.
-   **Nombre maximum de segments des hachures PAT** : nombre maximal de segments de hachures utilisés pour hachurer une face avec un motif PAT.
-   **Déplacement des infobulles** : la touche de modification pour le déplacement des infobulles peut être modifiée par rapport à la valeur par défaut pour éviter les conflits avec les raccourcis clavier du système d\'exploitation ou du style de navigation. {{Version/fr|1.0}}





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/fr
