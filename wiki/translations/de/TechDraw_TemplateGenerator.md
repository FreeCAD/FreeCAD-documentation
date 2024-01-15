---
 TutorialInfo:e
   Topic: TechDraw-Vorlagen erzeugen mittels Python-Macro
   Level: Grundkenntnisse von Python und SVG-Strukturen sind hilfreich
   FCVersion:  0.21 und neuer
   Time: 
   Author: User:FBXL5
   SeeAlso: Macro_TemplateHelper/de
---

# TechDraw TemplateGenerator/de







## Einleitung

Diese Anleitung beschreibt, wie man eine einfache Vorlage zur Benutzung mit dem TechDraw-Arbeitsbereich aus ein paar Zeilen Python-Kode erstellt.

Jeder Texteditor kann zum Erstellen von Kode genutzt werden. Mein Favorit ist Atom, aber FreeCADs eingebauter Editor funktioniert auch bestens.

Die folgenden Kode-Beispiele können kopiert, in eine leere Textdatei eingefügt und dann unter einem selbstgewählten Namen als \*.py oder \*.FCMacro abgespeichert werden.

Eine Vorlage stellt einen Hintergrund für Zeichnungsaufgaben bereit und ihre Maße werden vom Druckertreiber für die korrekte Skalierung der Zeichnung verwendet.

Die Vorlagen sind SVG-Dateien, daher muss ein Makro einige Zeilen SVG-Kode (eine Untermenge von XML-Kode) zusammenstellen.

**Hinweis:** nachdem FreeCAD von **freecadweb.org** nach **freecad.org** umgezogen ist, wurde diese Seite entsprechend aktualisiert und der resultierende SVG-Code ist nicht mehr kompatibel mit FreeCAD-Versionen, die älter sind als v0.21. Für diese versionen muss {{Incode|freecad.org}} in der Deklarationszeile des resultierenden SVG-Codes von Hand auf {{Incode|freecadweb.org}} zurückgeändert werden, da die editierbaren Texte sonst nicht erkannt werden.



## Struktur einer einfachen leeren Seite 

Das SVG-Format ist eine Untermenge des XML-Formats. Daher besteht eine SVG-Datei, wie auch jede XML-Datei, aus zwei Teilen:

-   Einem Kopf mit eine Formatdeklaration
-   Einem Körper, der die Informationen darüber enthält, was anzuzeigen ist und wo es platziert wird

:   (Ich weiß nicht, warum die Kopfzeile enthalten sein soll; die SVG-Datei funktioniert auch ohne sie als Vorlagedatei)



### Kopf

Der Kopf besteht aus nur einer Zeile zur Angabe der Version der XML-Sprache, die verwendet werden soll, um die im Körper befindlichen Anweisungen zu verarbeiten.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
}}



### Körper

Der Körper startet mit einem öffnenden Tag, der Informationen über Namensräume, über die Größe der Vorlage und darüber, wo sie platziert wird enthält. Und er hört mit einem schließenden Tag auf.


