def alert_key_rotation_due(days_active: int):
    if days_active > 90:
        print('[SECURITY ALERT] Master key older than 90 days - rotate recommended')
