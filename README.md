[ ![Download](https://api.bintray.com/packages/mmha/conan/verdigris/images/download.svg) ](https://bintray.com/mmha/conan/verdigris/_latestVersion)
# Qt without moc: set of macros to use Qt without needing moc

[Conan.io](https://conan.io) package for [verdigris](https://github.com/woboq/verdigris) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/mmha/conan/verdigris).

## For Users: Use this package

### Basic setup

    $ conan install verdigris/20171211@mmha/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    verdigris/20171211@mmha/testing

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## License
[LGPL-3.0](LICENSE)
