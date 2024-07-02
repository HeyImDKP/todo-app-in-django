#!/usr/bin/env python

import os
import django.core.management as management
import django.core.wsgi as wsgi

def main() -> int:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'http_server.settings')
    wsgi.get_wsgi_application()
    management.call_command('runserver', f"{os.environ['HOST']}:{os.environ['PORT']}")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())