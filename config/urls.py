from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('onboarding/', include('apps.onboarding.urls')),
    path('assessments/', include('apps.assessments.urls')),
    path('', include('apps.dashboard.urls')),
    path('ai/', include('apps.ai_engine.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)