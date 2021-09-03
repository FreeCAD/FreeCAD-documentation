---
- GuiCommand:/de
   Name:Ship Outline
   Name/de:Schiffskontur
   Icon:Ship_OutlineDraw.svg
   MenuLocation:Schiffskonstruktion → Konturzeichnung
   Workbenches:[Schiff](Ship_Workbench/de.md)
   Shortcut:
   SeeAlso:
---

## Beschreibung

Plottet die Konturzeichnung des Schiffsrumpfes

## Linienzeichnen

Der Arbeitsbereich Schiff stellt ein Werkzeug zur Verfügung, das es einfach macht, einen Linienplan aus der Schiffslinienzeichnung zu erstellen.

![Umrisszeichnungswerkzeug.](images/Ship_OutlineDraw.svg )


<center>

Umrisszeichnungswerkzeugsymbol


</center>

Das Linienzeichen ist ein Satz von Linien aus Schnitten in allen 3 Achsen, die schließlich die Rumpfgeometrie in einem Linienplan zeigen. Wir müssen die Linien für die 3 folgenden Ansichten bereitstellen:

-   Spantenriss (unter Verwendung der transversalen Schnitte)
-   Längsriss (unter Verwendung der Längsschnitte)
-   Wasserlinienriss (unter Verwendung der Wasserleitungskürzungen)

### Transversale Schnitte 

Normalerweise müssen 21 transversale äquidistante Schnitte zwischen den Senkrechten durchgeführt werden. Um dies zu tun, stellt FreeCAD ein automatisches Werkzeug zur Verfügung, wähle einfach den **Transversal** Typ der Schnitte, gehe in das **Auto create** Feld und setze **21** Schnitte, dann drücke **Schnitte erstellen**.

![Umrisszeichnung Transversale Schnitte Voransicht.](images/S60OutlineTransversal.png )


<center>

Umrisszeichnung Transversale Schnitte Voransicht


</center>

Die Sektionstabelle wird gefüllt und die Sektionsvorschau mit dem Namen **OutlineDraw** angezeigt. Gewöhnlich wurden weitere Abschnitte an Bug und Heck hinzugefügt, wo komplexere Krümmungen registriert werden, um es zu tun, gehe zum Ende der Tabelle, und mache den *Doppelklick* auf ein leeres Element, um es zu bearbeiten, drücke Intro zur Bestätigung. Folgende Abschnitte hinzufügen:

-   X~22~ = -12.1125 m
-   X~23~ = 12.1125 m

Je nach Komplexität der Rumpfgeometrie kann die Vorschau der Schnitte einige Zeit in Anspruch nehmen. Um einen Abschnitt zu entfernen, fülle ihn einfach mit einem leeren Text und drücke die Eingabetaste.

### Längsschnitte

Es müssen zwei Längsschnitte hinzugefügt werden, wähle also **Längsschnitte**, gehe in das Feld **Automatisch erstellen** und stelle **2** Abschnitte ein und drücke dann **Abschnitte erstellen**. Die Sektionstabelle wird gefüllt und die Sektionsvorschau aktualisiert.

### Wasserlinien

6 Wasserlinien zwischen Grundlinie und Konstruktionsentwurf müssen hinzugefügt werden, wähle also **Wasserlinien** Art der Abschnitte, gehe zum Feld *\'Automatisch erstellen* und stelle **5** ein (Z = 0 m wird nicht berücksichtigt, füge es manuell hinzu, wenn du es benötigst) Abschnitte, dann drücke **Abschnitte erstellen**. Die Schnitttabelle wird gefüllt und die Schnittvorschau aktualisiert.

Weitere zusätzliche Wasserlinien müssen hinzugefügt werden:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m

### Plot ausführen 

Wähle den Maßstab **1:100** und drücke **Accept**, damit das Werkzeug die 3D Schnitte in einem neuen Objekt erzeugt.

![Resultierende Schnitte.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Resultierende Schnitte.


</center>

Zum Plotten dieser Schnitte kannst du die [Arbeitsbereich Zeichnung](Drawing_Workbench/de.md) verwenden:

![Umrisszeichnungsplot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Umrisszeichnungsplot.


</center>

## Tutorien

-   [FreeCAD Schiffs s60 Tutorium](FreeCAD-Ship_s60_tutorial/de.md)
-   [FreeCAD Schiffs s60 Tutorium (II)](FreeCAD-Ship_s60_tutorial_(II)/de.md)





{{Ship_Tools_navi

}}  
