from django.db import models
#timezoneを使うためにインポート
from django.utils import timezone

# Create your models here.

#models.Modelを書くのはお決まり
class Posts(models.Model):

    #Metaとかobjectとかはおまじない
    class Meta(object):
        #作成されるテーブル名を指定
        db_table = 'posts'

    #カラム名=データの形式(管理画面に表示される名前,その他の制約)
    text = models.CharField(verbose_name='本文', max_length=255)
    created_at = models.DateField(verbose_name='作成日', default=timezone.now)

    #管理画面に表示されるように設定(おまじない)
    def __str__(self):
        return self.text, self.created_at