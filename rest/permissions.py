from rest_framework.permissions import BasePermission

class IsEnrolled(BasePermission):
    def has_object_permission(self,request,view,obj):
        return obj.user.filter(id=request,user.id).exists()