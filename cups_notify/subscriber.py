# -*- coding: utf-8 -*-


import time
from cups_notify import LOGGER
from cups_notify import event
from cups_notify.listener import NotificationListerner


class Subscriber(object):

    def __init__(self, cups_conn, local_address='localhost'):
        self._conn = cups_conn
        self._callbacks = {}
        self.address = local_address

    def __del__(self):
        self.unsubscribe_all()

    def subscribe(self, cb, filters=None):
        """Subscribe a new callback.
        """
        assert callable(cb), "Callback is not callable"
        if not filters:
            filters = [event.CUPS_EVT_ALL]
        if cb in self._callbacks:
            self._callbacks[cb].shutdown()
        self._callbacks[cb] = NotificationListerner(self._conn, cb, filters, self.address)
        self._callbacks[cb].start()

    def is_subscribed(self, cb):
        """Return True if the callback is already subscribed to some events.
        """
        return cb in self._callbacks

    def unsubscribe(self, cb):
        """Subscribe the given callback.
        """
        server = self._callbacks.pop(cb, None)
        if server:
            server.shutdown()

    def unsubscribe_all(self):
        """Do cleanup actions.
        """
        for cb, server in self._callbacks.items():
            LOGGER.debug("Stopping notification server")
            server.shutdown()
        self._callbacks = {}


def main():
    """Simple listener which print notification in the console.
    """
    import cups

    def on_event(evt):
        print(evt)

    sub = Subscriber(cups.Connection())
    sub.subscribe(on_event)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        sub.unsubscribe_all()
