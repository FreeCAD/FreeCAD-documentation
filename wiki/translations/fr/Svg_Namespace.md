# Svg Namespace/fr
**Le développement de l'[atelier Drawing](Drawing_Workbench/fr.md) s'est arrêté, et un nouvel atelier [Techdraw](TechDraw_Workbench/fr.md) visant à le remplacer, a été introduit dans la version 0.17. Les deux ateliers ont été livrés de la v0.17 à la v0.20, mais depuis la v0.21, l'atelier Drawing n'est plus inclus.**


{{Message|Actuellement, l'atelier TechDraw utilise toujours l'attribut '''freecad:EditableText''' et la déclaration d'espace de noms correspondante dans ses modèles aujourd'hui.}}




## Introduction

FreeCAD peut importer et exporter des documents [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) contenant du code appartenant à un certain **espace de noms** qui est un sous-ensemble d\'instructions XML.

Comme tout document XML, un document SVG se compose de deux sections :

-   L\'en-tête : une seule ligne pour déclarer la version du langage XML utilisée pour les instructions dans le corps de ce document.
-   Le corps : une liste d\'instructions. Les documents SVG contiennent toutes les instructions dans des balises<svg>.

:   La balise d\'ouverture contient des informations sur la taille et les espaces de noms SVG utilisés.



## Espace de noms par défaut 

=

L\'espace de noms SVG par défaut utilisé par FreeCAD est déclaré par cette ligne :


{{Code|lang=xml|code=
xmlns="http://www.w3.org/2000/svg" version="1.1"
}}

Le lien externe mène à un site web contenant des informations sur l\'espace de noms et son ensemble d\'instructions. Les attributs de cet espace de noms sont utilisés sans préfixe.



## Extension de l\'espace de noms 

Les attributs manquants dans l\'espace de noms SVG peuvent être ajoutés par des extensions d\'espace de noms. FreeCAD utilise une telle extension pour les modèles de dessin. Les modèles pour l\'atelier Drawing utilisent quatre attributs personnalisés qui sont marqués d\'un préfixe \"freecad:\" :

-   [freecad:EditableText](#freecad_EditableText.md), cet attribut est toujours utilisé pour les modèles de l\'atelier TechDraw.
-   [freecad:basepoint1](#freecad_basepoint1.md)
-   [freecad:basepoint2](#freecad_basepoint2.md)
-   [freecad:dimpoint](#freecad_dimpoint.md)

Une déclaration d\'espace de noms est utilisée pour introduire le préfixe et le lien vers le site web correspondant, **cette page** :


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
}}

Le lien n\'est pas utilisé pour récupérer des informations ou des valeurs au moment de l\'exécution, mais c\'est la clé qui permet d\'activer les attributs personnalisés.



### Modèles de Drawing 

Dans les documents [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) exportés par l\'[atelier Drawing](Drawing_Workbench/fr.md) de FreeCAD et utilisés comme des [modèles](Drawing_templates/fr.md) de pages (de dessin), les [attributs](http://www.w3schools.com/xml/xml_attributes.asp) personnalisés peuvent être utilisés, à l\'origine pour l\'usage interne de FreeCAD, mais ils pourraient également être utilisés par d\'autres applications compatibles avec FreeCAD à l\'avenir. Ces attributs utilisent tous le préfixe d\'[espace de nom](http://www.w3schools.com/xml/xml_namespaces.asp) **freecad:**. L\'URL de l\'espace de noms définie dans ces documents SVG renvoie à cette page.

:   L\'atelier Drawing n\'est plus inclus dans FreeCAD {{VersionPlus/fr|0.21}} et ces modèles de Drawing sont donc obsolètes.



### Modèles de TechDraw 

L\'atelier TechDraw utilise également des modèles SVG mais ne peut pas créer et exporter des modèles. Il s\'appuie sur [freecad:EditableText](#freecad_EditableText.md) pour les entrées dans les blocs de titre.



### Migrer vers freecad.org 

Depuis que le wiki de FreeCAD, y compris **cette page**, a été migré de **freecadweb.org** à **freecad.org** avec la version 0.21, le lien doit être mis à jour en conséquence :


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
}}

Les mises à jour des modèles TechDraw contiennent maintenant une clé qui ne peut pas activer les attributs personnalisés lorsqu\'ils sont utilisés avec FreeCAD {{VersionMinus/fr|0.20}} par conséquent, les textes éditables des modèles récents ne sont pas reconnus et sont donc traités comme du texte brut.

:   Dans de tels cas, le \"web\" doit être réinséré manuellement dans la déclaration de l\'espace de noms du modèle.

Il semble que {{VersionPlus/fr|0.21}} puisse traiter l\'une ou l\'autre adresse de lien.



## Utilisation

un pixel = un millimètre

