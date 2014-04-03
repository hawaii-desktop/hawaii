# File whose presence means the submodule was already configured
COOKIENAME_CONFIGURE = ".hawaii-ci-configure-cookie"

# File whose presence means the submodule was already built
COOKIENAME_BUILD = ".hawaii-ci-build-cookie"

# Modules
MODULES = {
    "kde-extra-cmake-modules": {
        "branch": "master"
    },
    "qtconfiguration": {
        "branch": "dev"
    },
    "libqtxdg": {
        "branch": "master"
    },
    "qtaccountsservice": {
        "branch": "dev",
    },
    "polkit-qt-1": {
        "branch": "wip/qt4and5",
    },
    "widget-styles": {
        "branch": "dev"
    },
    "icon-themes": {
        "branch": "dev"
    },
    "wallpapers": {
        "branch": "dev"
    },
    "fluid": {
        "branch": "dev"
    },
    "greenisland": {
        "branch": "dev"
    },
    "libhawaii": {
        "branch": "dev"
    },
    "shell": {
        "branch": "dev"
    },
    "swordfish": {
        "branch": "dev"
    },
    "system-preferences": {
        "branch": "dev"
    },
    "archiver": {
        "branch": "dev"
    },
    "eyesight": {
        "branch": "dev"
    },
    "yat": {
        "branch": "dev"
    },
    "terminal": {
        "branch": "dev"
    },
    "cinema": {
        "branch": "dev"
    },
    "widget-factory": {
        "branch": "dev"
    }
}

# Ignore modules
IGNORED_MODULES = [
    "archiver",
    "libqtxdg",
    "yat",
    "terminal"
]

# Dependencies
DEPENDENCIES = {
    "kde-extra-cmake-modules": "",
    "qtconfiguration": "",
    "libqtxdg": "",
    "qtaccountsservice": "",
    "polkit-qt-1": "kde-extra-cmake-modules",
    "fluid": "",
    "widget-styles": "fluid",
    "icon-themes": "",
    "wallpapers": "",
    "greenisland": "",
    "libhawaii": "kde-extra-cmake-modules",
    "shell": "greenisland,fluid,libhawaii,wallpapers,qtconfiguration,qtaccountsservice,polkit-qt-1",
    "swordfish": "fluid",
    "system-preferences": "polkit-qt-1,qtconfiguration,qtaccountsservice,libhawaii",
    "archiver": "",
    "eyesight": "",
    "yat": "",
    "terminal": "yat",
    "cinema": "fluid",
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
