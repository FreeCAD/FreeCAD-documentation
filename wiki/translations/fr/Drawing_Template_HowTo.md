---
- TutorialInfo   */fr
   Topic   *Modélisation 2D
   Level   *Intermédiaire
   Author   *Mark Stephen ([Quick61](User_Quick61.md))
   Time   *Moins d'une heure
   FCVersion   *0.14.3700 ou plus
---

# Drawing Template HowTo/fr




<div class="mw-translate-fuzzy">


**L'[atelier Drawing](Drawing_Workbench/fr.md) est devenu obsolète dans la version 0.17. Pensez à utiliser l'[atelier TechDraw](TechDraw_Workbench/fr.md) à la place.**


</div>



## Introduction

Ce tutoriel vous guidera pas à pas pour créer et modifier un fichier graphique SVG pour l\'utiliser comme feuille de dessin au sein de l\'[atelier Drawing](Drawing_Workbench/fr.md) de FreeCAD. À partir de la version 0.14, révision 2995, de FreeCAD l\'atelier Drawing va projeter la partie sélectionnée de votre objet sur la feuille en tenant compte de l\'ensemble des règles contenues dans le document SVG suivant. Ces règles définissent l\'espace de travail, en coordonnées X/Y, où FreeCAD peut afficher le projet et éviter automatiquement les intrusions dans l\'espace occupé par le cartouche.

Tout le monde peut s\'il le veut partager ses feuilles de conception, toutes les directives de base énoncées dans ce tutoriel devraient être suivies. Il y a des balises pour \"Working space\" et \"Title block\" (cartouche) incluses dans le modèle SVG, il ne sont pas inclus dans les anciennes versions de FreeCAD. En incluant ces balises, votre feuille sera entièrement fonctionnelle pour les versions actuelles.

Ce didacticiel commence avec la mise en place d\'une page dans Inkscape et crée le dessin de la feuille de base. Puis nous ajouterons un logo pour donner une touche personnelle ou professionnelle à notre travail. Ensuite, nous verrons comment modifier notre nouvelle feuille et quels renseignements elle doit contenir pour être utilisée avec FreeCAD.

Ce tutoriel suppose que vous connaissez les base sur l\'utilisation de Inkscape et d\'un éditeur de texte.

## Les Bases 

### Mise en page 

Commençons avec un nouveau document dans Inkscape. En se référant sur la page du Wiki de FreeCAD sur la construction de feuilles de dessin (Template), un pixel = un millimètre. Ce qui signifie que si vous souhaitez créer une feuille de format ANSI A la taille de la page, (format lettre), est de 216 mm X 279 mm, notre feuille devra avoir une taille 216px X 279px. Si vous souhaitez que la feuille ait une orientation paysage, ces chiffres doivent être inversés. Pour ce tutoriel, l\'orientation paysage sera utilisée. La feuille est définie comme ayant 279px de large et 216px de haut.

Après avoir exécuté Inkscape, déroulez le menu fichier et sélectionnez **Propriétés du Document**, vous devriez voir la fenêtre des propriétés du document. Modifiez la largeur et la hauteur comme indiqué et assurez vous que le px (pixel) est l\'unité.

<img alt="" src=images/Inkscape_Template_tut_1.png  style="width   *780px;">

Vous devriez maintenant avoir un document Inkscape qui est de 279px large et haute de 216px. Maintenant procédons pour ajouter une bordure.

### Le Cadre 

Ensuite, faites le cadre. Quoique non nécessaire pour ce tutoriel, il est référencé plus tard.

À l\'aide de l\'outil \"Courbes de Bézier et segments de droites\" et en sélectionnant le Mode \"Créer une séquence de segments de lignes droites\", faire un rectangle (cadre) à l\'intérieur du document. Une fois que ce rectangle est fermé, cliquez sur l\'outil \"Sélectionner et transformer des objets (F1)\". Le rectangle (cadre) doit maintenant être sélectionné. Si ce n\'est pas le cas, utilisez l\'outil et sélectionnez-le.

