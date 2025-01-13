# TechDraw Templates/de
## Beschreibung

Jedes TechDraw-Zeichnungsblatt (Page-Objekt) basiert auf einer Vorlage (Template-Objekt). Die Vorlage stellt die Hintergrundfläche eines Zeichnungsblattes zur Verfügung, in die Ansichten, Symbole und andere Beschriftungsobjekte eingefügt werden können und legt das Papierformat fest. Nur Elemente innerhalb dieser Zeichenfläche werden beim Exportieren oder Drucken ausgegeben.

Die Vorlage kann auch graphische Elemente enthalten, wie einen Rahmen, der die Zeichenfläche festlegt, inklusive Indexfeldern, Faltmarken und wahlweise einem Schriftfeld, das wiederum unveränderbare und [editierbare Texte](Svg_Namespace/de#freecad_editable.md) enthält. Das Schriftfeld kann auch als eigenständiges [Symbol](TechDraw_Symbol/de.md) eingefügt werden.

Die Vorlagen sind wie Symbole [SVG](SVG.md)-Dateien, die außerhalb von FreeCAD erstellt und geändert werden können, entweder mit einer Anwendung wie [Inkscape](https://de.wikipedia.org/wiki/Inkscape) oder mit einem einfachen Texteditor. Beide können editierbare Textfelder enthalten, verwenden aber unterschiedliche Werkzeuge zum Bearbeiten.

Ein neues Autofill-Werkzeug ({{Version/de|1.0}}) kann automatisch editierbare Textfelder in einer Vorlage ausfüllen, wenn sie eingefügt wird. Dies erfordert Vorlagen, die das neue Attribut [freecad:autofill](Svg_Namespace/de#freecad_autofill.md) verwenden. Die folgenden Attributnamen werden vom Autofill-Werkzeug berücksichtigt: \"author\", \"date\", \"organization\", \"scale\", \"sheet\", \"title\", \"page_number\", and \"page_count\".



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Template-Objekt besitzt die folgenden Eigenschaften:


{{TitleProperty|Basis}}

-    **Orientation|Enumeration**: {{Value|Portrait}} or {{Value|Landscape}}.


{{TitleProperty|Page Properties}}

-    **Width|Length**: Paper width in mm.

-    **Height|Length**: Paper height in mm.

-    **Editable Texts|Map|Hidden**: Key:Value list of editable texts in the template.


{{TitleProperty|Template}}

-    **Page Result|FileIncluded**: A copy of the original Template file including all changes to editable texts. This allows users who may not have a copy of the Template file to see the Page as intended. Not typically useful for end users.

-    **Template|File**: A pointer to the copy of the original Template file which is incorporated into this ***.FCStd** file, or a filepath to a template accessible on the current machine. See the [next paragraph](#Select_a_different_template_file.md) for information on how to change the Template.



## Eine andere Vorlagendatei auswählen 

Um eine andere Vorlage einer Zeichnung auszuwählen:

1.  Die gewünschte Seite in der [Baumansicht](Tree_view/de.md) ermitteln.
2.  Den Knoten des Zeichnungsblattes (Page-Objekt) aufklappen, wenn nötig.
3.  Die Vorlage (Template-Objekt) auswählen.
4.  Im [Eigenschafteneditor](Property_editor.md) in das Eingabefeld der {{PropertyData/de|Template}} klicken.
5.  Die Schaltfläche **...** (Ellipse) drücken, die erscheint.
6.  Ein Dateidialog öffnet das Verzeichnis, das die aktuelle Vorlage enthält. Wurde das Zeichnungsblatt in der laufenden FreeCAD-Sitzung erstellt, wird dies das Standard-Vorlagenverzeichnis sein (wie in den [TechDraw Einstellungen](TechDraw_Preferences/de#Dateien.md) gespeichert).
7.  Wahlweise zu einem anderen Verzeichnis wechseln.
8.  Eine andere Vorlagedatei auswählen.
9.  Die Schaltfläche **OK** drücken.

Wurde eine Vorlagendatei geändert und das dazugehörige Zeichnungsblatt, das in der aktuellen FreeCAD-Sitzung erstellt wurde, die diese Vorlage verwendet, soll aktualisiert werden, wählt man zuerst temporär eine andere Datei aus und dann wieder die geänderte Datei.



## Benutzerdefinierte Vorlagen 

Eine begrenzte Anzahl vorformatierter Vorlagen in verschiedenen Standardformaten (Blattgrößen) sind in FreeCAD enthalten. Diese sind zu finden in


```python
$INSTALL_DIR/Mod/TechDraw/Templates/
```

wobei `$INSTALL_DIR` das Verzeichnis ist, in dem FreeCAD installiert wurde, z.B.


```python
/usr/share/freecad/Mod/TechDraw/Templates/
```

Benutzerdefinierte Vorlagen können auch als Standard in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

Siehe auch [So wird eine benutzerdefinierte TechDraw Vorlage erstellt](TechDraw_TemplateHowTo/de.md) oder, wenn man skriptgenerierte Vorlagen bevorzugt, [TechDraw Vorlagengenerator](TechDraw_TemplateGenerator/de.md) und [Makro TemplateHelper](Macro_TemplateHelper/de.md).



## Hinweise

-   Die von FreeCAD verwendete Bibliothek zum Verarbeiten von SVG-Daten **unterstützt nur die SVG-Tiny Spezifikation**. Im Besonderen: \"SVG Tiny does not support gradients, transparency, clipping, masks, symbols, patterns, underline text, strike through text, vertical text, or SVG filter effects.\" (from Adobe Illustrator Help), also Farbverläufe, Transparenz, Ausschnitte, Masken, Symbole, Schraffurmuster, unterstrichenen Text, durchgestrichenen Text, vertikalen Text oder SVG-Filtereffekte. Werden diese Elemente in selbsterstellten Vorlagen verwendet, führen sie zu Darstellungsproblemen.

-   Svg-Transformationsanweisungen in benutzerdefinierten Vorlagen **können Probleme verursachen**, siehe eine Stackoverflow-Diskussion unter [removing transform clauses in SVG files](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files) (engl.), hauptsächlich wenn Inkscape zu viele von ihnen einsetzt. Aber sie lassen sich nicht verhindern, wenn gedrehter Text in der Vorlage erforderlich ist.

-   Die Anweisung **xml:space=\"preserve\"** verursacht manchmal Probleme mit der Textgröße und -positionierung. Es ist am besten, diese Anweisung zu vermeiden bzw. aus dem SVG-Code der benutzerdefinierten Vorlage entfernen.

-   Vorlagen funktionieren am besten, wenn sie keinen überflüssigen SVG-Code enthalten (von manchen als \"SVG-Müll\" bezeichnet). Es gibt einen guten Artikel über [Entfernen von Müll aus SVG hier](https://freecad-gost.ru/news/gost-templates-techdraw-09-01-2020/). Der Artikel ist auf Russisch.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Templates/de
