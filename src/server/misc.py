import base64
import uuid

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False


def isUUID(s):
    try:
        uuid.UUID(s)
        return True
    except Exception:
        return False


def isInt(s):
    try:
        int(s)
        return True
    except Exception:
        return False