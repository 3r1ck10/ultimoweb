from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('teach/',views.teach,name='teach'),
    path('goesir/',views.goesir,name='goesir'),
    path('goeswv/',views.goesvw,name='goeswv'),
    path('goesvis/',views.goesvis,name='goesvis'),
    path('modelocho/',views.model_cli_cho,name='cho'),
    path('modelopres/',views.model_cli_pres,name='pres'),
    path('modelotmn/',views.model_cli_tmn,name='tmn'),
    path('modelotmx/',views.model_cli_tmx,name='tmx'),
    path('modeloadv/',views.model_pro_advt,name='advt'),
    path('modelol250/',views.model_pro_l250,name='l250'),
    path('modelol500/',views.model_pro_l500,name='l500'),
    path('modelol850/',views.model_pro_l850,name='l850'),
    path('modelomgp/',views.model_pro_mgp,name='mgp'),
    path('modelopres2/',views.model_pro_pres,name='pres2'),
    path('estaciones/',views.estaciones,name='estaciones'),
    path('cambioc/',views.cambioc,name='cambioc'),
]
