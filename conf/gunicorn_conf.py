bind = '127.0.0.1:8018'

timeout = 30
max_requests = 1000
max_requests_jitter = 500


accesslog = None
errorlog = '-'
loglevel = 'warning'

secure_scheme_headers = {
    'X-FORWARDED-PROTO': 'https',
}
