from rest_framework.serializers import ModelSerializer
from .models import Notice

class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields =('notice_text',
        'date')