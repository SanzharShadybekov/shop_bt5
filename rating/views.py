from rest_framework.response import Response
from rest_framework.views import APIView


class TestApi(APIView):
    def get(self, request):
        return Response('404', status=200)

# мое что-что что-то
# еще раз мое что-что что-то
