---
- TutorialInfo   */de
   Topic   *Rendern
   Level   *Mittel
   Time   *120 Minuten
   Author   *[https   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=21943 vocx]
   FCVersion   *0.18 oder höher
   Files   *keine
---

# Tutorial FreeCAD POV ray/de




**Der Arbeitsbereich [Raytracing](Ray_Tracing_Workbench/de.md) wird abgelöst durch den neuen Arbeitsbereich [https   *//github.com/FreeCAD/FreeCAD-render Render Workbench], der als Ersatz geplant ist. Der Arbeitsbereich Render kann mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert werden. Diese Information wird bereitgestellt, weil FreeCAD als Standardeinstellung (mit Stand 0.19-24276) weiterhin mit dem Arbeitsbereich Raytracing ausgeliefert wird und der neue Arbeitsbereich generell in der gleichen Weise arbeiten sollte**



## Einleitung

Dieses Tutorial zeigt, wie man ein gerendertes Bild in FreeCAD mit dem POV-Ray Renderer erzeugt. Es wird davon ausgegangen, dass der Anwender bereits ein Teil oder eine Baugruppe in FreeCAD erstellt oder in FreeCAD importiert hat. Es verwendet die [Raytracing Arbeitsbereich](Raytracing_Workbench/de.md), um die Datei für das Rendern zu erzeugen.

Dieses Tutorial basiert auf dem Forumsbeitrag von schupin [FreeCAD / pov ray tutorial](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=32745), der auch eine `.pov` Datei enthält, die zur Erstellung eines Renderings benötigt wird.

<img alt="" src=images/Povray_before_after.png  style="width   *600px;">



*align=center|Beispiel von schupin eines mit FreeCAD und POV-Ray erstellten 3D Modells und eines qualitativ hochwertigen Renderings.*

Die in diesem Tutorial verwendeten Dateien befinden sich im Beitrag Nr. 8 [im selben Diskussionsbeitrag](https   *//forum.freecadweb.org/viewtopic.php?f=36&t=32745#p305169).

## Grundaufbau

Folge dem grundlegenden Arbeitsablauf, der in der Dokumentation [Raytracing Workbench/de](Raytracing_Workbench/de.md) beschrieben ist.

Damit das direkte Rendern funktioniert, muss die ausführbare Datei `povray` in {{MenuCommand/de|Bearbeiten → Einstellungen → Raytracing → Rendern → POV-Ray Programmdatei}}; setze sie auf deinem Speicherort in deinem System, z.B. `/usr/bin/povray`. Andere vom Renderer verwendete Optionen können hier ebenfalls definiert werden, einschließlich der Breite `+W` und Höhe `+H` des Bildes sowie die Verwendung von Antialiasing `+A`.

## Einrichten der .pov Datei 

1\. Erstelle eine Baugruppe mit Körpern aus der [Part](Part_Workbench/de.md) oder [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) oder eines anderen Arbeitsbereichs, die Volumenkörper erzeugt, z.B. der [Arch_Workbench](Arch_Workbench.md). Weise den einzelnen Körpern, aus denen die Baugruppe besteht, Farben oder Materialien zu, die ungefähr der Farbe entsprechen, die du in deinem Rendering wünschst.

<img alt="" src=images/01_T04_FreeCAD_POVray_model.png  style="width   *600px;">



*align=center|Zusammenbau von drei Körpern, die in FreeCAD erstellt und mit Farben oder Materialien versehen wurden.*

2\. Wenn dein Modell sehr detailliert ist, stelle sicher, dass die {{PropertyView/de|Ablenkung}} des Körpers auf einen niedrigen Wert zwischen `0.1` und `0.01` oder sogar kleiner eingestellt ist. Je niedriger dieser Wert ist, desto detaillierter wird das exportierte Mesh sein und desto besser wird die Qualität des Renderings sein.

![](images/02_T04_FreeCAD_POVray_deviation.png )



*align=center|Abweichungseigenschaft der in FreeCAD erstellten Körper; die Abweichung muss gering sein, um die Teile mit guter Auflösung exportieren zu können.*

3\. Erstelle ein POV-Ray Projekt, durch anklicken von **<img src="images/Raytrace_New.svg" width=16px> [Neu](Raytracing_New/de.md)** klickst. Wenn das Ansichtsfenster als [orthografisch](Std_OrthographicCamera/de.md) eingestellt ist, ändere es in [Perspektive](Std_PerspectiveCamera/de.md), da der Renderer normalerweise mit einer Kamera mit perspektivischer Ansicht arbeitet. Die Verwendung der perspektivischen Ansicht ermöglicht es dir, die Art der zu rendernden Szene besser zu erkennen.

4\. Wähle alle Objekte aus, die du zu deiner Szene hinzufügen möchtest, wähle dann das erstellte `PovProject` Objekt und klicke auf **<img src="images/Raytrace_NewPartSegment.svg" width=16px>. [EinfügenTeil](Raytracing_InsertPart.md)**.


**Hinweis   ***

Hüte dich vor den Objekten, die derzeit nicht im 3D Ansichtsfenster sichtbar sind. Wenn sie unsichtbar sind, aber in der Szene enthalten sind, werden sie trotzdem gerendert. Wenn andererseits ein Körper wirklich nicht gerendert werden soll, wähle ihn nicht für die Aufnahme in das POV-Ray Projekt aus.


**Hinweis 2   ***

Alle Objekte im POV-Ray Projekt werden einen Namen haben, der auf ihrem internen FreeCAD-Namen basiert. Es ist wichtig zu beachten, welches der POV-Ray Name ist, da diesen POV-Ray Namen weitere Optionen, z.B. die Materialtexturen, zugeordnet werden.

5\. Im 3D Ansichtsfenster kannst du die Ansicht zoomen, schwenken und drehen, um die Szene nach deinen Wünschen einzurichten. Stellen sicher, dass die Objekte im Ansichtsfenster zentriert sind, wähle dann das erstellte `PovProject` Objekt aus und drücke **<img src="images/Raytrace_ResetCamera.svg" width=16px>. [Kamera zurücksetzen](Raytracing_ResetCamera/de.md)**.

6\. Die POV-Ray Datei ist nun fertig; sie enthält die ausgewählten Objekte und die Kamerainformationen. Wähle das erstellte `PovProject` Objekt und drücke dann **<img src="images/Raytrace_ExportProject.svg" width=16px> [ExportProjekt](Raytracing_ExportProject/de.md)**, um die Datei `.pov` zu speichern.

7\. Die erzeugte `.pov` Datei kann nun direkt aus FreeCAD heraus gerendert werden. Wähle das erstellte `PovProject` Objekt aus und drücke dann **<img src="images/Raytrace_Render.svg" width=16px> [Render](Raytracing_Render/de.md)**. Wenn das Popup Bild auf dem Bildschirm erscheint, klicke auf es, damit es in einem eigenen Fensterreiter an FreeCAD gesendet wird.

<img alt="" src=images/03_T04_FreeCAD_POVray_first_render.png  style="width   *600px;">



*align=center|Erstes Rendern der mit POV-Ray erstellten Baugruppe mit der von der Raytracing Workbench geschriebenen Standardvorlage.*

7.1. Wenn die `.pov` Datei bereits erstellt wurde, ist es auch möglich, `povray` von der Befehlszeile aus zu starten. 
```python
povray assembly.pov +W800 +H600 +AM2 +A
```

Die Optionen `+WX +HY` legen die horizontale und vertikale Pixelgröße des endgültigen Bildes fest.

Die Optionen `+AM2` (Typ 2, rekursive Superabtastung) und `+A` lösen ein Antialiasing aus, um ein glatteres Bild zu erzeugen.

8\. Durch Doppelklicken auf das `PovProject` Objekt kann man sehen, dass es die `ProjectStd.pov` Vorlage verwendet; diese Vorlage erzeugt eine grundlegende `.pov` Datei, die ein einfaches und dunkles Bild erzeugt.

Um das Aussehen des Bildes zu verbessern, verwende eine bessere Vorlage. Doppelklicke auf das Objekt `PovProject` und wähle die Vorlage `RadiosityNormal.pov`. Exportiere dann eine neue `.pov` Datei und führe den Renderer erneut aus. Das Bild sollte heller und allgemein besser aussehen.

<img alt="" src=images/04_T04_FreeCAD_POVray_first_render_radiosity.png  style="width   *600px;">



*align=center|Rendern der mit POV-Ray erzeugten Baugruppe mit der von der Raytracing Workbench geschriebenen RadiosityNormal-Vorlage.*

Doppelklicke noch einmal auf das Objekt `PovProject` und wähle nun die Vorlage `RadiosityOutdoorHQ.pov`. Exportiere dann eine neue `.pov` Datei und führe den Renderer erneut aus. Die Erzeugung des Bildes sollte länger dauern, aber das Ergebnis sollte eine bessere Qualität haben. <img alt="" src=images/05_T04_FreeCAD_POVray_first_render_radiosity_outdoor.png  style="width   *600px;">



*align=center|Rendern der mit POV-Ray erzeugten Baugruppe, mit der von der Raytracing Workbench geschriebenen RadiosityOutdoorHQ Vorlage.*

Wenn das gerenderte Bild gut genug ist, dann kann es gespeichert werden, und es gibt nichts mehr zu tun. Um jedoch das Aussehen der Materialien genau zu kontrollieren und noch bessere Ergebnisse zu erzielen, muss die `.pov` Datei manuell bearbeitet werden.

In den folgenden Abschnitten bearbeiten wir die Basisdatei `.pov`, die mit der Vorlage `ProjectStd` erstellt wurde.

## Bearbeiten der .pov Datei 

9\. Die von FreeCAD generierte `.pov` Datei ist eine einfache Textdatei, die mit jedem Editor geöffnet werden kann. Sie ähnelt grob einer C++ Quellcodedatei   * Anweisungen beginnen mit einem Hash `#` und werden mit einem Semikolon `;` abgeschlossen. Geschweifte Klammern { } werden verwendet, um Abschnittsblöcke zu begrenzen, und die Einrückung ist ein beliebiger Weißraum. Kommentare werden mit einem doppelten Schrägstrich `//` angegeben; Blockkommentare können wie in C mit einem Paar `/* */` definiert werden.

Die Datei mag auf den ersten Blick kompliziert aussehen, aber 90 % ihres Inhalts sind nur Netzdaten, die nicht viele Änderungen erfordern, da diese Netze die Geometrie der Körper darstellen, die wir rendern wollen.

Die Datei ist wie folgt strukturiert   *

-   Beinhaltet
-   Globale Einstellungen
-   Himmelskugel
-   Flugzeuge
-   Oberflächen und Texturen
-   Kamera
-   Netz- und Körperinformationen
-   Lichtquelle

Die Kamerainformationen werden nicht berührt, ebenso wenig wie die meisten Informationen in den Netzen. Die wichtigsten Änderungen werden in den anderen Abschnitten vorgenommen.

Da die Netze nicht stark verändert werden, kann die Datei neu organisiert werden, so dass diese Informationen am Ende der Datei stehen.


<div class="toccolours mw-collapsible mw-collapsed">

Dies ist der vollständige Inhalt der Datei `.pov`, nur ohne die Netze.


<div class="mw-collapsible-content">


```python
// Persistence of Vision Ray Tracer Scene Description File
// for FreeCAD (http   *//www.freecadweb.org)

#version 3.6;

#include "colors.inc"
#include "metals.inc"

// 

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20
}  

// 


sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 rgb <0.6,0.7,1.0>]
      [0.7 rgb <0.0,0.1,0.8>]
    }
  }
}


// 

plane {
  y, -1
  texture { pigment {rgb <0.0,0.0,0.0>} finish {ambient 0.0 reflection 0.05 specular 0.0} }
}

// Standard finish
//#declare StdFinish = F_MetalA;
//#declare StdFinish = finish { diffuse 0.7 };
//#declare StdFinish = finish { phong 0.5 };
//#declare StdFinish = finish { ambient rgb <0.5,0.5,0.5> };
//#declare StdFinish = finish { crand 0.5 phong 0.9};
#declare StdFinish = finish { ambient 0.01 diffuse 0.9 phong 1.0 phong_size 70 metallic brilliance 1.5} ;

// declares position and view direction

// Generated by FreeCAD (http   *//www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}
// Written by FreeCAD http   *//www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ... meshes should be defined here until the end of the file ...




//default light
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
```


</div>


</div>

### Grundlegende Reorganisation 

10\. Öffne die Datei `.pov` mit einem Texteditor, gehe zum Ende der Datei, wähle den `light_source` Abschnitt aus, schneide ihn aus und füge ihn vor der ersten `//face number1` Zeile ein.

Die resultierende Datei sollte die Abschnitte `camera` und `light_source` nebeneinander haben, zum Beispiel


```python
// Generated by FreeCAD (http   *//www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}

//default light
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
// Written by FreeCAD http   *//www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.
.
.
```

### Lichter vorbereiten 

11\. Standardmäßig wird in der Projektdatei eine Leuchte mit einer Position und einer Farbe definiert. 
```python
light_source {
  cam_location + cam_angle * 100
  color rgb <10, 10, 10>
}
```

Die Position des Lichts wird durch einen Vektor `<x, y, z>` definiert. Die `Farbe` kann wie ein `<r, g, b>` Vektor festgelegt werden, oder es kann auch eine benannte Farbe wie `Weiß` sein. Wenn die RGB Werte angegeben werden, sollten sie im Bereich von `0.0` bis `1.0` liegen, damit das Licht eine normale Helligkeit hat.

Wie andere Objekte auch, kann das Licht mit vielen Optionen modifiziert werden. Die Option `area_light` erzeugt eine rechteckige Quelle, was realistischer ist, da es zu einer diffusen Beleuchtung führt, die weiche Schatten erzeugt. Das Schlüsselwort `adaptive` hilft, die Berechnungszeit der Lichtwege zu reduzieren; je größer der Wert, desto genauer wird das Ergebnis sein; um lange Renderingzeiten zu vermeiden, solltest du die kleinste Ganzzahl verwenden, die ein akzeptables Ergebnis liefert (`1` oder `2` ist normalerweise ausreichend); um das beste Ergebnis zu erhalten, entferne das Schlüsselwort vollständig (lange Renderingzeit). Das Schlüsselwort `jitter` hilft bei der Verbesserung der Schatten durch zufällige Verschiebung der Position der Lichter. Die Schlüsselwörter `circular` und `orient` verwandeln das Flächenlicht in eine sphärische Quelle, die bei abgerundeten Objekten in der Szene bessere Schatten erzeugt. Das Einbeziehen von `fade_distance` und `fade_power` ist hilfreich, um den Wert des Lichts mit der Entfernung abzuschwächen, genau wie es bei einer echten Lichtquelle geschieht.

Richte das von rechts und oben kommende Licht ein. 
```python
light_source {
    <1200, 1000, -1300>
    color White
    area_light <100, 0, 0>, <0, 0, 100>, 20, 20
    adaptive 1
    jitter
    circular orient
    fade_distance 1000 fade_power 2
}
```

Wenn die Lichtquelle in der Szene sein soll, kann es nützlich sein, auf dem Bildschirm einen Hinweis darauf zu sehen, wo diese Quelle sein sollte. Erstelle zu diesem Zweck eine Kugel mit einem kleinen Radius und nimm an, dass diese Kugel die Lichtquelle darstellt; positioniere die Kugel an der gewünschten Stelle, bewege dann das Licht sehr nahe an diese Koordinaten und teste die Beleuchtung der Szene; wenn du mit der Position des Lichts zufrieden bist, lösche die Kugel einfach. 
```python
sphere {
    <1200, 1000, -1200>, 10
    pigment { color White }
}
```

12\. Der Abschnitt `sky_sphere` wird verwendet, um einen realistischen Himmelshintergrund zu erstellen. Er wird üblicherweise als ein `gradient` und eine `color_map` von mindestens zwei Farben definiert, um einen fließenden Übergang von der Farbe des Horizonts zur Farbe des Zenits der Szene zu erzeugen.


```python
sky_sphere {
    pigment {
        gradient y
        color_map {
            [0.0 color Gray50]
            [0.7 color White]
        }
    }
}
```

<img alt="" src=images/06_T04_FreeCAD_POVray_render_lights.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage, Rendern der Szene mit POV-Ray, wobei die Lichtquelle und die Himmelskugel eingerichtet werden.*

### Bereite die Körpertexturen vor 

13\. Die Texturen der einzelnen Körper müssen angepasst werden. Dies ist die zeitaufwendigste Aufgabe dieses Prozesses.

In der `.pov` Datei wird jeder Körper auf folgende Weise beschrieben

-   Fläche1, Fläche2, Fläche3, Fläche4, \...
-   Körper (Vereinigung der Flächen)
-   Objekt

Ein Körpernetz wird durch Flächen definiert, und jede Fläche wird durch eine Reihe von Dreieckselementen definiert, die ihrerseits durch `vertex_vectors`, `normal_vectors` und `face_indices` definiert werden. Diese Informationen müssen überhaupt nicht geändert werden. Dann wird jeder Körper als Vereinigung der angegebenen Flächen definiert. Auch diese Information muss nicht verändert werden.

Schließlich wird jedes zu rendernde `object` als einer der spezifizierten Körper definiert, mit einer bestimmten `texture`, die ihrerseits durch Eigenschaften wie `pigment` und `finish` definiert wird. 
```python
// instance to render
object {Pov_Body
 texture {
      pigment {color rgb <0.827451,0.827451,0.431373>}
      finish {StdFinish } //definition on top of the project
  }
}
```

Indem man die `.pov` Datei nach dem Schlüsselwort `object` durchsucht, ist es möglich, direkt zum gewünschten Teil in der Datei zu gehen und die `texture` entsprechend zu modifizieren.

Wie im Kommentar angegeben, steht die Definition von `StdFinish` ganz oben in der Datei, in diesem Fall vor den Kamerainformationen. Dieser Wert kann auf vielfältige Weise deklariert werden, als Kombination verschiedener Eigenschaften, wie in den kommentierten und unkommentierten Zeilen gezeigt wird. 
```python
// Standard finish
//#declare StdFinish = F_MetalA;
//#declare StdFinish = finish { diffuse 0.7 };
//#declare StdFinish = finish { phong 0.5 };
//#declare StdFinish = finish { ambient rgb <0.5,0.5,0.5> };
//#declare StdFinish = finish { crand 0.5 phong 0.9};
#declare StdFinish = finish { ambient 0.01 diffuse 0.9 phong 1.0 phong_size 70 metallic brilliance 1.5} ;
```

Im Allgemeinen ist eine `Textur` ein Behälter, der ein Material beschreibt; er enthält Informationen wie das `Pigment` (Farbe oder Grafik), `normal` (wie sich die Farbe mit der Krümmung der Oberfläche ändert), `finish` (Wechselwirkung der Oberfläche mit dem Licht), `pattern` (Achat, Ziegel, Dellen, Leopard, Radial, Wellen, Fliesen, Wellen, Holz usw.) und andere Eigenschaften. Es gibt viele Optionen, die miteinander kombiniert werden können, um eine Textur zu erzeugen. Dieses Mischen ist nicht trivial, aber es gibt viele Beispiele online, um das gewünschte Aussehen des Materials zu erhalten.

#### Materialbibliotheken

14\. POV-Ray wird mit einer umfangreichen Bibliothek von Materialien geliefert, die namentlich verwendet werden können. Standardmäßig stellt die Projektvorlage einige Materialien durch die Verwendung von `#include` Anweisungen am Anfang der Datei zur Verfügung. Diese Materialien können nach Belieben weiter modifiziert werden. 
```python
#include "colors.inc"
#include "metals.inc"
```

Die Bibliothek `colors.inc` definiert die Grundfarben durch ihren Namen, `Red`, `Green`, `Blue`, `Yellow`, `Cyan`, `Magenta`, `Clear`, `White` und `Black`. Es definiert auch verschiedene andere Schattierungen sowie Funktionen zur Transformation von Farben. Die Bibliothek `metals.inc` enthält Kupfer-, Silber-, Chrom- und Messingtexturen, und `golds.inc` enthält die Goldtexturen.

Die Standardbibliotheken befinden sich im Installationsverzeichnis von POV-ray, zum Beispiel 
```python
/usr/share/povray-3.7/include/
```

#### Neue Texturen 

15\. Um zum Beispiel eine Spiegeltextur zu erzeugen, wird dem `finish` ein hoher Wert von `reflection` zugewiesen. 
```python
#declare T_mirror = texture {
    finish { reflection {0.9} }
}
```

Alternativ kann für Metalle eine vordefinierte Oberflächenbeschaffenheit verwendet werden. 
```python
#include "metals.inc"
#declare T_mirror = texture {
    finish { F_MetalE }
}
```

Dann kann sie dem spezifischen Objekt zugeordnet werden. 
```python
object {Pov_Body002
    texture { T_mirror }
}
```

Die `woods.inc` Bibliothek definiert die `T_Wood7` Textur (gelbe Kiefer, zerklüftete Maserung). Sie kann als Grundlage für eine komplexere Textur verwendet werden, mit zusätzlicher Skalierung und Übersetzung. 
```python
#include "woods.inc"
#declare T_wood = texture {
    T_Wood7
    scale 50.0
    translate x*1
    translate y*10
}
```

Dann wird sie dem spezifischen Objekt zugeordnet. 
```python
object {Pov_Body
    texture { T_wood }
}
```

Die `glass.inc` Bibliothek definiert `F_Glass2` als eine Oberfläche für transparentes Acryl; sie definiert auch `I_Glass` als ein Innenmaterial, das zusammen mit der Option `caustics` verwendet wird, um die Effekte von Licht, das durch ein transparentes Material hindurchgeht, so genau wie möglich zu berechnen. In diesem Fall wird der Abschnitt `material` verwendet, der äußere (`texture`) und innere (`interior`) Informationen des Materials enthält.


```python
#declare M_vase = material {
    texture {
        pigment { color rgbf <1.0, 0.73333, 0.0, 0.75> }
        finish { F_Glass2 }
    }
    interior { I_Glass caustics 1.0 }
}
```

Dann kann sie dem spezifischen Objekt zugeordnet werden. 
```python
object {Pov_Body001
    material { M_vase }
}
```

<img alt="" src=images/07_T04_FreeCAD_POVray_render_materials.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage, Rendern der Szene mit POV-Ray, mit der Lichtquelle und der Himmelskugel eingerichtet und den Materialien zugeordnet.*

### Ebenen vorbereiten 

16\. Wenn das ursprüngliche 3D Modell nicht zur Verfügung steht, können Ebenen hinzugefügt werden, um einen Boden oder eine Tischplatte zu simulieren, auf der die Objekte stehen. Es können weitere Ebenen definiert werden, die als Wände oder andere Arten von Begrenzungen dienen.

Standardmäßig wird eine einzige Ebene erstellt. Sie wird 1 Millimeter unterhalb des Modells platziert, so dass sie als Boden erscheint. Der Ebene wird eine Grundtextur zugewiesen, die schwarz und leicht reflektierend ist. 
```python
plane {
  y, -1
  texture { pigment {rgb <0.0,0.0,0.0>} finish {ambient 0.0 reflection 0.05 specular 0.0} }
}
```

Beachte, dass in POV-Ray die X Achse als horizontal (links-rechts), die Y Achse als vertikal (oben-unten) und die Z Achse als Tiefe (vorne-hinten) definiert ist.

Für einen einfachen grauen Boden, der kaum reflektierend verwendet wird 
```python
plane {
  y, -1
  texture { pigment {rgb <0.3, 0.3, 0.3>} finish {ambient 0.0 reflection 0.01 specular 0.0} }
}
```

<img alt="" src=images/08_T04_FreeCAD_POVray_render_floor_gray.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage wird die Szene mit POV-Ray gerendert, wobei die Lichtquelle und die Himmelskugel eingerichtet, die Materialien zugeordnet und eine Bodenebene mit einer grauen Grundtextur erstellt werden.*

17\. Mit Hilfe von Normalen und Materialbibliotheken kann die Ebene ein komplexeres Aussehen erhalten.

Definiere eine normale Karte, die verwendet wird, um der Fläche das Aussehen eines Parkettbodens zu geben.


```python
#declare Parquet_normal = normal {
    gradient z 2 slope_map { [0 <0,1>][0.05 <1,0>][0.95 <1,0>][1 <0,-1>] }
    scale 80
} ;
```

Definiere dann die Ebene. Als `pigment` verwende ein Holz `color_map`, das in `woods.inc` definiert ist, und modifiziere es mit `turbulence` und `scale`, so dass die Holzmaserung zufällig aussieht. Dann füge die erzeugte Normale zusammen mit einer weiteren Normalen hinzu; dies führt zu einer Textur des Parketts mit leichten Unregelmäßigkeiten. Dann als `finish`, mache es ein wenig reflektierend und glänzend.


```python
#include "woods.inc"
plane {
    y, -1
    pigment {
        wood color_map { M_Wood8A }
        turbulence 0.5 scale <10, 1, 1>*20
    }
    normal {
        average normal_map {
          [1 Parquet_normal]
          [1 wood 0.5 slope_map { [0 <0,0>][0.5 <0.5,1>][1 <1,0>] }
              turbulence 0.5 scale <10, 1, 1>*20]
        }
    }
    finish { ambient 0.0 reflection 0.1 specular 0.2 }
}
```

<img alt="" src=images/09_T04_FreeCAD_POVray_render_floor_wood.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage, Rendern der Szene mit POV-Ray, mit der Lichtquelle und der Himmelskugel eingerichtet, Materialien zugeordnet und einer Bodenebene mit einer Parketttextur.*

18\. Füge eine zweite Ebene hinzu, diesmal senkrecht zur Z Richtung, um als Rückwand zu dienen. Verschiebe sie ein wenig hinter das Modell, um den Spiegel nicht zu verdecken. Füge die `stones.inc` Bibliothek ein, füge eine generische Granittextur hinzu und skaliere sie ein wenig. Dadurch wird das Aussehen einer einfachen Trockenbauwand erreicht.


```python
#include "stones.inc"
plane {
    z, 10
    texture {
        T_Grnt1   
        scale 0.02
    }
}
```

Eine dritte Ebene kann hinter der Position der Kamera hinzugefügt werden, so dass der Spiegel einen begrenzten Bereich zwischen den beiden Wänden reflektiert.


```python
#include "stones.inc"
plane {
    z, -3700
    texture {
        T_Grnt1   
        scale 0.02
    }
}
```

<img alt="" src=images/10_T04_FreeCAD_POVray_render_floor_wood_walls.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage, Rendern der Szene mit POV-Ray, wobei die Lichtquelle und die Himmelskugel eingerichtet, die Materialien zugeordnet, eine Bodenebene mit einer Parketttextur und Rückwände mit Trockenbautexturen.*

### Bereite die globalen Einstellungen vor, radiosity 

19\. Die globalen Einstellungen definieren das Umgebungslicht.


```python
global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20
}
```

Die Eigenschaft `radiosity` innerhalb der `global_settings` steuert die Art und Weise, wie POV-Ray diffuse Lichtwechselwirkungen zwischen verschiedenen Objekten berechnet. Es ist wichtig, diese Eigenschaft anzupassen, um gute Rendering Ergebnisse zu erhalten.

Da es zeitaufwendig sein kann, verschiedene `Radiosity` Einstellungen zu testen, können Sie eine Variable `Rad_Quality` und eine `#switch` Anweisung verwenden, um schnell Render Einstellungen niedriger, mittlerer oder hoher Qualität festzulegen. Je höher die Qualitätseinstellungen sind, desto mehr Zeit wird zum Rendern eines Bildes benötigt.


```python
#declare Rad_Quality = 1;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        pretrace_start 0.08
        pretrace_end   0.02
        count 50
        error_bound 0.5
        recursion_limit 1
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        pretrace_start 0.08
        pretrace_end   0.01
        count 120
        error_bound 0.25
        recursion_limit 1
    }
    #break
 #case (3)
    radiosity { // Settings 3 (high quality)
        pretrace_start 0.08
        pretrace_end   0.005
        count 400
        error_bound 0.1
        recursion_limit 2
    }
    #break
#end
}
```

<img alt="" src=images/11_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_1.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage wird die Szene mit POV-Ray gerendert, wobei die Lichtquelle und die Himmelskugel eingerichtet, die Materialien zugeordnet, eine Bodenebene mit einer Parketttextur und die Rückwände mit Trockenbautexturen versehen werden. Radiosity Einstellungen für schnelles Rendern.*

20\. Die Bibliothek `rad_def.inc` definiert ein Makro, um die `radio` schnell auf eine vordefinierte Konfiguration einzustellen. 
```python
#include "rad_def.inc"
global_settings {
    radiosity {
        Rad_Settings(Setting, Normal, Media)
    }
}
```

Der `Setting` Wert kann eine der vordefinierten Konstanten sein   * 
```python
Radiosity_Default
Radiosity_Debug
Radiosity_Fast
Radiosity_Normal
Radiosity_2Bounce
Radiosity_Final
Radiosity_OutdoorLQ
Radiosity_OutdoorHQ
Radiosity_OutdoorLight
Radiosity_IndoorLQ
Radiosity_IndoorHQ
```

Die `Normal` und `Media` Werte sind entweder `off` oder `on`.

Um verschiedene Einstellungen zu testen, könnte daher die Anweisung `#switch` auch wie im Folgenden geschrieben werden.


```python
#declare Rad_Quality = 3;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        Rad_Settings(Radiosity_Fast, off, off)
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        Rad_Settings(Radiosity_2Bounce, on, on)
    }
    #break
 #case (3)
    radiosity{ // Settings 3 (high quality)
        Rad_Settings(Radiosity_Final, on, on)
        recursion_limit 2
    }
    #break
#end
}
```

Die genauen Werte, die von diesen Voreinstellungen verwendet werden, findest du in der Datei `rad_def.inc`, die z.B. im Installationsverzeichnis von POV-Ray zu finden ist   * 
```python
/usr/share/povray-3.7/include/
```

Der [Raytracing Arbeitsbereich](Raytracing_Workbench/de.md) hat drei Standardvorlagen   *

-    `ProjectStd.pov`, sie verwendet `radiosity` überhaupt nicht.

-    `RadiosityNormal.pov`, es verwendet die Voreinstellung `Radiosity_Normal`.

-    `RadiosityOutdoorHQ.pov`, es verwendet die Voreinstellung `Radiosity_OutdoorHQ`.

## Endgültiges Rendern 

21\. Die bearbeitete `.pov` Datei kann gespeichert werden, wenn alle Anpassungen vorgenommen wurden.

Die endgültige Struktur ist wie folgt   *

-   Beinhaltet, mit zusätzlichen Bibliotheken
-   Globale Einstellungen, mit Radiosity-Parametern
-   Himmelskugel, mit hellerer Farbe
-   Ebenen, positioniert und mit Texturen
-   Oberflächen und Texturen, mit benutzerdefinierten Definitionen
-   Kamera, nicht geändert
-   Lichtquelle, mit zusätzlichen Eigenschaften
-   Netz- und Körperinformationen, unter Verwendung der zuvor definierten Texturen


**Hinweis   ***

die Abschnitte der `.pov` Datei können in beliebiger Reihenfolge sein, obwohl es wahrscheinlich einfacher ist, mit der Datei zu arbeiten, wenn sich die Netzinformationen am Ende befinden.

Das endgültige Rendern kann durch Klicken auf **<img src="images/Raytrace_Render.svg" width=16px>** durchgeführt werden. oder durch Aufruf der ausführbaren Datei von der Befehlszeile aus.


```python
povray assembly.pov +W800 +H600 +AM2 +A
```

<img alt="" src=images/12_T04_FreeCAD_POVray_render_floor_wood_walls_radiosity_final.png  style="width   *600px;">



*align=center|Ausgehend von der Standardvorlage wird die Szene mit POV-Ray gerendert, wobei die Lichtquelle und die Himmelskugel eingerichtet, die Materialien zugeordnet, eine Bodenebene mit einer Parketttextur und die Rückwände mit Trockenbautexturen versehen werden. Radiosity Einstellungen für ein qualitativ hochwertiges Ergebnis   * `Radiosity_Final* und {{incode|recursion_limit 2`.}}


