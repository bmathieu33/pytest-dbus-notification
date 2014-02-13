# coding=utf-8
"""
"""
from __future__ import absolute_import

from time import time
import dbus

def pytest_addoption(parser):
    """Adds options to control dbus notifications."""
    group = parser.getgroup('terminal reporting')
    group.addoption('--dbus',
                    dest='dbus',
                    default=True,
                    help='Enable D-Bus notifications.')

notifications = {
    'success': {
        'title': u'PASSED',
        'body': u'{success} tests passed in {time}s.',
        'icon': u'dialog-information'
        },
    'failed': {
        'title': u'FAILED',
        'body': u'{failed}/{total} tests failed in {time}s.',
        'icon': 'dialog-warning'
        },
    'error': {
        'title': 'py.test: ERROR',
        'body': '',
        'icon': 'dialog-error'
        },
    }


def pytest_terminal_summary(terminalreporter):
    duration = time() - terminalreporter._sessionstarttime
    if not terminalreporter.config.option.dbus:
        return

    tr = terminalreporter
    results = dict(success=len(tr.stats.get('passed', [])),
                   failed=len(tr.stats.get('failed', [])),
                   time=u'{:.2f}'.format(duration)
    )
    results['total'] = results['success'] + results['failed']
    status = 'failed' if results['failed'] else 'success'
    notify("py.test", status, results)


def notify(title, status, results):
    notification = notifications[status]
    title = notification['title']
    body = notification['body'].format(**results)
    icon = notification['icon']
    actions = []
    hints = { 'transient': True }
    timeout = 1000 * 30 # 30s timeout

    bus = dbus.SessionBus()
    notifier = bus.get_object('org.freedesktop.Notifications',
                              '/org/freedesktop/Notifications')
    iface = dbus.Interface(notifier, 'org.freedesktop.Notifications')
    iface.Notify('py test', 0, icon, title, body, actions, hints, timeout)
