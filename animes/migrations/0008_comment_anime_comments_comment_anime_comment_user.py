# Generated by Django 4.0.6 on 2022-07-24 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("animes", "0007_alter_anime_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("comment", models.CharField(max_length=144)),
            ],
        ),
        migrations.AddField(
            model_name="anime",
            name="comments",
            field=models.ManyToManyField(
                related_name="Anime_comments",
                through="animes.Comment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="anime",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="animes.anime"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
