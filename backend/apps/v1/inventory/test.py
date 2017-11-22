import subprocess

from django.test import TestCase
from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.TDGs.DesktopTDG import DesktopTDG


# Create your tests here.
class TDGTests(TestCase):

    def setUp(self):

        self.desktop = Desktop(
            'ZZZZZZG',
            'Razer Desktop',
            46,
            15.0,
            'LBS',
            2299.99,
            'CAD',
            'RAZER',
            16,
            'GB',
            'INTEL',
            4,
            2,
            'TB',
            15,
            30,
            1,
            'INCH'
        )

    def test_DesktopTDG_insert(self):
        DesktopTDG.insert(self.desktop)
        result = DesktopTDG.find(self.desktop.modelNumber)
        print(result)
        self.assertEqual(True, True)

class testDeleteTDG(TestCase):
    def setUp(self):

        self.desktop = Desktop(
            'ZZZZZZG',
            'Razer Desktop',
            46,
            15.0,
            'LBS',
            2299.99,
            'CAD',
            'RAZER',
            16,
            'GB',
            'INTEL',
            4,
            2,
            'TB',
            15,
            30,
            1,
            'INCH'
        )

    def test_Desktop_delete(self):
        DesktopTDG.delete(self.desktop)
        self.assertEqual(True, True)