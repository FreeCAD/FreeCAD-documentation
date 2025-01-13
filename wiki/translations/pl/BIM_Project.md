---
 GuiCommand:
   Name: BIM Project
   Name/pl: BIM: Projekt
   MenuLocation: 3D/BIM , Projekt
   Workbenches: BIM_Workbench/pl
   Shortcut: 
   SeeAlso: 
---

# BIM Project/pl



## Opis

Narzędzie **BIM Projekt** tworzy projekt [natywnego IFC](NativeIFC/pl.md) w bieżącym dokumencie. W IFC, projekt (IfcProject) to baza wszystkich części modelu. Wymagane jest posiadanie jednego projektu w każdym pliku IFC.

Nie jest jednak konieczne tworzenie projektu żeby wyeksportować model programu FreeCAD do IFC, ponieważ domyślny projekt zostanie dodany za każdym razem podczas eksportu pliku IFC. Jednak, podczas pracy z [natywnym IFC](NativeIFC/pl.md), plik IFC jest dołączany do modelu i wszystkie geometrie i właściwości modelu i jego komponenty pochodzą z dołączonego pliku IFC. Projekt jest miejscem, w którym plik IFC jest dołączony do dokumentu.

Zwykle projekt BIM jest tworzony aby dołączyć plik IFC. Podczas tworzenia projektu, dołączony plik IFC jest pusty i niezapisany. Przy następnym zapisie pliku programu FreeCAD pojawi się pytanie o zapisanie pliku IFC.

Jeśli udostępniasz plik programu FreeCAD, wszystkie dołączone pliki IFC muszą być udostępnione razem. W innym wypadku FreeCAD nie będzie mógł wyciągnąć geometrii. Jednak, jeśli właściwość **shape mode** wszystkich obiektów zawartych w projekcie jest ustawiona na **Shape** to plik programu FreeCAD może być udostępniony bez towarzyszącego pliku IFC i nadal będzie się otwierał poprawnie na innych komputerach. Obiekty IFC nie będą już jednak edytowalne.

Podczas wstawiania pliku IFC tworzony jest obiekt projektu, który ma całą zawartość pliku. Jak wszystkie obiekty NativeIFC, projekt może być rozszerzony poprzez kliknięcie dwukrotnie w drzewie.



## Użycie

1.  Upewnij się, że masz otwarty dokument programu FreeCAD.
2.  Wciśnij przycisk **<img src="images/BIM_Project.svg" width=16px> [Projekt](BIM_Project/pl.md)**.
3.  Opcjonalnie, zablokuj dokument wciskając przycisk **<img src="images/IFC.svg" width=16px> [Blokada IFC](NativeIFC/pl#Tryb_zablokowany_i_odblokowany.md)**.



## Tryb zablokowany i odblokowany 

W [środowisku pracy BIM](BIM_Workbench.md), pasek statusu zawiera przycisk **<img src="images/IFC.svg" width=16px> [Blokada IFC](NativeIFC/pl#Tryb_zablokowany_i_odblokowany.md)**, który pozwala na przełączanie między trybami **zablokowany** i **odblokowany**. W trybie odblokowanym możesz mieć kilka [projektów](BIM_Project/pl.md) w dokumencie programu FreeCAD i mieć elementy IFC oraz inne niż IFC.

W trybie zablokowanym, dane dołączone do obiektu projektu stają się dołączone bezpośrednio do dokumentu programu FreeCAD. Dokument programu FreeCAD działa jak wierna replika lub render dokumentu IFC. Obiekt projektu jest więc usuwany. Możesz mieć tylko jeden projekt w dokumencie programu FreeCAd i nie możesz mieć obiektów innych niż IFC (każdy nowy obiekt jest od razu przekształcany do IFC).



## Dodawanie obiektów do projektu 

Aby dodać obiekty do projektu wystarczy przeciągnąć i upuścić je do projektu w widoku drzewa. Te obiekty zostaną przekształcone na IFC i mogą stracić niektóre wcześniejsze zachowania parametryczne jeśli nie są one wspierane przez IFC.

## Diff

Gdy projekt zawiera niezapisane zmiany, na jego ikonie w widoku drzewa wyświetlana jest czerwona kropka. Kliknięcie prawym przyciskiem myszy na projekcie i wybranie **IFC → Diff** otworzy okno dialogowe z [diff](https://en.wikipedia.org/wiki/Diff) tego co zmieniło się w dołączonym pliku IFC. Jest to dobry sposób na upewnienie się, że wprowadzone zmiany są poprawne.



## Zapisywanie

Pliki IFC dołączone do projektu są automatycznie zapisywane przy każdym zapisie pliku programu FreeCAD. Można je również zapisać ręcznie w każdej chwili klikając prawym przyciskiem myszy na projekcie i wybierając **IFC → Zapisz**.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Project/pl
