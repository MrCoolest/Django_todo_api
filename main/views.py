
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import TodoSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
def homepage(request):
    return Response({
        'status' : 200,
        'message' : 'Yes Its Working'
    })



class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data = data) 
        if not serializer.is_valid():
            return Response({'status' : False, "error" : serializer.errors, "Message" : "Something is not good"})
        else:
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            # user.save()

            return Response({'status' : True, "data" : serializer.data,  'refresh': str(refresh),
        'access': str(refresh.access_token) ,"Message" : "Register Successful"})




class TodoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id = None):
        if id:
            data = Todo_items.objects.filter(td_id=id).first()
            serializers = TodoSerializer(data)
            if data is not None:
                return Response({
                    'status' : 200,
                    'data' : serializers.data
                })
            else :
                return Response({
                    'status' : 404,
                    'message' : "Data is Not Found"
                })
        else :
            todo_data = Todo_items.objects.all()
            serializer = TodoSerializer(todo_data, many=True)
            return Response({
               "Status" : True,
                "Message" : "Todo Fetched",
                'data' : serializer.data
            })


    
    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            try:
                data = request.data
                data['user'] = request.user.id
                print(request.user.id)
                serializer = TodoSerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                    'status' : True,
                    'message' : "Success data!",
                    'data' : serializer.data
                    })
                else :
                    return Response({
                    'status' : False,
                    'message' : "All Fields are not Given",
                    'data' : serializer.errors
                    })
            except Exception as e:
                return Response({
                    'status' : False,
                    'message' : "Something Went Wrong!"
                })
        else :
            return Response({
                    'status' : 401,
                    'message' : "Unauthorized"
                })
            
    def patch(self, request, *args, **kwargs):
        if request.user.is_staff:
            try : 
                data = request.data
                if not data.get('td_id'):
                    return Response({
                        'status' : False,
                        'message' : "Data is not Found"
                    })
                elif data.get('td_id'):
                    obj = Todo_items.objects.filter(td_id=data.get('td_id')).first()
                    serializer = TodoSerializer(obj, data = data, partial = True)
                    if serializer.is_valid() and obj is not None:
                        serializer.save()
                        return Response({
                            'status' : True,
                            'message' : "Data Updated Successfully"
                        })
                    else: 
                        return Response({
                            'status' : False,
                            'message' : "Correct the Data"
                        }) 
            except Exception as e:
                return Response({
                    'status' : False,
                    'message' : "Something Went Wrong!"
                })
        else :
            return Response({
                    'status' : 401,
                    'message' : "Unauthorized"
                })
                

    def delete(self, request, *args, **kwargs):
        if request.user.is_staff:
            try : 
                data = request.data
                if not data.get('td_id'):
                    return Response({
                        'status' : False,
                        'message' : "Data is not Found"
                    })
                elif data.get('td_id'):
                    obj = Todo_items.objects.filter(td_id=data.get('td_id')).first()
                    if obj is not None:
                        obj.delete()
                        return Response({
                            'status' : True,
                            'message' : "Data Deleted Successfully"
                        })
                    else: 
                        return Response({
                            'status' : False,
                            'message' : "Data is not found"
                        }) 
            except Exception as e:
                return Response({
                    'status' : False,
                    'message' : "Something Went Wrong!"
                })
        else :
            return Response({
                    'status' : 401,
                    'message' : "Unauthorized"
                })
            
