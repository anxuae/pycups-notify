
.. image:: https://raw.githubusercontent.com/anxuae/pycups-notify/master/docs/pycups-notify.png
   :align: center
   :alt: pycups-notify


The ``pycups-notify`` library is an extension to the `pycups <https://github.com/OpenPrinting/pycups>`_
one. It enables subscription to CUPS RSS notifications.

This library implements the `Event notify <http://www.marco.panizza.name/dispenseTM/slides/exerc/eventnotify/eventnotify.html>`_
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

    def on_event(event):
        print(event)

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
        sub.stop()


A simple listener can be started by typing the following command line::

     $> pycups-notify
