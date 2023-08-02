---
- GuiCommand:
   Name: PartDesign Line
   Name/pl: Projekt Części: Utwórz linię odniesienia
   MenuLocation: Projekt Części -> Utwórz układ odniesienia -> Utwórz linię odniesienia
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_Point/pl, PartDesign_Plane/pl
---

# PartDesign Line/pl



## Opis

Tworzy **linię odniesienia**, która może być używana jako odniesienie dla szkiców, innej geometrii odniesienia lub elementów. Na przykład może być używana jako oś obrotu dla funkcji obrotu i rowka.

<img alt="" src=images/datum_line.png  style="width:600px;"> 
*Dwie linie odniesienia przechodzące przez przeciwległe narożniki sześcianu spotykają się w środku masy.*



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_Line.svg" width=24px> '''Utwórz linię odniesienia'''**.
2.  Zdefiniuj parametry linii. Wybierz pierwsze odniesienie w oknie widoku 3D, aby przefiltrować dostępne tryby mocowania.
3.  W zależności od wybranego odniesienia, na liście może być dostępny jeden lub więcej trybów dołączania. Najbardziej prawdopodobny z nich zostanie automatycznie wybrany i wyróżniony pogrubioną czcionką na liście. Tekst \"Dołączono w trybie\" wraz z nazwą trybu dołączania pojawi się w kolorze zielonym w górnej części panelu Parametry punktu odniesienia.
4.  Aby umieścić dodatkowe odniesienie, naciśnij następny przycisk **Odniesienie**. Po naciśnięciu jego etykieta zmienia się na *Wybieranie \...* do momentu dokonania wyboru.
5.  Wybierz tryb dołączania z listy.
6.  Zdefiniuj wartości przesunięcia dołączenia.
7.  Naciśnij **OK**.



## Opcje

Kliknij dwukrotnie etykietę LiniaOdniesienia w drzewie modelu lub kliknij prawym przyciskiem myszy i wybierz **Edytuj odniesienie** z menu kontekstowego, aby edytować jego parametry. Aby uzyskać więcej informacji na temat trybu dołączania i przesunięcia dołączania, zobacz stronę [Edytuj dołączenie](Part_EditAttachment/pl.md).



## Właściwości

-    **Tryb mapowania**: wymienia używany tryb dołączania.

-    **Odsunięcie dołaczenia**: stosuje transformację (przesunięcie i obrót) w odniesieniu do umieszczenia dołaczenia.

-    **Etykieta**: nazwa nadana obiektowi, nazwa ta może być dowolnie zmieniana.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Line/pl
