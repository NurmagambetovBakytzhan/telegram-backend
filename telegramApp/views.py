from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Thread, Message
from .serializers import ThreadSerializer, MessageSerializer


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@api_view(['GET'])
def get_messages_by_thread_id(request, thread_id):
    try:
        messages = Message.objects.filter(thread__id=thread_id)
        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
