from typing import Literal

Theme = Literal["light", "dark"]


def detect_theme(
        namespace: str,
        key: str,
        value: object,
        fallback: Theme = "dark",
) -> Theme | None:
        """Return "light", "dark", or None depending on the detected text."""
        # 1 — explicit numeric from portal
        if namespace == "org.freedesktop.appearance" and key == "color-scheme":
                num = int(value)
                return "light" if num == 1 else "dark"
        # 2 — KDE ColorScheme string
        if namespace == "org.kde.kdeglobals.General" and key == "ColorScheme":
                name = str(value)
                if "dark" in name.lower():
                        return "dark"
                if "light" in name.lower():
                        return "light"
                return fallback

        return None
