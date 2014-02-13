A py.test plugin that displays test results using `D-BUS notifications <https://developer.gnome.org/notification-spec/>`_.

This plugins requires the `dbus` module.

Using in virtualenv
-------------------

As of 14 feb 2014, `you cannot install python-dbus with
pip/easy_install<https://bugs.freedesktop.org/show_bug.cgi?id=55439>`_.

You have two options:

 * install python-dbus in your virtualenv by downloading and building it
 * install python-dbus using your system package (like `apt-get install python-dbus`).

In the latter case if your virtualenv does not use system packages (that's the default option), your virtualenv sitll hasn't `dbus` module available. Just copy it from system packages::

    venv # cp /usr/lib/pyshared/python2.7/_dbus_bindings.so lib/python2.7/site-packages/
    venv # cp -r cp -r /usr/share/pyshared/dbus lib/python2.7/site-packages/dbus