En utilisant les coordonnées horizontales et verticales des paramètres de sélection, ainsi que les paramètres Largeur et Hauteur de la sélection, nous placerons les unités frontalières à 10 unités, (px) sur les bords du document. Entrez la commande suivante. Pour la valeur X entrez 10, pour la valeur Y entrer 10, pour la Largeur entrer 259 et pour la Hauteur entrez 196. Vous verrez que le coin inférieur gauche du rectangle est à 10 points au dessus du bord et à 10 points du coin inférieur gauche de la page. Entrez la largeur et la hauteur de la taille du rectangle il est donc maintenant espacé (centré) dans les limites du document.

![](images/Inkscape_Template_tut_2.png )

### Le Cartouche 

Maintenant, vous aller faire le cartouche. C\'est là où le texte modifiable dans le dessin sera entré lorsqu\'il sera utilisé avec FreeCAD. Ce didacticiel utilise un simple exemple. Le cartouche peut être aussi simple ou complexe que l\'on veut.

Cet exemple de cartouche contient , Project Name, Date, Scale, et Author. Il sera ensuite placé dans le coin inférieur droit du cadre de la feuille.

Vous allez tout d\'abord faire un rectangle quelque part à l\'intérieur du document. Faites le de la même manière que vous avez fait le cadre. Puis divisez-le en 4 sections comme bon vous semble. Une fois fait, sélectionnez le rectangle et les séparations, faites un groupe et placez-le à X = 169, Y = 10 et la taille à L = 100, H = 50, de la même manière que pour le cadre.

![](images/Inkscape_Template_tut_3.png )

### Fixer le Texte 

Maintenant nous allons ajouter les blocs de texte qui seront solidaires du cartouche. Ceux-ci seront Project Name, Date, Scale, et Author. Pour ce faire, sélectionnez l\'outil texte et cliquez quelque part dans le document. Ensuite il suffit de taper le texte, un nom pour chaque case. Cliquez sur l\'outil texte dans le document et après avoir sélectionné la taille de police appropriée, (pour cet exemple taille 6), tapez Project Name. Puis, déplacez le pointeur vers un nouvel emplacement et cliquez encore une fois sur un nouveau bloc de texte pour la Date. Faites de même pour Scale et Author. Maintenant à l\'aide de l\'outil \"Sélectionner les blocs de texte individuels\" peut être déplacé en faisant glisser ou en utilisant les touches de direction pour les placer aux endroits désirés.

Après avoir mis les blocs de texte, sélectionnez les tous ainsi que le cartouche et faites un groupe avec l\'ensemble. À ce stade le cartouche et les textes fixes sont tous assemblés comme un bloc.

![](images/Inkscape_Template_tut_4.png )

### Textes Éditables 

Maintenant, vous allez ajouter les blocs de texte qui seront modifiables à partir de FreeCAD. De la même manière que les textes fixes ont été fait, les textes modifiables seront adaptés et placés à leurs positions respectives, vous utiliserez le texte comme suit, NAME, DATE, SCALE, AUTHOR et leurs donner une hauteur de police de 8 px. Une fois que les textes sont placés, sélectionnez les 4 textes qui seront modifiables et faites-en un groupe distinct. Ne les mettez pas dans le même groupe que le cartouche ou du cadre. Pour l\'instant, vous avez terminé avec le texte modifiable. Une fois la partie graphique de la feuille terminée, vous achèverez la finition de ces textes modifiables à partir de FreeCAD. Pour l\'instant, nous allons terminer cette partie avec l\'ajout d\'un petit logo dans notre feuille.

![](images/Inkscape_Template_tut_5.png )

## Mode avancé 

### Ajouter un logo 

Maintenant que la feuille de base est faite, vous pouvez lui ajouter un logo. Ce peut être n\'importe quelle image. Le logo d\'une firme ou un logo personnel, une photo ou un rendu de votre projet, etc\... Pour ce tutoriel le logo de FreeCAD, trouvé dans la section [Artwork](Artwork/fr.md) du Wiki FreeCAD sera utilisé. Choisissez votre image et vous pouvez tout simplement faire clic droit sur l\'image et sélectionnez \"Enregistrer l\'image sous\". Une fois l\'image enregistrée, importez-la dans Inkscape. Avec l\'image importée dans votre feuille, elle peut être de n\'importe quelle taille et placée où vous voulez. Ajouter une image à votre feuille est aussi simple que ça.

