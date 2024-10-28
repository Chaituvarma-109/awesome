from django.contrib import admin

from a_posts.models import Post, Tag, Comment, Reply, LikedPost, LikedComment, LikedReply

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPost)
admin.site.register(LikedComment)
admin.site.register(LikedReply)
