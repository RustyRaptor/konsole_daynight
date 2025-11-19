from collections.abc import Callable
from typing import Any

from gi.repository import GLib
from loguru import logger
from pydbus import SessionBus

DBusSignalHandler = Callable[[str, str, Any], None]


def start_settings_monitor(callback: DBusSignalHandler) -> None:
        """Listen for xdg-desktop-portal SettingChanged signals."""
        bus = SessionBus()

        portal = bus.get(
                "org.freedesktop.impl.portal.desktop.kde",
                "/org/freedesktop/portal/desktop",
        )

        def handler(namespace: str, key: str, value: object) -> None:
                logger.debug(
                        f"DBus signal: ns={namespace}, key={key}, value={value}"
                )
                callback(namespace, key, value)

        portal.SettingChanged.connect(handler)

        logger.info("Listening for XDG portal SettingChanged events...")
        loop = GLib.MainLoop()
        loop.run()
