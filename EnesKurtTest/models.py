from django.db import models

class User(models.Model):
    # id, name, username, email, adress, phone, website, company
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.JSONField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    company = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'user'
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Posts(models.Model):
    # userId, id, title, body
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Comments(models.Model):
    # postId, id, name, email, body
    postid = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Album(models.Model):
    # userId, id, title
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'album'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Photos(models.Model):
    # albumId, id, title, url, thumbnailUrl
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    thumbnailUrl = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photos'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Todos(models.Model):
    # userId, id, title, completed
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todos'
        ordering = ['created_at']

    def __str__(self):
        return self.title

