# Package Metadata/pl
{{TOCright}}

## Wprowadzenie

Począwszy od wersji 0.20 programu FreeCAD, zewnętrzne dodatki (środowiska pracy, makra i pakiety preferencji) mogą być dystrybuowane z plikiem metadanych opisującym zawartość pakietu. Jeżeli plik \"package.xml\" jest obecny, jest on odczytywany przez FreeCAD i jego zawartość jest wykorzystywana w różnych częściach interfejsu użytkownika. Obecnie jest on opcjonalny dla środowisk pracy i makrodefinicji, a wymagany dla pakietów preferencji. Ta strona dokumentuje format tego pliku metadanych. Format *(i zawartość tej strony Wiki)* są oparte na [REP 149](https   *//ros.org/reps/rep-0149.html).

## Ogólny format pliku 

This document currently describes file format version 1.

The metadata file must be a valid, well-formed XML 1.0 document. It must be called \"package.xml\", and must exist in the base directory of the software package\'s primary branch (as specified by the [FreeCAD-addons .gitmodules file](https   *//github.com/FreeCAD/FreeCAD-addons/blob/master/.gitmodules)) in its git repository. Only the package.xml file from the primary branch is considered by the Addon Manager. All understood XML tags are in lowercase, but unrecognized tags are **not** an error. Most tags are optional, and some only apply to certain types of package contents (for example, only Workbenches currently provide a \"classname\" element). Unneeded or unrecognized elements are ignored.

