from django.utils.baseconv import BaseConverter

# symbols allowed in URL's:
# '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-._~'

BASE_SYMBOLS = 'oxr2c7njdhay4bi51wms3t0p6vfkqzle9gu8'
converter = BaseConverter(BASE_SYMBOLS)
