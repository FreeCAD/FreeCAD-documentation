---
- TutorialInfo:/fr
   Topic:Création de modèles avec une macro Python
   Level:Des connaissances de base de Python et de svg-structures sont utiles.
   FCVersion:0.19.1 et plus
   Time:(ne sait pas)
   Author:[FBXL5](User_FBXL5.md)
---

# TechDraw TemplateGenerator/fr





## Introduction

Ce tutoriel décrit comment générer un modèle simple à utiliser avec l\'atelier TechDraw à partir de quelques lignes de code Python.

N\'importe quel éditeur de texte peut être utilisé pour coder. Mon choix se porte sur Atom, mais l\'éditeur intégré de FreeCAD fonctionne bien aussi.

Les exemples de code suivants peuvent être copiés et collés dans un fichier texte vide, puis enregistrés sous le nom de votre choix en tant que fichier \*.py ou \*.FCMacro.

Un modèle fournit un arrière-plan pour les tâches de dessin et ses dimensions sont utilisées par les pilotes d\'imprimante pour mettre le dessin à l\'échelle correctement.

Les modèles sont des fichiers svg et une macro doit donc composer quelques lignes de code svg (qui est un sous-ensemble du code xml).

## Structure d\'une simple page blanche 

Le format SVG est un sous-ensemble du format XML. C\'est pourquoi un fichier SVG, comme tout fichier XML, se compose de deux parties :

-   L\'en-tête, une déclaration de format
-   Le corps, qui contient les informations à afficher et où les placer.

le titre : (je ne sais pas pourquoi il devrait y avoir un titre, le fichier svg est toujours un fichier modèle valide sans lui\...)

### L\'en-tête 

L\'en-tête n\'est qu\'une ligne pour déclarer quelle version du langage XML un interpréteur doit utiliser pour traiter les instructions du corps.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
}}

### Le corps 

Le corps commence par une balise d\'ouverture qui contient des informations sur les espaces de nom et sur la taille du modèle et l\'endroit où le placer. Et il se termine par une balise de fermeture.


