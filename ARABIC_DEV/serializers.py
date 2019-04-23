
from apps.stemmers_comparer import models
from rest_framework import serializers


class RequirementSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Requirement
		fields = ('id', 'content')


class FeaturesSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Feature
		fields = ('id', 'content')


class FeaturesSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Feature
		fields = ('id', 'content')

class AuthorSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Author
		fields = ('id', 'first_name', 'last_name', 'github_account_link', 'website')


class ProgrammingLanguageSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.ProgrammingLanguage
		fields = ('name', 'website')


class StemmerSerializer(serializers.ModelSerializer):

	authors = serializers.PrimaryKeyRelatedField(required=True, many=True, read_only=False, queryset=models.Author.objects.all())
	programming_languages = serializers.PrimaryKeyRelatedField(required=True, many=True, read_only=False, queryset=models.ProgrammingLanguage.objects.all())
	requirements = serializers.PrimaryKeyRelatedField(required=True, many=True, read_only=False, queryset=models.Requirement.objects.all())
	features = serializers.PrimaryKeyRelatedField(required=True, many=True, read_only=False, queryset=models.Feature.objects.all())

	class Meta:
		model = models.Stemmer
		fields = ('name', 'display_name', 'authors', 'license', 'description', 'documentation_link', 'download_link', 'programming_languages', 'requirements', 'features', 'how_to_use')


class UserRatingSerializer(serializers.ModelSerializer):
	rating__count = serializers.ReadOnlyField(source='rating.count')
	rating__average = serializers.ReadOnlyField(source='rating.average')
	rating__total = serializers.ReadOnlyField(source='rating.total')
	rating__stemmer_id = serializers.ReadOnlyField(source='rating.stemmer__name')


	class Meta:
		model = models.UserRating
		fields = ('user_email_address', 'comment', 'score', 'rating__count', 'rating__average', 'rating__total', 'rating', 'rating__stemmer_id', 'created', 'modified')


class RatingSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Rating
		fields = ('id', 'count', 'average', 'total', 'stemmer')

