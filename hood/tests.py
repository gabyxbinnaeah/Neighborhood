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


class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Method that creates instance of profile class
        '''
        self.vin= Profile(image="start.pgn",bio="Motivated IT geek", email="gabs@gmail.com", contact="0791563569") 
        self.vin.save_profile() 

    def test_instance(self):
        '''
        method that checks if profile is instance
        '''
        self.assertTrue(isinstance(self.vin,Profile))


    def test_save_profile(self):
        '''
        Method that test if profile is being saved
        '''
        self.vin.save_profile()
        list_profile=Profile.objects.all()
        self.assertTrue(len(list_profile)>0) 

    def test_delete_profile(self):
        '''
        method that checks if profile is deleted
        '''
        self.vin.save_profile()
        self.vin.delete_profile()
        left_profiles=Profile.objects.all()
        self.assertTrue(len(left_profiles)==0) 

    def test_bio_update(self):
        '''
        method that checks if bio can be updated
        '''
        self.vin.save_profile()
        self.vin.update_profile_bio( self.vin.id,'Humble motivated coder')
        profile_list=Profile.objects.all()
        self.assertTrue(len(profile_list)==1)
        new_bio=Profile.objects.all().first()
        self.assertTrue(new_bio.bio=='Humble motivated coder') 


class BusinessTestClass(TestCase):
    def setUp(self):
        '''
        Method that creates instance of business class
        '''
        self.gas= Business(image="start.pgn",name="gas", business_email="gas@gmail.com", description="0791563569") 
        self.gas.save_business() 

    def test_instance(self):
        '''
        method that checks if business  is instance
        '''
        self.assertTrue(isinstance(self.gas,Business))


    def test_save_business(self):
        '''
        Method that test if business  is being saved
        '''
        self.gas.save_business()
        saved_bs=Business.objects.all()
        self.assertTrue(len(saved_bs)>0) 

    def test_delete_business(self):
        '''
        method that checks if business  is deleted
        '''
        self.gas.save_business()
        self.gas.delete_business()
        left_bs=Business.objects.all()
        self.assertTrue(len(left_bs)==0) 


class PostTestClass(TestCase):
    def setUp(self):
        '''
        Method that creates instance of posts class
        '''
        self.news= Post(post="will be delivered soon",title="gas") 
        self.news.save_post() 

    def test_instance(self):
        '''
        method that checks if post  is instancetiated
        '''
        self.assertTrue(isinstance(self.news,Post))


    def test_save_post(self):
        '''
        Method that test if post is being saved
        '''
        self.news.save_post()
        saved_post=Post.objects.all()
        self.assertTrue(len(saved_post)>0) 

    # def test_delete_business(self):
    #     '''
    #     method that checks if business  is deleted
    #     '''
    #     self.news.save_post()
    #     self.news.delete_post()
    #     left_post=Post.objects.all()
    #     self.assertTrue(len(left_post)==0) 



