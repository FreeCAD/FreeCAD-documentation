---
- GuiCommand:/pl
   Name:PartDesign Plane
   Name/pl:Projekt Części: Utwórz płaszczyznę odniesienia
   MenuLocation:Projekt Części → Utwórz układ odniesienia → Utwórz płaszczyznę odniesienia
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Utwórz punkt odniesienia](PartDesign_Point/pl.md), [Utwórz linię odniesienia](PartDesign_Line/pl.md)
---

# PartDesign Plane/pl



## Opis

Tworzy **płaszczyznę odniesienia**, która może być używana jako odniesienie dla szkiców lub innej geometrii odniesienia. Szkice mogą być dołączane do płaszczyzn odniesienia. ![](images/Datum_plane.png ) *Płaszczyzna odniesienia przecinająca 3 rogi sześcianu z naszkicowanym na niej walcem wykorzystującym płaszczyznę odniesienia jako płaszczyznę X-Y*.



## Wymagania wstępne 

Płaszczyzna odniesienia, od wersji FreeCAD 0.18, może być tworzona tylko wewnątrz <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Zawartości](PartDesign_Body/pl.md). Każda bryła ma punkt początkowy *(punkt doniesienia położenia)*, który jest domyślnie ukryty. Aby móc odwoływać się do płaszczyzn bazowych położenia początkowego, ustaw punkt doniesienia położenia jako widoczny. Można to zrobić przed utworzeniem płaszczyzny odniesienia.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_Plane.svg" width=16px> [Utwórz płaszczyznę odniesienia](PartDesign_Plane.md)**.
2.  Zdefiniuj parametry płaszczyzny. Wybierz pierwsze odniesienie w widoku 3D, aby filtrować dostępne tryby [dołączania](Part_EditAttachment.md).
3.  W zależności od wybranego odniesienia, na liście może być dostępny jeden lub więcej trybów dołączania. Najbardziej prawdopodobny z nich zostanie automatycznie wybrany i wyróżniony pogrubioną czcionką na liście. Tekst \"Dołączono w trybie\" wraz z nazwą trybu dołączania pojawi się w kolorze zielonym w górnej części panelu Parametry punktu odniesienia.
4.  Aby umieścić dodatkowe odniesienie, naciśnij następny przycisk **Odniesienie**. Po naciśnięciu jego etykieta zmienia się na *Wybieranie \...* do momentu dokonania wyboru.
5.  Wybierz tryb dołączania z listy.

**Przesunięcia:** Zdefiniuj wartości Odsunięcie dołączenia. **Uwaga**, przesunięcia x, y i z reprezentują lokalny układ współrzędnych płaszczyzny odniesienia, a nie globalny układ współrzędnych. Dlatego przesunięcie z jest zawsze przesunięciem wzdłuż wektora normalnego płaszczyzny odniesienia.

1.  **Obrót:** Zmiana opcji \"Wokół osi x\" powoduje obrót płaszczyzny wokół lokalnej osi X. Zmiana opcji \"Wokół osi y\" powoduje obrót płaszczyzny wokół lokalnej osi Y. Zmiana opcji \"Wokół osi z\" powoduje obrót płaszczyzny wokół lokalnej osi Z.
2.  Naciśnij **OK**.



## Opcje

Kliknij dwukrotnie etykietę PłaszczyznaOdniesienia w drzewie modelu lub kliknij prawym przyciskiem myszy i wybierz **Edytuj odniesienie** z menu kontekstowego, aby edytować jego parametry. Aby uzyskać więcej informacji na temat trybu dołączania i przesunięcia dołączania, zobacz stronę [Edytuj dołączenie](Part_EditAttachment/pl.md).



## Właściwości

-    **Tryb mapowania**: wymienia używany tryb dołączania.

-    **Odsunięcie dołaczenia**: stosuje transformację (przesunięcie i obrót) w odniesieniu do umieszczenia dołaczenia.

-    **Etykieta**: nazwa nadana obiektowi, nazwa ta może być dowolnie zmieniana.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Plane/pl
