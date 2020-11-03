from app.models import Comment
from app import db
class CommentTest(unittest.TestCase):
    def setUp(self):
        self.newComment = Comment(id = 1, comment = 'Test comment', user = self.userDorcas, blog_id = self.newBlog)
    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
    def checkvariablesTest(self):
        self.assertEquals(self.newComment.comment,'Test comment')
        self.assertEquals(self.newComment.user,self.dee)
        self.assertEquals(self.newComment.blogs_id,self.newblog)
class CommentTest(unittest.TestCase):
    def setUp(self):
        self.dee = User(username='dee', password='1233', email='sawe@gmail.com')
        self.newblog = Blog(id=1, title='Encapsulation', content='Testing', user_id=self.userDorcas.id)
        self.newComment = Comment(id=1, comment =' test comment', user_id=self.dee.id, blog_id = self.newblog.id )
    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
        Comment.query.deleteComment()
    def checkInstanceVariables(self):
        self.assertEquals(self.newComment.comment, 'test comment')
        self.assertEquals(self.newComment.user_id, self.dee.id)
        self.assertEquals(self.newComment.blog_id, self.new_blog.id)