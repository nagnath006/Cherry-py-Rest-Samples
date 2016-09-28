from tastypie.resources import ModelResource
from tastypie.constants import ALL	
from service.models import service

class ServiceResource(ModelResource):
      class Meta:
            queryset=Service.objects.all()
            resource_name='Service'
            filtering={'title':ALL}
