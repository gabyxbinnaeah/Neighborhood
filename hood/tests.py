from django.test import TestCase
from .models import Profile,Neighborhood,Business,Post
# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        '''
        method that creates instance of Neighborhood and profile
        '''
        self.vin= Profile(image="start.pgn",bio="Motivated IT geek", email="gabs@gmail.com", contact="0791563569")
        self.vin.save_profile()

        self.blog=Neighborhood(image="omollo.png",name="omollo",profile=self.vin,likes=700,description="Taken at peak",admin="omollo",health_contact="0700000000", police_contact="0700000004")
        self.blog.save_image()

    def test_hood_instance(self):
        '''
        function that checks if image is instanciated 
        '''
        self.assertTrue(isinstance(self.blog,Neighborhood))

    def test_save_hood(self):
        '''
        Method that test if  model is saved 
        '''
        self.blog.save_hood()
        hood_list=Neighborhood.objects.all()
        self.assertTrue(len(hood_list)>0) 

    def test_hood_delete(self):
        '''
        method that checks if image is delete_image method deletes image 
        '''
        self.blog.save_hood()
        self.blog.delete_hood()
        check_list=Neighborhood.objects.all()
        self.assertTrue(len(check_list)==0)

