
.. image:: https://raw.githubusercontent.com/anxuae/pycups-notify/master/docs/pycups-notify.png
   :align: center
   :alt: pycups-notify


The ``pycups-notify`` library is an extension to the `pycups <https://github.com/OpenPrinting/pycups>`_
one. It enables subscription to CUPS RSS notifications.

This library implements the `Event notify <http://www.marco.panizza.name/dispenseTM/slides/exerc/eventNotifier/eventNotifier.html>`_
pattern to match with the `design description <https://www.cups.org/doc/spec-design.html>`_
of the CUPS server.


Install
-------

::

     $> pip install pycups-notify


Usage
-----

.. code-block:: python

    import time
    import cups
    from cups_notify import Subscriber

    def on_event(evt):
        print(evt)

    # Create a CUPS connection
    conn = cups.Connection()

    # Create a new subscriber
    sub = Subscriber(conn)

    # Subscribe the callback to all CUPS events
    sub.subscribe(on_event)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        sub.unsubscribe_all()

The ``CupsEvent`` class has the following attributes:

============= ======== ===============================
Attribute     type     Description
============= ======== ===============================
guid          int      Unique ID
title         str      Title
description   str      Description
printer       str      Printer name
address       tuple    Address of the CUPS server
timestamp     datetime Published date
============= ======== ===============================

It is possible to define a list of event types on which the callback is binded:

.. code-block:: python

    import cups
    from cups_notify import Subscriber, event

    def my_callback(evt):
        print(evt.title, evt.description)

    # Create a new subscriber
    sub = Subscriber(cups.Connection())

    # Subscribe the callback
    sub.subscribe(my_callback, [event.CUPS_EVT_JOB_CREATED,
                                event.CUPS_EVT_JOB_COMPLETED,
                                event.CUPS_EVT_JOB_STOPPED])

The list of existing event types is defined below:

=============================== ==============================================================================
Type                            Description
=============================== ==============================================================================
CUPS_EVT_JOB_COMPLETED          Event when the job is completed
CUPS_EVT_JOB_CONFIG_CHANGED     Event when the job is changed
CUPS_EVT_JOB_CREATED            Event when a job is created
CUPS_EVT_JOB_PROGRESS           Event for job progress
CUPS_EVT_JOB_STATE_CHANGED      Event when the job-state changes
CUPS_EVT_JOB_STOPPED            Event when the job is stopped
CUPS_EVT_PRINTER_ADDED          Event when a printer is added
CUPS_EVT_PRINTER_CHANGED        Event when a printer is changed
CUPS_EVT_PRINTER_CONFIG_CHANGED Event when a printer's configuration is changed
CUPS_EVT_PRINTER_DELETED        Event when a printer is deleted
CUPS_EVT_PRINTER_MODIFIED       Event when a printer is modified
CUPS_EVT_PRINTER_STATE_CHANGED  Event when the printer-state changes
CUPS_EVT_PRINTER_STOPPED        Event when a printer is stopped
CUPS_EVT_SERVER_AUDIT           Event when a bad request, security error, or authentication error occurs
CUPS_EVT_SERVER_RESTARTED       Event when the server is restarted
CUPS_EVT_SERVER_STARTED         Event when the server is initially started
CUPS_EVT_SERVER_STOPPED         Event when the server is shutdown
=============================== ==============================================================================

If the CUPS server is not running on the same computer as the subscriber application
one, the local IP address (same network than the CUPS server) have to be provided to
the subscriber class:

.. code-block:: python

    # Create a CUPS connection
    cups.setServer('198.20.34.1')
    conn = cups.Connection()

    # Create a new subscriber
    sub = Subscriber(conn, '198.20.34.26')


Run
---

A simple listener can be started by typing the following command line::

     $> pycups-notify
