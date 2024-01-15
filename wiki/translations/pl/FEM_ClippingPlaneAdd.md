---
 GuiCommand:
   Name: FEM ClippingPlaneAdd
   Name/pl: Płaszczyzna cięcia na ścianie
   MenuLocation: Narzędzia , Płaszczyzna cięcia na ścianie
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_tutorial/pl
---

# FEM ClippingPlaneAdd/pl



## Opis

Dodaje płaszczyznę cięcia dla całego widoku modelu. Wszystkie widoczne obiekty zostaną przez nią przecięte, niezależnie od tego czy są to modele geometryczne, siatki czy obiekty prezentacji graficznej wyników.

Płaszczyzna cięcia jest taka sama jak ta w przypadku narzędzia [Płaszczyzna tnąca](Std_ToggleClipPlane/pl.md), z tą różnicą, że ta płaszczyzna cięcia jest trwała. Zatem posiada tą samą cechę umożliwiania tylko przekrojów bez wypełnienia.



## Użycie

Aby utworzyć płaszczyznę cięcia, wciśnij przycisk **<img src="images/FEM_ClippingPlaneAdd.svg" width=16px> '''Płaszczyzna cięcia na ścianie'''** lub wybierz opcję **Narzędzia → <img src="images/FEM_ClippingPlaneAdd.svg" width=16px> Płaszczyzna cięcia na ścianie**. Można mieć wiele płaszczyzn cięcia.

Mimo że płaszczyzna jest trwała, nie pojawi się w [drzewie dokumentu](Tree_view/pl.md). Płaszczyzna pojawia się w widoku modelu w ten sposób:

<img alt="" src=images/FEM_Clipping-Plane-Example.png  style="width:400px;">

Aby przesunąć płaszczyznę, kliknij na dużym białym prostopadłościanie, który jest prostopadły do płaszczyzny i trzymaj przycisk myszy wciśnięty podczas poruszania nią.

Aby obracać i pochylać płaszczyznę, kliknij na linii, która łączy małe kostki z dużym białym prostopadłościanem i trzymaj przycisk myszy wciśnięty podczas poruszania nią.

Sześć małych kostek służy za uchwyty do zmiany rozmiaru. Ponieważ jednak obiekt jest nieskończoną płaszczyzną, jego rozmiar nie ma znaczenia.

Aby usunąć wszystkie płaszczyzny cięcia użyj narzędzia [Usuń wszystkie płaszczyzny cięcia](FEM_ClippingPlaneRemoveAll/pl.md). Nie ma możliwości usunięcia tylko wybranej płaszczyzny.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ClippingPlaneAdd/pl
