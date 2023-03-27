from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

def upload_data(request):
    if request.method == 'POST':
        file_name = request.FILES.get('file').name
        file = request.FILES.get('file')
        content = documentService.extractFile(file)
        if content:
            data = documentService.convertfile(content)
            response = HttpResponse(content_type='application/file')
            response['Content-Deposition'] = f'attachment; filename="{file_name}.{data.getExt()}"'
            return response
        return Response(data={"detail": "Error"}, status=status.HTTP_400_BAD_REQUEST)


# response.setHeader("Content-Disposition", "attachment; filename=" + resource.getFilename())
