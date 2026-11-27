import logging

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import get_settings
from app.core.logging import setup_logging

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging(settings.log_level)

    application = FastAPI(title=settings.app_name, debug=settings.debug)
    application.include_router(health_router)

    logger.info("%s started (env=%s)", settings.app_name, settings.app_env)
    return application


app = create_app()
