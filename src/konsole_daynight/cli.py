from __future__ import annotations

import click
from loguru import logger

from konsole_daynight.dbus_listener import start_settings_monitor
from konsole_daynight.konsole_profile import apply_konsole_profile
from konsole_daynight.logging_setup import configure_logging
from konsole_daynight.theme_detector import detect_theme


@click.command()
@click.option(
        "--dark_profile",
        "-d",
        envvar="KONSOLE_DAYNIGHT_DARK_PROFILE",
        type=click.STRING,
        default="Dark",
)
@click.option(
        "--light_profile",
        "-v",
        envvar="KONSOLE_DAYNIGHT_LIGHT_PROFILE",
        type=click.STRING,
        default="Light",
)
@click.option(
        "--verbose",
        "-v",
        is_flag=True,
        help="Enable debug messages.",
)
def run(
        light_profile: str,
        dark_profile: str,
        *,
        verbose: bool = False,
) -> None:
        """Monitor KDE theme and adjust Konsole profile."""
        configure_logging(verbose=verbose)

        logger.info("Starting Konsole theme auto-switcher")

        def on_setting_changed(namespace: str, key: str, value: object) -> None:
                theme = detect_theme(namespace, key, value)
                if theme:
                        logger.info(f"Detected global theme: {theme}")
                        apply_konsole_profile(
                                light_profile
                                if theme == "light"
                                else dark_profile
                        )

        start_settings_monitor(on_setting_changed)


if __name__ == "__main__":
        run()
