from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from poller.models import PollerProcess


class LongPollView(APIView):
    def get(self, request):
        user = request.user
        try:
            poller_process = PollerProcess.objects.get(user=user)
        except PollerProcess.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        poller_process.updated_at = timezone.now()
        poller_process.save()

        return Response(
            {
                "message": "Updated successfully"
            },
            status=status.HTTP_200_OK
        )
