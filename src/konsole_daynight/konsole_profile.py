import subprocess
import xml.etree.ElementTree as ET

from loguru import logger
from pydbus import SessionBus


def apply_konsole_profile(profile: str) -> None:
        """Apply the selected Konsole profile."""
        logger.info(f"Applying Konsole profile → {profile}")

        # 1️⃣ Update default profile for new terminals
        try:
                _ = subprocess.run(  # noqa: S603
                        [  # noqa: S607
                                "kwriteconfig6",
                                "--file",
                                "konsolerc",
                                "--group",
                                "Desktop Entry",
                                "--key",
                                "DefaultProfile",
                                f"{profile}.profile",
                        ],
                        check=True,
                )
                logger.debug("Updated default Konsole profile")
        except Exception as exc:  # noqa: BLE001
                logger.error(f"Failed to update default Konsole profile: {exc}")

        try:
                bus = SessionBus()
                instance_name = "org.kde.konsole"
                sessions_root = "/Sessions"
                sessions_obj = bus.get(instance_name, sessions_root)

                introspect_xml = sessions_obj.Introspect()
                root = ET.fromstring(introspect_xml)
                session_nodes = [
                        node.attrib["name"] for node in root.findall("node")
                ]

                for session_name in session_nodes:
                        session_path = f"{sessions_root}/{session_name}"
                        session_obj = bus.get(instance_name, session_path)
                        session_obj.setProfile(profile)
                        logger.debug(
                                f"Updated session {session_path} "
                                f"to profile {profile}"
                        )

                logger.info("Applied profile to all open sessions")

        except Exception as exc:
                logger.error(f"Failed to update open Konsole sessions: {exc}")
