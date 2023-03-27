from django.urls import path
from documentconvert.views import (
        convert_pdf_to_docx_api,
        convert_word_to_excel_api,
        convert_docx_to_pdf_api,
        convert_xsxl_to_docx_api,
        convert_xsxl_to_corel_draw,
        convert_xsxl_to_pdf_api
)

urlpatterns = [
    path('pdf-to-docx/', convert_pdf_to_docx_api),
    path('word-to-excel/', convert_word_to_excel_api),
    path('docx-to-pdf/', convert_docx_to_pdf_api),
    path('xsxl-to-docx/', convert_xsxl_to_docx_api),
    path('xsxl-to-corel-draw/', convert_xsxl_to_corel_draw),
    path('xsxl-to-pdf-api/', convert_xsxl_to_pdf_api)
]


