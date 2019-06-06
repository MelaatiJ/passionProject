from django import forms
from .models import NaniEntryModel, DiscussionEntryModel, CommentEntryModel, GalleryEntryModel, \
    UpcomingEventsEntryModel, LibraryEntryModel

# for for post only created by admin or VP
class NaniForm(forms.ModelForm):
    class Meta:
        model = NaniEntryModel
        fields = "__all__"


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionEntryModel
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentEntryModel
        fields = "__all__"


class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryEntryModel
        fields = "__all__"


class UpcomingEventForm(forms.ModelForm):
    class Meta:
        model = UpcomingEventsEntryModel
        fields = "__all__"


class LibraryForm(forms.ModelForm):
    class Meta:
        model = LibraryEntryModel
        fields = "__all__"
