from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     my_username = data.get('username')
    #     my_password = data.get('password')

    #     try:
    #         user_obj = User.objects.get(username=my_username)
    #     except:
    #         raise serializers.ValidationError("This username does not exist")

    #     if not user_obj.check_password(my_password):
    #         raise serializers.ValidationError("Incorrect username/password combination! Noob..")

    #     return data

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	added_by = UserSerializer()
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'api-detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'item_id',
		)
	fav_count = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['name', 'description', 'detail', 'added_by', 'fav_count',]

	def get_fav_count(self, obj):
		return obj.favs.count()

class FavoriteItemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = FavoriteItem
		fields = ['id', 'user',]

class ItemDetailSerializer(serializers.ModelSerializer):
	favs = FavoriteItemsSerializer(many=True)
	class Meta:
		model = Item
		fields = '__all__'
		