Any file path specified in package.xml must use the slash (\"/\") as the directory separator   * on systems that expect a different separator during execution (e.g. Windows) FreeCAD will automatically convert to the correct separator.

## Content elements 

### 

The only top-level element allowed is , and the file may only contain one  element. Immediately subordinate to that are several required or optional elements, defined here. No other tags are permitted directly under the  element.

    <package format="1" xmlns="https   *//wiki.freecad.org/Package_Metadata">

The  tag is the unique top-level tag in a package.xml file. All other tags are nested under it.

#### Attributes

-   format=\"NUMBER\"   * Specifying the package.xml format being used. For this interface, you must specify format=\"1\".
-   xmlns=\"NAMESPACE\"   * Specifies the XML namespace for this package, and must be included exactly as shown above, as a link to <https   *//wiki.freecad.org/Package_Metadata>.

#### Required child tags 

The top-level  element must contain at least the following tags   *

-   [](#.3Cname.3E.md)
-   [](#.3Cversion.3E.md)
-   [](#.3Cdate.3E.md)
-   [](#.3Cdescription.3E.md)
-   [](#.3Cmaintainer.3E.md) (multiple, but at least one)
-   [](#.3Clicense.3E.md) (multiple, but at least one)
-   [](#.3Cicon.3E.md)
-   [](#.3Ccontent.3E.md) (container element for package content items)

#### Optional child tags 

-   [](#.3Curl.3E.md) (multiple)
-   [](#.3Cauthor.3E.md) (multiple)
-   [](#.3Cdepend.3E.md) (multiple)
-   [](#.3Cconflict.3E.md) (multiple)
-   [](#.3Creplace.3E.md) (multiple)
-   [](#.3Ctag.3E.md) (multiple)
-   [](#.3Cfreecadmin.3E.md)
-   [](#.3Cfreecadmax.3E.md)
-   [](#.3Cpythonmin.3E.md)

###  

REQUIRED

The name of this package. Must only contain characters that are valid for filenames (disallowed characters are /\\?%\*   *|\"\<\> ).

###  

REQUIRED

A version number that follows either the [semantic versioning 2.0 standard](https   *//semver.org) (e.g. 1.0.2-beta) or the [CalVer style](https   *//calver.org/) (e.g. 2021.12.08). Note that you cannot include both types, and switching between types is not supported. Internally the code has no concept of which type is chosen, when comparing versions it performs a simple numerical comparison between each successive numeric component regardless of type. Note that this cannot be left blank, some kind of version number must be assigned. When the Addon Manager detects an increase in version number it will display the \"update available\" information to users.

###  

REQUIRED

The date of the current version, in the format YYYY-MM-DD or YYYY.MM.DD.

###  

REQUIRED

A concise (up to several sentences) text-only description of this package. No markup is supported.

###  

AT LEAST ONE REQUIRED (multiple allowed)

The name of the person maintaining the package. All packages require a maintainer. For orphaned packages see below.

#### Attributes 

-   email=\"name@domain.tld\" (required)   * Email address of the maintainer.

An orphaned package is one with no current maintainer. Orphaned packages should use the following maintainer information   *

    <maintainer email="no-one@freecad.org">No current maintainer</maintainer>

###  

AT LEAST ONE REQUIRED (multiple allowed)

Name of license for this package, e.g. BSD, GPL, LGPL. In order to assist machine readability, only include the license\'s SPDX short identifier (documented by OSI at [their site](https   *//opensource.org/licenses/alphabetical)). For multiple licenses multiple separate tags must be used. A package will have multiple licenses if different source files have different licenses. Every license occurring in the source files should have a corresponding  tag. For any explanatory text about licensing caveats, please use the  tag.

Most common open-source licenses are described on the [OSI website](https   *//opensource.org/licenses/alphabetical).

Commonly-used license strings   *

-    `"Apache-2.0"`
    

-    `"BSD-2-Clause"`
    

-    `"BSD-3-Clause"`
    

-    `"BSL-1.0"`
    

-    `"GPL-2"`
    

-    `"GPL-3"`
    

-    `"LGPL-2.1"`
    

-    `"LGPL-3"`
    

-    `"MIT"`
    

-    `"MPL-1.1"`
    

-    `"CC0v1"`(Public Domain dedication)

#### Attributes 

-    `file<nowiki>=</nowiki>"FILE"`(optional)   * A path relative to the `package.xml` file containing the full license text. Many licenses require including the license text when redistributing the software. E.g. the Apache License, Version 2.0 states in paragraph 4.1   * \"You must give any other recipients of the Work or Derivative Works a copy of this License\"

###  

REQUIRED

The  tag describes the actual contents of the package. It has no attributes, and contains any number of children. Those children can have arbitrary tag names, only some of which may be recognized by FreeCAD. FreeCAD currently supports \"workbench\", \"macro\", and \"preferencepack\" elements. Each child is then defined recursively by this standard, containing any or all of the elements allowed for the root  node. For example   *

    <content>
      <preferencepack>
        <name>Unicorn Sparkles Theme</name>
        <version>1.0.0</version>
        <url type="readme">https   *//github.com/chennes/FreeCAD-themes/blob/main/Unicorn%20Sparkles%20Theme/Readme.md</url>
        <icon>sparkles.svg</icon>
      </preferencepack>
    </content>

The existence of  items implies a set of subfolders, one for each content item, named exactly as the given name of the item. So for the example above, the package\'s folder structure is   *

    Package Directory/
      package.xml
      Unicorn Sparkles Theme/
        Unicorn Sparkles Theme.cfg
        sparkles.svg
        (the theme's other files)

In addition to the other elements of , content items can optionally provide information in , , and  tags (technically these can be provided to the root  tag as well, but they are generally unused there).

**Backwards-compatibility note**   * to avoid having to restructure packages that pre-date this metadata standard, the optional [](#.3Csubdirectory.3E.md) tag is allowed to specify \"./\" as the subdirectory for a content item, in which case no subdirectory is required. This matches the pre-standard system where a single workbench was located at the top of the directory structure.

####  

REQUIRED for Workbenches

The path to an icon file. If it is an icon for the top-level package this path is relative to the package.xml file itself. If the icon is an element of a  item, then the path is relative to the content\'s folder. The Addon Manager will display the top-level icon as the icon for the overall package. If no top-level icon is present, the first specified workbench icon will be used as the package icon.

####  

Optional.

Normally a content item is assumed to be located in a subdirectory with the same name as the item. In some cases, however, it is useful to explicitly specify the subdirectory. For example, many macros may be located within a single subdirectory, but each have their own entry in the package.xml file. It also provides backwards-compatibility support for packages that predate the package.xml file format specification, and do not follow the expected subdirectory structure. Often in these cases, a \"./\" is used to indicate that the item is not located in a subdirectory at all.

####  

REQUIRED for Workbenches

For workbenches, the name of the Python main entry class. This is the class that FreeCAD will try to load on startup to locate the workbench\'s icon, which should be set as a member variable of the class. For example, if your workbench defines the following class (usually in InitGui.py)   *


```python
class MyNewWB   *
    Icon = "resources/icon.svg"
```

then the package.xml file expects   *

    <classname>MyNewWB</classname>

####  

Optional

Provided for convenience to other tools, any number of other files may be listed here. Their use depends on the type of content. In a macro content item, each file entry is a single macro, and will be linked into the user\'s Macros installation directory by the [Addon Manager](Std_AddonMgr.md).

###  

Multiple allowed   * \"repository\" is required, and \"readme\"-type is highly recommended.

A Uniform Resource Locator for the package\'s website, bug tracker, source repository, zip download link, readme file, or documentation (as specified by the \"type\" attribute, see below).

When specifying the \"readme\" type, a direct link to a rendered version of the README should be provided. For example, on GitHub, this is a \"blob\"-type link such as \"<https   *//github.com/FreeCAD/FreeCAD-addons/blob/master/README.md>\", or on a GitLab instance, \"<https   *//gitlab.com/opensimproject/cfdof/-/blob/master/README.md>\" (note the slightly different URL format between the two).

It is a good idea to include  tags pointing users to your package\'s online resources. The website is commonly a wiki page on wiki.freecad.org where users can find and update information about the package, for example. The Addon Manager lists these URLs and provides clickable links to them in the package description.

#### Attributes 

-   type=\"TYPE\" (required)   * The type should be one of the following identifiers   * \"website\", \"bugtracker\", \"repository\", \"readme\", \"documentation\", or \"discussion\".
-   branch=\"BRANCH\" (required for type=\"repository\")   * The name of the branch to check out to obtain this package. Typically the name of your main development branch. May also specify any other type of git reference, e.g. a tag or specific commit.

###  

Multiple allowed

The name of a person who is an author of the package, as acknowledgement of their work and for questions.

#### Attributes 

-   email=\"name@domain.tld\" (optional)   * Email address of author.

###  

Multiple allowed

Declares a dependency on another FreeCAD Addon or internal workbench, or Python package. The named dependency is first checked against the list of known Addons (e.g. those available either from the official FreeCAD Addons git repository, or those in a custom user-specified repository). The check is against the canonical name of the Addon. If a package.xml file is present for that Addon, the name is that package\'s  element. An exact match is required. If no match is found it is checked against the list of known internal workbenches (both installed and uninstalled). Finally, if the named dependency has not been located in the previous two steps it is assumed to be a Python package dependency. Note that not all dependency-related features are fully implemented yet.

#### Attributes 

All dependencies and relationships may restrict their applicability to particular versions. For each comparison operator an attribute can be used. Two of these attributes can be used together to describe a version range.

-   version_lt=\"VERSION\" (optional)   * The dependency to the package is restricted to versions less than the stated version number.
-   version_lte=\"VERSION\" (optional)   * The dependency to the package is restricted to versions less or equal than the stated version number.
-   version_eq=\"VERSION\" (optional)   * The dependency to the package is restricted to a version equal than the stated version number.
-   version_gte=\"VERSION\" (optional)   * The dependency to the package is restricted to versions greater or equal than the stated version number.
-   version_gt=\"VERSION\" (optional)   * The dependency to the package is restricted to versions greater than the stated version number.
-   condition=\"CONDITION_EXPRESSION\"   * Every dependency can be conditional on a condition expression. If the condition expression evaluates to \"true\" the dependency is used and considered as if it doesn\'t have a condition attribute. If the condition expression evaluates to \"false\" the dependency is ignored and considered as if it doesn\'t exist. The expression must be a valid FreeCAD Expression (i.e. Python syntax), and may refer to the variables \"\$BuildVersionMajor\", \"\$BuildVersionMinor\", and \"\$BuildRevision\" representing the version of FreeCAD currently running.
-   optional=\"true\|false\"   * If \"optional\" is \"true\", then the dependency is treated as optional when the Addon is installed using the Addon Manager. In general this means that a failure to install the dependency does not prevent the Addon from installing, and the user may be prompted about whether they want to install it. Versions of FreeCAD prior to 0.21 do not recognize this attribute and will ignore it.
-   type=\"automatic\|addon\|internal\|python\"   * Optional, defaults to \"automatic\". Indicates what this dependency statement refers to. \"addon\" is for external addons, \"internal\" is for internal workbenches (e.g. \"arch\", \"sketcher\", etc.), and \"python\" indicates a Python package dependency. Versions of FreeCAD prior to 0.21 do not use this attribute, and \"automatic\" is always assumed.

###  

Multiple allowed

Declares a package name with which this package conflicts. This package and the conflicting package should not be installed at the same time.

#### Attributes 

See .

###  

Multiple allowed

Declares a package name that this package is intended to replace.

#### Attributes 

See .

###  

A simple text tag used for categorization when using a package manager. Multiple  elements may be specified.

###  

The minimum version of FreeCAD required to use this package/element, as a semantic version 2.0 string in the format MAJOR.MINOR.BUILD

###  

The maximum version of FreeCAD required to use package/element, as a semantic version 2.0 string in the format MAJOR.MINOR.BUILD

###  

(New in FreeCAD 0.21, ignored by previous versions.) The minimum version of Python required to use package/element, as a semantic version 2.0 string in the format MAJOR.MINOR. The Addon Manager will not permit an Addon to be installed on a system running a version of Python before this one. Only Python 3.x versions are supported. Although you may specify a three-component version, only the minor number is considered during the compatibility check.

## Sprawdzanie poprawności 

To validate your package.xml file you can enable \"developer mode\" in the Addon Manager   * create a boolean variable called \"developerMode\" in the \"Addons\" parameter group and set it to True   * **Tools → Edit parameters... → BaseApp → Preferences → Addons → developerMode**. When the Addon Manager has finished reading the Addons database it will examine all available package.xml files for errors.

## Examples

Note that comments (the text between `&lt;&#33;--` and `--&gt;`) are ignored by the XML parser, and are not a required part of the file format. They are provided here for information purposes and may be omitted from the final package.xml if desired.

A simple workbench-only package (for example, to add a metadata file to a package that predates this metadata format)   *

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https   *//wiki.freecad.org/Package_Metadata">
      <name>Legacy Workbench</name> 
      <description>Text that the Addon Manager shows for the Addon. Any length, but remember that Addon Manager's compact view only shows the first sentence or so.</description>
      <version>1.0.1</version> 
      <date>2022-01-07</date> 
      <maintainer email="your_address@null.com">Your Name</maintainer>
      <license file="LICENSE">LGPL-2.1</license> 
      <url type="repository" branch="main">https   *//github.com/chennes/FreeCAD-Package</url> 
      <url type="readme">https   *//github.com/chennes/FreeCAD-Package/blob/main/README.md</url> 
      <icon>Resources/icons/PackageIcon.svg</icon> 

      <content>
        <workbench>
          <classname>MyLegacyWorkbench</classname> 
          <subdirectory>./</subdirectory>
        </workbench>
      </content>

    </package>

A complex, multi-component package   *

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https   *//wiki.freecad.org/Package_Metadata">
      <name>Example Package Format</name>
      <description>An example of the package.xml file format</description>
      <version>2022.01</version>
      <date>2022-01-07</date>
      <maintainer email="no-one@freecad.org">No Maintainer</maintainer>
      <license file="LICENSE">GPL-3</license>
      <url type="repository" branch="main">https   *//github.com/chennes/FreeCAD-Package</url>
      <icon>PackageIcon.svg</icon>

      <content>
        <preferencepack>
          <name>FreeCAD Classic Colors</name>
          <description>FreeCAD default colors for core app and included Mods.</description>
          <version>1.0.0</version>
          <tag>color</tag>
          <tag>stylesheet</tag>
        </preferencepack>
        <workbench>
          <name>Metadata Creation Workbench</name>
          <description>A set of tools to assist in creation of package.xml metadata files</description>
          <classname>MetadataCreationWorkbench</classname>
          <subdirectory>MCW</subdirectory>
          <icon>Resources/mcw.svg</icon>
          <tag>developers</tag>
          <version>0.9.0-alpha</version>
        </workbench>
        <macro>
          <name>Problem Solver 9000</name>
          <description>Deletes all emails in your inbox</description>
          <subdirectory>./</subdirectory>
          <file>PS9000.FCMacro</file>
        </macro>
      </content>

    </package>

A package with dependencies   *

    <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <package format="1" xmlns="https   *//wiki.freecad.org/Package_Metadata">
      <name>Example with Dependencies</name>
      <description>An example of the package.xml file format</description>
      <version>1.0.1-beta3</version>
      <date>2022-01-07</date>
      <maintainer email="no-one@freecad.org">No Maintainer</maintainer>
      <license file="LICENSE">GPL-3</license>
      <url type="repository" branch="main">https   *//github.com/chennes/FreeCAD-Package</url>
      <icon>PackageIcon.svg</icon>

      <content>
        <workbench>
          <name>Metadata Creation Workbench</name>
          <description>A set of tools to assist in creation of package.xml metadata files</description>
          <classname>MetadataCreationWorkbench</classname>
          <subdirectory>MCW</subdirectory>
          <icon>Resources/mcw.svg</icon>
          <tag>developers</tag>

          <depend>FEM</depend>
          <depend version_gte="0.3.0">Curves workbench</depend>
          <depend version_gte="3.3" version_lt="4">Steel column</depend>

          
          <depend optional="true" type="python">markdown</depend>
          <depend type="addon">TabBar</depend>

          
          <replace>Metadata Creation Workbench Beta</replace>

          
          <conflict condition="$BuildRevision==24267">Do not use with build 24267</conflict> 

          
          <depend>matplotlib</depend>
          <depend>some_other_package</depend> 
        </workbench>
      </content>

    </package>




[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Package Metadata/pl
