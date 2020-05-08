import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """
    
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.pitch= Pitch(title = 'This is a heading', content = 'This is the body')
        # self.comment= Comment(comment = 'testing testing')

    def tearDown(self):
        Pitch.query.delete()



    def test_instance(self):
        self.assertTrue(isinstance(self.pitch, Pitch))
        # self.assertTrue(isinstance(self.comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.pitch.title,'This is a heading')
        self.assertEquals(self.pitch.content,'This is the body')
        # self.assertEquals(self.comment.comment,'testing testing')