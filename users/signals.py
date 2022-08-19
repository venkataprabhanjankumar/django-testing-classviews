import logging
from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed

from django.dispatch.dispatcher import receiver

logging.basicConfig(filename='logs/logs', filemode='a', datefmt='%H:%M:%S', level=logging.INFO)

logger = logging.getLogger(__name__)


@receiver(user_logged_in)
def log_user_logged_in(sender, request, user, **kwargs):
    logger.info("User %s logged in" % user)
    logger.log(msg="User %s logged in" % user, level=logging.INFO)


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info("User %s logged out" % user)
    logger.log(msg="User %s logged out" % user, level=logging.INFO)


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    logger.warning("Login Failed with credentials %s" % credentials)
    logger.log(msg="Login Failed with credentials %s" % credentials, level=logging.WARNING)
