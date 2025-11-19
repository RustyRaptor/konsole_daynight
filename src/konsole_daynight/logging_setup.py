import sys

from loguru import logger


def configure_logging(*, verbose: bool = False) -> None:
        """Configure loguru."""
        logger.remove()  # remove default handler
        _ = logger.add(sys.stdout, level="DEBUG" if verbose else "INFO")
