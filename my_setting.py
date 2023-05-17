SECRET_KEY = '3^o_vku=o(7=^n7mhnv+89newblf+_xr^3$fx(w)+&l*_w3n1^'

KAKAO_REST_API_KEY = "d3af1b9ce3b1198e6ca9af3e5ec581d1"
KAKAO_REDIRECT_URI = "http://localhost:8000/accounts/kakao/login/callback/ "
KAKAO_SECRET_KEY = "924e1eaea8b166203d8c1d804f353482"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'gnu', #2
        'USER': 'Movie', #3
        'PASSWORD': 'movie@1234',  #4
        'HOST': 'localhost',   #5
        'PORT': '3306', #6
    }
}