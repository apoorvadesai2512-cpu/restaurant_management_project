import logging
from email.utils import parseaddr
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:

    try:
        name, addr = parseaddr(email)
        if not addr or '@' not in addr:
            return False

        validate_email(addr)
        return True
    except ValidationError:
        return False
    except Exception as e:
        logger.error(f"Unexcepted error validating email '{email}': {e}")
        return False