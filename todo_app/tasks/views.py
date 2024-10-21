from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task, UserProfile
from .serializers import TaskSerializer, UserSerializer, AddTaskSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .permission import IsEmployer, IsEmployee
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployer])
def add_task(request):
    """
    Allow an Employer to add the task
    :param request: User Request Object
    :return: Response Json Object
    """
    serializer = AddTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(employer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsEmployer])
def edit_task(request, task_id):
    """
    Allow an Employer to edit the task.
    :param request: User Request Object
    :param task_id: Task ID
    :return: Response Json Object
    """
    try:
        task = Task.objects.get(id=task_id, employer=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found or you do not have a permission to edit this task.'}, status=status.HTTP_404_NOT_FOUND)
    try:
        if request.data.get('title') and request.data.get('description') and request.data.get('status') and request.data.get('employee'):
            task.title = request.data.get('title')
            task.description = request.data.get('description')
            task.status = request.data.get('status')
            task.employee = UserProfile.objects.get(id=request.data.get('employee'))
            task.save()
            return Response({'message': 'Task Data Updated Successfully.'}, status=status.HTTP_205_RESET_CONTENT)
        else:
            raise Exception("Invalid Request.")
    except Exception as e:
        print("Error: ", e)
        return Response({'error': "Invalid Request."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsEmployer])
def delete_task(request, task_id):
    """
    Allow an Employer to delete the task.
    :param request: User Request Object
    :param task_id: Task ID
    :return: Response Json Object
    """
    try:
        task = Task.objects.get(id=task_id, employer=request.user)
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Task not found or you do not have permission to delete this Task.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployer])
def view_tasks(request):
    """
    Allow an Employer to view all the task they created
    :param request:
    :return:
    """
    tasks = Task.objects.filter(employer=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def view_employee_tasks(request):
    """
    Allow an Employee to view their Tasks.
    :param request: User Request Object
    :return: Response Json Object
    """
    tasks = Task.objects.filter(employee=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsEmployee])
def update_task_status(request, task_id):
    """
    Allow an Employee to Update their task status
    :param request: User Request Object
    :param task_id: Task ID
    :return: Response Json Object
    """
    task = get_object_or_404(Task, id=task_id, employee=request.user)
    if 'status' in request.data:
        task.status = request.data['status']
        task.save()
        return Response({'status': 'Task status updated'})
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Allow the User to log in and generate or retrieve their Token
    :param request: User Request Object
    :return: Response Json Object
    """
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    user = authenticate(phone_number=phone_number, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'message': 'Login successful',
            'user_id': user.id,
            'role': user.role
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployer])
def add_employee(request):
    """
    Allow an employer to add an employee under them.
    :param request: User Request Object
    :return: Allow an employer to add an employee under them.
    """
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    if not phone_number or not password:
        return Response({'error': 'Phone number and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if UserProfile.objects.filter(phone_number=phone_number).exists():
        return Response({'error': 'Phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    employee = UserProfile.objects.create_user(
        phone_number=phone_number,
        password=password,
        role='employee',
        employer=request.user
    )
    return Response({'message': 'Employee added successfully'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsEmployer])
def delete_employee(request, employee_id):
    """
    Allow an employer to delete an employee under them.
    :param request: User Request Object
    :param employee_id: Employee ID
    :return: Response Json Object
    """
    try:
        employee = UserProfile.objects.get(id=employee_id, employer=request.user, role='employee')
        employee.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Employee not found or you do not have permission to delete this employee.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsEmployer])
def edit_employee(request, employee_id):
    """
    Allow an employer to edit an employee's phone number or password.
    :param request: User Request Object
    :param employee_id: Employee ID
    :return: Response Json Object
    """
    try:
        employee = UserProfile.objects.get(id=employee_id, employer=request.user, role='employee')
    except UserProfile.DoesNotExist:
        return Response({'error': 'Employee not found or you do not have permission to edit this employee.'}, status=status.HTTP_404_NOT_FOUND)

    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    if phone_number:
        if UserProfile.objects.filter(phone_number=phone_number).exclude(id=employee.id).exists():
            return Response({'error': 'Phone number already in use.'}, status=status.HTTP_400_BAD_REQUEST)
        employee.phone_number = phone_number

    if password:
        employee.set_password(password)

    employee.save()
    return Response({'message': 'Employee information updated successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployer])
def view_employees(request):
    """
    Allow an employer to view all employees under them.
    :param request: User Request Object
    :return: Response Json Object
    """
    employees = UserProfile.objects.filter(employer=request.user, role='employee')
    serializer = UserSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
