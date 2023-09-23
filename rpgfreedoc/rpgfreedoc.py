#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:10:41 2023

@author: jwoehr
"""

import re

DOCCOMMENT = re.compile(r"^\s*// {.*")


class RPGFreeDocCommentLine:
    def __init__(self, comment_line, line_number):

        self.comment_line = comment_line
        self.line_number = line_number


class RPGFreeDocComment:
    def __init__(self):
        self.comment_lines = []
        self.entity = None
        self.entity_line_number = None

    def add_comment_line(self, line: str) -> None:
        self.comment_lines.append(line)


class RPGFreeDocCommentCollection:
    def __init__(self):
        self.comments = []


class RPGFreeDocCommentHarvester:
    def __init__(self, fh, line_number):
        self.fh = fh
        self.line_number = line_number
        self.rpg_free_doc_comment = RPGFreeDocComment()

    def harvest(self, a_line) -> (RPGFreeDocComment, int):
        while a_line and DOCCOMMENT.search(a_line):
            self.rpg_free_doc_comment.add_comment_line(
                RPGFreeDocCommentLine(a_line, self.line_number)
            )
            self.line_number += 1
            a_line = self.fh.readline()
        self.rpg_free_doc_comment.entity = a_line
        self.rpg_free_doc_comment.entity_line_number = self.line_number
        self.line_number += 1
        return (self.rpg_free_doc_comment, self.line_number)


class RPGFreeDocCommentBundler:
    def __init__(self, fh):
        self.fh = fh
        self.line_number = 0
        self.rpg_free_doc_comment_collection = RPGFreeDocCommentCollection()

    def bundle(self) -> RPGFreeDocCommentCollection:
        a_line = self.fh.readline()
        while a_line:
            if DOCCOMMENT.search(a_line):
                rpg_free_doc_comment_harvester = RPGFreeDocCommentHarvester(
                    self.fh, self.line_number
                )
                result = rpg_free_doc_comment_harvester.harvest(a_line)
                self.rpg_free_doc_comment_collection.comments.append(result[0])
                self.line_number = result[1]
            a_line = self.fh.readline()
            self.line_number += 1
        return self.rpg_free_doc_comment_collection

    @staticmethod
    def bundle_file(filepath) -> RPGFreeDocCommentCollection:
        fh = open(filepath, "r")
        rpg_free_doc_comment_bundler = RPGFreeDocCommentBundler(fh)
        one_bundle = rpg_free_doc_comment_bundler.bundle()
        fh.close()
        return one_bundle


if __name__ == "__main__":
    pass
