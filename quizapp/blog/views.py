from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz,Category,Question
from .serializer import QuizSerializer,CategorySerializer,QuestionSerializer



# for category
@api_view(['GET', 'POST'])
def category_list(request):
    # List all the category or create a new category.
    if request.method == 'GET':
        categry = Category.objects.all()
        serializer = CategorySerializer(categry, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        getdata=Category.objects.filter(name__contains=request.data['name'])
        if getdata:
            name=request.data['name']
            return Response({'error':f'{name} is already exist !'}, status=400)
        else:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response({'error':'something went wrong !'}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    # Retrieve, update or delete a category.
    try:
        categry = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response({'error':'particular id is not exist'},status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(categry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        getdata=Category.objects.filter(name__contains=request.data['name'])
        if getdata:
            name=request.data['name']
            return Response({'error':f'{name} is already exist !'}, status=400)
        else:
            serializer = CategorySerializer(categry, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'error':'something went wrong !'}, status=400)

    elif request.method == 'DELETE':
        categry.delete()
        return Response(f'question with id-{pk} deleted')


# for quiz
@api_view(['GET', 'POST'])
def quiz_list(request):
    # List all the quiz or create a new quiz.
    if request.method == 'GET':
        quiz = Quiz.objects.all()
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        getdata=Quiz.objects.filter(subcategory__contains=request.data['subcategory'])
        if getdata:
            name=request.data['subcategory']
            return Response({'error':f'{name} is already exist !'}, status=400)
        else:
            serializer = QuizSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response({'error':'something went wrong !'}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def quiz_detail(request, pk):
    # Retrieve, update or delete a quiz.
    try:
        quiz = Quiz.objects.get(id=pk)
    except Quiz.DoesNotExist:
        return Response({'error':'particular id is not exist'},status=404)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':'something went wrong !'}, status=400)

    elif request.method == 'DELETE':
        quiz.delete()
        return Response(f'question with id-{pk} deleted')


# for question
@api_view(['GET', 'POST'])
def question_list(request):
    # List all the question or create a new question.
    if request.method == 'GET':
        ques = Question.objects.all()
        serializer = QuestionSerializer(ques, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({'error':'something went wrong !'}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):
    # Retrieve, update or delete a question.
    try:
        ques = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        return Response({'error':'particular id is not exist'},status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(ques)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(ques, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':'something went wrong !'}, status=400)

    elif request.method == 'DELETE':
        ques.delete()
        return Response(f'question with id-{pk} deleted')