{{Code|lang=xml|code=
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


:   **xmlns=**\"<http://www.w3.org/2000/svg>\": Externer Verweis auf den XML-Namensraum, um Standard-XML-Befehle nachzuschlagen.
:   **version=**\"1.1\": Die verwendete XML-Version ist 1.1
:   **xmlns:freecad=**\"\...=Svg_Namespace\": Externe Verknüpfung zu FreeCADs [Svg-Namensraum](Svg_Namespace/de.md)\"-Erweiterung, zum Nachschlagen spezieller Befehle, die nur innerhalb einer FreeCAD-Umgebung verwendet werden, wie z.B. editierbare Texte.
:   \"freecad:\" wird Attributnamen vorangestellt, damit sie durch die besagten speziellen Befehle verarbeitet werden.
:   **width=**\"420mm\": Breite der Zeichenfläche
:   **height=**\"297mm\": Höhe der Zeichenfläche
:   **viewBox=**\"0 0 420 297\": Position der oberen linken Ecke (0;0) und der unteren rechten Ecke (420;297) im SVG-Konstruktionsraum (in SVG-Einheiten).
:   Width, height, and viewBox, in dieser Kombination, setzen 1 SVG-Einheit gleich 1 mm, für das gesamte Dokument. Von jetzt an kann die Maßeinheit weggelassen werden.
:   In diesem Falle ergeben 420 und 297 eine A3-Seite. Diese Werte werden angepasst, um andere Seitenformate zu erzeugen.

Für eine leere DIN-A3-Seite im Querformat war das alles.


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



## Python-Kode\... 

Bevor überhaupt Kode erzeugt wird, benötigt man einen Ordner zum Speichern der neuen Vorlagen.

Der Benutzer sollte bereits einen Vorlagenordner ausgewählt haben. Sein Pfad ist dann in den TechDraw-Voreinstellungen gespeichert.  Es ist nicht nötig zu wissen, wo die Voreinstellungen gespeichert werden, da FreeCAD Befehle enthält, mit denen man die benötigten Parameter direkt ansprechen kann.


{{Code| |code=
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
template_file = os.path.join(template_path, template_name)
}}

**parameter_path** erhält den Pfad zum \"Verzeichnis\" innerhalb der Konfigurationsdatei, wo die Variable \"TemplateDir\" gefunden werden kann.  **template_path** erhält den Inhalt von \"TemplateDir\", also den Pfad zum Vorlagenverzeichnis.  **template_name** erhält den Namen der neu zu erstellenden Vorlage.

Nun muss der **template_name** noch so mit dem **template_path** verknüpft werden, dass das Ergebnis sowohl zu unix-basierten Betriebssystemen als auch zu Windows kompatibel ist.  Dies wird mit dem Befehl \"os.path.join\" erreicht und in der Variablen **template_file** gespeichert.



### \... zum Erstellen einer leeren Seite 


<div class="mw-collapsible mw-collapsed toccolours">

Dieses Makro zeigt das Prinzip, wie eine SVG-Datei zusammengestellt werden kann. (Format ist A3)


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
def CreateSvgFile(file_path):
    t=open(file_path, "w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
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


:   Das Hauptprinzip ist:
    -   eine Datei zum Schreiben zu öffnen und so als ersten Schritt eine leere SVG-Datei anzulegen, eine Kopfzeile zu schreiben und die Datei zu schließen
    -   und danach wiederholt die Datei zum Anhängen weiterer Segmente zu öffnen und nach erfolgtem Anhängen wieder zu schließen.
:   
:   Das Makro besteht aus mehreren Funktionen, die vom Hauptprogramm aufgerufen werden.
:   Zusätzliche Funktionen können vor der EndSvg-Funktion eingefügt werden und die dazugehörigen Aufrufe werden vor dem EndSvg()-Aufruf eingesetzt.
:   Man muss auf die Anzahl der Leerzeichen achten, die mit den Schreiboperationen erzeugt werden, und damit auf den korrekten Zeileneinzug.



### \... zum Erstellen einer Seite mit ein paar Strichen 

Um aus einer leeren Seite eine Zeichnung zu machen, braucht man:

  - Rahmen, d.h. Rechtecke, die mit der Anweisung **rect** erstellt werden

  - ein Schriftfeld und noch etwas mehr, das aus Linien besteht, die mit der Anweisung **path** erstellt werden

  - einfache Texte für Indizes und die Benennungen der Schriftfeldzellen

  - editierbare Texte für z.B. Sachnummer und Benennung

Diese graphischen Elemente werden normalerweise mehrfach benutzt, daher werden für die erzeugenden Kodes Funktionen erstellt.



### Funktion svgrect 

Um ein Rechteck zu zeichnen, muss die Funktion **svgrect** aufgerufen und die Werte für Breite, Höhe und die Position der linken oberen Ecke übergeben werden. Das ist besser zu lesen als der Kode, der mit **svgline** erzeugt wird, den man stattdessen verwenden würde.


{{Code| |code=
#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine
}}



### Funktion svgpath 

Um eine Linie zu zeichnen, muss die Funktion **svgpath** aufgerufen und die Koordinaten für Start- und Endpunkt einer Linie übergeben werden.

Anstatt der Endpunktkoordinaten kann ein Kennwert übergeben werden, um eine horizontale (h) oder vertikale (v) Linie zu zeichnen, gefolgt von der Länge der Linie, oder ein Kennwert, um eine Horizontale (H) oder vertikale (V) Linie zu zeichnen, gefolgt von der X- bzw. Y-Ordinate des Endpunktes.

Jeder Pfad beginnt am Ursprung und die erste Aktion ist eine Bewegung mit \"angehobenem Stift\" (nicht zeichnend) zum Startpunkt. In diesem Fall sind die relative und die absolute Bewegung identisch und daher ist es egal, ob der M-Tag ein großes oder ein kleines M enthält.


{{Code| |code=
#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine
}}



### Funktion svgtext 

Um etwas Text zu zeichnen, muss die Funktion **svgtext** aufgerufen und die Koordinaten für den Ankerpunkt des Textes sowie die Textzeichenkette selbst übergeben werden.

(Die Textausrichtung wird durch den umschließenden Gruppen-Tag gesteuert oder ist standardmäßig linksbündig)


{{Code| |code=
#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine
}}



### Funktion FCeditext 

Um einen editierbaren Text zu zeichnen, muss die Funktion **FCeditext** aufgerufen und die Koordinaten für den Ankerpunkt des Textes sowie die Textzeichenkette selbst übergeben werden.

FreeCAD erzeugt ein Dictionary-Objekt für jede hinzugefügte Vorlage, und jeder Eintrag hat einen Namen (key) und einen Wert (value).

(Die Textausrichtung wird durch den umschließenden Gruppen-Tag gesteuert oder ist standardmäßig linksbündig)


{{Code| |code=
#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine
}}



### Funktionen CreateXxxx 

Diese Funktionen beginnen mit Kode zum öffnen einer Datei im Anfüge-Modus (append mode) sowie zum schreiben des öffnenden Gruppen-Tags.

Dann folgt ein Abschnitt zum setzen und berechnen von Werten und mit Schreibanweisungen, die die obigen Funktionen zum erstellen von SVG-Kode aufrufen.

Und am Ende steht der schließende Gruppen-Tag, gefolgt von einer Anweisung zum Schließen der Datei.


{{Code| |code=
#- Frame creation
def CreateFrame(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
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



### Das resultierende Makro 


<div class="mw-collapsible mw-collapsed toccolours">

Dieses Makro fügt ein paar grundlegende graphische Elemente hinzu, die für richtige Vorlagen gebraucht werden, wie z.B. Linienelemente, Texte und editierbares Texte.


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
def CreateSvgFile(file_path):
    t=open(file_path, "w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
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
def CreateFrame(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
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
def CreateTitleBlock(file_path, shWidth, shHeight):

    #- lower left corner
    tbX=str(int(shWidth)-10-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-10)
    #- group to transform all elements at once
    t=open(file_path, "a", encoding="utf-8")
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
def CreateEditableText(file_path, shWidth, shHeight):

    #- offsets for editable texts
    edX=int(shWidth)-10-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-10

    t=open(file_path, "a", encoding="utf-8")
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

Und das ist der SVG-Kode aus diesem Makro:


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

Und so soll es aussehen, wenn sie (die Vorlage) eingefügt wurde (mit vergrößertem Schriftfeld):

<img alt="" src=images/TechDraw_TemplateGenerator.png  style="width:600px;">



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator/de
