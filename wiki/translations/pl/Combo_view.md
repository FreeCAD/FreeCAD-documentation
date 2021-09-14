# Combo view/pl

 {{TOCright}}

## Wprowadzenie

[Widok połączony](combo_view/pl.md) jest jednym z głównych paneli w [interfejsie](interface/pl.md) FreeCAD . Domyślnie znajduje się on po lewej stronie ekranu. Składa się z **dwóch części**:

-   [Sekcja górna](#Upper_section.md) posiada dwie zakładki dla właściwości **Model** i **Zadania**,
-   [Sekcja dolna](#Lower_section.md) pokazuje [edytor właściwości](property_editor/pl.md), który również wyświetla dwie zakładki dla właściwości **Widok** i **Dane**.

**Uwaga:** [Edytor właściwości](property_editor/pl.md) jest wyświetlany tylko wtedy, gdy aktywna jest zakładka **Model**, czyli gdy widoczny jest [widok drzewa](tree_view/pl.md).


**Uwaga:**

Pierwotnie górna część *([widoku drzewa](tree_view/pl.md))* była oddzielona od dolnej części *([edytora właściwości](property_editor/pl.md))*, ale następnie zostały one połączone i w ten sposób powstał widok *połączony*.

## Sekcja górna 

Zakładka **Model** pokazuje [widok drzewa](tree_view/pl.md), który jest reprezentacją zawartości dokumentu. W tym geometrii 2D i 3D z ich historią parametryczną, ale także obsługuje obiekty, które zawierają dane zapisane w dokumencie.

Zakładka **Zadania** zawiera [panel zadań](task_panel/pl.md), który pokazuje różne działania w zależności od aktywnego stołu roboczego i aktywnego narzędzia.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="600px;">


*Widok połączony posiada dwie karty: <br />kartę Model, która steruje wyświetlaniem [widoku drzewa](tree_view/pl.md) i [edytor właściwości](property_editor/pl.md), <br />oraz kartę Zadania, która kontroluje wyświetlanie [panel zadań](task_panel/pl.md).*

## Sekcja dolna 

W dolnej części widoku połączonego wyświetlane są [edytor właściwości](property_editor/pl.md), zawierający dwie zakładki dla parametrów **Widok** i **Dane**. Edytor właściwości jest wyświetlany tylko wtedy, gdy zakładka **Model** jest aktywna, to znaczy, gdy jest aktywny [widok drzewa](tree_view/pl.md).

-   Zakładka **Widok** pokazuje właściwości wyświetlania obiektów, które mają wpływ tylko na wygląd w oknie [widoku 3D](3D_view/pl.md).

-   Zakładka **Dane** pokazuje właściwości parametryczne obiektów, które określają sposób rzeczywistego definiowania kształtów geometrycznych.

<img alt="" src=images/FreeCAD_Combo_view_Tree_View_properties.png  style="width:" height="600px;"> <img alt="" src=images/FreeCAD_Combo_view_Tree_Data_properties.png  style="width:" height="600px;">


*W dolnej części widoku połączonego znajduje się edytor właściwości, prezentujący właściwości widoku i danych.*

## Wyłączenie widoku połączonego 

Aby móc samodzielnie korzystać z tych poglądów, należy użyć [edytora parametrów](Std_DlgParameter.md). Jeśli nie istnieją stwórz następujące podgrupy:

-    `BaseApp/Preferences/DockWindows/TreeView`
    

-    `BaseApp/Preferences/DockWindows/PropertyView`
    

następnie dodaj parametr `Enabled` typu `Boolean`, i ustaw jego wartość na `True`.

Następnie należy aktywować widok za pomocą menu, **Widok → Panele → Widok drzewa** lub **→ Właściwości widoku**.


{{Std Base navi

}} {{Interface navi}} 
