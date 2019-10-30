# -*- coding: utf-8 -*-

"""Notification system for the pycups library."""

import logging

LOGGER = logging.getLogger(__name__)

__version__ = "0.0.4"

from cups_notify.subscriber import Subscriber
