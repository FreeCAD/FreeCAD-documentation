---
 GuiCommand:
   Name: PartDesign CoordinateSystem
   Name/pl: Projekt Części: Utwórz lokalny układ współrzędnych.
   MenuLocation: Projekt Części , Utwórz lokalny układ współrzędnych
   Workbenches: PartDesign_Workbench/pl
   Version: 0.18
   SeeAlso: PartDesign_Point/pl, PartDesign_Line/pl, PartDesign_Plane/pl
---

# PartDesign CoordinateSystem/pl



## Opis

Tworzy **lokalny układ współrzędnych**, który może być użyty jako odniesienie dla innej geometrii układu odniesienia. Pomaga również zidentyfikować orientację geometrii odniesienia w przestrzeni 3D. ![](images/PartDesign_LocalCoordinateSystem_Example.png ) 
*Lokalny układ współrzędnych pochodzący z punktu położenia odniesienia płaszczyzny.*



## Użycie

1.  Naciśnij przycisk **[<img src=images/PartDesign_CoordinateSystem.svg style="width:16px"> '''Utwórz lokalny układ współrzędnych'''**.
2.  Zdefiniuj parametry układu współrzędnych. Wybierz pierwsze odniesienie w oknie widoku 3D, aby filtrować dostępne tryby dołączania.
3.  W zależności od wybranego odniesienia, na liście może być dostępny jeden lub więcej trybów dołączania. Najbardziej prawdopodobny z nich zostanie automatycznie wybrany i wyróżniony pogrubioną czcionką na liście. Tekst \"Dołączono w trybie\" wraz z nazwą trybu dołączania pojawi się w kolorze zielonym w górnej części panelu Parametry punktu odniesienia.
4.  Aby dodać dodatkowe odniesienie, naciśnij następny przycisk **Odniesienie**. Po naciśnięciu jego etykieta zmienia się na *Wybieranie \...* do momentu dokonania wyboru.
5.  Wybierz tryb dołączania z listy.
6.  Zdefiniuj wartości przesunięcia dołączenia.
7.  Naciśnij **OK**.



## Opcje

Kliknij dwukrotnie etykietę **Local_CS** w Drzewie modelu lub kliknij prawym przyciskiem myszy i wybierz **Edytuj odniesienie** z menu kontekstowego, aby edytować jego parametry. Aby uzyskać więcej informacji na temat trybu dołączania i przesunięcia dołączania, zobacz stronę [Edytuj dołączenie](Part_EditAttachment/pl.md).



## Ustawienia

Zobacz [Projekt Części: Płaszczyzna odniesienia](PartDesign_Plane/pl#Właściwości.md).



## Właściwości



### Dane

-    **Tryb mapowania**: wymienia używany tryb dołączania.

-    **Odwrócenie dołączenia**: wskazuje, czy układ współrzędnych jest odwrócony w orientacji.

-    **Odsunięcie dołaczenia**: stosuje transformację *(przesunięcie i obrót)* w odniesieniu do umieszczenia dołączenia.

-    **Umiejscowienie**: wskazuje współrzędne i wyrównanie początku układu współrzędnych.

-    **Etykieta**: nazwa nadawana obiektowi, nazwa ta może być dowolnie zmieniana.



## Tworzenie skryptów 


```python
lcs = App.activeDocument().addObject( 'PartDesign::CoordinateSystem', 'LCS' )
```





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign CoordinateSystem/pl
