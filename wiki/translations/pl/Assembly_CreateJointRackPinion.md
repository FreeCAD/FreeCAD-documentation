---
 GuiCommand:
   Name: Assembly CreateJointRackPinion
   Name/pl: Złożenie Utwórz połączenie zębatki i koła zębatego
   MenuLocation: Złożenie , Utwórz połączenie zębatki i koła zębatego
   Workbenches: Assembly_Workbench/pl
   Shortcut: **Q**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointRackPinion/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateJointRackPinion.svg  style="width:24px;"> [Utwórz połączenie zębatki i koła zębatego](Assembly_CreateJointRackPinion/pl.md) tworzy połączenie zębatki i koła zębatego, które wiąże przesunięcie części połączenia typu Przesuwne i obrót części połączenia typu Obrotowe.



## Użycie

1.  Opcjonalnie wybierz dwa obiekty geometryczne należące do dwóch różnych części, które wcześniej były użyte do zdefiniowania połączeń typu Przesuwne i Obrotowe.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateJointRackPinion.svg" width=16px> [Utwórz połączenie zębatki i koła zębatego](Assembly_CreateJointRackPinion/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateJointRackPinion.svg" width=16px> Utwórz połączenie zębatki i koła zębatego** z menu.
    -   Użyj skrótu: **Q**.
3.  Okno dialogowe **Utwórz połączenie** zostanie otwarte w [panelu zadań](Task_panel/pl.md), wymieniając wcześniej wskazane obiekty.
4.  Dla dalszych kroków zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Użycie.md).



## Uwagi

-   Promień skoku odnosi się do okręgu podziałowego koła zębatego. Jest przechowywany we właściwości **Distance** i jest podstawą do wyznaczenia stosunku między obrotem i przesunięciem.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **RackPinion** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Właściwości.md) aby znaleźć dodatkowe właściwości.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointRackPinion/pl
