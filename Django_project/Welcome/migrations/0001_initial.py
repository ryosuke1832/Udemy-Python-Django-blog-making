# Generated by Django 4.1.7 on 2023-03-27 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MemberList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="名前")),
                ("mail", models.EmailField(max_length=100, verbose_name="メール")),
                ("gender", models.BooleanField(verbose_name="性別")),
                ("age", models.IntegerField(default=0, verbose_name="年齢")),
                ("address", models.CharField(max_length=100, verbose_name="住所")),
            ],
        ),
    ]