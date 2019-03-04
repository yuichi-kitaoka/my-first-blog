from django.shortcuts import render

# 新しく作成
from django.utils import timezone
from .models import Post

def post_list(request):
    # 公開したブログ記事を published_dateで並べ替えをしたい
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
