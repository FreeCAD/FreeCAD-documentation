---
 TutorialInfo:r
   Topic: Créer un modèle TechDraw à l'aide d'une macro Python
   Level: Des connaissances de base en Python et de structures SVG sont utiles.
   FCVersion: 0.21 et plus
   Time: 
   Author: User:FBXL5
   SeeAlso: Macro_TemplateHelper/fr
---

# TechDraw TemplateGenerator/fr





## Introduction

Ce tutoriel décrit comment générer un modèle simple à utiliser avec l\'atelier TechDraw à partir de quelques lignes de code Python.

N\'importe quel éditeur de texte peut être utilisé pour coder. Mon choix se porte sur Atom, mais l\'éditeur intégré de FreeCAD fonctionne bien aussi.

Les exemples de code suivants peuvent être copiés et collés dans un fichier texte vide, puis enregistrés sous le nom de votre choix en tant que fichier \*.py ou \*.FCMacro.

Un modèle fournit un arrière-plan pour les tâches de dessin et ses dimensions sont utilisées par les pilotes d\'imprimante pour mettre le dessin à l\'échelle correctement.

Les modèles sont des fichiers svg et une macro doit donc composer quelques lignes de code svg (qui est un sous-ensemble du code xml).

**Remarque :** lorsque FreeCAD a été migré de **freecadweb.org** à **freecad.org**, cette page a été mise à jour en conséquence et le code SVG résultant n\'est plus compatible avec les versions de FreeCAD antérieures à la v0.21. Pour ces versions, vous devez changer manuellement {{Incode|freecad.org}} en {{Incode|freecadweb.org}} à la ligne de déclaration de l\'espace des noms dans le code SVG résultant, sinon les textes éditables ne sont pas reconnus.



## Structure d\'une simple page blanche 

Le format SVG est un sous-ensemble du format XML. C\'est pourquoi un fichier SVG, comme tout fichier XML, se compose de deux parties :

-   En-tête, une déclaration de format
-   Corps, contient les informations à afficher et où les placer.

:   (je ne sais pas pourquoi il devrait y avoir un titre, le fichier svg est toujours un fichier modèle valide sans lui\...)



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
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


:   **xmlns=** \"<http://www.w3.org/2000/svg>\" : lien externe vers l\'espace de noms xml pour rechercher les commandes xml standard
:   **version=** \"1.1\" : la version de xml utilisée est 1.1
:   **xmlns:freecad=**\"\...=Svg_Namespace\" : lien externe vers la page wiki [Svg Namespace](Svg_Namespace/fr.md) de FreeCAD. Le lien n\'est pas utilisé pour récupérer des informations ou des valeurs au moment de l\'exécution, mais c\'est la clé pour activer les attributs personnalisés, par exemple ceux pour les textes éditables.
:   \"freecad :\" sera préfixé à ces noms d\'attributs personnalisés.
:   **width=** \"420mm\" : largeur de la zone de dessin
:   **height=** \"297mm\" : hauteur de la zone de dessin
:   **viewBox=** \"0 0 420 297\" : position du coin supérieur gauche (0;0) et du coin inférieur droit (420;297) dans l\'espace de construction svg (en unités svg).
:   Width, height et viewBox dans cette combinaison définissent 1 unité svg à 1 mm pour l\'ensemble du document. Une unité dimensionnelle peut être omise à partir de maintenant.
:   Dans ce cas, 420 et 297 donnent une page A3. Personnalisez ces valeurs pour générer d\'autres tailles de page.

Pour une page blanche de taille DIN A3 en orientation paysage, c\'est tout.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}



## Code Python\... 

Le codage commence par un cadre contenant une fonction principale distincte :


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2024 Your name LGPL


def main():
    """Here is where the magic happens"""
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}



### \...pour créer une page blanche 

Le processus de création d\'un modèle consiste à :

-   Localiser le dossier du modèle.
-   Ouvrir un fichier en écriture pour créer un fichier svg à partir de zéro, écrire la ligne d\'en-tête et fermer le fichier dans un premier temps.
-   Et ensuite, ouvrir le fichier à plusieurs reprises pour ajouter d\'autres segments, en le refermant à chaque fois.

La macro est composée de plusieurs fonctions qui sont appelées à partir de la section principale.
Des fonctions supplémentaires peuvent être insérées avant la fonction EndSvg et les appels nécessaires sont placés avant l\'appel à EndSvg().
Nous devons surveiller le nombre d\'espaces utilisés avec les opérations d\'écriture pour une indentation correcte.

#### pathToTemplate()

Avant que le code ne soit généré, un dossier est nécessaire pour stocker le nouveau fichier modèle, et un nom de fichier doit être défini.

