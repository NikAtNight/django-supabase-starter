from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('skynet/doc/', include('django.contrib.admindocs.urls')),
    path('skynet/', admin.site.urls),
    # path('api/', include((combined_urls, 'budget'), namespace='v1')),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

admin.site.site_header = "BudgeBase Admin - v1"
admin.site.site_title = "BudgeBase Admin Portal"
admin.site.index_title = "Welcome to BudgeBase Portal"
