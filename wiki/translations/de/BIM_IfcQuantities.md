---
 GuiCommand:
   Name: BIM IfcQuantities
   Name/de: BIM IfcGrößen
   MenuLocation: Manage , Manage IFC quantities...
   Workbenches: BIM_Workbench/de
---

# BIM IfcQuantities/de



## Beschreibung

Der Dialog **IFC Quantities Manager** ermöglicht die **expliziten Größen** zu überprüfen, die Objekten zugeordnet sind, die nach IFC exportiert werden sollen.

<img alt="" src=images/BIM_ifcquantities_screenshot.png  style="width:600px;"> 
*IFC Quantities Manager*

Das IFC-Format erlaubt es, für jedes Objekt explizite Größen anzugeben, z. B. \"Breite\", \"Höhe\" oder \"Fläche\". Es gibt keinen Standard, der definiert, welcher Objekttyp welche Art von Größe enthalten muss, und es gibt auch keine Garantie, dass solche expliziten Größen tatsächlich die Geometrie des Objekts widerspiegeln. Mit anderen Worten: Diese Größen könnten falsche Werte haben oder sogar lügen. Eine Wand könnte ihre Geometrie als Würfel mit einer Länge von 10 Metern haben, aber eine zugeordnete Größe \"Länge\" von 8 Metern haben.

Die Idee hinter expliziten Größen ist, sie für Anwendungen verfügbar zu machen, die keine Geometrie lesen können, wie z. B. eine Tabellenkalkulationsanwendung. Eine solche Anwendung könnte sich beim Lesen einer IFC-Datei mit expliziten Größen trotzdem ein Bild von den Abmessungen eines Objekts machen und diese z.B. für Mengenberechnungen verwenden.

Beim Exportieren einer IFC-Datei aus FreeCAD werden standardmäßig keine expliziten Größen exportiert. Mit dem IFC-Größenverwalter kann markiert werden, welche Größen exportiert werden, und deren Werte überprüft werden sollen. Neben Nullwerten werden Warnzeichen angezeigt, die auf mögliche Probleme hinweisen, die vor dem Exportieren behoben werden sollten.

Der Größenmanager kann auch dazu verwendet werden, die tatsächlichen Werte **Höhe**, **Breite** und **Länge** von Objekten zu ändern oder festzulegen. Dies hat jedoch Auswirkungen auf die Objektgeometrie in FreeCAD.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM IfcQuantities/de
