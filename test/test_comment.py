import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):    
    def setUp(self):
        self.new_comment = Comment()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))