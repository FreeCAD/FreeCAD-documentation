




Nejsnadnější způsob instalace FreeCADu na Windows je stáhnout níže uvedený instaler.


{{DownloadWindowsStable}}


{{DownloadWindowsStable}}

Po stažení souboru .msi (Microsoft Installer) jenom na něj dvojklikněte a spusťte instalační proces.

Dále jsou další informace o technických volbách. Jestli se Vám zdají strašidelné, žádný problém! Většina uživatelů Windows nebude k instalaci FreeCADu potřebovat nic víc než nainstalovat .msi a **[ začít](Getting_started/cs.md)**!

### Jednoduchá instalace s Microsoft Installerem 

Nejsnadnější způsob **instalace FreeCADu na Windows** je použít výše uvedný instaler. Tato stránka popisuje použití a vlastnosti *Microsoft Installeru* s dalšími instalačními volbami.

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

Chcete-li stáhnout buď 64-bitovou verzi nebo nestabilní vývojovou verzi podívejte se na stránku [Download](Download.md).

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


```python
choco install freecad
```

every once in a while you can update your software with


```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### Instalace z příkazové řádky 

Při použití příkazové utility *msiexec.exe* jsou dostupné další možnosti, jako jsou neinteraktivní instalace a administrátorská instalace.

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### Neinteraktivní instalace 

z příkazové řádky

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

instalace může být iniciována programově. Dodatečné parametry mohou být vloženy na konec příkazové řádky jako


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### Omezený uživatelský interface 

Množství uživatelského interface, který je zobrazován instalerem může být řízeno volbou /q, hlavně:

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - Žádný interface
-   /qb - Základní interface - pouze malý dialog při postupu
-   /qb! - Jako /qb, ale je skryto tlačítko Cancel
-   /qr - Omezený interface - zobrazuje všechny dialogy, které nevyžadují uživatelskou reakci (přeskakuje všechny modální dialogy (vyžadující odpověď))
-   /qn+ - Jako /qn, ale na konci zobrazí dialogové okno \"Completed(Hotovo)\"
-   /qb+ - Jako /qb, ale na konci zobrazí dialogové okno \"Completed(Hotovo)\"


</div>

#### Cílový adresář 

Vlastnost TARGETDIR určuje základní adresář pro instalaci FreeCADu. Například jiný disk pro instalaci může být specifikován takto

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

Defaultní TARGETDIR je \[WindowsVolume\\Programm Files\\\]FreeCAD.

#### Instalace pro všechny uživatele 

Přidání

Adding


```python
ALLUSERS=1
```

provede instalaci pro všechny uživatele. Standardně neinteraktivní instalace nainstaluje balíček právě jen pro aktuálního uživatele a interaktivní instalace nabízí dialog s přednastavením pro \"všechny uživatele\" pokud má aktuální uživatel dostatečná oprávnění.

#### Výběr vlastností 

K dispozici je spousta možností vyběru k instalaci, reinstalaci nebo odstranění. Seznam možností pro FreeCAD instaler je

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - instaluje odpovídající software plus základní knihovny
-   Documentation - instaluje dokumentaci
-   Source code - nainstaluje i zdrojové kódy
-   \... ToDo

navíc, ALL specifikuje všechny možnosti. Všechny možnosti závisejí na DefaultFeature, takže instalace jakékoliv vlastnosti instaluje i všechny defaultní vlastnosti. Následující vlastnosti řídí vlastnosti, které budou nainstalovány nebo odstraněny

-   ADDLOCAL - seznam vlastností, které budou nainstalovány na lokálním počítači
-   REMOVE - seznam vlastností, které budou odstraněny
-   ADDDEFAULT - seznam vlastností, které budou přidány k defaultní konfiguraci (která je lokální pro všechny vlastnosti FreeCADu)
-   REINSTALL - seznam vlastností, které budou reinstalovány /opraveny
-   ADVERTISE - seznam vlastností, které budou prováděny při propagační instalaci

Zde je několik dostupných dodatečných vlastností; podívejte se na MSDN dokumentaci na detaily.

S těmito volbami, přidáním


```python
ADDLOCAL=Extensions
```

instaluje samotný interpreter a registruje rozšíření, ale neinstaluje nic dalšího.

### Odinstalace

Pomocí

With


```python
msiexec /x FreeCAD<version>.msi
```

může být FreeCAD odinstalován. Pro odinstalaci není nutné mít dostupný MSI soubor; alternativně může být specifikován balíček nebo kód produktu. Kód produktu můžete nalézt, když se podíváte na vlastnosti odkazu Uninstal, který FreeCAd nainstaluje do startovního menu.

### Administrátorská instalace 

Pomocí

With


```python
msiexec /a FreeCAD<version>.msi
```

může být spuštěna \"administrátorská\" (sťová) instalace. Soubory jsou rozbalené v cílovém adresáři (měl by to být síťový adresář), ale na lokálním počítači nejsou provedeny žádné modifikace. Navíc je v cílovém adresáři vygenerován další (menší) msi soubor, který potom mohou klienti použít k provedení lokálních instalací (budoucí verze by měly také nabízet zachování některých vlastností společně na síťovém disku).

V současnosti není žádné uživatelské rozhraní pro administrátorskou instalaci, takže cílový adresář musí být zadán z příkazové řádky.

K dispozici není pro administrátorskou instalaci ani žádná odinstalační procedura, takže se jen smaže cílový adresář, pokud jej ještě nepoužívá nějaký klient.

### Propagace

Pomocí

With


```python
msiexec /jm FreeCAD<version>.msi
```

by mělo být v podstatě možné \"propagovat\" FreeCAD na počítači (s /ju na uživateli). Výsledkem je to, že ve startovním menu se zobrazuje ikona FreeCADu a jsou registrována rozšíření, ale ve skutečnosti naní nainstalován žádný software. První použití této vlastnosti zapříčiní, že tato vlastnost bude nainstalována.

V současnosti instaler FreeCADu podporuje pouze propagaci ve startovním menu ale ne v odkazech.

### Automatická instalace na skupině počítačů 

S Windows Group Policy je možné automaticky nainstalovat FreeCAD na skupinu počítačů. K tomu je potřeba udělat následující kroky:

1.  Nalogovat se na domain controller
2.  Zkopírovat soubor MSI do složky, která má sdílený s přístup na všechny cílové počítače.
3.  Otevřít MMC snapin \"Active Directory users and computers\"
4.  Přejít na skupinu počítačů, které potřebují FreeCAD
5.  Otevřít vlastnosti
6.  Otevřít Skupinovou politiku (Group Policies)
7.  Přidat novou politiku a upravit ji
8.  V Computer Configuration/Software Installation, vybrat New/Package
9.  Vybrat soubor MSI přes síťovou cestu
10. Volitelně, vybrat že chcete FreeCAD odinstalovat pokud se počítač dostane z dosahu této politiky.

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

Propagace Skupinové politiky typicky zabere nějaký čas - ke spolehlivému rozšíření balíčku by měly být restartovány všechny počítače.

### Instalace na Linux použitím Crossover Office 

Na Linuxový systém můžete nainstalovat windowsovskou verzi FreeCADu použitím *CXOffice 5.0.1*. Spusťte *msiexec* z příkazového řádku CXOffice, předpokládá se, že instalační balíček je umístěn v \"softwarovém\" adresáři, který je namapován na disk \"Y:\":

.msi

FreeCAD běží, ale je oznámeno, že OpenGL display nefunguje, podobně jako u jiných programů běžících pod [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia:SketchUp.md).


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia:SketchUp.md).


<div class="mw-translate-fuzzy">


{{docnav/cs|[Seznam charakteristických vlastností](Feature_list/cs.md)|[Instalace na Unix](Install_on_Unix/cs.md)}}


</div>