{{Code|lang=xml|code=
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


:   **xmlns=** \"<http://www.w3.org/2000/svg>\" : Lien externe vers l\'espace de noms xml pour rechercher les commandes xml standard
:   **version=** \"1.1\" : La version de xml utilisée est 1.1
:   **xmlns:freecad=** \"[Svg Namespace](https://wiki.freecadweb.org/Svg_Namespace/fr)\" : Lien externe vers l\'extension de l\'espace de nom de FreeCAD
:   \"freecad :\" sera préfixé aux noms d\'attributs pour qu\'ils soient traités par lesdites commandes spéciales.
:   **width=** \"420mm\" : Largeur de la zone de dessin
:   **height=** \"297mm\" : Hauteur de la zone de dessin
:   **viewBox=** \"0 0 420 297\" : Position du coin supérieur gauche (0;0) et du coin inférieur droit (420;297) dans l\'espace de construction svg (en unités svg).
:   Width, height et viewBox dans cette combinaison définissent 1 unité svg à 1 mm pour l\'ensemble du document. Une unité dimensionnelle peut être omise à partir de maintenant.
:   Dans ce cas, 420 et 297 donnent une page A3. Personnalisez ces valeurs pour générer d\'autres tailles de page.

Pour une page blanche de taille DIN A3 en orientation paysage, c\'est tout.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}

## Code Python\... 

Avant que le code ne soit généré, un dossier est nécessaire pour stocker le nouveau fichier modèle.

L\'utilisateur doit avoir sélectionné un dossier de modèle. Son chemin est alors enregistré dans les préférences de TechDraw.  Il n\'est pas nécessaire de savoir où sont stockées les préférences, car FreeCAD dispose de commandes permettant d\'adresser directement les paramètres nécessaires.


{{Code| |code=
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
template_file = os.path.join(template_path, template_name)
}}

**parameter_path** reçoit le chemin vers le \"dossier\" dans le fichier de configuration où se trouve le paramètre \"TemplateDir\".  **template_path** reçoit le contenu de \"TemplateDir\" qui est le chemin vers le répertoire du modèle.  **template_name** reçoit le nom du modèle à créer.

Maintenant, le nom du modèle doit être associé au chemin du modèle d\'une manière qui soit compatible avec les systèmes d\'exploitation basés sur unix et Windows. Ceci est fait avec la commande \"os.path.join\" et stocké dans le **template_file**.

### \... pour créer une page blanche 


<div class="mw-collapsible mw-collapsed toccolours">

Cette macro montre le principe d\'assemblage d\'un fichier svg. (Le format est A3)


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- Get the path to the template folder that is set in the FreeCAD parameters
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
#- Link template_path and template_name for any OS
template_file = os.path.join(template_path, template_name)

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(filePath):
    t=open(filePath,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(filePath):
    t=open(filePath,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(filePath):
    t=open(filePath,"a")
    t.write("</svg>")
    t.close

# --- Main section ---

CreateSvgFile(template_file) # overwrites existing File

# Set sheet format (DIN A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(template_file)  # adds Start tag and namespaces
CreateSheet(template_file, formatWidth, formatHeight)
EndSvg(template_file)
# At this point a new SVG-file is generated and saved
}}


</div>


</div>


:   Le principe essentiel est :
    -   d\'ouvrir un fichier en écriture et donc de démarrer un fichier svg à partir de zéro, d\'écrire la ligne d\'en-tête et de fermer le fichier dans un premier temps.
    -   puis d\'ouvrir à plusieurs reprises le fichier pour ajouter d\'autres segments et de le refermer après l\'ajout.
:   
:   La macro est composée de plusieurs fonctions qui sont appelées depuis la section principale.
:   Des fonctions supplémentaires peuvent être insérées avant la fonction EndSvg et les appels nécessaires sont placés avant l\'appel EndSvg().
:   Nous devons surveiller le nombre d\'espaces utilisés lors des opérations d\'écriture pour une indentation correcte.

### \... pour créer une page avec de l\'encre 

Pour faire un dessin à partir d\'une page blanche, nous avons besoin de :

  - de cadres, c\'est-à-dire des rectangles créés avec l\'instruction **rect**.

  - d\'un cartouche et de lignes créées avec l\'instruction **path**.

  - de textes simples pour les index et l\'étiquetage des cellules du bloc titre

  - de textes modifiables comme le numéro ou le nom de la pièce.

Normalement, ces éléments graphiques sont utilisés de manière répétée et le code de génération est donc placé dans des fonctions.

### Fonction svgrect 

Pour dessiner un rectangle, il suffit d\'appeler la fonction **svgrect** et de lui transmettre les valeurs de largeur, de hauteur et de position du coin supérieur gauche. C\'est plus lisible que le contenu de la svgline qui devait être utilisé à la place.


{{Code| |code=
#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine
}}

### Fonction svgpath 

Pour dessiner une ligne, il suffit d\'appeler la fonction **svgpath** et de fournir les coordonnées du point de départ et du point d\'arrivée d\'une ligne.

Au lieu des coordonnées du point final, nous pouvons remettre une étiquette pour dessiner une ligne horizontale (h) ou verticale (v) suivie de la longueur de la ligne ou l\'étiquette pour dessiner une ligne horizontale (H) ou verticale (V) suivie de l\'ordonnée x ou y du point final.

Chaque chemin commence à l\'origine et la première action est un mouvement avec le \"stylo levé\" (pas de dessin) vers le point de départ. Dans ce cas, le mouvement relatif et le mouvement absolu sont identiques et il n\'est donc pas important que l\'étiquette m (m-tag? ndlt) soit en majuscule ou en minuscule.


{{Code| |code=
#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine
}}

### Fonction svgtext 

Pour dessiner un morceau de texte, il suffit d\'appeler la fonction **svgtext** et de fournir les coordonnées du point d\'ancrage du texte et la chaîne de texte elle-même.

(L\'alignement du texte est contrôlé par la balise de groupe qui l\'entoure ou aligné à gauche par défaut).


{{Code| |code=
#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine
}}

### Fonction FCeditext 

Pour dessiner un morceau de texte modifiable, il suffit d\'appeler la fonction **FCeditext** et de lui donner un nom, les coordonnées du point d\'ancrage du texte et la chaîne de texte elle-même.

FreeCAD crée un objet dictionnaire avec chaque modèle inséré et chaque entrée possède un nom (clé) et une valeur.

(L\'alignement du texte est contrôlé par la balise de groupe qui l\'entoure ou aligné à gauche par défaut).


{{Code| |code=
#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine
}}

### Fonctions CreateXxxx 

Ces fonctions commencent par du code pour ouvrir un fichier en mode append et pour écrire la balise d\'ouverture de groupe.

Suit une section pour définir et calculer les valeurs et des instructions d\'écriture qui appellent les fonctions ci-dessus pour générer le code svg.

Et enfin la balise de fermeture de groupe suivie d\'une instruction pour fermer le fichier.


{{Code| |code=
#- Frame creation
def CreateFrame(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(20)
    drawingY=str(10)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20-10)
    drawingHeight=str(int(shHeight)-10-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(15)
    drawingY=str(5)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20)
    drawingHeight=str(int(shHeight)-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close
}}

### Macro résultante 


<div class="mw-collapsible mw-collapsed toccolours">

Cette macro ajoute certains éléments graphiques de base nécessaires à l\'élaboration de modèles appropriés, à savoir des éléments de ligne, des textes et des textes modifiables.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- Get the path to the template folder that is set in the FreeCAD parameters
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
#- Link template_path and template_name for any OS
template_file = os.path.join(template_path, template_name)

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(filePath):
    t=open(filePath,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(filePath):
    t=open(filePath,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(filePath):
    t=open(filePath,"a")
    t.write("</svg>")
    t.close

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine

#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine

#- Frame creation
def CreateFrame(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(20)
    drawingY=str(10)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20-10)
    drawingHeight=str(int(shHeight)-10-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(15)
    drawingY=str(5)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20)
    drawingHeight=str(int(shHeight)-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Title block movable
def CreateTitleBlock(filePath,shWidth,shHeight):

    #- lower left corner
    tbX=str(int(shWidth)-10-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-10)
    #- group to transform all elements at once
    t=open(filePath,"a")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("  4.5","-43.5 ","Some static text")+"\n")
    t.write("        "+svgtext("  4.5","-13.5 ","More static text")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def CreateEditableText(filePath,shWidth,shHeight):

    #- offsets for editable texts
    edX=int(shWidth)-10-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-10

    t=open(filePath,"a")
    t.write("    <g id=\"titleblock-editable-texts\"\n")
    t.write("      style=\"font-size:7.0;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("EdiText-1",str(edX+60),str(edY-43.5),"Some editable text")+"\n")
    t.write("      "+FCeditext("EdiText-2",str(edX+60),str(edY-13.5),"More editable text")+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateSvgFile(template_file) # overwrites existing File

# Set sheet format (A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(template_file)  # adds Start tag and namespaces
CreateSheet(template_file, formatWidth, formatHeight)
CreateFrame(template_file, formatWidth, formatHeight)
CreateTitleBlock(template_file, formatWidth, formatHeight)
CreateEditableText(template_file, formatWidth, formatHeight)
EndSvg(template_file)
# At this point a new SVG-file is generated and saved
}}

Et voici le code svg qui sort de cette macro :


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width ="420mm"
  height="297mm"
  viewBox="0 0 420 297">
    <g id="drawing-frame"
      style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round">
      <rect width="390" height="277" x="20" y="10" />
      <rect width="400" height="287" x="15" y="5" />
    </g>

    <g id="titleblock"
      transform="translate(230,287)">
      <g id="titleblock-frame"
        style="fill:none;stroke:#000000;stroke-width:0.35;stroke-linecap:miter;stroke-miterlimit:4">
        <path d="m   0,  0 l   0,-63" />
        <path d="m   0,-63 l 180,  0" />
        <path d="m   0,-30 h 155" />
        <path d="m 155,  0 v -63" />
      </g>
      <g id="titleblock-text-non-editable"
        style="font-size:5.0;text-anchor:start;fill:#000000;font-family:osifont">
        <text x="  4.5" y="-43.5 ">Some static text</text>
        <text x="  4.5" y="-13.5 ">More static text</text>
      </g>
    </g>

    <g id="titleblock-editable-texts"
      style="font-size:7.0;text-anchor:start;fill:#0000d0;font-family:osifont">
      <text freecad:editable="EdiText-1" x="290" y="243.5">  <tspan>Some editable text</tspan>  </text>
      <text freecad:editable="EdiText-2" x="290" y="273.5">  <tspan>More editable text</tspan>  </text>
    </g>

</svg>
}}


</div>


</div>

Et ce à quoi il devrait ressembler une fois inséré (avec un bloc titre agrandi) :

![TechDraw TemplateGenerator.png](images/TechDraw_TemplateGenerator.png )



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator/fr
