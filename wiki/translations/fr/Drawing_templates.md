# Drawing templates/fr
**L'[atelier Drawing](Drawing_Workbench/fr.md) est devenu obsolète dans la version 0.17. Pensez à utiliser l'[atelier TechDraw](TechDraw_Workbench/fr.md) à la place.**




## Création d\'une feuille SVG 

Créer des modèles pour le module de dessin est très facile. Voir aussi le tutoriel [Drawing Template : Comment faire](Drawing_Template_HowTo/fr.md). Les modèles sont des fichiers svg, créés avec n\'importe quelle application capable d\'exporter des fichiers svg, tels que [Inkscape](http://www.inkscape.org). Cependant, vous devrez souvent ouvrir le fichier svg dans un éditeur de texte par la suite, afin de respecter les règles suivantes. Seulement deux règles doivent être suivies:

### Règles de base 

-   Un pixel = un millimètre. Vous pouvez avoir la taille de la page spécifiée à l\'intérieur de la balise d\'ouverture<svg>, sans unités ou avec \"mm\". Par exemple, ces deux formes sont valides:

 html
width="1067mm"
height="762mm"


ou

 html
width="1067"
height = "762"


Bien que svg supporte les pouces (\"42in\"), ceux-ci ne sont actuellement pas supportés par FreeCAD, donc il est toujours préférable d\'avoir la taille de votre page svg spécifiée en millimètres. L\'attribut \"viewBox\" doit avoir la même valeur, par exemple:

 html
viewBox="0 0 1067 762"


-   Vous devez insérer, quelque part dans votre code svg, l\'endroit où vous voulez que le contenu du dessin apparaisse (par exemple à la fin du fichier, juste avant la dernière balise \</ svg\>), la ligne suivante:

 html



Ce texte ci-dessus (qui est en fait un commentaire XML) doit se trouver sur une ligne distincte et ne pas être intégré au milieu d\'autres parties du texte. Prenez garde, si vous rouvrez et réenregistrez votre modèle dans inkscape, après avoir ajouté la ligne ci-dessus, inkscape conservera la ligne, mais ajoutera d\'autres éléments xml sur la même ligne, ce qui empêchera le modèle de fonctionner. Vous devrez l\'éditer avec un éditeur de texte et isoler le commentaire ci-dessus sur sa propre ligne.

### Espace de noms 

-   Plusieurs objets (en particulier ceux créés avec la commande [Draft Dessin](Draft_Drawing/fr.md) et si votre modèle contient des textes éditables) utilisent un [Espace de noms Svg](Svg_Namespace/fr.md) spécifique à FreeCAD. Cela permet à FreeCAD de détecter des éléments spécifiques dans les fichiers svg, que les autres applications vont ignorer. Si vous prévoyez d\'utiliser l\'un de ces éléments, vous devez ajouter cette ligne dans la balise d\'ouverture<svg>, par exemple avec les autres lignes xmlns ajoutées par inkscape:

xmlns:freecad=\"<http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace>\"

### Bloc de titre 

En plus de ces règles, depuis FreeCAD 0.14, des informations sur le bloc Border et Title peuvent être ajoutées au modèle pour être utilisées par l\'outil de projection orthographique. Cette information définit où FreeCAD peut et ne peut pas placer les projections.

Pour définir la bordure, la ligne suivante doit apparaître avant la balise  dans le fichier svg.

 html



Où X1, Y1, X2, Y2 sont définies comme suit:

-   X1 est la distance sur l\'axe X entre le bord gauche de la page et le côté gauche de la bordure.
-   Y1 est la distance sur l\'axe Y entre le bord supérieur de la page et le haut de la bordure.
-   X2 est la distance sur l\'axe X du bord gauche de la page au côté droit de la bordure.
-   Y2 est la distance sur l\'axe Y entre le bord supérieur de la page et le bas de la bordure.

![](images/XY_Working_v2.svg )

Pour définir le cartouche, la ligne suivante doit être insérée avant la balise  et après la balise Working space.

 html



Où X1a, Y1a, X2a Y2a sont définies comme suit:

-   X1a est la distance sur l\'axe X du bord gauche de la page au côté gauche du bloc Titre
-   Y1a est la distance sur l\'axe Y du bord supérieur de la page au sommet du bloc Titre
-   X2a est la distance sur l\'axe X du bord gauche de la page au côté droit du bloc de titre
-   Y2a est la distance sur l\'axe Y du bord supérieur de la page au bas du bloc Titre
-   X1a \<= X1 ou X2a\> = X2
-   Y1a \<= Y1 ou Y2a\> = Y2

![](images/XY_Title_v2.svg )

Voici un exemple de code qui définit les zones Espace de travail et Bloc de titre à insérer avant la balise . Vous n\'avez pas besoin de spécifier un cartouche, mais si vous le faites, vous devez le définir sur la ligne suivante immédiatement après l\'espace de travail:

 html




Afin d\'avoir une impression à la bonne échelle, la taille réelle du texte doit être fixée dans les attributs width et height de la section SVG-Tag. L\'unité du document doit être donnée en (px), et doit être donnée dans l\'attribut viewBox.

Ce qui suit doit être formaté comme dans l\'exemple ci-dessous où:

-   xxx = pixel width
-   yyy = pixel height

 html
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


-   Plusieurs attributs personnalisés peuvent être placés dans les modèles. La liste des attributs pris en charge actuellement est disponible sur la page [Svg Namespace](Svg_Namespace/fr.md).

## Modèles au format DXF 

Depuis la version 0.15, FreeCAD peut exporter une page [Drawing](Drawing_Workbench/fr.md) au format DXF. Ce système utilise également des templates. Si un fichier DXF avec le même nom se trouve dans le même dossier que le modèle SVG utilisé pour une page, il sera utilisé pour l\'exportation. Si non, un modèle vide sera créé par défaut.

Par conséquence, si vous créez vos propres templates au format SVG, et que vous souhaitez exporter les pages de dessin que vous créez au format DXF, il vous suffit de créer un modèle DXF correspondant, et de l\'enregistrer avec le même nom et dans le même dossier.

Les modèles DXF peuvent être créés avec n\'importe quelle application qui produit des fichiers au format DXF, comme LibreCAD. Vous devez ensuite les éditer avec un éditeur de texte, et ajouter deux lignes supplémentaires, une au début ou à la fin de la section BLOCKS, et l\'autre au début ou à la fin de la section ENTITIES, entre ces deux lignes se trouve l\'espace où FreeCAD va ajouter ses propres blocs et entités.

Un modèle (feuille de dessin) très simple ressemble à ceci:

    999
    FreeCAD DXF exporter v0.15
    0
    SECTION
    2
    HEADER
    9
    $ACADVER
    1
    AC1009
    0
    ENDSEC
    0
    SECTION
    2
    BLOCKS
    $blocks
    0
    ENDSEC
    0
    SECTION
    2
    ENTITIES
    $entities
    0
    ENDSEC
    0
    EOF

Le modèle ci-dessus ne contient aucune entité. Si vous créez votre fichier DXF avec une application de CAO, il y aura probablement beaucoup plus de contenu dans les sections HEADER, BLOCKS et ENTITIES.

Les deux lignes que FreeCAD recherchera sont \"\$blocks\" et \"\$entities\". Elles doivent exister dans le modèle, et doivent être placées leur place. Vous pouvez choisir de les placer juste après les lignes BLOCKS ou ENTITIES, ce qui est plus facile (il suffit d\'utiliser la fonction \"recherche\" de votre éditeur de texte pour les trouver), ou à la fin, juste avant les lignes \"0 ENDSEC\" (méfiez-vous il y en a un pour chaque section, assurez-vous d\'utiliser ceux relatifs aux BLOCKS et ENTITIES). Cette dernière méthode sera utilisée pour placer les objets de FreeCAD après que les objets soient définis dans le modèle, ce qui devrait être plus logique.

## Modèles A3 

### A3 classique : 

<img alt="" src=images/A3_Classic.svg  style="width:800px;">

### A3 vide : 

<img alt="" src=images/A3_Clean.svg  style="width:800px;">

### A3 moderne : 

<img alt="" src=images/A3_Modern.svg  style="width:800px;">

### A3 vitrine : 

<img alt="" src=images/A3_Showcase.svg  style="width:800px;">

### A3 paysage anglais : 

<img alt="" src=images/A3_Landscape_english.svg  style="width:800px;">

## A4 Templates 

### Landscape:

<img alt="" src=images/A4_Landscape_english.svg  style="width:800px;">

### A4 Portrait 1 english: 

<img alt="" src=images/A4_Portrait_1_english.svg  style="width:400px;">

## US Letter Templates 

### US Letter Landscape: 

<img alt="" src=images/US_Letter_landscape.svg  style="width:800px;">

### US Letter portrait: 

<img alt="" src=images/US_Letter_portrait.svg  style="width:400px;">

### US Letter ds Landscape: 

<img alt="" src=images/US_Letter_ds_Landscape.svg  style="width:800px;">

### US Legal ds Landscape: 

<img alt="" src=images/US_Legal_ds_Landscape.svg  style="width:800px;">

### US Ledger ds Landscape: 

<img alt="" src=images/US_Ledger_ds_Landscape.svg  style="width:800px;">

## Autres standards disponibles 

-   [ANSI templates](ANSI_templates/fr.md): au standard American National Standards Institute [ANSI](http://en.wikipedia.org/wiki/American_National_Standards_Institute)
-   [Arch templates](Arch_templates/fr.md): au standard American National Standards Institute [Arch](http://en.wikipedia.org/wiki/American_National_Standards_Institute)
-   [Misc templates](Misc_templates/fr.md): Autres modèles


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Documentation](Category_Documentation.md) > [Drawing](Category_Drawing.md) > Drawing templates/fr
