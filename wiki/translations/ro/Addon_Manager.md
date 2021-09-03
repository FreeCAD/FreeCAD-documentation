---
- GuiCommand:/ro
   Name:Std AddonMgr
   Name/ro:Addon manager
   Icon:AddonManager.svg
   MenuLocation:Tools → Addon manager
   Workbenches:''None''
   SeeAlso:[Macros](Macros/ro.md), [External workbenches](External_workbenches/ro.md)
   Version:0.17
---


</div>

## Description


<div class="mw-translate-fuzzy">

[Addon Manager](AddonManager.md) "-gestionarul de extensii-" este un instrument pentru a instala și administra [external workbenches](external_workbenches/ro.md) atelierele de lucru și [macros](macros/ro.md) oferite de comunitatea FreeCAD. Dacă pachetul [git-python](https://github.com/gitpython-developers/GitPython) este instalat pe computer, Managerul de aplicații addon îl va utiliza pentru a actualiza atelierele de lucru instalate, făcând descărcările mai rapide.


</div>

Addons that are marked as {{emphasis|Python 2 Only}} will not work in FreeCAD version 0.19 or higher.

Due to changes to the GitHub platform in the year 2020 the Addon manager no longer works if you use FreeCAD version 0.17 or earlier. You need to upgrade to version [0.18.5](https://github.com/FreeCAD/FreeCAD/releases/tag/0.18.5) or a recent [0.19](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19_pre) version. Alternatively you can install addons manually, see [Notes](#Notes.md) below.

![](images/Std_AddonMgr_dialog.png )


<div class="mw-translate-fuzzy">

![](images/Addon_Manager_example.png ) *Interface of the [Addon Manager](Addon_Manager/ro.md)*


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}


</div>


<div class="mw-translate-fuzzy">

-   Deschideți meniul de instrumente {{MenuCommand|Tools → Addon manager}}.
-   Pentru a instala un atelier sau o macro: derulați în jos lista și selectați atelierul de completare. O scurtă descriere a atelierului suplimentar va fi afișată sub listă, precum și link-ul către pagina complementară. Apoi apăsați butonul **Install/update** pentru a instala noul instrument. Pentru macro-uri, faceți clic pe tab-ul {{MenuCommand|Macros}} și repetați pașii.
-   Pentru a elimina un atelier sau macro parcurgeți lista, selectați atelierul sau add-on și apăsați butonul **Install/update** .
-   Pentru a actualiza un atelier sau macro parcurgeți, selectați plugin-ul și apăsați butonul **Install/update**.
-   Pentru a verifica actualizările apăsați **<img src=images/Std_Refresh.png style="width:16px"> Refresh** Actulaizările disponibile vor fi raportatea în partea de jos a listei. Apăsați **<img src=images/Std_Refresh.png style="width:16px"> Refresh** pentru a instala odată toate actualizările

**Note:** Notă: pictograma poate să arate diferit în funcție de sistemul dvs. de operare. Actualizările disponibile vor fi raportate în listă. 

-   Pentru a rula o macrocomandă: instalați mai întâi macroul dorit, apoi selectați din nou din listă, apoi apăsați butonul **Execute**.
-   Apăsați butonul **Close** pentru a ieși din manager.


</div>

## Options

The Addon manager dialog box has two tabs on the left, one listing the available workbenches and the other listing the available macros. The information panel on the right will display the homepage of the selected addon.

### Uninstall

1.  Select an installed addon on the <img alt="" src=images/Folder.svg  style="width:16px;"> **Workbenches** tab or the <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macros** tab.
2.  Press the **<img src="images/Delete.svg" width=16px> Uninstall selected** button.

### Install/update

1.  Select an addon on the <img alt="" src=images/Folder.svg  style="width:16px;"> **Workbenches** tab or the <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macros** tab.
2.  Press the **<img src="images/Edit_OK.svg" width=16px> Install/update selected** button.
3.  If you want to add a macro to a custom toolbar then don\'t forget to manually download the icon image file, if available, by clicking on the link on the homepage in the information panel. See [Interface Customization](Interface_Customization#Toolbars.md).
4.  To change the position of an addon workbench in the [Workbench selector](Std_Workbench.md) list see [Interface Customization](Interface_Customization#Workbenches.md).

### Configuration

1.  Press the **<img src="images/Preferences-general.svg" width=16px> Configure...** button.
2.  The Addon manager options dialog box opens.
3.  Optionally check the {{CheckBox|TRUE|Automatically check for updates at start (requires GitPython)}} checkbox.
4.  Optionally add repositories to the **Custom repositories** list. Addons from these repositories will be added on the <img alt="" src=images/Folder.svg  style="width:16px;"> **Workbenches** tab or the <img alt="" src=images/Applications-python.svg  style="width:16px;"> **Macros** tab.
5.  Optionally choose proxy settings.
6.  Press the **OK** button or the **Cancel** button to close the dialog box.

## Notes

-   The use of addons is not restricted to the FreeCAD version they were installed from. You will also be able to use them in any other FreeCAD version, supported by the addon, that you may have on your system.
-   The addons available in the Addon manager are not part of the official FreeCAD program and are not supported by the core FreeCAD development team. You should read the provided information carefully to make sure you know what you are installing.
-   Bug reports and feature requests should be made directly to the creator of the addon by visiting the indicated website. Many addon developers are regular users of the [FreeCAD forum](https://forum.freecadweb.org), and can also be contacted there.
-   If the [GitPython](https://github.com/gitpython-developers/GitPython) package is installed on your computer the Addon manager will make use of it, making downloads faster.
-   You can also install addons manually. See [How to install additional workbenches](How_to_install_additional_workbenches.md) and [How to install macros](How_to_install_macros.md).

## Information for developers {#information_for_developers}


<div class="mw-translate-fuzzy">

Dacă ați dezvoltat un atelier de lucru sau o macrocomandă și doriți să îl vedeți inclus în Addon Manager, citiți cum să faceți acest lucru în paginile de depozitului ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) și [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). Dacă adăugați macrocomanda în [Macros recipes](Macros_recipes/ro.md), nu mai este nimic altceva de făcut, acesta va fi selectat automat de către Addon Manager.


</div>

### Python workbenches {#python_workbenches}


<div class="mw-translate-fuzzy">

Pentru atelierele de lucru python, nu aveți nevoie de aprobarea specifică pentru a adăuga atelierul dvs. de lucru la Addon Manager și, în afara codului sursă al FreeCAD, puteți alege licența dorită. Dacă cereți ca atelierul dvs. de lucru să fie adăugat pe listă (nu vom adăuga un nou atelier de lucru fără o solicitare din partea autorilor săi), fie prin solicitarea acestuia pe forum, fie prin deschiderea unei probleme în [/ FreeCAD / FreeCAD-addons / FreeCAD-addons](https://github.com), codul dvs. va rămâne pe propriul depozit git, îl vom adăuga ca submodul la [FreeCAD- addons](https://github.com/FreeCAD/FreeCAD-addons/) repository. Desigur, înainte de a adăuga atelierul dvs. de lucru, vom examina acest lucru și vă vom asigura că nu există nimic potențial problematic cu acesta.


</div>

### C++ workbenches {#c_workbenches}


<div class="mw-translate-fuzzy">

Dacă dezvoltați un aelier de lucru în C ++, acesta nu poate fi rulat direct de către utilizatori și trebuie compilat mai întâi. Apoi, aveți două opțiuni, fie că furnizați dvs. înșiși versiuni precompilate ale atelierului dvs. de lucru, fie pentru diferite sisteme de operare, fie că doriți să introduceți codul sursă în codul sursă al FreeCAD. Pentru aceasta, ar trebui să utilizați licența LGPL (sau pe deplin compatibilă ca MIT sau BSD) și trebuie să prezentați noile instrumente comunității pe forumul [FreeCAD](https://forum.freecadweb.org) pentru examinare. Odată ce codul dvs. a fost testat și aprobat, ar trebui să bifurcați depozitului FreeCAD, dacă nu ați făcut-o deja, pentru a crea o nouă ramură, în care să puneți codul și să solicitați, astfel încât ramura dvs. să fuzioneze în depozitul principal.


</div>





{{Std Base navi

}}  
