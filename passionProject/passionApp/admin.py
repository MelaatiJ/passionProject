from django.contrib import admin

# Register your models here.

from .models import NaniEntryModel
from .models import DiscussionEntryModel
from .models import CommentEntryModel
from .models import GalleryEntryModel
from .models import UpcomingEventsEntryModel
from .models import LibraryEntryModel
# from .models import MembershipEntryModel


admin.site.register(NaniEntryModel)
admin.site.register(DiscussionEntryModel)
admin.site.register(CommentEntryModel)
admin.site.register(GalleryEntryModel)
admin.site.register(UpcomingEventsEntryModel)
admin.site.register(LibraryEntryModel)
# admin.site.register(MembershipEntryModel)


