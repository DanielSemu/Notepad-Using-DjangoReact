from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response
from rest_framework import status

def updateNote(request,pk):
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
def getSingleNote(request, pk):
    notes =Note.objects.get(id=pk)
    serializer=NoteSerializer(notes, many=False)
    return Response(serializer.data)
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note Was Deleted')
def createNote(request):
    data=request.data
    note =Note.objects.create(
        body=data['body']
    )
    serializer= NoteSerializer(note, many=False)
    return Response(serializer.data)
def getNotes():
    notes =Note.objects.all().order_by('-updated')
    serializer=NoteSerializer(notes, many=True)
    return Response(serializer.data)