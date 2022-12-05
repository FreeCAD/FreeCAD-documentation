# Svg Namespace/fr
**Le développement de l'[atelier Mise en plan](Drawing_Workbench/fr.md) s'est arrêté, et un nouvel atelier [Techdraw](TechDraw_Workbench/fr.md) visant à le remplacer sera introduit dans la version 0.17. Les deux ateliers seront fournis dans la version v0.17, mais l'atelier Mise en plan peut être supprimé dans les versions ultérieures.**


{{TOCright}}

Dans les documents [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) exportés par l\'[atelier Drawing](Drawing_Workbench/fr.md) de FreeCAD et utilisés comme des pages [modèles](Drawing_templates.md), plusieurs [attributs](http://www.w3schools.com/xml/xml_attributes.asp) personnalisés peuvent être utilisés, à l\'origine pour l\'usage interne de FreeCAD, mais pourraient également être utilisés par d\'autres applications compatibles avec FreeCAD dans le futur. Ces attributs utilisent tous le préfixe **freecad:** [namespace](http://www.w3schools.com/xml/xml_namespaces.asp). L\'URL de l\'espace de nom défini dans ces documents SVG fait référence à cette page.

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/fr