Vous devez insérer, quelque part dans votre code svg, où vous souhaitez que le contenu du dessin apparaisse (par exemple à la fin du fichier, juste avant la derniere balise \'\'\'


</svg>

\'\'\'), la ligne suivante :

 xml



 xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Pour obtenir une impression à l\'échelle, la taille réelle doit être inscrite dans les attributs width et height du SVG-Tag. L\'unité du document utilisateur doit être le pixel(px), et doit être renseigné dans l\'attribut viewBox.

Ce qui suit doit être formaté comme dans l\'exemple ci-dessous :

-   xxx = pixel width (largeur)
-   yyy = pixel height (hauteur)

 xml
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


Les informations complémentaires pour l\'espace de travail et le bloc du titre peuvent être ajoutées et sont définies sur la page [Drawing Modèles](Drawing_templates/fr.md).



## Attributs



### [freecad:EditableText](#Exemple_de_code_freecad_EditableText.md)

Pour utiliser l\'un des attributs **freecad:** dans vos documents SVG, vous devez d\'abord définir l\'espace de nom freecad comme un attribut de la balise d\'ouverture


<svg>

Définit un texte dans un modèle qui peut être édité par FreeCAD.

Exemple :

 xml
<text freecad:EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad:basepoint1

Définit le premier point d\'un objet [Draft Dimension](Draft_Dimension/fr.md) (représenté comme un groupe dans un document SVG). Cet attribut est utilisé lors de l\'importation du fragment SVG dans FreeCAD, afin de recréer l\'objet dimension. Le groupe contient des chemins et d\'autres éléments graphiques pour rendre correctement l\'objet de dimension dans d\'autres applications SVG.

Exemple :

 xml
<g freecad:basepoint1="0.5 4.34" freecad:basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>


### freecad:basepoint2

Définit le deuxième point d\'un objet [Draft Dimension](Draft_Dimension/fr.md) (représenté comme un groupe dans un document SVG). Cet attribut est utilisé lors de l\'importation du fragment SVG dans FreeCAD, afin de recréer l\'objet dimension. Le groupe contient des chemins et d\'autres éléments graphiques pour rendre correctement l\'objet de dimension dans d\'autres applications SVG.

Exemple: voir [freecad:basepoint1](#freecad_basepoint1.md)

### freecad:dimpoint

Définit le point d\'un objet [Draft Dimension](Draft_Dimension/fr.md) par lequel passe la ligne de cote. Cet attribut est utilisé lors de l\'importation du fragment SVG dans FreeCAD, afin de recréer l\'objet dimension. Le groupe contient des chemins et d\'autres éléments graphiques pour rendre correctement l\'objet de dimension dans d\'autres applications SVG.

Exemple: voir [freecad:basepoint1](#freecad_basepoint1.md)



### Exemple de code freecad:EditableText 

Cet exemple provient du cartouche de la feuille [A3 Paysage](Misc_templates/fr#A3_paysage_texte_US_complet_avec_convention_US.md)



#### 1 : Titre sans textedit 

<img alt="" src=images/Svg_Namespace_01.png  style="width:300px;">

 xml
  <g
     id="g3587">
    <text
       sodipodi:linespacing="119.00001%"
       id="text3482"
       y="229.10912"
       x="220.8476"
       style="font-size:1.97555566px;font-style:normal;font-weight:normal;line-height:119.00000572%;letter-spacing:0.01975556px;word-spacing:0.00846667px;writing-mode:lr-tb;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"
       xml:space="preserve"><tspan
         y="229.10912"
         x="220.8476"
         id="tspan3484"
         sodipodi:role="line">AUTHOR NAME :</tspan></text>




#### 2 : Titre avec textedit 

<img alt="" src=images/Svg_Namespace_02.png  style="width:300px;">

 xml
  <g
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">
    <text
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"
       freecad:editable="AuthorName"><tspan
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>
    <text
    ...
    ...
    ...
    ... </text>
  
  </g>




#### Explications

 xml
  <g


Début du cadre

 xml
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">


Données dans le cadre

 xml
    <text


Début du bloc de textes

 xml
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"


Toutes les informations sur le texte qui va être affiché

 xml
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"


Coordonnées et renseignements du texte qui va être affiché.

 xml
       freecad:editable="AuthorName"><tspan


Ici **AuthorName** est la variable qui va mémoriser la chaîne **freecad:editable** qui sera modifiée et affichée dans la feuille.

 xml
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Coordonnées et renseignements sur le texte qui est affiché par défaut, la balise **** délimite la fin du bloc texte.

 xml
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Autres blocs textes et la balise **** détermine la fin du groupe de textes.

Il est possible qu\'après avoir travaillé dans le fichier SVG avec Inkscape le fichier ne fonctionne plus, il est possible que des informations aient disparu.

Ensuite, vérifiez que **freecad:editable:** n\'est pas modifié.

Exemple:

-   **editable** = \"AuthorName\"
-   replacer par **freecad:editable** = \"AuthorName\"



## Autres attributs disponibles 

Voir [Drawing Modèles](Drawing_templates/fr.md)


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/fr
