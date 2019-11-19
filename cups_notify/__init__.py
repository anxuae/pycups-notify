# -*- coding: utf-8 -*-

"""Notification system for the pycups library."""

import logging

LOGGER = logging.getLogger(__name__)

__version__ = "0.0.5"

try:
    from cups_notify.subscriber import Subscriber
except ImportError:
    LOGGER.warning("pycups is not installed")
