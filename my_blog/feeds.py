from django.contrib.syndication.views import Feed

from .models import Post


class AllPostsRssFeed(Feed):

    title = "杭州兄弟博客"

    link = "hangzhoubrother.com/all/rss"

    description = "the blog which about Python3!"
    
    #显示的内容条目
    def items(self):
        return Post.objects.all()

    #内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_discription(self, item):
        return item.body
