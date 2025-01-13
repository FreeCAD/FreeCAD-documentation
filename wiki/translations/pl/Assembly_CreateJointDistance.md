---
 GuiCommand:
   Name: Assembly CreateJointDistance
   Name/pl: Złożenie Utwórz połączenie dystansowe
   MenuLocation: Złożenie , Utwórz połączenie dystansowe
   Workbenches: Assembly_Workbench/pl
   Shortcut: **D**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointDistance/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateJointDistance.svg  style="width:24px;"> [Utwórz połączenie dystansowe](Assembly_CreateJointDistance/pl.md) tworzy połączenie dystansowe między dwiema wskazanymi częściami, blokując odległość między nimi.



## Użycie

1.  Opcjonalnie wybierz dwa obiekty geometryczne należące do dwóch różnych kształtów. Inne wskazania będą odrzucane.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateJointDistance.svg" width=16px> [Utwórz połączenie dystansowe](Assembly_CreateJointDistance/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateJointDistance.svg" width=16px> Utwórz połączenie dystansowe** z menu.
    -   Użyj skrótu: **D**.
3.  Okno dialogowe **Utwórz połączenie** zostanie otwarte w [panelu zadań](Task_panel/pl.md), wymieniając wskazane wcześniej obiekty.
4.  Dla dalszych kroków zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Użycie.md).



## Uwagi

Podpowiedź narzędzia mówi, że odległość 0 powoduje współpłaszczyznowe połączenie między wybranymi elementami płaskimi lub połączenie styczne między elementem cylindrycznym i płaskim. Żadne z tych rozwiązań nie działa w wydaniu cotygodniowym 0.22. -- .37645.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Distance** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Właściwości.md) aby znaleźć dodatkowe właściwości.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointDistance/pl
