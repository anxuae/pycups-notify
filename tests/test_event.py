# -*- coding: utf-8 -*-

import pytest
from datetime import datetime
from cups_notify import event


def test_event_parsing(evts):
    evt = event.CupsEvent(evts[0])

    assert evt.guid > 0
    assert evt.title
    assert evt.description
    assert evt.timestamp < datetime.now()
    assert evt.address == ('hello', 631)
    assert evt.printer == 'Print_to_VipRiser'


def test_use_locale():
    date = "lun, 23 Mar 2020 15:58:43 GMT"
    fr_fr = "fr_FR.UTF-8"

    with pytest.raises(ValueError):
        datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")

    with event.use_locale(fr_fr):
        datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")
