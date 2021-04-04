from django.db import models


# Create your models here.
# tapleの右側(high)は管理画面の中で表示される名前、右側（danger）は機械が読む名前
CHOICE = ('danger', 'high'),('warning', 'normal'),('primary','low')


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        # 人間がタイピングで選択するのではなく、選択肢が与えられてその選択肢の中から選ぶことができる
        choices = CHOICE
        )
    duedate = models.DateField()

    # オブジェクトが作成されたときに実行される関数
    def __str__(self):
        return self.title