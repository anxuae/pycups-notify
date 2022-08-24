# -*- coding: utf-8 -*-

import sys
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
