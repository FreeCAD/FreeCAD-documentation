# TechDraw TemplateHowTo/fr



{{TutorialInfo/fr
|Topic=Dessin
|Level=Intermédiaire
|Time=60 minutes
|Author=[wandererfan](User:wandererfan.md)
|FCVersion=0.17
}}

## Introduction

Ce tutoriel explique comment créer un fichier [SVG](SVG/fr.md) pouvant être utilisé comme [modèle](TechDraw_Templates/fr.md) d\'arrière-plan pour les pages de l\'[Atelier Techdraw](TechDraw_Workbench/fr.md).

Ce tutoriel suppose que vous connaissez moyennement [Inkscape](https://fr.wikipedia.org/wiki/Inkscape) et [SVG](SVG/fr.md) ainsi que FreeCAD et l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

Nous allons créer un modèle simple pour le papier de format Lettre US en orientation paysage.

Une copie du résultat de ce tutoriel est disponible dans 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/HowToExample.svg
```

Où `$INSTALL_DIR` est le répertoire où FreeCAD a été installé, par exemple 
```python
/usr/share/freecad/Mod/TechDraw/Templates/HowToExample.svg
```

## Créer un document de base 

1\. Ouvrez un nouveau document dans Inkscape.

2\. Dans les propriétés du document

-   Sélectionnez le format de page \"Lettre US\" ou \"A4\" et l\'orientation \"Paysage\".
-   Définissez les unités par défaut sur \"mm\" et le format de page sur les largeurs \"279.4\" et les \"215.9\". Pour DIN-A4, vous voudrez bien utiliser \"210\" and \"297\".

<img alt="" src=images/InkDocProp.png  style="width:800px;"> *align=center|Inkscape: document avec la taille et l'orientation de la page* 

3\. Utilisez l\'éditeur XML pour ajouter une clause d\'espace de noms \"freecad\" à l\'élément `<svg>`.

:   xmlns:freecad="[http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace](http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace)".

Notez que vos textes modifiables *ne fonctionneront pas* si vous utilisez \"<https://>\...\" même si le wiki est accessible via https de nos jours. Puisque SVG est un format lisible par l\'homme, vous pouvez aussi entrer la ligne ci-dessus dans le fichier avec un éditeur de texte. <img alt="" src=images/InkXMLNameSpace.png  style="width:800px;"> *align=center|Inkscape: éditeur XML ajoutant la clause d'espace de noms "freecad" à l'élément <svg>* 

## Créer un modèle de dessin 

4\. Tracez des contours, des numéros de zone, des lignes centrales et autre géométrie.

5\. Dessinez les cases et les lignes du cartouche.

6\. Ajoutez et positionnez votre texte statique.

7\. Ajoutez et positionnez le texte qui sera éditable.

8\. Vous avez maintenant terminé votre illustration, qui devrait ressembler à ceci: <img alt="" src=images/InkFinishedArt.png  style="width:800px;"> *align=center|Inkscape: disposition provisoire du modèle* 

## Créer des champs modifiables 

9\. Utilisez l\'éditeur XML pour ajouter une balise `freecad:editable` à chaque élément `<text>` éditable.

-   Attribuez un nom de champ significatif à chaque texte modifiable.

<img alt="" src=images/InkXMLeditableTag.png  style="width:800px;"> *align=center|Inkscape: éditeur XML ajoute la propriété "freecad:editable" à l'élément <text> souhaitée* 

## Ajuster la taille du SVG 

10\. Utilisez l\'éditeur XML pour ajuster l\'attribut `viewBox` afin qu\'il corresponde à la taille de votre page en millimètres.

-   Il s\'agit de quatre valeurs, au format `"0 0 width height"`

<img alt="" src=images/InkXMLviewBox.png  style="width:800px;"> *align=center|Inkscape: l'éditeur XML ajuste la zone d'affichage pour qu'elle corresponde à la taille de la page en millimètres* 

11\. Votre modèle apparaîtra maintenant beaucoup plus gros que souhaité. <img alt="" src=images/InkMuchTooBig.png  style="width:800px;"> *align=center|Inkscape: mise en page provisoire du modèle dépassant la taille de la page* 

12\. Nous devons le réduire.

-    **Edition → Tout sélectionner dans tous les calques**, ou à partir de la boîte de sélection, sélectionnez tout.

-   Ajustez les boutons **W:** et **H:** à la taille de votre illustration en millimètres.

-   Définissez la taille de la page moins les marges applicables, par exemple, **W: 250** et **H: 200**.

13\. Utilisez \"Aligner et répartir\" ou les sélections **X:** et **Y:** pour positionner l\'illustration dans les limites de la page, si nécessaire.

14\. Votre modèle devrait maintenant être correct comme dans l\'image ci-dessus.

## Supprimer les transformants sur le SVG 

15\. Assurez-vous que tous vos textes modifiables sont \"dissociés\" avec **Shift**+**Ctrl**+**g**.

16\. Sélectionner tout sur votre page, **Edition → Tout sélectionner** puis **Edition → Copier** (**Ctrl**+**c**).

17\. Supprimez ensuite le calque actuel, **Calque → Supprimer le calque courant**.

:   Remarque: si vous avez déjà supprimé le calque (aucun calque n\'est répertorié dans votre panneau Calque), cette étape n\'est pas nécessaire. Dans ce cas, vous devez tout sélectionner (**Ctrl**+**a**), couper la sélection (**Ctrl**+**x**) et la coller avec la commande à l\'étape suivante.

18\. Puis copiez, **Edition → Coller en place**.

:   **Remarque:** Cette commande empêche que les positions du texte soient stockées dans les balises de transformation. Il est important que vous n\'utilisiez pas la commande de collage normale!

19\. Votre modèle devrait maintenant être correct et ne devrait pas avoir de transformations indésirables.

20\. Enregistrez votre modèle. Lorsque vous utilisez Inkscape, enregistrez-le de préférence sous **SVG simple** car FreeCAD ne peut gérer que les fonctionnalités de la spécification SVG 1.1. **SVG simple** supprimera toutes les balises XML spécifiques à Inkscape.

21\. Essayez-le dans FreeCAD et dans l\'[atelier TechDraw](TechDraw_Workbench/fr.md) avec [Nouvelle page selon modèle](TechDraw_PageTemplate/fr.md). ![](images/FCTemplateHow.png ) *align=center|FreeCAD: modèle fini avec un champ de texte modifiable en cours de modification* 

## Remarques

N\'utilisez pas les calques dans Inkscape tant que vous n\'avez pas maîtrisé la création de modèles. Les calques et les groupes peuvent automatiquement insérer des transformations non désirées dans votre fichier [SVG](SVG/fr.md).

Comme dernière étape avant d\'utiliser votre nouveau modèle, assurez-vous de supprimer toutes les clauses de transformation du code Svg. Les clauses de transformation **causeront des problèmes**.

Voir une discussion sur Stackoverflow à l\'adresse [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

Si vous ne voyez pas les cases vertes pour vos textes modifiables, il se peut qu\'il y ait un problème avec l\'échelle de votre document. Ouvrez à nouveau votre fichier dans Inkscape et confirmez les valeurs de la boîte de vue et les tailles correspondantes.


{{Tutorials navi

}} {{TechDraw Tools navi}} 
