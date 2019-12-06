from django.test import TestCase
from .models import Post, User
import unittest
# Create your tests here.
def test_post(): #Testea existencia de post segun titulo
    status = True
    try : 
        testpost = Post.object.values_list('title')
        print(str(testpost))
        status = True
    except : 
        status = False
    return testpost

def test_usuarios(): #Testear usuarios segun su username
    status = True
    try:
        testeouser = User.objects.values_list('username')
        print(str(testeouser))
        status = True
    except:
        status = False
    return testeouser

class prueba_post(unittest.TestCase):#prueba con query que muestra post existentes en la base de datos
    def test_post(self):
        self.assertTrue(test_post())
class prueba_user(unittest.TestCase):#prueba con query que muestra usuarios en la base de datos
    def test_usuarios(self):
        self.assertTrue(test_usuarios())