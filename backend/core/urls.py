

from django.contrib import admin
from django.urls import path,include
from customaccount.urls import router as users_router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/users/",include(users_router.urls))
]
