---
- GuiCommand:Addon
   Name:BIM Project
   Workbenches:<img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench.md)
   Addon:BIM
   MenuLocation:Manage → Project
---


</div>

## Descriere

<img alt="" src=images/BIM_project_screenshot.png  style="width:1024px;">

Dialogul de configurare a proiectului este un dialog cu asistent/expert care vă permite să creați un set de bază de obiecte de ghidare în documentul curent sau într-un document nou, care vă va ajuta să începeți să modelați un proiect BIM.

Dialogul de configurare a proiectului poate crea:


<div class="mw-translate-fuzzy">

-   O nouă [ document](Document_structure.md). Alternativ, celelalte obiecte vor fi create în documentul deschis în prezent.
-   Un site [site](Arch_Site.md). Obiectul site-ului reprezintă o zonă de teren în care va fi amplasat proiectul. Puteți să-i dați un număr de proprietăți utile, cum ar fi adresa străzii și coordonatele pământului. La crearea, site-ul este doar un container gol pentru alte obiecte BIM, dar un obiect 3D reprezentând terenul real poate fi atașat ulterior la acesta.
-   O [building](Arch_Building.md). Obiectul Clădire este un container pentru toate obiectele BIM care vor aparține aceleiași clădiri. Puteți defini un tip de clădire și să-i dați dimensiuni rectangulare brute, care vor fi reprezentate drept un dreptunghi desenat pe plan (X, Y).
-   Un set de axuri [Axe arc](Axe_arc.md), prin definirea numărului și distanței lor. Axele sunt folosite ca linii directoare pentru alinierea obiectelor 2D și 3D. Aceste axe pot fi modificate sau se pot introduce noi axe mai târziu.
-   Un set de [ BuildingParts](Arch_BuildingPart.md) pentru a reprezenta nivele. BuildingParts sunt obiecte generice de containere BIM care pot fi folosite pentru a grupa alte obiecte BIM într-un număr de moduri semnificative, cum ar fi componente repetate sau niveluri de clădiri.
-   Un set de grupuri [groups](Group.md) implicite în fiecare nivel. Grupurile pot fi utilizate pentru a vă organiza obiectele BIM în categorii mai clare, cum ar fi \"Pereți\" sau \"Coloane\". Ele nu au nici un impact asupra modelului în sine, dar de multe ori ajută la a face structura modelului dvs. mai clară atunci când conține o mulțime de obiecte.


</div>

### Templates


<div class="mw-translate-fuzzy">

După ce ați completat diferitele opțiuni, conținutul expertului de configurare a proiectului BIM poate fi salvat ca șablon. Aceste șabloane pot fi \"restaurate\" și adaptate ulterior. Șabloanele de proiect sunt stocate ca fișiere text în folderul de utilizatori FreeCAD.


</div>

Alternatively, you can also save the contents of the current document as a template. This will save the currently opened document as a standard **.FCStd** file, but also include additional BIM settings like the current working plane, or current units. By using the **restore** option anytime, the contents of that template file will be merged into the active document and all settings found in it applied.
