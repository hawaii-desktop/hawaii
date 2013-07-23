# File whose presence means the submodule was already configured
COOKIENAME_CONFIGURE = ".hawaii-ci-configure-cookie"

# File whose presence means the submodule was already built
COOKIENAME_BUILD = ".hawaii-ci-build-cookie"

# Modules
MODULES = [
    "kde-extra-cmake-modules",
    "kde-solid",
    "kde-libkdeqt5staging",
    "kde-kcoreaddons",
    "kde-kconfig",
    "kde-karchive",
    "qtxdg",
    "qt-accountsservice-addon",
    "polkit-qt-1",
    "vibe",
    "widget-styles",
    "icon-themes",
    "wallpapers",
    "fluid",
    "greenisland",
    "shell",
    "shell-weston-plugins",
    "swordfish",
    "system-preferences",
    "archiver",
    "eyesight",
    "terminal",
    "cinema",
    "widget-factory",
]

# Ignore modules
IGNORED_MODULES = [
    "kde-karchive",
    "vibe",
    "greenisland",
    "archiver",
    "terminal"
]

# Dependencies
DEPENDENCIES = {
    "kde-extra-cmake-modules": "",
    "kde-solid": "kde-extra-cmake-modules",
    "kde-libkdeqt5staging": "kde-extra-cmake-modules",
    "kde-kcoreaddons": "kde-libkdeqt5staging",
    "kde-kconfig": "kde-extra-cmake-modules,kde-libkdeqt5staging,kde-kcoreaddons",
    "kde-karchive": "kde-extra-cmake-modules",
    "qtxdg": "",
    "qt-accountsservice-addon": "",
    "polkit-qt-1": "kde-extra-cmake-modules",
    "vibe": "kde-solid",
    "fluid": "",
    "widget-styles": "",
    "icon-themes": "",
    "wallpapers": "",
    "greenisland": "",
    "shell": "fluid,wallpapers,qt-accountsservice-addon,qtxdg,polkit-qt-1,kde-kconfig",
    "shell-weston-plugins": "shell",
    "swordfish": "",
    "system-preferences": "polkit-qt-1,qtxdg,qt-accountsservice-addon",
    "archiver": "kde-karchive",
    "eyesight": "",
    "terminal": "vibe",
    "cinema": "",
    "widget-factory": "widget-styles",
}

# Protocols for GitHub repositories
PROTOCOLS = ["http", "ssh"]

# Base URLs for GitHub repositories
BASE_URLS = {
    "http": "https://github.com/",
    "ssh": "git@github.com:",
}

# vim:set ts=4 sw=4 et:
