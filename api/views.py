from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note
from rest_framework import status
from .utils import updateNote,getSingleNote,deleteNote,createNote,getNotes
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response("hello from Json")

@api_view(["GET", "POST"])
def getNotes(request):
    if request.method =='GET':
        # return getNotes(request)
        notes =Note.objects.all().order_by('-updated')
        serializer=NoteSerializer(notes, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        return createNote(request)
@api_view(["GET",'POST',"PUT","DELETE"])
def getNote(request, pk):
    if request.method =='GET':
        return getSingleNote(request,pk)
    if request.method =='PUT':
        return updateNote(request,pk)
    if request.method =='DELETE':
        return deleteNote(request,pk)
       

