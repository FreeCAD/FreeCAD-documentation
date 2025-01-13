---
 GuiCommand:
   Name: Arch Survey
   Name/pl: BIM: Spis wymiarów
   MenuLocation: Narzędzia , Spis wymiarów
   Workbenches: BIM_Workbench/pl
   SeeAlso: Macro_FCInfo/pl, Macro_SimpleProperties/pl
---

# Arch Survey/pl



## Opis

Narzędzie **Spis wymiarów** uruchamia specjalny tryb geodezyjny, który pozwala na szybkie pobieranie pomiarów i informacji z modelu oraz przesyłanie ich do innych aplikacji. Po przejściu do trybu geodezyjnego, kliknięcie różnych elementów podrzędnych obiektów 3D powoduje zebranie następujących informacji *(w zależności od klikniętego elementu)*:

-   Jeśli klikniesz na krawędź, otrzymasz jej długość.
-   Jeśli klikniesz na wierzchołek, otrzymasz jego wysokość *(współrzędna na osi Z)*.
-   Jeśli klikniesz na ścianę, otrzymasz jej powierzchnię.
-   Dwukrotne kliknięcie czegokolwiek, czyli zaznaczenie całego obiektu, spowoduje wyświetlenie jego objętości.

Po zebraniu takich informacji dzieje się kilka rzeczy:

-   Na górze klikniętego elementu umieszczana jest etykieta wyświetlająca wartość *(z \"a\" dla powierzchni, \"l\" dla długości, \"z\" dla wysokości lub \"v\" dla objętości)*.
-   Wartość liczbowa jest kopiowana do schowka, dzięki czemu można ją wkleić w innej aplikacji.
-   Linia jest drukowana w oknie wyjściowym FreeCAD. Po wyjściu z trybu spisu linie te można skopiować i wkleić w innej aplikacji *(wartości są oddzielone przecinkami, co ułatwia konwersję na dane arkusza kalkulacyjnego)*.
-   Całkowita długość lub powierzchnia klikniętych elementów jest również drukowana w oknie wyjściowym.
-   Każda długość lub powierzchnia jest również rejestrowana w oknie dialogowym zadania.

<img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;">

*Powyższy obraz pokazuje, co dzieje się po uruchomieniu trybu spisu.*



## Użycie

1.  Naciśnij przycisk w menu **Narzędzia → <img src="images/Arch_Survey.svg" width=16px> '''Spis wymiarów'''**.
2.  Kliknij wierzchołki, krawędzie, ściany lub kliknij dwukrotnie, aby zaznaczyć całe obiekty.
3.  Kliknij poza dowolną geometrią *(w oknie widoku 3D)*, aby usunąć istniejące etykiety, zostanie wydrukowana linia sumaryczna w oknie dialogowym Zadanie, a liczenie długości i powierzchni zostanie wznowione od zera.
4.  Naciśnij **Esc** lub przycisk **Zamknij**, aby wyjść z trybu pomiaru i usunąć wszystkie etykiety.



## Opcje

-   Można dodać niestandardową etykietę do dowolnego wiersza w oknie dialogowym zadania, klikając ten wiersz, a następnie dodaj tekst w polu opisu i naciśnij przycisk **ustaw opis**.
-   Po zakończeniu, przed zamknięciem, można wyeksportować zawartość okna dialogowego Zadanie, naciskając przycisk \"eksportuj CSV\". Wynikowy plik CSV można następnie otworzyć w dowolnej aplikacji arkusza kalkulacyjnego, takiej jak Excel lub LibreOffice Calc. Wartości i jednostki zostaną rozdzielone w wynikowym pliku CSV, a sumy zostaną zapisane jako funkcje SUM().

<img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;">



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Spis nie ma interfejsu programistycznego, ale zbieranie tych samych informacji z dowolnego wybranego obiektu opartego na obiekcie [Część](Part_Workbench/pl.md) można odtworzyć za pomocą następującego skryptu:


```python
import FreeCADGui

selection = FreeCADGui.Selection.getSelectionEx()

for obj in selection:
    for element in obj.SubObjects:
        print("Area: %f", element.Area)
        print("Length: %f", element.Length)
        print("Volume: %f", element.Volume)
        print("Center of Mass: %f", element.CenterOfMass)
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Survey/pl