À ce stade, vous pouvez sélectionner le fichier, puis enregistrez votre feuille. Dans ce tutoriel, le fichier a été tout simplement nommé TemplateExample.svg, mais vous pouvez lui donner le nom que vous voulez.

![](images/Inkscape_Template_tut_6.png )

## Une fois la feuille finie 

### Ouvrir le fichier dans un éditeur de texte 

Une fois votre feuille enregistrée, ouvrez-la avec votre éditeur de texte favori. Cela peut être quelque chose d\'aussi simple que le bloc-notes ou un éditeur plus complet comme Kate ou (Notepad++ pour Windows). Dans ce tutoriel, Kate est utilisé et toutes les captures d\'écran sont faites sur de cet éditeur.

Ouvrez le fichier SVG avec votre éditeur de texte, vous verrez le texte suivant.

![](images/Kate1.png )

### Le Tag \"xmlns   *freecad\" 

La première chose à faire est d\'insérer la ligne suivante dans le document. Cette ligne est la déclaration **SVG\_namespace** et doit être fournie afin que tous les éléments SVG soient identifiés comme appartenant à **SVG\_namespace**

 {.XML}
xmlns   *freecad="http   *//www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Cette ligne est ajoutée immédiatement après la première balise


<svg>

, et dans le même alignement où les autres entrées xmlns sont placées.

![](images/Kate2.png )

### Taille de la page 

Afin de permettre l\'impression du dessin final dans la bonne échelle, la page doit contenir ses dimensions en unités réelles 1/1. Sinon la page de dessin entière serait imprimée à une échelle plus basse avec un facteur de 3.54 (90 (px/in) / 25.4 (mm/po)). A l\'intérieur de la feuille \<SVG\>-Tag l\'unité \"mm\" est ajoutée aux champs de width et height. Et un attribut viewBox doit être ajouté. Les données dans viewBox varient de 0 0 à width et height (largeur et hauteur) de la feuille. De cette façon, l\'unité utilisée par la feuille SVG qui est le (px) est redéfini pour être 1 mm de longueur. Dans les programmes comme Inkscape pourront imprimer une élaboration résultante à l\'échelle. Les versions actuelles de Inkscape gèrent très mal cette information. Inkscape redimensionne efficacement l\'ensemble du document à 90dpi. Ce n\'est pas vraiment un problème pour un dessin final, mais impose des difficultés pour l\'édition de modèles de dessin. Après modification d\'une feuille dans Inkscape, elle aurait la même taille de format sur Inkscape mais les éléments du dessin seraient réduits d\'un facteur de 3.54. (Parce que le modèle serait créé en 90dpi mais FreeCAD l\'interprète comme 1px/mm.) Par conséquent, il est recommandé de retirer le \"mm\" de la largeur et la hauteur des attributs avant d\'ouvrir une feuille existante dans Inkscape et après de recréer les unités et attribut dans la balise viewBox.

 {.html}
width="279mm"
height="216mm"
viewBox="0 0 279 216"


![](images/Kate2a.png )

### Working space et la balise Title block 


<div class="mw-translate-fuzzy">

Dans les lignes suivantes nous ajouterons un espace de travail et une balise pour le bloc de textes. Ces balises et leurs utilisations sont définis dans la feuille de dessin. Même si ces balises ne sont pas nécessaires, les versions plus récentes de l\'atelier Draw de FreeCAD les utilisent et n\'affectent pas les anciennes versions.


</div>


<div class="mw-translate-fuzzy">

La balise **Working space** est utilisée pour définir l\'espace dans lequel FreeCAD peut faire ses projections. Cela permet à FreeCAD de faire des projections automatiques dans le cadre et dans l\'espace défini sur la page.


</div>

La balise **Title block** est utilisée pour définir où le cartouche se situe dans l\'espace de travail. Cette information est utilisée par FreeCAD pour que cet espace de travail ne sois pas utilisé. Ceci peut être traduit comme \"espace réservé à ne pas utiliser\".

