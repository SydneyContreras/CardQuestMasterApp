# Generated by Django 5.0 on 2023-12-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='pokemoncard',
            old_name='released_date',
            new_name='release_date',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='card',
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='collection',
            name='trainer',
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='abilities',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='card_type',
            field=models.CharField(blank=True, choices=[('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon'), ('Dark', 'Dark'), ('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Steel', 'Steel'), ('Fairy', 'Fairy')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='evolution_stage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='rarity',
            field=models.CharField(blank=True, choices=[('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pokemoncard',
            name='weakness',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='card',
            field=models.ManyToManyField(blank=True, to='Myapp.pokemoncard'),
        ),
        migrations.AddField(
            model_name='collection',
            name='trainer',
            field=models.ManyToManyField(blank=True, to='Myapp.trainer'),
        ),
    ]