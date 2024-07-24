from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


class FoodLikeListView(generics.ListAPIView):
    serializer_class = FoodLikeSerializer

    # request berayotgan userga tegishli like modellari korinadi
    def get_queryset(self):
        return FoodLike.objects.filter(author=self.request.user)


class FoodLikeApiView(APIView):

    # homeni pk orqali shu modelga like ni sqlash va o'chirish
    def post(self, request, pk):
        # avval try bajariladi va request erayotgan user va shu pkli home model bazada bo'lsa olinib o'chiladi
        try:
            food_like = FoodLike.objects.get(
                author=self.request.user,
                recipe_id=pk
            )
            food_like.delete()
            data = {
                "success": True,
                "message": "LIKE muvaffaqiyatli o'chirildi"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        # agar bazada unday malumot bo'lmasa xudi shu malumot yaratiladi
        except FoodLike.DoesNotExist:
            food_like = FoodLike.objects.create(
                author=self.request.user,
                recipe_id=pk
            )
            serializer = FoodLikeSerializer(food_like)
            data = {
                "success": True,
                "message": "LIKE muvaffaqiyatli qo'shildi",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
