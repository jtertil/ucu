from django.utils.baseconv import BaseConverter

# symbols allowed in URL's:
# '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-._~'

BASE_SYMBOLS = 'abcdefghijklmnopqrstuvwxyz0123456789'
converter = BaseConverter(BASE_SYMBOLS)
