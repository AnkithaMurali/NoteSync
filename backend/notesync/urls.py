from django.contrib import admin
from django.urls import path
from notes.views import home, add_note, signup_view, login_view, logout_view, edit_note, delete_note
from notes.views import toggle_pin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:note_id>/', edit_note, name='edit_note'),   # ✅ Add this
    path('delete/<int:note_id>/', delete_note, name='delete_note'),  # ✅ Add this
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('pin/<int:note_id>/', toggle_pin, name='toggle_pin'),
]