<div class="toccolours mw-collapsible mw-collapsed">

Dies ist der vollständige Inhalt der Datei `.pov`, nur ohne den letzten Abschnitt, d.h. ohne die Netze.


<div class="mw-collapsible-content">


```python
// Persistence of Vision Ray Tracer Scene Description File
// for FreeCAD (http   *//www.freecadweb.org)

#version 3.6;

#include "colors.inc"
#include "metals.inc"
#include "woods.inc"
#include "glass.inc"
#include "stones.inc"
#include "rad_def.inc"

// 
#declare Rad_Quality = 3;

global_settings {
    assumed_gamma 1.0
    ambient_light color rgb <1.0,1.0,1.0>
    max_trace_level 20

#switch (Rad_Quality)
 #case (1)
    radiosity { // Settings 1 (fast)
        Rad_Settings(Radiosity_Fast, off, off)
    }
    #break
 #case (2)
    radiosity { // Settings 2 (medium quality)
        Rad_Settings(Radiosity_2Bounce, on, on)
    }
    #break
 #case (3)
    radiosity{ // Settings 3 (high quality)
        Rad_Settings(Radiosity_Final, on, on)
        recursion_limit 2
    }
    #break
#end
}

// 


sky_sphere {
    pigment {
        gradient y
        color_map {
            [0.0 color Gray50]
            [0.7 color White]
        }
    }
}


// 

#declare Parquet_normal = normal {
    gradient z 2 slope_map { [0 <0,1>][0.05 <1,0>][0.95 <1,0>][1 <0,-1>] }
    scale 80
} ;

// Floor
plane {
    y, -1
    pigment {
        wood color_map { M_Wood8A }
        turbulence 0.5 scale <10, 1, 1>*20
    }
    normal {
        average normal_map {
          [1 Parquet_normal]
          [1 wood 0.5 slope_map { [0 <0,0>][0.5 <0.5,1>][1 <1,0>] }
              turbulence 0.5 scale <10, 1, 1>*20]
        }
    }
    finish { ambient 0.0 reflection 0.1 specular 0.2 }
}

// Back wall
plane {
    z, 10
    texture {
        T_Grnt1   
        scale 0.02
    }
}

// Behind camera wall
plane {
    z, -3700
    texture {
        T_Grnt1   
        scale 0.02
    }
}

#declare T_mirror = texture {
    finish { reflection {0.9} }
//    finish { F_MetalE }
}

#declare T_wood = texture {
    T_Wood7
    scale 50.0
    translate x*1
    translate y*10
}

#declare M_vase = material {
    texture {
        pigment { color rgbf <1.0, 0.73333, 0.0, 0.75> }
        finish { F_Glass2 }
    }
    interior { I_Glass caustics 1.0 }
}
// declares position and view direction

// Generated by FreeCAD (http   *//www.freecadweb.org/)
#declare cam_location =  <-171.753,1229.11,-2667.08>;
#declare cam_look_at  = <636.959,359.955,160.296>;
#declare cam_sky      = <0.068217,0.958943,0.275273>;
#declare cam_angle    = 45; 
camera {
  location  cam_location
  look_at   cam_look_at
  sky       cam_sky
  angle     cam_angle 
  right x*800/600
}
//default light
light_source {
    <1200, 1000, -1300>
    color White
    area_light <100, 0, 0>, <0, 0, 100>, 20, 20
    adaptive 1
    jitter
    circular orient
    fade_distance 1000 fade_power 2
}
// Written by FreeCAD http   *//www.freecadweb.org/
// face number1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ... meshes should be defined here until the end of the file ...
```


</div>


</div>

## Schlussbemerkungen

POV-Ray ist ein relativ altes Stück Software, das erstmals Anfang der 1990er Jahre veröffentlicht wurde. Seine Hauptvorteile gegenüber modernerer Software sind

-   es ist eine seit vielen Jahren bewährte Lösung
-   läuft in vielen Betriebssystemen
-   die Szene kann mit nur einer Textdatei eingestellt werden
-   erfordert einfache Berechnungsressourcen, um ein qualitativ hochwertiges Bild zu erzeugen, so dass es auch mit relativ alter Hardware funktioniert

Dem Benutzer wird empfohlen, die POV-Ray Dokumentation und weitere Tutorials oder Beispiele zu lesen, um die richtigen Einstellungen für seine Bedürfnisse zu erhalten.

-   [POV-Ray für Unix Version 3.7](http   *//www.povray.org/documentation/3.7.0/index.html)
-   [POV-Ray Anleitung](http   *//www.povray.org/documentation/3.7.0/t2_0.html)
-   [POV-Ray Referenz](http   *//www.povray.org/documentation/3.7.0/r3_0.html)


 {{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Tutorial FreeCAD POV ray/de
