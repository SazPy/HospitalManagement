from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_fns_app.urls')),  # Include your main app's URLs
    # Add other includes as needed
]
