from tastypie.resources import ModelResource
from tastypie.constants import ALL	
from service.models import service

class serviceresource(ModelResource):
      class Meta:
            queryset=service.objects.all()
            resource_name='service'
            filtering={'title':ALL}
