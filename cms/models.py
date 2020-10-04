from django.db import models


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=200)
    cat_desc = models.TextField()

    def __str__(self):
        return self.cat_title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200)
    post_author = models.CharField(max_length=36)
    post_doc = models.DateTimeField(auto_now_add=True)
    post_desc = models.TextField()

    def __str__(self):
        return self.post_title
