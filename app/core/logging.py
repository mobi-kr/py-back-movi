import logging

LOG_FORMAT = "%(asctime)s %(levelname)s [%(name)s] %(message)s"


def setup_logging(level: str = "INFO") -> None:
    """표준 logging 기반 기본 로깅 설정."""
    logging.basicConfig(level=level, format=LOG_FORMAT, force=True)
