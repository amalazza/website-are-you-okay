# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from rest_framework.response import Response
from rest_framework import generics
from .models import Pengguna, Pertanyaan, Jawaban, TingkatDepresi, HasilDeteksi, Penanganan, HistoryPertanyaanJawaban, Pencegahan, Artikel
from .serializers import PenggunaSerializer, PertanyaanSerializer, JawabanSerializer, TingkatDepresiSerializer, HasilDeteksiSerializer, PenangananSerializer, HistoryPertanyaanJawabanSerializer, PencegahanSerializer, ArtikelSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverviewPengguna(request):
    api_urls={
        'List': 'pengguna-list',
        'Detail View': 'pengguna-detail/<int:id>/',
        'Create': 'pengguna-create',
        'Update View': 'pengguna-update/<int:id>/',
        'Delete View': 'pengguna-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPengguna(request):
    pengguna = Pengguna.objects.all()
    serializer = PenggunaSerializer(pengguna, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewPertanyaan(request):
    api_urls={
        'List': 'pertanyaan-list',
        'Detail View': 'pertanyaan-detail/<int:id>/',
        'Create': 'pertanyaan-create',
        'Update View': 'pertanyaan-update/<int:id>/',
        'Delete View': 'pertanyaan-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPertanyaan(request):
    pertanyaan = Pertanyaan.objects.all()
    serializer = PertanyaanSerializer(pertanyaan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewJawaban(request):
    api_urls={
        'List': 'jawaban-list',
        'Detail View': 'jawaban-detail/<int:id>/',
        'Create': 'jawaban-create',
        'Update View': 'jawaban-update/<int:id>/',
        'Delete View': 'jawaban-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllJawaban(request):
    jawaban = Jawaban.objects.all()
    serializer = JawabanSerializer(jawaban, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewTingkatDepresi(request):
    api_urls={
        'List': 'tingkatdepresi-list',
        'Detail View': 'tingkatdepresi-detail/<int:id>/',
        'Create': 'tingkatdepresi-create',
        'Update View': 'tingkatdepresi-update/<int:id>/',
        'Delete View': 'tingkatdepresi-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllTingkatDepresi(request):
    tingkatdepresi = TingkatDepresi.objects.all()
    serializer = TingkatDepresiSerializer(tingkatdepresi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewHasilDeteksi(request):
    api_urls={
        'List': 'hasildepresi-list',
        'Detail View': 'hasildeteksi-detail/<int:id>/',
        'Create': 'hasildeteksi-create',
        'Update View': 'hasildeteksi-update/<int:id>/',
        'Delete View': 'hasildeteksi-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllHasilDeteksi(request):
    hasildeteksi = HasilDeteksi.objects.all()
    serializer = HasilDeteksiSerializer(hasildeteksi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewPenanganan(request):
    api_urls={
        'List': 'penanganan-list',
        'Detail View': 'penanganan-detail/<int:id>/',
        'Create': 'penanganan-create',
        'Update View': 'penanganan-update/<int:id>/',
        'Delete View': 'penanganan-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPenanganan(request):
    penanganan = Penanganan.objects.all()
    serializer = PenangananSerializer(penanganan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewHistoryPertanyaanJawaban(request):
    api_urls={
        'List': 'historypertanyaanjawaban-list',
        'Detail View': 'historypertanyaanjawaban-detail/<int:id>/',
        'Create': 'historypertanyaanjawaban-create',
        'Update View': 'historypertanyaanjawaban-update/<int:id>/',
        'Delete View': 'historypertanyaanjawaban-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllHistoryPertanyaanJawaban(request):
    historypertanyaanjawaban = HistoryPertanyaanJawaban.objects.all()
    serializer = HistoryPertanyaanJawaban(historypertanyaanjawaban, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewPencegahan(request):
    api_urls={
        'List': 'pencegahan-list',
        'Detail View': 'pencegahan-detail/<int:id>/',
        'Create': 'pencegahan-create',
        'Update View': 'pencegahan-update/<int:id>/',
        'Delete View': 'pencegahan-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllPencegahan(request):
    pencegahan = Pencegahan.objects.all()
    serializer = PencegahanSerializer(pencegahan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOverviewArtikel(request):
    api_urls={
        'List': 'artikel-list',
        'Detail View': 'artikel-detail/<int:id>/',
        'Create': 'artikel-create',
        'Update View': 'artikel-update/<int:id>/',
        'Delete View': 'artikel-delete/<int:id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAllArtikel(request):
    artikel = Artikel.objects.all()
    serializer = ArtikelSerializer(artikel, many=True)
    return Response(serializer.data)

