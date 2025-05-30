from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from users.models import EmailVerificationCode
from django.utils import timezone


User = get_user_model()

# class RegisterViewTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.register_url = reverse('register-list')
#         self.user_data = {
#             'username' : "testuser123",
#             'email' : "testuser123@gmail.com",
#             'password' : "strongpassword123",
#             'password2' : "strongpassword123",
#             'first_name' : "fakefake",
#             'last_name' : "fakefake",
#             'phone_number' : "995568633770",
#         }
        
#     def test_registration_success(self):
#         response = self.client.post(self.register_url, self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(User.objects.filter(email=self.user_data['email']).exists())
#         user = User.objects.get(email=self.user_data['email'])
#         self.assertFalse(user.is_active)
#         self.assertTrue(EmailVerificationCode.objects.filter(user=user).exists())
        
#     def test_user_registration_password_mismatch(self):
#         self.user_data['password2'] = 'differentpassword123'
#         response = self.client.post(self.register_url, self.user_data, format = 'json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('password', response.data)
#         self.assertFalse(User.objects.filter(email=self.user_data['email']).exists())
        
#     def test_user_registration_duplicate_mail(self):
#         User.objects.create(
#             username='random123',
#             email=self.user_data['email'],
#             password='randompassword123',
#         )
#         response = self.client.post(self.register_url, self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('email', response.data)
        
        
        
# class EmailVerificationCodeTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
        
#         self.user = User.objects.create(
#             username = "testuser123",
#             email = "testuser123@gmail.com",
#             password = "strongpassword123",
#             is_active = False
#         )
        
#         self.confirm_url = reverse('register-confirm-code')
#         self.verification_code = EmailVerificationCode.objects.create(
#             user = self.user,
#             code = '123456',
#             created_at = timezone.now()
#         )
        
        
#     def test_successful_verification(self):
#         data = {
#             'email' : 'testuser123@gmail.com',
#             'code' : '123456',
#         }
#         response = self.client.post(self.confirm_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.user.refresh_from_db()
#         self.assertTrue(self.user.is_active)
        
    
#     def test_invalid_code(self):
#         data = {
#             'email': 'testuser123@gmail.com',
#             'code' : '685549',
#         }
#         response = self.client.post(self.confirm_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.user.refresh_from_db()
#         self.assertFalse(self.user.is_active)
        
        
#     def test_expired_code(self):
#         self.verification_code.created_at = timezone.now() - timezone.timedelta(hours=24)
#         self.verification_code.save()
#         data = {
#             'email': 'testuser123@gmail.com',
#             'code' : '123456'
#         }
#         response = self.client.post(self.confirm_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.user.refresh_from_db()
#         self.assertFalse(self.user.is_active)
        
        
        

class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('token_obtain_pair')
        self.category_detail_url = reverse('category_list')
        
        self.user = User.objects.create_user(
            username = 'authuser',
            email = 'auth@example.com',
            password = 'auth123password',
        )
        
        
    def test_invalid(self):
        data = {
            'email': 'auth@example.com',
            'password' : '1234',
        }
       
        
    