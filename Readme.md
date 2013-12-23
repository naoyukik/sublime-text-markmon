Sublime Text 2/3 - Marked App Menu plugin
=========================================

Adds a handy menu item that opens [Marked.app](http://markedapp.com/).

![screenshot](http://i.imgur.com/oCEb7.jpg)

Adapted from the excellent [Github for mac](https://github.com/csytan/sublime-text-2-github) plugin for Sublime Text by Chris Tan. Originally developed by [jocelynmallon](https://github.com/jocelynmallon), now supported by [icio](https://github.com/icio).


## Installation Instructions

**Package Installer:**

* Install [Sublime Package Control](http://wbond.net/sublime_packages/package_control)
* Select "Package Control: Install Package" from the Command Palette (⌘⇧P)
* Find "Marked.app Menu" and select

**Manually:**

* Install [Marked.app](http://markedapp.com/) ([App Store](http://itunes.apple.com/us/app/marked/id448925439?ls=1&mt=12))
* Download [sublime-text-marked](https://github.com/icio/sublime-text-marked/zipball/master) and copy unzipped folder to your Sublime Text packages folder (Sublime Text (2) → Preferences → Browse Packages...)
* Restart Sublime Text

```bash
# For Sublime Text 2
cd ~/Library/Application Support/Sublime Text 2/Packages
mkdir Marked.app\ Menu
curl -L https://github.com/icio/sublime-text-marked/tarball/master | tar --strip-components 1 -C Marked.app\ Menu -xvf -
```


## Usage

With the view selected containing the file you wish to preview in Marked:

**Command Palette:**

* Select "Marked" from the Command Palette (⌘⇧P)

**Keyboard Shortcut:**

* Add the following to your User Key Binding, adjusting the key configuration to taste:

    ```json
    { "keys": ["super+alt+m"], "command": "marked" }
    ```

**Menus:**

* Select Tools → Marked
