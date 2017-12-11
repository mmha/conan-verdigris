#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os

class VerdigrisConan(ConanFile):
    name = "verdigris"
    version = "20171211"
    url = "https://github.com/mmha/conan-verdigris"
    description = "Qt without moc: set of macros to use Qt without needing moc"
    license = ["LGPL-3.0", "GPL-2.0"]
    commit = "9f2f06257078bc550ec4ab3780ec802be32e382b"

    def source(self):
        source_url = "https://github.com/woboq/verdigris"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.commit))
        extracted_dir = self.name + "-" + self.commit
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="sources")
        self.copy(pattern="wobject*.h", dst="include", src=os.path.join("sources","src"))

    def package_id(self):
        self.info.header_only()