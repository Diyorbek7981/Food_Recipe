from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


class FoodLikeListView(generics.ListAPIView):  # ---------------------------------  foodlike
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


class FoodSaveListView(generics.ListAPIView):  # ------------------------------- save
    serializer_class = SaveSerializer

    # request berayotgan userga tegishli like modellari korinadi
    def get_queryset(self):
        return SaveModel.objects.filter(author=self.request.user)


class FoodSaveApiView(APIView):

    def post(self, request, pk):
        try:
            food_save = SaveModel.objects.get(
                author=self.request.user,
                recipe_id=pk
            )
            food_save.delete()
            data = {
                "success": True,
                "message": "Saqlash o'chirildi"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except SaveModel.DoesNotExist:
            food_save = SaveModel.objects.create(
                author=self.request.user,
                recipe_id=pk
            )
            serializer = FoodLikeSerializer(food_save)
            data = {
                "success": True,
                "message": "Muvaffaqiyatli saqlandi",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)


# Coment  ----------------------------------------------------------------------------------------------------------->

class FoodCommentListView(generics.ListAPIView):  # coment list 1 retsept uchun
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        recipe_id = self.kwargs['pk']  # recipe id si orqali shu resepga tegishli comentlar keladi
        queryset = FoodComment.objects.filter(parent=None, recipe_id=recipe_id)
        return queryset


class FoodCommentCreateView(generics.CreateAPIView):  # coment create retsept idsi orqali
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        recipe_id = self.kwargs['pk']
        serializer.save(author=self.request.user, recipe_id=recipe_id)


class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):  # coment uchun update delete retrive(detail)
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = FoodComment.objects.all()


class CommentLikeListView(generics.ListAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        return CommentLike.objects.filter(author=self.request.user)


class CommentLikeAPiView(APIView):  # coment like create delete
    def post(self, request, pk):
        try:
            comment_like = CommentLike.objects.get(
                author=self.request.user,
                comment_id=pk
            )
            comment_like.delete()
            data = {
                "success": True,
                "message": "LIKE muvaffaqiyatli o'chirildi",
                "data": None
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except CommentLike.DoesNotExist:
            comment_like = CommentLike.objects.create(
                author=self.request.user,
                comment_id=pk
            )
            serializer = CommentLikeSerializer(comment_like)
            data = {
                "success": True,
                "message": "LIKE muvaffaqiyatli qo'shildi",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)


class RecipeListView(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [permissions.AllowAny, ]
