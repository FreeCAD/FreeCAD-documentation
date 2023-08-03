---
 GuiCommand:Addon/de
   Name: BIM IfcQuantities
   Name/de: BIM IfcGrößen
   Workbenches: Image:IFC.svg BIM Workbench/de
   Addon: BIM
   MenuLocation: Verwalten , IFC GRößen
   SeeAlso: BIM IfcElements/de,BIM IfcQuantities/de
---

# BIM IfcQuantities/de

## Beschreibung

<img alt="" src=images/BIM_ifcquantities_screenshot.png  style="width:1024px;">

Mit dem IFC Größenverwalter kannst du die **expliziten Größen** überprüfen, die an Objekte angehängt sind, die nach IFC exportiert werden sollen.

Das IFC Format erlaubt es, für jedes Objekt explizite Größen anzugeben, z. B. \"Breite\", \"Höhe\" oder \"Fläche\". Es gibt keinen Standard, der definiert, welcher Objekttyp welche Art von Größe enthalten muss, und es gibt auch keine Garantie, dass solche expliziten Größen tatsächlich die Geometrie des Objekts widerspiegeln. Mit anderen Worten: Diese Größen könnten falsche Werte haben oder sogar lügen. Eine Wand könnte ihre Geometrie als Würfel mit einer Länge von 10 Metern haben, aber eine angehängte \"Länge\" Größe von 8 Metern haben.

Die Idee hinter expliziten Größen ist, sie für Anwendungen verfügbar zu machen, die keine Geometrie lesen können, wie z. B. eine Tabellenkalkulationsanwendung. Eine solche Anwendung könnte sich beim Lesen einer IFC Datei mit expliziten Größen trotzdem ein Bild von den Abmessungen eines Objekts machen und diese z.B. für Größenberechnungen verwenden.

Beim Exportieren einer IFC Datei aus FreeCAD werden standardmäßig keine expliziten Größen exportiert. Mit dem IFC Größenverwalter kannst du markieren, welche Größen exportiert werden sollen, und deren Werte überprüfen. Neben Nullwerten werden Warnzeichen angezeigt, die dich auf mögliche Probleme hinweisen, die du vor dem Exportieren beheben solltest.

Du kannst auch den Größenmanager verwenden, um die tatsächlichen **Höhe**, **Breite** und **Länge** Werte von Objekten zu ändern oder zu fixieren. Dies hat jedoch Auswirkungen auf die Objektgeometrie in FreeCAD.



---
⏵ [documentation index](../README.md) > BIM IfcQuantities/de
