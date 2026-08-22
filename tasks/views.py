from rest_framework import permissions, viewsets

from .filters import TaskFilter
from .models import Task
from .serializers import TaskSerializer


class IsOwner(permissions.BasePermission):
    """Only allow the owner of a task to view/edit/delete it."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class TaskViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for tasks, scoped to the logged-in user.

    Supports:
      - GET    /api/tasks/            list (filter/search/order)
      - POST   /api/tasks/            create
      - GET    /api/tasks/{id}/       retrieve
      - PUT    /api/tasks/{id}/       full update
      - PATCH  /api/tasks/{id}/       partial update
      - DELETE /api/tasks/{id}/       delete

    Filtering: ?status=pending&priority=high&due_before=2026-12-31
    Search:    ?search=keyword  (title, description)
    Ordering:  ?ordering=due_date or ?ordering=-created_at
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at', 'priority', 'status']

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
