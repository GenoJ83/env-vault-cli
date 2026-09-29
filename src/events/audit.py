import time
def log_audit_event(action: str, user: str = 'local'):
    return {'timestamp': time.time(), 'action': action, 'user': user}
