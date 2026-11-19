import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import find_leftovers

def installed(software, version="1.0"):
    return {"software": software, "version": version}

def leftover(path, software):
    return {"path": path, "software": software}

class TestLeftoverFinder(unittest.TestCase):
    def test_uninstalled_program_leftover(self):
        ranked, _ = find_leftovers([installed("Office Suite")],
                                   [leftover("C:/OldApp/config.ini", "OldApp")])
        self.assertEqual(ranked, [("OldApp", ["C:/OldApp/config.ini"])])

    def test_installed_program_skipped(self):
        ranked, skipped = find_leftovers([installed("Photo Editor")],
                                         [leftover("C:/Photo Editor/plugin.dll", "Photo Editor")])
        self.assertEqual((ranked, skipped), ([], 1))

    def test_grouped_by_program(self):
        ranked, _ = find_leftovers([],
                                   [leftover("C:/OldApp/a.ini", "OldApp"),
                                    leftover("C:/OldApp/b.dat", "OldApp"),
                                    leftover("C:/Video Editor/s.xml", "Video Editor")])
        self.assertEqual([s for s, _ in ranked], ["OldApp", "Video Editor"])
        self.assertEqual(len(ranked[0][1]), 2)

    def test_most_items_first(self):
        ranked, _ = find_leftovers([],
                                   [leftover("C:/A/1", "SmallApp"),
                                    leftover("C:/B/1", "BigApp"),
                                    leftover("C:/B/2", "BigApp")])
        self.assertEqual(ranked[0][0], "BigApp")

    def test_tie_broken_alphabetically(self):
        ranked, _ = find_leftovers([],
                                   [leftover("C:/B/1", "BetaApp"),
                                    leftover("C:/A/1", "AlphaApp")])
        self.assertEqual([s for s, _ in ranked], ["AlphaApp", "BetaApp"])

    def test_empty_input(self):
        self.assertEqual(find_leftovers([], []), ([], 0))
