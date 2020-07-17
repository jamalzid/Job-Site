from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','HEAD'])
def Job_api_list(request):
    jobs=Job.objects.all()
    data=Jobserializer(jobs,many=True).data
    return Response({'data':data})


@api_view(['GET'])
def job_detail_api(request,id):
    job = Job.objects.get(id=id)
    data = Jobserializer(job).data
    return Response({'data': data})
