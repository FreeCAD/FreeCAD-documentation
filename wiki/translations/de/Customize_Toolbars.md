# Customize Toolbars/de
{{TutorialInfo/de
|Topic=Beispielthema
|Level=Anfänger
|Time=5 Minuten
|Author=[Mario52](User_Mario52.md)
|FCVersion=Alle
}}

## Zusammenfassung

Dieses Tutorium zeigt dir die Anpassung von Werkzeugleisten. Werkzeuge (einschließlich Makrowerkzeuge) können in verschiedenen Arbeitsbereichen verwendet werden. In einem Beispiel wird ein Makro zu einem Makrowerkzeug, indem ein **Menütext**, eine **Werkzeugspitze** und ein **Symbol** erstellt wird. Danach wird dieses Makrowerkzeug Teil einer zusätzlichen Werkzeugleiste in einem Arbeitsbereich.

## Anwendung

**1.** Finde das Anpassungsmenü

-   Klicke {{MenuCommand/de|Hauptmenü → Werkzeuge → Benutzerdefiniert}},

<img alt="Benutzerdefiniert" src=images/CustomizeToolBar_01.png  style="width:640px;"> 

-   oder rechtsklicke auf eine beliebige Werkzeugleiste.

<img alt="Rechter Mausklick" src=images/CustomizeToolBar_02.png  style="width:640px;"> 

-   Das Anpassungsfenster erscheint.

<img alt="Das Anpassungsfenster erscheint" src=images/CustomizeToolBar_03.png  style="width:640px;"> 

**2.** Erzeuge ein Makro zu einem Makro-Werkzeug

-   Wähle den \"Makro\" Reiter.

-   Um ein Symbol für das bereitgestellte Makro hinzuzufügen, klicke auf die Pixmap Schaltfläche (labelled **... **).

<img alt="Wähle eine Werkzeugleiste" src=images/CustomizeToolBar_04.png  style="width:640px;"> 

-   Suche nach einem geeigneten Symbol aus den vorhandenen Symbolen von FreeCAD,


<div class="mw-collapsible mw-collapsed toccolours">

      \[oder füge Dein eigenes Symbol durch klicken von **Symbole hinzufügen...**\] hinzu.                  (erweitere für ein Beispiel)


<div class="mw-collapsible-content">

<img alt="Symbol hinzufügen" src=images/CustomizeToolBar_05.png  style="width:640px;"> 

     \[Du erhälst ein Dateiauswahlfenster, wähle deine benutzerdefinierte Bilddatei (PNG format, 64x64 pixels)\]

<img alt="Hole eine Datei" src=images/CustomizeToolBar_06.png  style="width:640px;"> 


</div>


</div>

-   Wähle dein Symbol und klicke **OK**.

<img alt="Wähle dein Symbol" src=images/Customize5de.jpg  style="width:640px;"> 

-   Das von dir gewählte Symbol wird nun neben der Pixmap Schaltfläche mit der Beschriftung **...** angezeigt.

<img alt="Dein Symbol wird angezeigt" src=images/Customize6de.jpg  style="width:640px;"> 

-   Wähle das mitgelieferte Makro in der Zeile **Makro:** aus und gib einen **Menütext**: an (der als Textbeschriftung im Menü erscheint); fülle auch die *\'Werkzeugspitze\':* aus (das ist der Text, der erscheint, wenn sich die Maus über der Schaltfläche auf der Symbolleiste befindet); weitere Zeilen sind optional.

-   Klicke die Schaltfläche **Add**.

<img alt="Drücke die Schaltfläche" src=images/CustomizeToolBar_09.png  style="width:640px;"> 

-   Die Schaltfläche des Makrowerkzeugs ist nun erstellt.

<img alt="Deine Schaltfläche ist erstellt" src=images/CustomizeToolBar_10.png  style="width:640px;"> 

**3.** Erstelle eine Werkzeugleiste außerhalb des Arbeitsbereichs **Makro**, die das erstellte **Makrowerkzeug** enthält

-   Wähle die Registerkarte **Werkzeugleisten** und wähle den Arbeitbereich (für den die Werkzeugleiste vorgesehen ist) in der Aufklappliste auf der rechten Seite (**Teil** in diesem Beispiel).

        \[Seit Version 0.15 gibt es einen Arbeitsbereich  **[<img src=images/Freecad.svg style="width:16px"> Global**  Werkzeugleiste. Wenn dies ausgewählt wird, befindet sich die bereitgestellte Werkzeugleiste in jedem Arbeitsbereich.\]

<img alt="Werkzeugleistenreiter" src=images/CustomizeToolBar_11.png  style="width:640px;"> 

-   Wähle in der Aufklappliste auf der linken Seite **Makros**.

<img alt="Makros" src=images/CustomizeToolBar_12.png  style="width:640px;"> 

-   Das Makrowerkzeug mit seinem Symbol erscheint in der Liste.

<img alt="Dein Symbol wird aufgeführt" src=images/CustomizeToolBar_13.png  style="width:640px;"> 

-   Klicke die Schaltfläche **Neu**.

<img alt="Klicke auf \"Neu\"" src=images/CustomizeToolBar_14.png  style="width:640px;"> 

-   Im Fenster \"Neue Werkzeugleiste\" gib den Namen der bereitgestellten zusätzlichen Werkzeugleiste für den **Part** Arbeitsbereich ein und klicke auf **OK**

<img alt="Gib den Namen für die Werkzeugleiste ein" src=images/CustomizeToolBar_15.png  style="width:640px;"> 

-   Die Werkzeugleiste ist nun erstellt.

-   Um das erzeugte Makrowerkzeug dieser Symbolleiste hinzuzufügen, wähle es im linken Fenster aus und klicke dann auf die **Button**-Schaltfläche, wobei der Pfeil nach rechts zeigt.

<img alt="Wähle Dein Makro" src=images/CustomizeToolBar_16.png  style="width:640px;"> 

-   Du hast nun eine Werkzeugleiste mit dem Namen \"Kamera\" erstellt (mit dem Makrowerkzeug **Kamera** darin)

-   Klicke die **Close** Schaltfläche.

<img alt="Schließen" src=images/CustomizeToolBar_17.png  style="width:640px;"> 

-   Deine neue Werkzeugleiste ist jetzt im Rechtsklickmenü der Werkzeugleisten enthalten. Seine Symbole (in unserem Beispiel nur die Kamera) sind sichtbar, wenn die Symbolleiste aktiviert ist (blaues Häkchen).

<img alt="Neue Werkzeugleiste" src=images/CustomizeToolBar_18.png  style="width:640px;"> 

## Hinweise

Siehe auch [Anpassung der Oberfläche](Interface_Customization/de.md).



[<img src="images/Property.png" style="width:16px"> Preferences](Category_Preferences.md)

---
[documentation index](../README.md) > [Preferences](Category_Preferences.md) > Customize Toolbars/de
