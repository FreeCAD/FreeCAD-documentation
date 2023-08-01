---
- GuiCommand:/de
   Name:PartDesign Sprocket
   Name/de:PartDesign Kettenrad
   MenuLocation:Part Design → Kettenrad...
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.19
---

# PartDesign Sprocket/de

## Beschreibung

Mit diesem Werkzeug kann ein 2D-Profil eines Kettenrads (oder Ritzels) erstellt werden. Es kann mit der Funktion [PartDesign Aufpolsterung](PartDesign_Pad/de.md) extrudiert werden.

## Anwendung

1.  Bei Bedarf den richtigen Körper auswählen.

2.  Den Menüeintrag **Part Design → [<img src=images/PartDesign_Sprocket.svg style="width:24px"> Sprocket...** auswählen.

3.  Die {{PropertyData/de|Number Of Teeth}} und die {{PropertyData/de|Sprocket Reference}} festlegen.

4.  
    **OK**klicken.

5.  Wenn es keinen aktiven Körper gibt: Das Kettenrad zur Anwendung weiterer Formelemente wie Aufpolsterung auf einen Körper ziehen.

## Eigenschaften

-    **Anzahl der Zähne**: Anzahl der Zähne

-    **Kettenrad Referenz**: Der Kettenradtyp. Eine Liste von Kettenraddefinitionen. {{Version/de|0.20}} Die Liste enthält ANSI- und ISO-Normen sowie einige Fahrrad- und Motorrad Kettenraddefinitionen.

-    **Zahnteilung**: Abstand zwischen zwei Zähnen

-    **Rollendurchmesser**: Durchmesser der Kettenrollen, für die das Kettenrad ausgelegt ist

-    **Dicke**:Die Hauptdicke des Kettenrads. **Hinweis:** Das Kettenrad kann nicht einfach mit dieser Dicke aufgefüllt werden, da die Zähne seitliche Fasen haben. Schau daher die Kettenraddefinition an, um ein gültiges 3D Kettenrad zu modellieren. {{Version/de|0.20}}





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Sprocket/de
