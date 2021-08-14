# 进行users子应用试图
from django.urls import path
from users.views import RegisterView, ImageCodeView, LoginView
from users.views import SmsCodeView, LogoutView, ForgetPasswordView
from users.views import UserCenterView, WriteBlogView

urlpatterns = [
    # 第一各参数是路由，参数二是视图函数
    path('register/', RegisterView.as_view(), name='register'),

    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),

    path('smscode/', SmsCodeView.as_view(), name='smscode'),
    # 登录
    path('login/', LoginView.as_view(), name='login'),
    # 退出登录
    path('logout/', LogoutView.as_view(), name='logout'),
    # 忘记密码
    path('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),
    # 用户中心
    path('center/', UserCenterView.as_view(), name='center'),
    # 写博客路由
    path('writeblog/', WriteBlogView.as_view(), name='writeblog'),
]


