from django.db.models import Q
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.utils.timezone import now, timedelta
from .models import Box
from .serializers import BoxSerializer, BoxListSerializer, MyBoxSerializer
from .permissions import IsStaffUser, IsCreatorOrReadOnly

A1 = 100
V1 = 1000
L1 = 100
L2 = 50

class BoxCreateView(generics.CreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]

    def perform_create(self, serializer):
        if Box.objects.filter(created_at__gte=now()-timedelta(days=7)).count() >= L1:
            raise PermissionDenied("Total Boxes added in a week cannot be more than L1")
        if Box.objects.filter(created_by=self.request.user, created_at__gte=now()-timedelta(days=7)).count() >= L2:
            raise PermissionDenied("Total Boxes added in a week by a user cannot be more than L2")
        if Box.objects.all().aggregate(models.Avg('area'))['area__avg'] and Box.objects.all().aggregate(models.Avg('area'))['area__avg'] > A1:
            raise PermissionDenied("Average area of all added boxes should not exceed A1")
        if Box.objects.filter(created_by=self.request.user).aggregate(models.Avg('volume'))['volume__avg'] and Box.objects.filter(created_by=self.request.user).aggregate(models.Avg('volume'))['volume__avg'] > V1:
            raise PermissionDenied("Average volume of all boxes added by the current user shall not exceed V1")
        
        serializer.save(created_by=self.request.user)

class BoxUpdateView(generics.UpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]

    def perform_update(self, serializer):
        serializer.save()

class BoxListView(generics.ListAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxListSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, filters.DjangoFilterBackend]
    filterset_fields = {
        'length': ['gte', 'lte'],
        'breadth': ['gte', 'lte'],
        'height': ['gte', 'lte'],
        'area': ['gte', 'lte'],
        'volume': ['gte', 'lte'],
        'created_by__username': ['exact'],
        'created_at': ['gte', 'lte'],
    }

class MyBoxListView(generics.ListAPIView):
    serializer_class = MyBoxSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]

    def get_queryset(self):
        return Box.objects.filter(created_by=self.request.user)

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, filters.DjangoFilterBackend]
    filterset_fields = {
        'length': ['gte', 'lte'],
        'breadth': ['gte', 'lte'],
        'height': ['gte', 'lte'],
        'area': ['gte', 'lte'],
        'volume': ['gte', 'lte'],
    }

class BoxDeleteView(generics.DestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]
