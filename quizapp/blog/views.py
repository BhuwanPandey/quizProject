from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz
from .serializer import QuizSerializer





@api_view(['GET', 'POST'])
def question_list(request):
    # List all the question or create a new question.
    if request.method == 'GET':
        ques = Quiz.objects.all()
        serializer = QuizSerializer(ques, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({'error':'something went wrong !'}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):
    # Retrieve, update or delete a question.
    try:
        ques = Quiz.objects.get(id=pk)
    except Quiz.DoesNotExist:
        return Response({'error':'particular id is not exist'},status=404)

    if request.method == 'GET':
        serializer = QuizSerializer(ques)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuizSerializer(ques, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':'something went wrong !'}, status=400)

    elif request.method == 'DELETE':
        ques.delete()
        return Response(f'question with id-{pk} deleted')

