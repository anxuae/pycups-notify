# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def evts():
    return [
        {
            'title': 'Tâche d’impression\xa0: Print_to_VipRiser-485 (anxuaepycupsnotify Run failed Python package  master b376800) retenue',
            'description': 'Job created.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:26 GMT',
            'guid': '1'
        },
        {
            'title': 'Tâche d’impression\xa0: Print_to_VipRiser-485 (anxuaepycupsnotify Run failed Python package  master b376800) en attente',
            'description': 'Job released by user.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:26 GMT',
            'guid': '2'
        },
        {
            'title': 'Tâche d’impression\xa0: Print_to_VipRiser-485 (anxuaepycupsnotify Run failed Python package  master b376800) en attente',
            'description': 'Job restarted by user.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:26 GMT',
            'guid': '3'
        },
        {
            'title': 'Tâche d’impression\xa0: Print_to_VipRiser-485 (anxuaepycupsnotify Run failed Python package  master b376800) en attente',
            'description': 'Job options changed by user.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:26 GMT',
            'guid': '4'
        },
        {
            'title': 'Imprimante : Print_to_VipRiser en cours',
            'description': 'Printer "Print_to_VipRiser" state changed to processing.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:26 GMT',
            'guid': '5'
        },
        {
            'title': 'Tâche d’impression\xa0: Print_to_VipRiser-485 (anxuaepycupsnotify Run failed Python package  master b376800) en cours',
            'description': 'Job #485 started.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:26 GMT',
            'guid': '6'
        },
        {
            'title': 'Tâche d’impression\xa0: Print_to_VipRiser-485 (anxuaepycupsnotify Run failed Python package  master b376800) terminée',
            'description': 'Job completed.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:28 GMT',
            'guid': '7'
        },
        {
            'title': 'Imprimante : Print_to_VipRiser inactive',
            'description': 'Printer "Print_to_VipRiser" state changed to idle.',
            'link': 'http://nefle:631/printers/Print_to_VipRiser',
            'pubDate': 'Sat, 16 Nov 2019 13:49:28 GMT',
            'guid': '8'
        }
    ]