L\'utilisateur doit avoir sélectionné un dossier de modèle. Son chemin est alors enregistré dans les préférences de TechDraw.  Il n\'est pas nécessaire de savoir où sont stockées les préférences, car FreeCAD dispose de commandes permettant d\'adresser directement les paramètres nécessaires.


{{Code| |code=
def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file
}}

**parameter_path** reçoit le chemin vers le \"dossier\" dans le fichier de configuration où se trouve le paramètre \"TemplateDir\".  **template_path** reçoit le contenu de \"TemplateDir\" qui est le chemin vers le répertoire du modèle.
**template_name** reçoit le nom du modèle à créer.

Maintenant, le nom du modèle doit être associé au chemin du modèle d\'une manière qui soit compatible avec les systèmes d\'exploitation basés sur unix et Windows. Ceci est fait avec la commande \"os.path.join\" et stocké dans le **template_file**. Pour activer cette commande, une instruction \"import os\" est nécessaire.

#### createSvgFile()

Cette opération crée un nouveau fichier modèle et enregistre la ligne d\'en-tête xml.


{{Code| |code=
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close
}}

#### startSvg()

Cette instruction ajoute le fichier modèle et crée la balise d\'ouverture svg, y compris ses attributs.
Chaque instruction d\'écriture contient une seule ligne de code svg se terminant par \"\\n\", le marqueur pour CR/LF.


{{Code| |code=
def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close
}}

#### endSvg()

Cette instruction ajoute ensuite le fichier modèle et crée la balise de fermeture svg, ce qui termine le code du modèle.


{{Code| |code=
def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close
}}

#### main()

La fonction main() appelle les fonctions et transmet certains paramètres.


{{Code| |code=
def main():
    """This one creates an empty A3 template"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return
}}

Dans cet exemple, {{Incode|format_width}} et {{Incode|format_height}} sont des dimensions codées en dur, les deux lignes inutiles marquent les points où d\'autres moyens de récupération des données de format pourraient placer leur contenu.


<div class="mw-collapsible mw-collapsed toccolours">

#### La macro complète de la page blanche 

Cette macro se compose de segments de code comme ci-dessus, prêts à être exécutés.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2024 Your name LGPL

import os  # to enable the use of os.path.join()


# - SVG creation -
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close

def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file

def main():
    """This one creates an empty A3 template"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>



### \...pour créer une page avec de l\'encre 

Pour faire un dessin à partir d\'une page blanche, nous avons besoin de :

  - de cadres, c\'est-à-dire des rectangles créés avec l\'instruction **rect**.

  - d\'un cartouche et de lignes créées avec l\'instruction **path**.

  - de textes simples pour les index et l\'étiquetage des cellules du bloc titre

  - de textes modifiables comme le numéro ou le nom de la pièce.

Normalement, ces éléments graphiques sont utilisés de manière répétée et le code de génération est donc divisé en quatre fonctions :

-   svgRect() pour les éléments de cadre rectangulaire.
-   svgPath() pour les éléments de ligne droite.
-   svgText() pour les textes statiques.
-   ediText() pour les textes modifiables.

Toutes les fonctions sont placées à l\'intérieur de la macro ci-dessus avant la fonction main() et leurs appels de fonction sont insérés dans la fonction main() entre {{Incode|startSvg(...)}} et {{Incode|endSvg(...)}}.

#### svgRect()

Pour dessiner un rectangle, il suffit d\'appeler la fonction **svgRect** et de lui transmettre les valeurs de largeur, de hauteur et de position du coin supérieur gauche. C\'est plus lisible à cet endroit que si svg_line contenait toute la ligne de code svg.


{{Code| |code=
def svgRect(width, height, x, y):
    # Generates an svg-instruction to draw a rectangle with the given values
    svg_line = (
        "<rect width=\"" + width + "\" height=\"" + height + "\" x=\"" + x
        + "\" y=\"" + y + "\" />"
        )
    return svg_line
}}

L\'instruction svg est divisée pour rester dans la longueur des lignes recommandée par Python, il en résultera néanmoins une seule ligne svg.

#### svgPath()

Pour dessiner une ligne, il suffit d\'appeler la fonction **svgPath** et de fournir les coordonnées du point de départ et du point d\'arrivée d\'une ligne.

Au lieu des coordonnées du point final, nous pouvons remettre une étiquette pour dessiner une ligne horizontale (h) ou verticale (v) suivie de la longueur de la ligne ou l\'étiquette pour dessiner une ligne horizontale (H) ou verticale (V) suivie de l\'ordonnée x ou y du point final.

Chaque chemin commence à l\'origine et la première action est un mouvement avec le \"stylo levé\" (pas de dessin) vers le point de départ. Dans ce cas, le mouvement relatif et le mouvement absolu sont identiques et il n\'est donc pas important que l\'étiquette m (m-tag? ndlt) soit en majuscule ou en minuscule.


{{Code| |code=
def svgPath(x1, y1, x2, y2):
    # Generates an svg-instruction to draw a path element (line) with the given values
    if x2 == "v" or x2 == "V" or x2 == "h" or x2 == "H":
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " " + x2 + " " + y2 + "\" />")
    else:
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " l " + x2 + "," + y2 + "\" />")
    return svg_line
}}

