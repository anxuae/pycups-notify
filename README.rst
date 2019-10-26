
.. image:: https://raw.githubusercontent.com/anxuae/pycups-notifier/master/docs/pycups-notifier.png
   :align: center
   :alt: pycups-notifier


The ``pycups-notifier`` library is an extension to the `pycups <https://github.com/OpenPrinting/pycups>`_
one. It enables registration to CUPS RSS ("Really Simple Syndication") notifications.

This library implements the `Event Notifier <http://www.marco.panizza.name/dispenseTM/slides/exerc/eventNotifier/eventNotifier.html>`_
pattern to match with the `design description <https://www.cups.org/doc/spec-design.html>`_
of the CUPS server.


Install
-------

::

     $> pip install pycups-notifier


Usage
-----

.. code-block:: python

    import time
    import cups
    from cups_notifier import Subscriber

    def on_event(event):
        print(event)

    conn = cups.Connection()

    sub = Subscriber(conn)
    sub.add_callback(on_event, filters=('all'))

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sub.stop()
