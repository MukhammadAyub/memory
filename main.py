from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', views.index, name='home'),
    path('home/', include('home.urls')),
    path('course/', include('course.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student/', views.student, name='student'),
    path('tutors/', views.tutors, name='tutors'),
    path('subjects/', views.subjects, name='subjects'),
    path('subject/<int:id>/<slug:slug>', views.subject_detail, name='subject_detail'),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
