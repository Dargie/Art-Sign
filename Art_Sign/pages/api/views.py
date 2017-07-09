import os.path
import random

from rest_framework.views import APIView
from rest_framework.response import Response

from Art_Sign.settings import BASE_DIR


class HomeAPIView(APIView):

    def get(self, request):
        try:
            with open(os.path.join(BASE_DIR, 'videos.txt'), 'r') as videos:
                video = random.choice(videos.readlines())
        except IOError:
            video = 'www.youtube.com/embed/rz3jw0_XXoc?rel=0'

        return Response({"video": video})
