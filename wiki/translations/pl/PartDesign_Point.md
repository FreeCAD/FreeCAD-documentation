---
- GuiCommand:
   Name:PartDesign Point
   Name/pl:Projekt Części: Utwórz punkt odniesienia
   MenuLocation:Projekt Części → Utwórz układ odniesienia → Utwórz punkt odniesienia
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Utwórz linię odniesienia](PartDesign_Line/pl.md), [Utwórz płaszczyznę odniesienia](PartDesign_Plane/pl.md)
---

# PartDesign Point/pl



## Opis

Tworzy **punkt odniesienia**, który może być użyty jako odniesienie dla szkiców oraz innej geometrii odniesienia.

![](images/DatumPoint.png ) 
*Punkt odniesienia dołączony do kuli z przesunięciem dołączenia {{Value|2* w kierunku Z.}}



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_Point.svg" width=24px> '''Utwórz punkt odniesienia'''**.
2.  Zdefiniuj parametry punktu. Wybierz pierwsze odniesienie w oknie widoku 3D, aby przefiltrować dostępne tryby dołączania.
3.  W zależności od wybranego odniesienia, na liście może być dostępny jeden lub więcej trybów dołączania. Najbardziej prawdopodobny z nich zostanie automatycznie wybrany i wyróżniony na liście pogrubioną czcionką. Tekst *Dołączono w trybie* wraz z nazwą trybu załącznika pojawi się na zielono w górnej części panelu Parametrów.
4.  Aby dodać dodatkowe odniesienie, naciśnij następny przycisk **Odniesienie**. Po naciśnięciu jego etykieta zmieni się na *Wybieranie\...* do momentu dokonania wyboru.
5.  Wybierz tryb dołączania z listy.
6.  Zdefiniuj wartości przesunięcia dołączenia.
7.  Naciśnij **OK**.



## Opcje

Kliknij dwukrotnie etykietę PunktDołączenia w drzewie modelu lub kliknij prawym przyciskiem myszy i wybierz **Edytuj odniesienie** z menu kontekstowego, aby edytować jego parametry. Aby uzyskać więcej informacji na temat trybu dołączania i przesunięcia dołączania, zobacz stronę [Edytuj dołączenie](Part_EditAttachment/pl.md).



## Właściwości

-    **Tryb mapowania**: wymienia używany tryb dołączania.

-    **Odsunięcie dołaczenia**: stosuje transformację (przesunięcie i obrót) w odniesieniu do umieszczenia dołaczenia.

-    **Etykieta**: nazwa nadana obiektowi, nazwa ta może być dowolnie zmieniana.



## Ograniczenia

-   Punkt odniesienia nie może być użyty jako przekrój dla funkcji Rura i Wyciągnięcie przez profile.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Point/pl
