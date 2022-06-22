---
- GuiCommand   */pl
   Name   *PartDesign Draft
   Name/pl   *Projekt części   * Pochylenie ścian
   MenuLocation   *Projekt Części → Zastosuj funkcje ulepszenia → Pochylenie ścian
   Workbenches   *[Projekt Części](PartDesign_Workbench/pl.md)
---

# PartDesign Draft/pl

## Opis

Narzędzie <img alt="" src=images/PartDesign_Draft.svg  style="width   *24px;"> **Pochylenie ścian** tworzy pochylenie kątowe wybranych ścian obiektu. Dodaje on do dokumentu obiekt **Draft** wraz z jego reprezentacją w oknie [widoku drzewa](Tree_view/pl.md).

   --
  ![Wybierz jedną lub więcej ścian na obiekcie przed uruchomieniem narzędzia. Tutaj zostały wybrane 2 ściany.](images/PartDesign_Draft-01.png ) ![Wyświetlanie parametrów funkcji w Panelu zadań.](images/PartDesign_Draft-02.png ) ![Dodano 2 ściany i zastosowano 10 stopniowe pochylenie. Dolna płaszczyzna pozostała wymiarowo niezmienna, podczas gdy pochylenie spowodowało zmniejszenie górnej płaszczyzny.](images/PartDesign_Draft-03.png ) ![Płaszczyzna neutralna została zmieniona na górną. Teraz górna płaszczyzna pozostała stabilna wymiarowo, podczas gdy szkic powiększył dolną płaszczyznę..](images/PartDesign_Draft-04.png ) ![Kierunek ścinania jest ustawiony na dolną prawą krawędź, co powoduje, że projekt jest ścinany w lewo..](images/PartDesign_Draft-05.png ) ![Zaznaczenie pola wyboru Kierunek odwrotny spowodowało zastosowanie zanurzenia do wewnątrz zamiast na zewnątrz..](images/PartDesign_Draft-06.png )   
   --




## Użycie

### Dodanie pochylenia ścian 

1.  Opcjonalnie [aktywuj](PartDesign_Body#Active_status/pl.md) bryłę, do której ma zostać zastosowane ścięcie.
2.  Wybierz jedną lub więcej powierzchni bryły.
3.  Narzędzie można wywołać na kilka sposobów   *
    -   Naciśnij przycisk **<img src="images/PartDesign_Draft.svg" width=16px> [Pochylenie ścian](PartDesign_Draft/pl.md)**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj funkcje ulepszenia → <img src="images/PartDesign_Draft.svg" width=16px> Pochylenie ścian**.
4.  Jeśli nie ma aktywnej bryły, a w dokumencie znajdują się dwie lub więcej brył, zostanie otwarte okno dialogowe **Wymagana jest aktywna zawartość** z prośbą o uaktywnienie jednej z nich. Jeśli jest tylko jedna zawartość, zostanie ona uaktywniona automatycznie.
5.  Zostanie otwarty [panel zadań](Task_panel/pl.md) funkcji **Parametry funkcji pochylenie ścian**. Więcej informacji na ten temat znajdziesz w sekcji [Opcje](#Opcje.md).
6.  Naciśnij przycisk **OK**, aby zakończyć.

   *   *Pamiętaj*\'   *
    -   Ponieważ dla danej cechy musi istnieć przynajmniej jedna ściana, ostatnia pozostała na liście ściana nie może zostać usunięta.

### Edycja pochylenia ścian 

1.  Do one of the following   *
    -   Double-click the Draft object in the [Tree view](Tree_view.md).
    -   Right-click the Draft object in the [Tree view](Tree_view.md) and select **Edit Draft** from the context menu.
2.  The **Draft parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Opcje

-    **Add face**   * Add faces to the selection by pressing the **Add face** button and selecting more faces.

-    **Remove face**   * Choose a way to remove faces from the selection   *

    -   Select one or more faces in the list and press the **Del** key or right-click the list and select **Remove** from the context menu.
    -   Press the **Remove face** button. All previously selected faces are highlighted in purple. Select each face to be removed.

-    **Draft angle**   * Set the Draft angle either by entering a value or by clicking the up/down arrows.

-    **Neutral plane**   * Set the the neutral plane by pressing the **Neutral plane** button and selecting the plane that must not change dimensionally.

-    **Pull direction**   * Set the the pull direction by pressing the **Pull direction** button, then select an edge. Pull Direction is only effective if the Neutral Plane has been set. Results can be unpredictable.

-    **Reverse pull direction**   * Invert the pull direction by checking the **Reverse pull direction** checkbox. This will toggle the draft between positive and negative angles.

## Uwagi

Narzędzie Pochylenie ścian działa tylko na powierzchniach, które nie są styczne z innymi powierzchniami. Często popełnianym błędem jest próba zastosowania funkcji do powierzchni, na którą nałożono już zaokrąglenie. Aby rozwiązać ten problem, należy usunąć zaokrąglenie, zastosować pochylenie ścian, a następnie ponownie zastosować zaokrąglenie.

## Właściwości

See also   * [Property editor](Property_editor.md).

A PartDesign Draft object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *

### Dane


{{Properties_Title|Podstawowe}}

-    **Angle|Angle**   * Cannot be negative. Default   * {{value|1.5 °}}.

-    **Reversed|Bool**   * Default   * `False`.

-    **Base|LinkSub**   * Sub-link to the parent feature\'s list of selected edges and faces.

-    **Support Transform|Bool**   * \"Include the base additive/subtractive shape when used in pattern features. If disabled, only the dressed part of the shape is used for patterning\". Default   * `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**   * Link to the parent feature.

-    **_ Body|LinkHidden|hidden**   * Link to the parent body.


{{Properties_Title|Draft}}

-    **Neutral Plane|LinkSub**   * Sub-link to the parent feature\'s list containing the neutral plane.

-    **Pull Direction|LinkSub**
    


{{Properties_Title|Projekt Części}}

-    **Refine|Bool**   * \"Refine shape (clean up redundant edges) after adding/subtracting\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Draft/pl
