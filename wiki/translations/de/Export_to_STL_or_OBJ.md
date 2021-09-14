# Export to STL or OBJ/de




{{TutorialInfo/de
|Topic= Export nach STL oder OBJ
|Level=Anfänger
|Time=20 Minuten
|Author=r-frank
|FCVersion=0.16.6703
}}

## Einführung

In diesem Tutorial werden wir beschreiben, wie man STL/OBJ-Dateien aus FreeCAD exportiert. Da das Mesh-Format STL/OBJ dimensionslos ist, geht FreeCAD beim Export davon aus, dass die im Modell benutzen Einheiten in mm sind. Falls dies nicht der Fall sein sollte, muss das Modell entsprechend skaliert werden. Ein Weg dazu ist die Nutzung von <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Draft Skalieren](Draft_Scale/de.md).

## Beispiel-Teil 

Natürlich kann ein eigenes Modell verwendet werden, aber man kann sich auch schnell ein Modell zum Testen erstellen, indem man

-   FreeCAD startet
-   Ein neues Dokument erstellt
-   Zum <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part-Arbeitsbereich](Part_Workbench/de.md) wechselt
-   Einen Würfel einfügt durch Klick auf <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Part Würfel](Part_Box/de.md)
-   Einen Kegel einfügt durch Klick auf <img alt="" src=images/Part_Cone.png  style="width:32px;"> [Part Kegel](Part_Cone/de.md)
-   Beide Objekte in der [Baumansicht](Tree_view/de.md) auswählt
-   Eine bool\'sche Verschmelzung erzeugt durch Klick auf <img alt="" src=images/Part_Fuse.png  style="width:32px;"> [Part Vereinigung](Part_Fuse/de.md)
-   Danach die Datei speichert \...

## Export-Methode 1: Benutzung von \"Datei → Exportieren\" 

-   Den zu exportierenden Körper in der Baumansicht auswählen
-   Wähle **Datei** → **Exportieren...** und setze den Dateityp auf \"STL mesh (\*.stl \*.ast)\"
-   Gib den Dateinamen ein. Die Standarddateiendung ist \".stl.\". Für die Erzeugung einer .ast-Datei ist sie auf \".ast\" zu ändern. Klicke auf ** Speichern**.

## Export-Methode 2: Benutzung des Mesh-Design-Arbeitsbereichs in FreeCAD 

-   Wechsle in den [Mesh Design-Arbeitsbereich](Mesh_Workbench/de.md)
-   Wähle den zu vernetzenden Körper in der Baumansicht aus
-   Wähle ** Netze** → **<img src="images/Mesh_Mesh_from_Shape.svg" width=32px> Netz aus Form erstellen...** aus dem obersten Menü aus
-   Wähle einen der drei verfügbaren Vernetzer und wähle die Vernetzungs-Parameter, für weitere Informationen siehe [diese Seite (Netz aus Körpern)](Mesh_FromPartShape/de.md)
-   Wähle **OK** und der Netzkörper wird in der Baumansicht erstellt (mit einem grünen Netz-Icon)
-   Wähle den Netzkörper in der Baumansicht aus und mache einen Rechts-Klick auf den Eintrag
-   Wähle **<img src="images/Mesh_ExportMesh.png" width=32px> Exportiere Netz** um das Netz zu exportieren
-   Nun den Dateinamen festlegen (es wird der Name des Netzkörpers vorgeschlagen) und den Dateityp (Standard ist \"Binary STL (\*.stl)\")
-   Wähle **Speichern**

## Welche Methode sollte man wählen? 

Methode 2 ist zu bevorzugen: Wenn Du mehr als einen Body zu konvertieren hast, kannst Du Werkzeuge aus dem <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh-Arbeitsbereich](Mesh_Workbench/de.md) verwenden. Beispielweise kannst Du Netze vor dem Exportieren verschmelzen.

-   Gewölbte Oberflächen werden in STL als eine Reihe von geradlinigen Segmenten dargestellt, generiert durch Parkettierung (Tesselation). Dies resultiert in geringfügig zu kleinen inneren Abmessungen für gewölbte Oberflächen. In diesen Fällen kann ein feinerer Parkettierungswert helfen. Beim Exportieren aus anderen Arbeitsbereichen über **Datei** → **Export...** wird die Parkettierung über die Einstellungen in ** Bearbeiten** → **Einstellungen...** → Part design → Form-Ansicht → Tesselierung kontrolliert. Allerdings beeinflussen diese Parameter die Parkettierung bei der Anzeige von Formen, so dass Verringerungen zu einer Verlangsamung führen werden, oftmals spürbar. Außerdem hat ein Export direkt nach der Änderung der Parameter nicht den gewünschten Effekt, weil die Anzeige nicht sofort aktualisiert wird. Man muss eine Änderung im darunter liegenden Modell erzwingen, damit die Parkettierung aktualisiert wird - z.B. durch Anpassung eines Skizzenparameters (setzen auf den ursprünglichen Wert reicht aus).

## Verweise

-   [Import von STL or OBJ](Import_from_STL_or_OBJ/de.md)
-   [Import/Export](Import_Export/de.md)




[Category:File\_Formats](Category:File_Formats.md)
