from django.shortcuts import render
from django.http import HttpResponse, JsonReponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorator_csrf import csrf_exempt
from rest_framework import status

# Create your views here.
from restframework.views import APIView


documentConverterService = DocumentConverterService()


@csrf_exempt
@api_view(['POST'])
def convert_pdf_to_docx_api(request, format=None):
    if request.method == 'POST' and request.FILES:
        if len(request.FILES['files']) > 1:
            for f in request.FILES['files']:
                content = documentConverterService.extractfiletype(f)
                pdfcontents, filename, ext = documentConverterService.convertPdfToDocx(content)
                if pdfcontents is not None:
                    response =  Response(status=status.HTTP_200_OK, content_type="application/docx")
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        else:
            content = documentConverterService.extractfiletype(request.FILES['files'])
            if content is not None:
                pdfcontents = documentConverterService.convertPdfToDocx(content)
                response = Response(status=status.HTTP_200_OK, content_type="application/docx")
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@csrf_exempt
@api_view(['POST'])
def convert_word_to_excel_api(request, format=None):
    if request.method == "POST" and request.FILES:
        if len(request.FILES['files']) > 1:
            for f in request.FILES['files']:
                content = documentConverterService.extractfiletype(f)
                wordtoexcel, filename, ext = documentConverterService.convertWordToExcel(content)
                if wordtoexcel is not None:
                    response = Response(status=status.HTTP_200_OK, content_type="application/xsxl")
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        else:
            content = documentConverterService.extractfiletype(request.FILES['files'])
            if content is not None:
                wordtoexcel = documentConverterService.convertWordToExcel(content)
                response = Response(status=status.HTTP_200_OK, content_type="application/xsxl")
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@csrf_exempt
@api_view(['POST'])
def convert_docx_to_pdf_api(request, format=None):
    if request.method == "POST" and request.FILES:
        if len(request.FILES['files']) > 1:
            for f in request.FILES['files']:
                content = documentConverterService.extractfiletype(f)
                docxtopdf, filename, ext  = documentConverterService.convertDocxToPdf(content)
                if docxtopdf is not None:
                    response = Response(status=status.HTTP_200_OK, content_type="application/docx")
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        else:
            content = documentConverterService.extractfiletype(request.FILES['files'])
            if content is not None:
                docxtopdf = documentConverterService.convertDocxToPdf(content)
                response = Response(status=status.HTTP_200_OK, content_type="application/pdf")
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

@csrf_exempt
@api_view(['POST'])
def convert_xsxl_to_docx_api(request, format=None):
    if request.method == "POST" and request.FILES:
        if len(request.FILES['files']) > 1:
            for f in request.FILES['files']:
                content = documentConverterService.extractfiletype(f)
                xsxltodocx, filename, ext = documentConverterService.convertXsxlToDocx(content)
                if xsxltodocx is not None:
                    response = Response(status=status.HTTP_200_OK, content_type="application/xsxl")
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        else:
            content = documentConverterService.extractfiletype(request.FILES['files'])
            if content is not None:
                xsxltodocx, filename = documentConverterService.convertXsxlToDocx(content)
                response = Response(status=status.HTTP_200_OK, content_type="application/xsxl")
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@csrf_exempt
@api_view(['POST'])
def convert_xsxl_to_corel_draw(request, format=None):
    if request.method == "POST" and request.FILES:
        if len(request.FILES['files']) > 1:
            for f in request.FILES['files']:
                content = documentConverterService.extractfiletype(f)
                xsxltocoreldraw, filename, ext = documentConverterService.convertXsxlToCorelDraw(content)
                if xsxltocoreldraw is not None:
                    response = Response(status=status.HTTP_200_OK, content_type="application/corel-draw")
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        else:
            content = documentConverterService.extractfiletype(request.FILES['files'])
            if content is not None:
                xsxltocoreldraw, filename = documentConverterService.convertXsxlToCorelDraw(content)
                response = Response(status=status.HTTP_200_OK, content_type="application/corel-draw")
                return response
            return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")


@csrf_exempt
@api_view(['POST'])
def convert_xsxl_to_pdf_api(request, format=None):
    if request.method == "POST" and request.FILES:
        if len(request.FILES['files']) > 1:
            for f in request.FILES['files']:
                content = documentConverterService.extractfiletype(f)
                xsxltopdf, filename, ext = documentConverterService.convertXsxlToPdf(content)
                if xsxltopdf is not None:
                    response = Response(status=status.HTTP_200_OK, content_type="application/pdf")
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")
        else:
            content = documentConverterService.extractfiletype(request.FILES['files'])
            xsxltopdf, filename, ext = documentConverterService.convertXsxlToPdf(content)
            if xsxltopdf is not None:
                response = Response(status=status.HTTP_200_OK, content_type="application/pdf")
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            return Response(body={"detail": "Error converting file"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

