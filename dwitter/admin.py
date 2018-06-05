from django.contrib import admin
from .models import MessageBox
from .models import Comments
from .models import Like
from .models import Relationship


admin.site.register(MessageBox)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Relationship)
