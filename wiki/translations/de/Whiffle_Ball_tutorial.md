# Whiffle Ball tutorial/de
---
 TutorialInfo:e
   Topic: Produktgestaltung
   Level: Anfänger
   Time: 30 min
   Author: r-frank und vocx
   FCVersion: 0.17 und höher
   Files: https://github.com/FreeCAD/Examples/blob/master/Whiffle_Ball_Tutorial_ExampleFiles/WhiffleBall_Tutorial_FCWiki.FCStd?raw=true WhiffleBall_Tutorial_FCWiki.FCStd
}}



## Einleitung

Diese Anleitung wurde ursprünglich von Roland Frank  verfasst und  von vocx überarbeitet und illustriert.

Diese Anleitung soll vermitteln, wie man den Arbeitsbereich Part verwendet.

Der Arbeitsbereich Part war der Arbeitsbereich, der zuerst entwickelt wurde. Er stellt die grundlegenden geometrischen Elemente zur Verfügung, die als Bausteine für andere Arbeitsbereiche verwendet werden können. Der Arbeitsbereich Part ist für die Verwendung in einem herkömmlichen Arbeitsablauf für konstruktive Festkörpergeometrie  gedacht. Für einen moderneren Arbeitsablauf mit Skizzen, Blöcken und Formelementen wird der Arbeitsbereich PartDesign verwendet.

Geübt wird:

-   Grundelemente  einfügen
-   Parameter dieser Grundelemente anpassen
-   Ihre Positionierung ändern
-   Boolesche Verknüpfungen anwenden

! 
*Endgültiges Modell des Wiffleballs*



## Einrichtung

1\. FreeCAD öfnen, ein neues leeres Dokument mit **Datei , File:Std_New.svg   16px Std_New/de**{: mediawiki} erstellen und zum Arbeitsbereich Part wechseln.

:   1.1. Die Schaltfläche **File:Std_ViewIsometric.svg   16px Std_ViewIsometric/de**{: mediawiki} drücken oder **0** auf dem Ziffernblock der Tastatur, um die Ansicht auf isometrisch zu ändern, für eine bessere Darstellung der 3D-Festkörper.
:   1.2. Die Schaltfläche **File:Std_ViewFitAll.svg   16px Std_ViewFitAll/de**{: mediawiki} drücken, wann immer Objekte hinzugefügt werden, um die 3D-Ansicht so zu schwenken und zoomen, dass alle Elemente in der Ansicht zu sehen sind.
:   1.3. **Strg** gedrückt halten, um mehrere Elemente durch Anklicken auszuwählen. Wurde etwas falsch ausgewählt oder soll die Auswahl aufgehoben werden, klickt man einfach auf einen leeren Bereich in der 3D-Ansicht.



## Würfel-Grundelemente einfügen 

2\. Ein Würfel-Grundelement einfügen durch Anklicken der Schaltfläche **Image:Part_Box.svg   16px Part_Box/de**{: mediawiki}.

:   2.1. {{incode   Quader}}{: mediawiki} in der Baumansicht auswählen.
:   2.2. Die Abmessungen im Reiter **Daten** des Eigenschafteneditors anpassen.
:   2.3. **Length**  auf {{incode   90 mm}}{: mediawiki} ändern.
:   2.4. **Width**  auf {{incode   90 mm}}{: mediawiki} ändern.
:   2.5. **Height**  auf {{incode   90 mm}}{: mediawiki} ändern.

3\. Im Reiter **Daten** des Eigenschafteneditors den Wert von **Placement** anklicken, damit rechts die Taste **...**  erscheint.

:   3.1. Das Auslassungszeichen drücken, um den Dialog Positionierung zu öffnen.
:   3.2. Die Werte für die **Verschiebung** anpassen.
:   3.3. **X** auf {{incode   -45 mm}}{: mediawiki} ändern.
:   3.4. **Y** auf {{incode   -45 mm}}{: mediawiki} ändern.
:   3.5. **Z** auf {{incode   -45 mm}}{: mediawiki} ändern.
:   3.6. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.