#### svgText()

Pour dessiner un morceau de texte, il suffit d\'appeler la fonction **svgText** et de lui fournir les coordonnées du point d\'ancrage du texte, la chaîne de texte elle-même et, éventuellement, un angle pour le texte pivoté. Pour faire pivoter un texte, une instruction de transformation doit être insérée dans chaque balise de texte séparément ; les centres de rotation sont fixés aux mêmes coordonnées que les points d\'ancrage du texte.

(L\'alignement du texte est contrôlé par la balise de groupe qui l\'entoure ou aligné à gauche par défaut).


{{Code| |code=
def svgText(x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place a text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated texts
    """
    if str_angle == "0":
        svg_line = ("<text x=\"" + x + "\" y=\"" + y + "\">" + str_value + "</text>")
    else:
        svg_line = (
            "<text x=\"" + x + "\" y=\"" + y + "\" transform=\"rotate(" + str_angle
            + "," + x + "," + y + ")\">" + str_value + "</text>"
            )
    return svg_line
}}

#### ediText()

Pour dessiner un morceau de texte éditable, il suffit d\'appeler la fonction **ediText** et de lui fournir un nom, les coordonnées du point d\'ancrage du texte, la chaîne de texte elle-même, et éventuellement un angle pour le texte pivoté. Pour faire pivoter un texte, une instruction de transformation doit être insérée dans chaque balise de texte séparément ; les centres de rotation sont fixés aux mêmes coordonnées que les points d\'ancrage du texte.

FreeCAD crée un objet dictionnaire avec chaque modèle inséré et chaque entrée possède un nom (clé) et une valeur.

(L\'alignement du texte est contrôlé par la balise de groupe qui l\'entoure ou aligné à gauche par défaut).


{{Code| |code=
def ediText(entry_name, x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place an editable text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated editable texts
    """
    if str_angle == "0":
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\">  <tspan>" + str_value + "</tspan>  </text>"
            )
    else:
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\" transform=\"rotate(" + str_angle + "," + x + "," + y + ")\">  <tspan>"
            + str_value + "</tspan>  </text>"
            )
    return svg_line
}}



### Fonctions createXxxx 

Ces fonctions commencent par du code pour ouvrir un fichier en mode append et pour écrire la balise d\'ouverture de groupe.

Suit une section permettant de définir et de calculer des valeurs, ainsi que des instructions d\'écriture appelant les fonctions susmentionnées afin de générer du code svg.

Et enfin la balise de fermeture de groupe suivie d\'une instruction pour fermer le fichier.


{{Code| |code=
def createFrame(file_path, sheet_width, sheet_height):
    # Creates rectangles for sheet frame and drawing area
    t = open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round\">\n")
    #- upper left corner of inner Frame, drawing area
    frame_x = str(20)
    frame_y = str(10)
    #- frame dimensions
    frame_width = str(int(sheet_width) - 20 - 10)
    frame_height = str(int(sheet_height) - 10 - 10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    #- upper left corner outer frame, sheet frame
    frame_x = str(15)
    frame_y = str(5)
    #- frame dimensions
    frame_width = str(int(sheet_width)-20)
    frame_height = str(int(sheet_height)-10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
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
# (c) 2024 Your name LGPL

import os  # to enable the use of os.path.join()


# - SVG creation -
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close

def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

def svgRect(width, height, x, y):
    # Ggenerates an svg-instruction to draw a rectangle with the given values
    svg_line = (
        "<rect width=\"" + width + "\" height=\"" + height + "\" x=\"" + x
        + "\" y=\"" + y + "\" />"
        )
    return svg_line

def svgPath(x1, y1, x2, y2):
    # Generates an svg-instruction to draw a path element (line) with the given values
    if x2 == "v" or x2 == "V" or x2 == "h" or x2 == "H":
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " " + x2 + " " + y2 + "\" />")
    else:
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " l " + x2 + "," + y2 + "\" />")
    return svg_line

def svgText(x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place a text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated texts
    """
    if str_angle == "0":
        svg_line = ("<text x=\"" + x + "\" y=\"" + y + "\">" + str_value + "</text>")
    else:
        svg_line = (
            "<text x=\"" + x + "\" y=\"" + y + "\" transform=\"rotate(" + str_angle
            + "," + x + "," + y + ")\">" + str_value + "</text>"
            )
    return svg_line

def ediText(entry_name, x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place an editable text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated editable texts
    """
    if str_angle == "0":
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\">  <tspan>" + str_value + "</tspan>  </text>"
            )
    else:
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\" transform=\"rotate(" + str_angle + "," + x + "," + y + ")\">  <tspan>"
            + str_value + "</tspan>  </text>"
            )
    return svg_line

