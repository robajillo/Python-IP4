from app.models import Blog
from app import db
   
def setUp(self,id,title,blog,posted):
    self.new_blog = Blog(1,'test','go away errors',1,'2020-09-30 09:33:10.512236')
    
def test_check_instance_variables(self):
    self.assertEquals(self.new_blog.id,1)
    self.assertEquals(self.new_blog.title,'test')
    self.assertEquals(self.new_blog.blog,"go away errors")
    self.assertEquals(self.new_blog.user_id,1)
    self.assertEquals(self.new_blog.posted,'2020-09-30 09:33:10.512236')
    
def test_save_pitch(self):
    self.new_blog.save_blog()
    self.assertTrue(len(Blog.query.all())>0)
    
def test_get_blog_by_id(self):

    self.new_blog.save_pitch()
    got_blog = Blog.get_pitch(1)
    self.assertTrue(len(got_blog) == 1)