# -*- coding: utf-8 -*-

from xml.etree import ElementTree


CUPS_EVT_ALL = 'all'  # All events
CUPS_EVT_JOB_COMPLETED = 'job-completed'  # Event when the job is completed
CUPS_EVT_JOB_CONFIG_CHANGED = 'job-config-changed'  # Event when the job is changed
CUPS_EVT_JOB_CREATED = 'job-created'  # Event when a job is created
CUPS_EVT_JOB_PROGRESS = 'job-progress'  # Event for job progress
CUPS_EVT_JOB_STATE_CHANGED = 'job-state-changed'  # Event when the job-state changes
CUPS_EVT_JOB_STOPPED = 'job-stopped'  # Event when the job is stopped
CUPS_EVT_PRINTER_ADDED = 'printer-added'  # Event when a printer is added
CUPS_EVT_PRINTER_CHANGED = 'printer-changed'  # Event when a printer is changed
CUPS_EVT_PRINTER_CONFIG_CHANGED = 'printer-config-changed'  # Event when a printer's configuration is changed
CUPS_EVT_PRINTER_DELETED = 'printer-deleted'  # Event when a printer is deleted
CUPS_EVT_PRINTER_MODIFIED = 'printer-modified'  # Event when a printer is modified
CUPS_EVT_PRINTER_STATE_CHANGED = 'printer-state-changed'  # Event when the printer-state changes
CUPS_EVT_PRINTER_STOPPED = 'printer-stopped'  # Event when a printer is stopped
CUPS_EVT_SERVER_AUDIT = 'server-audit'  # Event when a bad request, security error, or authentication error occurs
CUPS_EVT_SERVER_RESTARTED = 'server-restarted'  # Event when the server is restarted
CUPS_EVT_SERVER_STARTED = 'server-started'  # Event when the server is initially started
CUPS_EVT_SERVER_STOPPED = 'server-stopped'  # Event when the server is shutdown


class CupsEvent(object):

    def __init__(self, xml_event):
        self.xml = xml_event

    def __str__(self):
        return self.xml
