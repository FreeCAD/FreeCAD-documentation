# Asymptote/pl
## Opis

[Asymptote](https://asymptote.sourceforge.io/) to język wektorowy dla grafiki komputerowej 2D i 3D. Kod Asymptote może być zawarty w dokumentach [LaTeX](https://www.latex-project.org/) lub użyty do wygenerowania plików [PostScript](https://en.wikipedia.org/wiki/PostScript), [PDF](PDF/pl.md), [SVG](SVG/pl.md), [WebGL](https://www.khronos.org/webgl/) i [PRC](https://en.wikipedia.org/wiki/PRC_(file_format)). Interaktywne pliki PDF 3D utworzone z kodu Asymptote wymagają programu Acrobat Reader w wersji 9 lub nowszej.

Obsługa Asymptote została dodana w FreeCAD w wersji 0.19.



## Eksportowanie

1.  Opcjonalnie przypisz kolory do ścian obiektu, który chcesz wyeksportować za pomocą narzędzia <img alt="" src=images/Part_FaceColors.svg  style="width:24px;"> [Kolor dla ściany](Part_FaceColors/pl.md) środowiska Część.
2.  Zmień środowisko pracy na <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md).
3.  Utwórz siatkę z obiektu za pomocą <img alt="" src=images/Mesh_FromPartShape.svg  style="width:24px;"> [Siatka z kształtu środowiska Część](Mesh_FromPartShape/pl.md).
4.  Wybierz nowy obiekt siatki.
5.  Wywołaj polecenie <img alt="" src=images/Mesh_Export.svg  style="width:24px;"> [Eksport](Mesh_Export/pl.md).
6.  Wybierz format pliku ***.asy** w oknie dialogowym.
7.  Wprowadź nazwę pliku.
8.  Naciśnij przycisk **Zapisz**.



## Konwersja

Do konwersji plików ***.asy** wymagany jest kompilator [Asymptote](https://sourceforge.net/projects/asymptote/). Do konwersji do formatu PDF wymagany jest również system [LaTeX](https://www.latex-project.org/get/).

Kompilator jest narzędziem wiersza poleceń. Do konwersji do formatu PDF można użyć następującej składni: 
```pythonPathToAsyExecutable/asy -f pdf AsymptoteFileName.asy```.



## Powiązane

-   [Import Eksport](Import_Export/pl.md)



## Poradniki Wideo 

Poniższe filmy są w języku hiszpańskim:

-   [Sposób generowania interaktywnych plików pdf-3D. *(1/3)* *(Z FreeCAD, MeshLab i LaTeX)*](https://www.youtube.com/watch?v=U0m3643Vb1Q)
-   [Sposób generowania interaktywnych plików pdf-3D. *(2/3)* *(Z Asymptote i LaTex)*](https://www.youtube.com/watch?v=PhVNvDZIerM)
-   [Sposób generowania interaktywnych plików pdf-3D. *(3/3)* *(Z FreeCAD, Asymptote i LaTeX)*](https://www.youtube.com/watch?v=Q_ufaCN2hb4)


{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Mesh](Category_Mesh.md) > Asymptote/pl
