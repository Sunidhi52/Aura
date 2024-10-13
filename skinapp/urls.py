from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('normal/', views.normal_skin, name='normal_skin'),
    path('oily/',views.oily_skin,name='oily_skin'),
    path('dry/',views.dry_skin,name='dry_skin'),
    path('combination/',views.combination_skin,name='combination_skin'),
    path('normal/', views.NormalSkinList.as_view(), name='normal_skin_list'),
    path('oily/', views.OilySkinList.as_view(), name='oily_skin_list'),
    path('dry/', views.DrySkinList.as_view(), name='dry_skin_list'),
    path('combination/', views.CombinationSkinList.as_view(), name='combination_skin_list'),
    path('about/',views.about,name='about_page'),
    path('bodycare/',views.bodycare,name='bodycare_page'),
    path('find/',views.find,name='find_page'),
    path('signup/',views.signup_view,name='signup_page'),
    path('login/',views.login_view,name='login_page'),


    path('normal/<int:pk>/', views.NormalSkinDetail.as_view(), name='normal_skin_detail'),
    path('oily/<int:pk>/', views.OilySkinDetail.as_view(), name='oily_skin_detail'),
    path('dry/<int:pk>/', views.DrySkinDetail.as_view(), name='dry_skin_detail'),
    path('combination/<int:pk>/', views.CombinationSkinDetail.as_view(), name='combination_skin_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
