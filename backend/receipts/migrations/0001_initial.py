from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='receipts.category')),
            ],
        ),
        migrations.CreateModel(
            name='StoreItemAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias_name', models.CharField(max_length=200)),
                ('canonical_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.item')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.store')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('raw_text', models.TextField(blank=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.store')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('price_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipts.receipt')),
                ('store_item_alias', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipts.storeitemalias')),
            ],
        ),
    ]
