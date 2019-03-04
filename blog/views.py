from django.shortcuts import render

# 新しく作成
def post_list(request):
    return render(request, 'blog/post_list.html', {})
