from users.models import User

# def get_user_user(request):
#     if request.user.is_authenticated:
#         return User.objects.filter(username=request.user)

#     if not request.session.session_key:
#         request.session.create()
#     return User.objects.filter(session_key=request.session.session_key)
