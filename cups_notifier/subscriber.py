# -*- coding: utf-8 -*-


import time
from cups_notifier import LOGGER
from cups_notifier import event
from cups_notifier.listener import NotificationListerner


class Subscriber(object):

    def __init__(self, cups_conn, local_address='localhost'):
        self._conn = cups_conn
        self._callbacks = {}
        self.address = local_address

    def __del__(self):
        self.stop()

    def add_callback(self, cb, filters=(event.CUPS_EVT_ALL,)):
        """Add a new callback.
        """
        assert callable(cb), "Callback is not callable"
        self._callbacks[cb] = NotificationListerner(self._conn, cb, filters, self.address)
        self._callbacks[cb].start()

    def stop(self):
        """Do cleanup actions.
        """
        for cb, server in self._callbacks.items():
            LOGGER.debug("Stopping notification ")
            server.shutdown()


def main():
    """Simple listener which print notification in the console.
    """
    import cups

    def on_event(evt):
        print(evt)

    conn = cups.Connection()

    sub = Subscriber(conn)
    sub.add_callback(on_event, filters=('all'))

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sub.stop()
