from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import View
#form.pyからフォームをインポート
from .form import WriteForm
from .models import Posts


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Postsテーブルのデータを全て取得
        queryset = Posts.objects.all().order_by('-created_at')
        # 値付きでpost.htmlに飛ぶ
        return render(request, 'posts/post.html', {'posts': queryset})


index = IndexView.as_view()


class WriteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'posts/write.html', {'form': WriteForm})

    def post(self, request, *args, **kwargs):
        # formに書いた内容を格納する
        form = WriteForm(request.POST)
        # 保存する前に一旦取り出す
        post = form.save(commit=False)
        # 保存
        post.save()
        # indexのviewに移動
        return redirect(to='posts:index')


write = WriteView.as_view()