4\. Den Vorgang wiederholen, um einen zweiten, kleineren Würfel einzufügen, durch Anklicken der Schaltfläche **Image:Part_Box.svg   16px Part_Box/de**{: mediawiki}.

:   4.1. Der zweite Quader wird mit dem gleichen Namen, aber mit einer zusätzlichen Nummer zum Unterscheiden der Objekte erstellt.
:   4.2. {{incode   Quader001}}{: mediawiki} in der Baumansicht auswählen und die Abmessungen sowie die Positionierung wie beim vorherigen Objekt anpassen.
:   4.3. **Length**  auf {{incode   80 mm}}{: mediawiki} ändern.
:   4.4. **Width**  auf {{incode   80 mm}}{: mediawiki} ändern.
:   4.5. **Height**  auf {{incode   80 mm}}{: mediawiki} ändern.
:   4.6. Den Dialog Positionierung öffnen.
:   4.7. **X** auf {{incode   -40 mm}}{: mediawiki} ändern.
:   4.8. **Y** auf {{incode   -40 mm}}{: mediawiki} ändern.
:   4.9. **Z** auf {{incode   -40 mm}}{: mediawiki} ändern.
:   4.10. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.



## Visuelle Eigenschaften anpassen 

5\. Die vorigen Operationen erstellen einen kleineren Würfel in einem größeren Würfel. Um dies zu veranschaulichen, können wir die **Ansicht**-Eigenschaften im Eigenschafteneditor ändern.

:   5.1. {{incode   Quader001}}{: mediawiki}, den kleineren Würfel in der Baumansicht auswählen und die Farbe ändern. Dafür im Reiter **Ansicht** auf den Wert von **Shape Color**  klicken, um den Dialog **Farbauswahl** zu öffnen und darin einen grünen Farbton auswählen; auch den Wert von **Line Width**  auf {{incode   2.0}}{: mediawiki} ändern.
:   5.2. {{incode   Quader}}{: mediawiki}, den größeren Würfel, in der Baumansicht auswählen. Im Reiter **Ansicht** den Wert von **Transparency**  auf {{incode   70}}{: mediawiki} ändern.

! 
*Ein Festkörper-Würfel innerhalb eines anderen  Festkörper-Würfels*



## Zylinder-Grundelemente einfügen 

6\. Ein Zylinder-Grundelement einfügen durch Anklicken der Schaltfläche **Image:Part_Cylinder.svg   16px Part_Cylinder/de**{: mediawiki}.

:   6.1. {{incode   Zylinder}}{: mediawiki} in der Baumansicht auswählen.
:   6.2. Die Abmessungen im Reiter **Daten** des Eigenschafteneditors anpassen.
:   6.3. **Radius** auf {{incode   27,5 mm}}{: mediawiki} ändern.
:   6.4. **Height**  auf {{incode   120 mm}}{: mediawiki} ändern.
:   6.5. Den Dialog Positionierung öffnen.
:   6.6. **Z** auf {{incode   -60 mm}}{: mediawiki} ändern.
:   6.7. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.

7\. Den Vorgang wiederholen, um einen zweiten Zylinder einzufügen, durch Anklicken der Schaltfläche **Image:Part_Cylinder.svg   16px Part_Cylinder/de**{: mediawiki}.

:   7.1. Der zweite Zylinder wird mit dem gleichen Namen, aber mit einer zusätzlichen Nummer zum Unterscheiden der Objekte erstellt.
:   7.2. {{incode   Zylinder001}}{: mediawiki} in der Baumansicht auswählen und die Abmessungen sowie die Positionierung wie beim vorherigen Objekt anpassen.
:   7.3. **Radius** auf {{incode   27.5 mm}}{: mediawiki} ändern.
:   7.4. **Height**  auf {{incode   120 mm}}{: mediawiki} ändern.
:   7.5. Den Dialog Positionierung öffnen.
:   7.6. **Y** auf {{incode   60 mm}}{: mediawiki} ändern.
:   7.7. Unter **Drehung** {{incode   Rotationsachse mit Winkel}}{: mediawiki} einstellen; **X-Achse** festlegen  und **Angle**  auf {{incode   90 °}}{: mediawiki} ändern.
:   7.8. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.

