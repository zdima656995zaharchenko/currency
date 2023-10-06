from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from rest_framework import filters as rest_framework_filters

from currency.models import Rate, Source, ContactUs, RequestResponseLog
from currency.api.v1.filters import RateFilter, ContactUsFilter
from currency.api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer, LogsSerializer
from rest_framework.renderers import JSONRenderer
from currency.api.v1.paginators import RatePagination


# from rest_framework_xml.renderers import XMLRenderer
# from rest_framework_yaml.renderers import YAMLRenderer


# class RateViewSet(viewsets.ModelViewSet):
#     queryset = Rate.objects.all().order_by("-created")
#     serializer_class = RateSerializer
#     renderer_classes = JSONRenderer
#     pagination_class = RatePagination
#     filter_backends = (
#         filters.DjangoFilterBackend,
#         rest_framework_filters.OrderingFilter,
#     )
#     filterset_class = RateFilter
#     ordering_fields = ("buy", "sell", "created")


# class RateDetailDestroyApiView(generics.RetrieveDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

class RateListAPIView(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateDetailedAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateCreateAPIView(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class SourceListAPIView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailedAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceCreateAPIView(generics.CreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsListAPIView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = (filters.CharFilter,)
    search_fields = ['name', 'message']

    ordering_fields = ('created',)

class ContactUsDetailedAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ContactUsCreateAPIView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class LogsListAPIView(generics.ListAPIView):
    queryset = RequestResponseLog.objects.all()
    serializer_class = LogsSerializer


class LogsDetailedAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestResponseLog.objects.all()
    serializer_class = LogsSerializer