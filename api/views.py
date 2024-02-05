from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response("hello from Json")

@api_view(["GET"])
def getNotes(request):
    notes =Note.objects.all().order_by('-updated')
    serializer=NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def createNote(request):
    print("gate Here")
    data=request.data
    note =Note.objects.create(
        body=data['body']
    )
    serializer= NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getNote(request, pk):
    notes =Note.objects.get(id=pk)
    serializer=NoteSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note Was Deleted')