8\. Einen weiteren Zylinder einzufügen. Diesmal wird ein Duplikat erstellt, damit Radius und Höhe nicht geändert werden müssen, sondern nur seine Positionierung.

:   8.1. {{incode   Zylinder001}}{: mediawiki} in der Baumansicht auswählen und danach den Menüeintrag **Bearbeiten , Std_DuplicateSelection/de   Auswahl duplizieren**{: mediawiki}. Dies erstellt {{incode   Zylinder002}}{: mediawiki}.
:   8.2. Den Dialog Positionierung öffnen.
:   8.3. **X** auf {{incode   -60 mm}}{: mediawiki} und **Y** zurück auf {{incode   0 mm}}{: mediawiki} ändern.
:   8.4. Unter **Drehung** {{incode   Rotationsachse mit Winkel}}{: mediawiki} einstellen; **Y-Achse** festlegen und **Angle**  auf {{incode   90 °}}{: mediawiki} ändern.
:   8.5. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.



## Visuelle Eigenschaften anpassen 

9\. Die vorigen Operationen erstellen drei Zylinder, die sich gegenseitig durchdringen und auch die Würfel durchdringen. Um dies zu veranschaulichen, können wir die **Ansicht**-Eigenschaften im Eigenschafteneditor ändern.

:   9.1. {{incode   Quader001}}{: mediawiki}, den kleineren Würfel in der Baumansicht auswählen und die Transparennz ändern. Im Reiter **Ansicht** den Wert von **Transparency**  auf {{incode   70}}{: mediawiki} ändern.
:   9.2. {{incode   Zylinder}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Shape Color**  anklicken, um den Dialog **Farbauswahl** zu öffnen und einen roten Farbton auszuwählen.
:   9.3. {{incode   Zylinder001}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Shape Color** anklicken, um den Dialog **Farbauswahl** zu öffnen und einen blauen Farbton auszuwählen.
:   9.4. {{incode   Zylinder002}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Shape Color** anklicken, um den Dialog **Farbauswahl** zu öffnen und einen rosafarbenen Farbton auszuwählen.
:   9.5. Alle drei Zylinder auswählen und im Reiter **Ansicht** auch hier **Line Width**  auf {{incode   2,0}}{: mediawiki} ändern.

! 
*Festkörper-Zylinder, die sich selbst durchdringen und die Festkörper-Würfel*



## Vereinigen und Ausschneiden 

10\. In der Baumansicht {{incode   Quader001}}{: mediawiki} , und die drei Zylinder auswählen und danach die Schaltfläche **File:Part_Fuse.svg   16px Part_Fuse/de**{: mediawiki} drücken. Dies erstellt ein Vereinigungsobjekt {{incode   Fusion}}{: mediawiki}.

11\. Dann wird die boolesche Verknüpfung Differenz angewendet, um das neue Objekt {{incode   Fusion}}{: mediawiki} aus den größeren Würfel {{incode   Quader}}{: mediawiki} herauszuschneiden.

:   11.1. In der Baumansicht zuerst {{incode   Quader}}{: mediawiki} auswählen und dann {{incode   Fusion}}{: mediawiki}.
:   11.2. Danach die Schaltfläche **File:Part_Cut.svg   16px Part_Cut/de**{: mediawiki} drücken. Dies erstellt ein Differenzobjekt {{incode   Cut}}{: mediawiki}.
:   
    **Hinweis:**Die Reihenfolge, in der die Objekte ausgewählt werden, ist entscheidend für diesen Vorgang. Das Basisobjekt wird zuerst ausgewählt und danach die Objekte, die etwas entfernen .
:   11.3. Wenn die Farben nicht gefallen, das neue Objekt {{incode   Cut}}{: mediawiki} auswählen, zum Reiter **Ansicht** wechseln, Den Wert von **Shape Color** anklicken, um den Dialog **Farbauswahl** zu öffnen und einen grauen Farbton auszuwählen; auch hier den Wert von **Line Width** auf {{incode   2.0}}{: mediawiki} ändern.

! 
*Hohle Form, hergestellt durch Entfernen eines Würfels und dreier Zylinder aus einem größeren Würfel.*



## Würfel-Grundelemente einfügen, um die Ecken des Teilkörpers zu beschneiden 

Jetzt werden weitere Würfel erstellt, die als Beschnittwerkzeuge für die Ecken des zuvor erstellten Objekts {{incode   Cut}}{: mediawiki} verwendet werden.

12\. Die Schaltfläche **Image:Part_Box.svg   16px Part_Box/de**{: mediawiki} drücken.

:   12.1. {{incode   Quader002}}{: mediawiki} in der Baumansicht auswählen und Abmessungen ung Positionierung anpassen.
:   12.2. **Length** auf {{incode   140 mm}}{: mediawiki} ändern.
:   12.3. **Width** auf {{incode   112 mm}}{: mediawiki} ändern.
:   12.4. **Height** auf {{incode   112 mm}}{: mediawiki} ändern.
:   12.5. Den Dialog Positionierung öffnen.
:   12.6. **X** auf {{incode   -70 mm}}{: mediawiki} ändern.
:   12.7. **Y** auf {{incode   -56 mm}}{: mediawiki} ändern.
:   12.8. **Z** auf {{incode   -56 mm}}{: mediawiki} ändern.
:   12.9. Die Schaltfläche **OK** drücken.

13\. Die Schaltfläche **Image:Part_Box.svg   16px Part_Box/de**{: mediawiki} drücken.

:   13.1. {{incode   Quader003}}{: mediawiki} in der Baumansicht auswählen und Abmessungen ung Positionierung anpassen.
:   13.2. **Length** auf {{incode   180 mm}}{: mediawiki} ändern.
:   13.3. **Width** auf {{incode   180 mm}}{: mediawiki} ändern.
:   13.4. **Height** auf {{incode   180 mm}}{: mediawiki} ändern.
:   13.5. Den Dialog Positionierung öffnen.
:   13.6. **X** auf {{incode   -90 mm}}{: mediawiki} ändern.
:   13.7. **Y** auf {{incode   -90 mm}}{: mediawiki} ändern.
:   13.8. **Z** auf {{incode   -90 mm}}{: mediawiki} ändern.
:   13.9. Die Schaltfläche **OK** drücken.

Die beiden vorherigen Objekte werden wieder dupliziert, um sie auch wieder als Beschnittobjekte zu verwenden.

14\. Nur {{incode   Quader002}}{: mediawiki} in der Baumansicht auswählen und danach den Menüeintrag **Bearbeiten , Std_DuplicateSelection/de   Auswahl duplizieren**{: mediawiki}. Dies erstellt {{incode   Quader004}}{: mediawiki}.

14\. Nur {{incode   Quader003}}{: mediawiki} in der Baumansicht auswählen und danach den Menüeintrag **Bearbeiten , Std_DuplicateSelection/de   Auswahl duplizieren**{: mediawiki}. Dies erstellt {{incode   Quader005}}{: mediawiki}.

16\. Um dies zu veranschaulichen, können wir die **Ansicht**-Eigenschaften im Eigenschafteneditor ändern.

:   16.1. Das Objekt {{incode   Cut}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Shape Color** anklicken, um den Dialog **Farbauswahl** zu öffnen und einen blauen Farbton auszuwählen.
:   16.2. Alle neuen Würfel, {{incode   Quader002}}{: mediawiki}, {{incode   Quader003}}{: mediawiki}, {{incode   Quader004}}{: mediawiki} und {{incode   Quader005}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Transparency** auf {{incode   80}}{: mediawiki} ändern.

! 
*Weitere äußere Würfel, die als Beschnittobjekte für den inneren Festkörper verwendet werden*



## Beschneiden der Ecken 1 

17\. In der Baumansicht {{incode   Cube002}}{: mediawiki} und {{incode   Cube003}}{: mediawiki} auswählen.

:   17.1. Den Dialog Positionierung öffnen.
:   17.2. Die Option **Inkrementelle Änderungen anwenden** aktivieren; man beachte, dass alle Werte unter **Verschiebung** auf Null zurückgesetzt werden
:   17.3. Unter **Drehung** {{incode   Rotationsachse mit Winkel}}{: mediawiki} einstellen; **X-Achse** festlegen und **Angle**  auf {{incode   45 °}}{: mediawiki} ändern; danach die Schaltfläche **Anwenden** drücken. Dies wendet eine Drehung um die X-Achse an und setzt den Wert des Feldes **Angle** auf Null zurück.
:   17.4. Noch einmal **Drehung** einstellen, jetzt die **Z-Achse** festlegen und **Angle** auf {{incode   45 °}}{: mediawiki} ändern; danach die Schaltfläche **Anwenden** drücken. Dies wendet eine Drehung um die lokale Z-Achse an und setzt den Wert des Feldes **Angle** auf Null zurück.
:   17.5. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.

18\. In der Baumansicht alle Objekte abwählen, dann zuerst {{incode   Quader003}}{: mediawiki}, den größeren Würfel, auswählen und danach {{incode   Quader002}}{: mediawiki}, den kleineren Würfel.

:   18.1. Danach die Schaltfläche **File:Part_Cut.svg   16px Part_Cut/de**{: mediawiki} drücken. Dies erstellt das Differenzobjekt {{incode   Cut001}}{: mediawiki}. Dies ist ein hohler Körper, der den Basiskörper {{incode   Cut}}{: mediawiki} nur an bestimmten Ecken überschneidet.

19\. Um dies zu veranschaulichen, können wir die **Ansicht**-Eigenschaften im Eigenschafteneditor ändern.

:   19.1. {{incode   Quader004}}{: mediawiki} und {{incode   Quader005}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Visibility**  auf {{incode   false}}{: mediawiki} ändern oder die **Leertaste** drücken.
:   19.2. {{incode   Cut001}}{: mediawiki} auswählen, den Wert von **Shape Color** anklicken, um den Dialog **Farbauswahl** zu öffnen und einen roten Farbton auszuwählen; abschließend auch den Wert von **Transparency** auf {{incode   90}}{: mediawiki} ändern.

! 
*Ein gedrehter hohler Festkörper, der als Beschnittobjekt für einige Ecken des inneren Festkörpers verwendet wird*



## Beschneiden der Ecken 2 

20\. In Der Baumansicht {{incode   Cut001}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Visibility**  auf {{incode   false}}{: mediawiki} ändern oder die **Leertaste** drücken.

21\. In der Baumansicht {{incode   Quader004}}{: mediawiki} und {{incode   Quader005}}{: mediawiki} auswählen, im Reiter **Ansicht** den Wert von **Visibility** auf {{incode   true}}{: mediawiki} ändern oder die **Leertaste** drücken.

:   21.1. Den Dialog Positionierung öffnen.
:   21.2. Die Option **Inkrementelle Änderungen anwenden** aktivieren; man beachte, dass alle Werte unter **Verschiebung** auf Null zurückgesetzt werden.
:   21.3. Unter **Drehung** {{incode   Rotationsachse mit Winkel}}{: mediawiki} einstellen; **X-Achse** festlegen und **Angle**  auf {{incode   45 °}}{: mediawiki} ändern; danach die Schaltfläche **Anwenden** drücken. Dies wendet eine Drehung um die X-Achse an und setzt den Wert des Feldes **Angle** auf Null zurück.
:   21.4. Noch einmal **Drehung** einstellen, jetzt die **Z-Achse** festlegen und **Angle** auf {{incode   -45 °}}{: mediawiki} ändern; danach die Schaltfläche **Anwenden** drücken. Dies wendet eine Drehung um die lokale Z-Achse an und setzt den Wert des Feldes **Angle** auf Null zurück.
:   21.5. Die Schaltfläche **OK** drücken, um den Dialog zu schließen.

22\. In der Baumansicht alle Objekte abwählen, dann zuerst {{incode   Quader005}}{: mediawiki}, den größeren Würfel, auswählen und danach {{incode   Quader004}}{: mediawiki}, den kleineren Würfel.

:   22.1. Danach die Schaltfläche **File:Part_Cut.svg   16px Part_Cut/de**{: mediawiki} drücken. Dies erstellt das Differenzobjekt {{incode   Cut002}}{: mediawiki}. Dies ist ein hohler Körper, der den Basiskörper {{incode   Cut}}{: mediawiki} nur an bestimmten Ecken überschneidet.

23\. Um dies zu veranschaulichen, können wir die **Ansicht**-Eigenschaften im Eigenschafteneditor ändern.

:   23.1. {{incode   Cut002}}{: mediawiki} auswählen, den Wert von **Shape Color** anklicken, um den Dialog **Farbauswahl** zu öffnen und einen rosafarbenen Farbton auszuwählen; abschließend auch den Wert von **Transparency** auf {{incode   90}}{: mediawiki} ändern.

! 
*Ein gedrehter hohler Festkörper, der als Beschnittobjekt für einige Ecken des inneren Festkörpers verwendet wird*



## Das Modell fertigstellen 

24\. Sicherstellen, dass alle Objekte sichtbar sind. In Der Baumansicht alle Objekte auswählen, im Reiter **Ansicht** den Wert von **Visibility** auf {{incode   true}}{: mediawiki} ändern oder die **Leertaste** drücken.

! 
*Der innere hohle Festkörper zusammen mit den Äußeren Objekten, die ihn beschneiden werden*

25\. In der Baumansicht alle Objekte abwählen, dann zuerst {{incode   Cut}}{: mediawiki} auswählen und danach {{incode   Cut001}}{: mediawiki}.

:   25.1. Danach die Schaltfläche **File:Part_Cut.svg   16px Part_Cut/de**{: mediawiki} drücken. Dies erstellt das Differenzobjekt {{incode   Cut003}}{: mediawiki}.

! 
*Der innere hohle Festkörper mit {{incode   Cut001* beschnitten}}{: mediawiki}

26\. In der Baumansicht alle Objekte abwählen, dann zuerst {{incode   Cut003}}{: mediawiki} auswählen und danach {{incode   Cut002}}{: mediawiki}.

:   26.1. Danach die Schaltfläche **File:Part_Cut.svg   16px Part_Cut/de**{: mediawiki} drücken. Dies erstellt das Differenzobjekt {{incode   Cut004}}{: mediawiki}. Dies ist das endgültige Objekt.
:   26.2. {{incode   Cut004}}{: mediawiki} auswählen, den Wert von **Shape Color** anklicken, um den Dialog to open the **Farbauswahl** zu öffnen und einen grünen Farbton auszuwählen; abschließend auch den Wert von **Line Width** auf {{incode   2.0}}{: mediawiki} ändern.

! 
*Der innere hohle Festkörper mit {{incode   Cut001*  und `Cut002` beschnitten. Das endgültige Modell}}{: mediawiki}

27\. Echt Objekte haben keine perfekt scharfe Kanten oder Ecken, daher kann Verrunden das Modell noch verfeinern.

:   27.1. In der Baumansicht {{incode   Cut004}}{: mediawiki} auswählen, dann die Schaltfläche **File:Part_Fillet.svg   16px Part_Fillet/de**{: mediawiki} drücken.
:   27.2. Im Aufgaben-Bereich **Kanten abrunden** unter **Auswahl** **Kanten auswählen** aktivieren und die Schaltfläche **Alle** drücken. Als **Typ der Abrundung** {{incode   Konstanter Radius}}{: mediawiki} auswählen und **Radius** auf {{incode   1 mm}}{: mediawiki} ändern.
:   24.3. **OK** drücken. Dies erstellt ein Verrundungsobjekt {{incode   Fillet}}{: mediawiki}.
:   27.4. Im Reiter **Ansicht** den Wert von **Line Width** auf {{incode   2.0}}{: mediawiki} ändern.

! 
*Das fertige Whiffle-Ball-Modell mit verrundeten Kanten*


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Whiffle Ball tutorial/de
