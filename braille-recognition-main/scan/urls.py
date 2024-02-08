from django.urls.conf import path

from scan.views import ResultView, UploadView, UserHistorylView


app_name = 'scan'

urlpatterns = [
    path('', UploadView.as_view(), name='upload'),
    path('history/', UserHistorylView.as_view(), name='history'),
    path('result/<int:pk>/', ResultView.as_view(), name='result')
]
