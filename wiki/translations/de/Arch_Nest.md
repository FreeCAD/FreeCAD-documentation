---
 GuiCommand:
   Name: Arch Nest
   Name/de: Arch Verschachteln
   MenuLocation:  Utils , Plattenwerkzeuge , Verschachteln
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_Panel/de, Arch_Panel_Sheet/de
---

# Arch Nest/de



## Beschreibung

Das Werkzeug **Arch Verschachteln** ermöglicht die Auswahl einer ebenen Form (Flächenobjekt) als Behälter und einer Reihe anderer ebener Formen, die innerhalb der Fläche angeordnet werden sollen, die die Behälterform vorgibt. Dies ist in der Regel für CNC-Bearbeitungen erforderlich, bei denen eine Reihe von Teilen aus einer Grundplatte (Tafel) ausgeschnitten werden, um diese Teile so kompakt wie möglich anzuordnen, damit sie weniger Platz auf der Grundplatte einnehmen.

Der Algorithmus hinter dem Verschachtelungswerkzeug befindet sich in ständiger Entwicklung und ist derzeit noch nicht vollständig optimiert. In der Zukunft sollte die Leistung dieses Werkzeugs viel besser werden.

<img alt="" src=images/Arch_Nest_example.jpg  style="width:600px;">

*Das obige Bild zeigt eine Reihe von Formen vor und nach dem Verschachtelungsvorgang.*



## Anwendung

1.  Den Menüeintrag **Utils → Plattenwerkzeuge → <img src="images/Arch_Nest.svg" width=16px> Verschachteln** auswählen.
2.  Ein ebenes Flächenobjekt als Behälter (Container) auswählen. Dieses Objekt muss aktuell noch rechteckig sein.
3.  Auf die Schaltfläche **Auswahl hinzufügen** klicken, um dieses Objekt als Container zu verwenden.
4.  Eine Reihe anderer ebener Flächenobjekte auswählen, die im Behälter platziert werden sollen. Diese Objekte müssen sich alle in derselben Ebene wie der Behälter befinden.
5.  Die gewünschten Optionen unten einstellen.
6.  Den Berechnungsvorgang starten.
7.  Klicke am Ende der Berechnung auf die Schaltfläche **Vorschau**, um eine temporäre Ergebnisvorschau zu erhalten.
8.  Soll das Ergebnis angewendet werden (die tatsächlichen Formen auf ihren neuen Platz verschoben und gedreht werden), Schaltfläche **OK** drücken.

<img alt="" src=images/Arch_Nest_panel.jpg  style="width:800px;"> 
*Aufgaben-Bereich für das Werkzeug [Arch Verschachteln](Arch_Nest/de.md)*



## Hinweise

-   Alle Objekte müssen aus einer Fläche bestehen.
-   Im Moment arbeitet das Werkzeug nur mit ebenen Objekten, die alle gleich ausgerichtet sind.
-   Im Moment muss der Behälter rechteckig sein.
-   Im Moment ist ein Rand/Abstand zwischen den Teilen noch nicht implementiert.
-   Die Berechnung kann bei vielen Objekten sehr viel Zeit in Anspruch nehmen. Das wird in Zukunft optimiert werden.



---
⏵ [documentation index](../README.md) > Arch Nest/de