Si les deux balises sont utilisées, la balise **Working space** doit être placée en premier et être immédiatement suivie par la balise **Title block**. Les deux balises doivent également se trouver avant la première balise **metadata**. Ces balises peuvent être placées dans la partie supérieure (entête du fichier), suite à la balise **xml** ou immédiatement avant la balise **metadata**. Pour ce tutoriel, nous les placerons en haut.

#### La balise Working space 


<div class="mw-translate-fuzzy">

La première balise est la balise **Working space** et est formatée comme suit.


</div>

 {.html}



Où X1, Y1, X2, Y2 sont définis comme    *

-   X1 est la distance de l\'axe X du bord gauche de la page sur le côté gauche de la bordure.
-   Y1 est la distance de l\'axe Y du bord supérieur de la page le haut de la bordure.
-   X2 est la distance de l\'axe X du bord gauche de la page à droite de la bordure.
-   Y2 est la distance de l\'axe Y du bord supérieur de la page le bas de la bordure.

Donc pour la feuille de ce tutoriel, la balise sera **Working space**.

 {.html}



#### La balise Title block 

La balise suivante est la balise **Title block** et est formatée comme suit    *

 {.html}



Où X1a, Y1a, X2a Y2a sont définis comme   *

-   X1a est la distance de l\'axe X du bord gauche de la page sur au bord gauche du cartouche
-   Y1a est la distance de l\'axe Y du bord supérieur de la page au bord supérieur du cartouche
-   X2a correspond à la distance de l\'axe X entre le bord gauche de la page au bord droit du cartouche
-   Y2a est la distance de l\'axe Y du bord supérieur de la page au bord inférieur du cartouche
-   X1a \< = X 1 ou X2a \> = 2 X \* Y1a \< = Y1 ou Y2a \> = Y2

Pour, la balise qui référence le cartouche créé avec ce tutoriel, elle est défini comme suit    *

 {.html}



La position des deux balises, dans l\'ordre et en haut du document ressemble à ceci    *

![](images/Kate3.png )

### La balise freecad   *editable 

Ajouter la balise **freecad   *editable** permet à FreeCAD d\'accéder aux blocs de textes modifiables définis pour l\'édition dans le document SVG. Pour modifier les blocs de textes que vous souhaitez modifier à partir de FreeCAD, procédez comme suit.

Cherchez vers le bas dans le document SVG jusqu\'à trouver la section qui contient le texte que vous souhaitez modifier. Lorsque vous avez effectué votre feuille, vous les avez placés dans un groupe, et par conséquent, ils doivent apparaître dans le document aussi comme un groupe. Les groupes sont délimités par les balises **\<g . . . . \<g/\>**. Une fois que ce groupe d\'éléments de textes est trouvé, vous allez ajouter la ligne \'\'\'freecad   *editable = \"\" \'\'\' la variable de chaque bloc de texte que vous souhaitez modifier est contenu entre guillemets. Placez la ligne comme indiqué pour les quatre lignes de texte modifiables.

![](images/Kate4.png )

### La balise DrawingContent 

La dernière balise qui est nécessaire dans la feuille est la balise **DrawingContent**. Sans elle, FreeCAD ne peut pas accéder à notre feuille de dessin. Cette balise informe FreeCAD où il peut écrire ses projections et autres attributs dans le document SVG. Cette balise doit être située dans le document SVG pour que FreeCAD puisse travailler avec elle.

Cette balise est formatée comme suit et est insérée juste avant la dernière balise \'\'\'


</svg>

\'\'\'.

 {.html}



![](images/Kate5.png )

C\'est terminé. Le document SVG peut maintenant être enregistré et utilisé avec FreeCAD.

## Exemple Complet de la feuille 


<div class="mw-translate-fuzzy">

Voici la feuille SVG finie. Elle est au format SVG, vous pouvez l\'enregistrer et l\'ouvrir dans votre éditeur de texte pour l\'examiner comme référence à ce tutoriel et la création de vos propres feuilles.


</div>

![](images/TemplateExample.svg )

## Les outils 

Les deux outils utilisés dans ce tutoriel sont Inkscape et Kate. Ils peuvent être trouvés en cliquant sur les liens ci-dessous.

-   [Inkscape](http   *//www.inkscape.org/)
-   [Kate](http   *//kate-editor.org/)


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing Template HowTo/fr