def createFrame(file_path, sheet_width, sheet_height):
    # Creates rectangles for sheet frame and drawing area
    t = open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round\">\n")
    #- calculate upper left corner of inner Frame, drawing area
    frame_x = str(20)
    frame_y = str(10)
    #- frame dimensions
    frame_width = str(int(sheet_width) - 20 - 10)
    frame_height = str(int(sheet_height) - 10 - 10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    #- calculate upper left corner outer frame, sheet frame
    frame_x = str(15)
    frame_y = str(5)
    #- frame dimensions
    frame_width = str(int(sheet_width)-20)
    frame_height = str(int(sheet_height)-10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    t.write("    </g>\n\n")
    t.close

def createTitleBlock(file_path, sheet_width, sheet_height):
    """Creates a title block and transfers it to the position according to the sheet dimensions"""
    #- calculate title block origin (lower left corner), offset from page origin
    tbX = str(int(sheet_width) - 10 - 180)  # 180 according to DIN EN ISO 7200
    tbY = str(int(sheet_height) - 10)
    t = open(file_path, "a", encoding="utf-8")
    #- group to transfer all included title block elements at once
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate(" + tbX + "," + tbY + ")\">\n")
    #- sub-group of title block line framework
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        " + svgPath("  0","  0","  0","-63") + "\n")
    t.write("        " + svgPath("  0","-63","180","  0") + "\n")
    t.write("        " + svgPath("  0","-30","h","155") + "\n")
    t.write("        " + svgPath("155","  0","v","-63") + "\n")
    t.write("      </g>\n")
    #- sub-group of title block static texts (left-aligned by default)
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        " + svgText("  4.5","-43.5 ","Some static text") + "\n")
    t.write("        " + svgText("  4.5","-13.5 ","More static text") + "\n")
    t.write("        " + svgText("162.5","-3.5 ","Vertical static text","-90") + "\n")
    t.write("      </g>\n")
    t.write("    </g>\n\n")
    t.close

def createEditableText(file_path, sheet_width, sheet_height):
    """Creates editable texts positioned according to the page origin"""
    #- calculate offset to titleblock origin
    edX = int(sheet_width) - 10 - 180 # 180 according to DIN EN ISO 7200
    edY = int(sheet_height) - 10
    t = open(file_path, "a", encoding="utf-8")
    #- group editable texts using the same attributes
    t.write("    <g id=\"titleblock-editable-texts\"\n")
    t.write("      style=\"font-size:7.0;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write(
        "      " + ediText("EdiText-1",str(edX + 60),str(edY - 43.5),"Some editable text") + "\n"
        )
    t.write(
        "      " + ediText("EdiText-2",str(edX + 60),str(edY - 13.5),"More editable text") + "\n"
        )
    t.write(
        "      " + ediText("EdiText-3",str(edX + 173),str(edY - 4.5),"90° editable text","-90")
        + "\n"
        )
    t.write("    </g>\n\n")
    t.close

def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file

def main():
    """This one creates an A3 template with simple frame and title block"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    createFrame(template_file, format_width, format_height)
    createTitleBlock(template_file, format_width, format_height)
    createEditableText(template_file, format_width, format_height)
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}

Et voici le code svg qui sort de cette macro :


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
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
        <text x="162.5" y="-3.5 " transform="rotate(-90,162.5,-3.5 )">Vertical static text</text>
      </g>
    </g>

    <g id="titleblock-editable-texts"
      style="font-size:7.0;text-anchor:start;fill:#0000d0;font-family:osifont">
      <text freecad:editable="EdiText-1" x="290" y="243.5">  <tspan>Some editable text</tspan>  </text>
      <text freecad:editable="EdiText-2" x="290" y="273.5">  <tspan>More editable text</tspan>  </text>
      <text freecad:editable="EdiText-3" x="403" y="282.5" transform="rotate(-90,403,282.5)">  <tspan>90° editable text</tspan>  </text>
    </g>

</svg>
}}


</div>


</div>

Et ce à quoi il devrait ressembler une fois inséré (avec un bloc titre agrandi) :

<img alt="" src=images/TechDraw_TemplateGenerator.png  style="width:600px;">

La coloration en bleu des textes modifiables est un choix personnel qui permet de distinguer plus facilement les textes statiques des textes modifiables sur le dessin fini.



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator/fr
