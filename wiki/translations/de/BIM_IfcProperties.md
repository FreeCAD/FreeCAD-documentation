---
- GuiCommand:Addon/de
   Name:BIM IfcProperties
   Name/de:BIM IfcEigenschaften
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench/de.md)
   Addon:BIM
   MenuLocation:Verwalten → IFC Eigenschaften
   SeeAlso:[BIM IfcElemente](BIM_IfcElements/de.md),[BIM IfcGrößen](BIM_IfcQuantities/de.md)
---

## Beschreibung

<img alt="" src=images/BIM_ifcproperties_screenshot.png  style="width:1024px;">

Der IFC Eigenschaften Verwalter erlaubt dir die IFC Eigenschaften eines ausgewählten Objekts, vieler ausgewählter Objekte oder aller Objekte des Dokuments zu bearbeiten. IFC Eigenschaften sind Informationen, die an einzelne Objekte angehängt sind. Sie können nur an [BIM Objekte](BIM_Workbench/de.md) angehängt werden, daher muss jedes Nicht BIM Objekt zunächst über das Menü **3D/BIM -\> Komponente erstellen** in ein BIM Objekt umgewandelt werden, bevor es IFC Eigenschaften enthalten kann.

IFC Eigenschaften können benutzerdefiniert sein, d. h., du kannst einen eigenen Namen und einen eigenen Wert für sie definieren, oder sie folgen einem voreingestellten Schema, das durch den IFC Standard definiert ist. Diese Eigenschaften sind in **Eigenschaftssätzen** definiert und werden in der Regel für die gängigsten IFC Typen zur Verfügung gestellt. Zum Beispiel ist der Eigenschaftssatz **Pset\_BeamCommon** für Träger vorgesehen. Vordefinierte Eigenschaftssätze enthalten in der Regel übliche Eigenschaften, die das IFC Schema für einen bestimmten Typ definiert hat. So enthält z. B. der Eigenschaftssatz *Pset\_WallCommon*, der an Wände angehängt werden soll, Eigenschaften, die definieren, ob die Wand tragend ist oder außen bzw. innen liegt.

Du kannst deine eigenen Eigenschaften und Eigenschaftssätze erstellen und sie jedem Objekt zuweisen. Es gibt im IFC Schema keine Vorgabe, vordefinierte Psets für gängige Typen hinzuzufügen, und auch keine Begrenzung für das Hinzufügen eigener Eigenschaften. Dies ist eine Entscheidung, die den Benutzern überlassen wird. Normalerweise werden diese Dinge bei der Arbeit im Team zusammen mit anderen BIM Anforderungen entschieden, um sicherzustellen, dass alle produzierten BIM Modelle die gleichen Anforderungen erfüllen.

### Eigene Eigenschaftssätze definieren {#eigene_eigenschaftssätze_definieren}

Die verfügbaren Eigenschaftssätze, die im IFC Standard vordefiniert sind, werden in einer [csv Datei, die mit FreeCAD gebündelt ist](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/pset_definitions.csv) gespeichert. Du kannst auch eine benutzerdefinierte csv Datei mit deinen eigenen Eigenschaftssätzen hinzufügen. Diese Datei muss CustomPsets.csv heißen und in \$USERAPPDATA/BIM abgelegt werden.

Der \$USERAPPDATA Ordner hängt von deiner Plattform/deinem Betriebssystem ab (normalerweise \$HOME/.FreeCAD auf linux/mac, /users/YOUR USER/Application Data/roaming/FreeCAD auf windows) und kann auch durch Eingabe in der FreeCAD Python Konsole gefunden werden:

FreeCAD.getUserAppDataDir()

In der CSV Datei steht jede Zeile für einen anderen Eigenschaftssatz, beginnend mit dem Namen des Satzes und einer beliebigen Anzahl von Name;Typ Paaren, die einen Eigenschaftsnamen und seinen [Typ](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/ifc_types_IFC4.json) definieren. Zum Beispiel:

Pset_FreeCAD;Name;IfcLabel;Version;IfcReal

würde einen Eigenschaftssatz mit dem Namen \"FreeCAD\" definieren (das Präfix Pset\_ ist nicht obligatorisch, aber üblich), der zwei Eigenschaften enthält: eine namens \"Name\", die ein IfcLabel (ein Text) ist, und eine andere namens \"Version\", die ein IfcReal (ein numerischer Wert mit Dezimalstellen) ist
