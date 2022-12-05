# Embedding FreeCAD/de
{{TOCright}}

## Einführung

FreeCAD kann als ein [Python](Python/de.md)-Modul in anderen Programmen oder einer eigenständigen Python-Konsole importiert werden, zusammen mit all seinen Modulen und Komponenten. Es ist sogar möglich, die FreeCAD-GUI als ein Python-Modul zu importieren, allerdings mit [einigen Einschränkungen](Embedding_FreeCAD/de#Caveats.md).

## FreeCAD benutzen ohne GUI 

Die erste, direkte, einfache und nützliche Anwendung die für Sie daraus entsteht, ist, FreeCAD-Dokumente in Ihre Programme zu importieren. Im folgenden Beispiel werden wir die Part-Geometrie eines FreeCAD-Dokuments in [Blender](http://www.blender.org) importieren. Hier ist das komplette Skript. Ich hoffe, Sie werden durch seine Einfachheit beeindruckt sein: {{Code|lang=python|code=
<nowiki>
FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.pyd file,
# for Windows you must either use \\ or / in the path, using a single \ is problematic
# FREECADPATH = 'C:\\FreeCAD\\bin'
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

Der erste und wichtigste Teil ist sicherzustellen, das Python unsere FreeCAD-Bibliothek finden wird. Nachdem Python sie findet, werden alle FreeCAD-Module wie Part (das wir auch nutzen werden) automatisch zur Verfügung stehen. Also nehmen wir einfach die {{Incode|sys.path}}-Variable, wo Python nach Modulen suchen wird, und wir ergänzen sie um den FreeCAD-library-Pfad. Diese Änderung ist nur temporär und geht verloren, wenn wir unseren Python-Interpreter schließen. Ein alternativer Weg wäre, einen Link zu Ihrer FreeCAD-Bibliothek in einem der Python-Suchpfade anzulegen. Ich speicherte den Pfad in einer Konstanten {{Incode|FREECADPATH}}, so dass es für einen anderen Benutzer des Skripts dann einfacher ist, dieses für sein eigenes System zu konfigurieren.


</div>


{{Code|lang=python|code=
FREECADPATH = 'C:\\FreeCAD\\bin' # path to your FreeCAD.so or FreeCAD.pyd file
import sys
sys.path.append(FREECADPATH)
}}

Sobald wir sicher sind, dass die Bibliothek geladen wird (siehe `try`/`except` Sequenz), können wir jetzt auf die gleiche Weise mit FreeCAD arbeiten, wie wir es Innerhalb des FreeCAD eigenen Python-Interpreters tun würden. Wir öffnen das FreeCAD-Dokument, das uns von der `main()`-Funktion übergeben wird, und wir erstellen eine Liste der Objekte. Da wir uns nur um die Part-Geometrie kümmern wollten, überprüfen wir, ob jedes Objekt die Type-Eigenschaft \"`Part`\" enthält, dann werden wir es tessellieren.


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

Die Tesselation erzeugt eine Liste der Knoten und eine Liste der Flächen, die durch Ecken Indizes definiert wird. Dies ist Ideal, da es genau auf die gleiche Weise wie Blender Netze definiert. Somit wird unsere Aufgabe lächerlich einfach, wir übergeben einfach beide Listeninhalte an die Punkte und Flächen von einem Blender-Netz. Wenn alles fertig ist, lassen wir den Bildschirm neu zeichnen(aufbauen), und das ist alles!


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}

Natürlich ist es ein sehr einfaches Skript(tatsächlich habe ich eine erweiterte Version [FreeCAD nach Blender-Import](https://yorik.orgfree.com/scripts/import_freecad.py)), die Sie vielleicht erweitern möchten, z. B. auch zum importieren von Mesh-Objekten, oder importieren von Part-Geometrie ohne Flächen, oder Import anderer Dateiformate, die FreeCAD lesen kann. Vielleicht wollen Sie auch Geometrien ein FreeCAD-Dokument exportieren, was auf die gleiche Weise durchgeführt werden kann. Vielleicht wollen Sie auch einen Dialog aufbauen, womit der Benutzer wählen kann, was zu importieren ist, etc\... Die Schönheit in alle dem liegt in der Tatsache, dass Sie FreeCAD die gesaamte Grundarbeit überlassen, während der Präsentation des Ergebnisses in dem Programm Ihrer Wahl geschiet.


**Hinweis:**

Probiere [Headless FreeCAD](Headless_FreeCAD/de.md), um FreeCAD ohne GUI zu betreiben.

## FreeCAD nutzen mit GUI 

Ab der Version 4.2 hat Qt die faszinierende Fähigkeit, Qt-GUI-abhängige-plugins in nicht-Qt-Host-Anwendungen einzubetten und sich an der Ereignis-Schleife des Gastgebers zu beteiligen.

Insbesondere für FreeCAD bedeutet dies, dass es aus einer anderen Anwendung mit seiner ganzen Oberfläche importiert werden kann, wobei die Host-Anwendung die volle Kontrolle über FreeCAD behält.

Der ganze Python-Code dies zu erreichen, besteht nur aus zwei Zeilen


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Wenn die Host-Anwendung auf Qt basiert, dann sollte diese Lösung auf allen Plattformen, die Qt unterstützt arbeiten. Allerdings sollte der Host die gleiche Qt-Version wie FreeCAD nutzen, weil man sonst unerwartete Laufzeitfehler erhalten könnte.

Für Nicht-Qt-Anwendungen aber, gibt es ein paar Einschränkungen, die Sie beachten müssen. Diese Lösung wird wahrscheinlich nicht mit allen anderen Toolkits funktionieren. Für Windows funktioniert es, solange die Host-Anwendung direkt aufbaut auf Win32 oder andere Toolkits, die intern die Win32-API verwenden, wie z.B. wxWidgets, MFC oder WinForms. Damit es unter X11 arbeitet, muss die Host-Anwendung mit der \"glib\"-Bibliothek verknüpft sein.

Beachten Sie, für Konsole-Anwendungen wird diese Lösung natürlich nicht funktionieren, weil keine Ereignis-Schleife läuft.

## Vorbehalte

Obwohl es möglich ist, FreeCAD in einen externen Python-Interpreter zu importieren, ist dies kein übliches Benutzungsszenario und erfordert etwas Sorgfalt. Generell ist es besser, das in FreeCAD enthaltene Python zu verwenden, FreeCAD auf der Kommandozeile auszuführen oder als ein Sub-Prozess. Zu den letzten beiden Optionen gibt es [hier](Start_up_and_Configuration/de.md) nähere Einzelheiten.

Weil das FreeCAD-Python-Modul aus C++ kompiliert wurde (anstatt ein reines Python-Modul zu sein), kann es nur von einem kompatiblen Python-Interpreter importiert werden. Generell bedeutet das, dass der Python-Interpreter mit dem gleichen C-Compiler wie bei der Erstellung von FreeCAD kompiliert werden muss. Informationen über den bei der Erstellung des (in FreeCAD enthaltenen) Python-Interpreters benutzten Compilers köönen wie folgt ermittelt werden: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Verwandtes

-   [Headless FreeCAD](Headless_FreeCAD.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Embedding FreeCAD/de
