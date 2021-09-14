# Installing on Windows/sv






The easiest way to install FreeCAD on Windows is to download the installer below. {{DownloadWindowsStable}} Det lättaste sättet att **installera FreeCAD på Windows** är genom att använda installeraren. Denna sida beskriver hur man använder den och egenskaperna av *Microsoft Installeraren* för mer installationsalternativ.

### Enkel Installation 

FreeCAD installeraren levereras i .msi (Windows Installer) format.

Du kan ladda ned den senaste .msi filen från [den officiella FreeCAD nedladdningssidan](http://sourceforge.net/project/showfiles.php?group_id=49159&package_id=206659).

Efter att du har laddat ned filen, dubbelklicka på den för att starta installationsprocessen.


{{DownloadWindowsStable}}

After downloading the .exe (NSIS Installer) file, double-click on it to start the installation process.

Below is more information about some technical options. Nevertheless, most users don\'t need more than the above .exe files. Head to [Get started](Getting_started.md) after installation is complete.

## Simple NSIS Installer Installation 

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

If you would like to download either a 64 bit or unstable development version, see the [Download](Download.md) page. [Download/sv](Download/sv.md)

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

### Kommandolinje Installation 

Med *msiexec.exe* kommandolinje programmet, så finns ytterligare funktioner tillgängliga, som o-interaktiv installation och administrativ installation.

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### O-interaktiv Installation 

Med kommandoraden

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

installation kan startas via ett program. Extra parametrar kan läggas till i slutet på denna kommandorad, som


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### Begränsat användargränssnitt 

Det användargränssnitt som installeraren visar kan kontrolleras med /q alternativ, som:

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - Inget gränssnitt
-   /qb - Grundläggande gränssnitt - endast en liten förloppsdialog
-   /qb! - Som /qb, men göm Avbryt knappen
-   /qr - Reducerat gränssnitt - visar alla dialoger som inte kräver svar från användaren (skippa alla modala dialoger)
-   /qn+ - Like /qn, men visa \"Färdig\" dialogen vid slutet
-   /qb+ - Like /qb, men visa \"Färdig\" dialogen vid slutet


</div>

#### Målkatalog

Egenskapen TARGETDIR avgör FreeCAD installationens rotkatalog. Till exempel, en annan installationsenhet kan specificeras med

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

Standard TARGETDIR är \[WindowsVolume\\Program\\\]FreeCAD.

#### Installation för Alla användare 

Genom att lägga till

Adding


```python
ALLUSERS=1
```

så installeras programmet för alla användare. Som standard, så installerar den o-interaktiva installeraren paketet endast för den nuvarande användaren, och den interaktiva installeraren visar en dialog som har \"alla användare\" som standard, om användaren har tillräckliga rättigheter.

#### Val av funktioner 

Ett antal egenskaper tillåter val av vilka funktioner som ska installeras, ominstalleras, eller tas bort. Funktionerna för FreeCAD installeraren är

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - installera mjukvaran korrekt, plus kärnbiblioteken
-   Documentation - installera dokumentationen
-   Source code - installera källkoden
-   \... ToDo

I tillägg, så specificerar ALL alla funktioner. Alla funktioner beror på DefaultFeature, så när en funktion installeras, så installeras även standardfunktionen automatiskt. Följande egenskaper kontrollerar vilka funktioner som ska installeras eller tas bort

-   ADDLOCAL - lista på funktioner som ska installeras på den lokala maskinen
-   REMOVE - lista på funktioner som ska tas bort
-   ADDDEFAULT - lista på funktioner som ska läggas till i dess standardkonfiguration (vilket är lokal för alla FreeCAD funktioner)
-   REINSTALL - lista på funktioner som ska ominstalleras/repareras
-   ADVERTISE - lista på funktioner som ska annonsera en installation

Det finns en del ytterligare alternativ tillgängliga; se MSDN dokumentationen för detaljer.

Med dessa alternativ, genom att lägga till


```python
ADDLOCAL=Extensions
```

installerar själva tolken och registrerar extensionerna, men installerar inget annat.

### Avinstallering

Med

With


```python
msiexec /x FreeCAD<version>.msi
```

så kan FreeCAD avinstalleras. Det är inte nödvändigt att ha MSI filen tillgänglig för avinstalleringar; alternativt så kan även paketet eller produktkoden specificeras. Du kan hitta produktkoden genom att titta på avinstalleringsgenvägens egenskaper som FreeCAD installerar i startmenyn.

### Administrativ installation 

Med

With


```python
msiexec /a FreeCAD<version>.msi
```

så kan en \"administrativ\" (nätverks) installation startas. Filerna packas upp till målkatalogen (vilken ska vara en nätverkskatalog), men inga andra ändringar görs på det lokala systemet. Dessutom genereras en annan (mindre) msi fil i målkatalogen, vilken klienter sedan kan använda för att utföra en lokal installation (framtida versioner kan också erbjuda att behålla vissa funktioner på nätverksenheten).

För närvarande finns det inget användargränssnitt för administrativa installationer, så målkatalogen måste specificeras på kommandolinjen.

Det finns ingen specifik avinstallationsprocedur för en administrativ installation - radera bara målkatalogen om inga klienter använder den längre.

### Annonsering

Med

With


```python
msiexec /jm FreeCAD<version>.msi
```

så är det i princip möjligt att \"annonsera\" FreeCAD till en maskin (med /ju till en användare). Detta gör att ikonerna syns i startmenyn, och extensionerna registreras, utan att någon mjukvara installeras. Det första användandet av en funktion orsakar en installation av densamma.

FreeCAD installeraren stödjer för närvarande endast annonsering till startmenyn, men inga annonseringar av genvägar.

### Automatisk Installation på en maskingrupp 

Med Windows Group Policy, så är det möjlig att automatiskt installera FreeCAD på en grupp av maskiner. För att göra det, utför följande steg:

1.  Logga in på domän controllern
2.  Kopiera MSI filen till en delad mapp som alla målmaskiner har åtkomst till.
3.  Öppna MMC snapin \"Active Directory users and computers\"
4.  Navigera till den datorgrupp som behöver FreeCAD
5.  Öppna egenskaper
6.  Öppna Group Policy
7.  Lägg till en ny policy, och redigera den
8.  I datorkonfiguration/Mjukvaruinstallation, välj Ny/Paket
9.  Välj MSI filen i nätverkssökvägen
10. Välj alternativt att du vill att FreeCAD ska avinstalleras om datorn lämnar policyns område.

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

Grupp policy propagering brukar ta lite tid - för att distribuera paketet pålitligt, starta om samtliga maskiner.

### Installation på Linux om du använder Crossover Office 

Du kan installera windows versionen av FreeCAD på ett Linux system genom att använda *CXOffice 5.0.1*. Kör *msiexec* frånCXOffice\'s kommandolinje, det antas att installationspaketet finns i \"software\" katalogen som är mappad till enhetsbokstaven \"Y:\":


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia:SketchUp.md).


<div class="mw-translate-fuzzy">


{{docnav/sv|Feature list/sv|Install on Unix/sv}}


</div>



