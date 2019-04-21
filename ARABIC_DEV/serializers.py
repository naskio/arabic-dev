
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
		fields = ('id', 'first_name', 'last_name')


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
		fields = ('name', 'display_name', 'authors', 'programming_languages', 'requirements', 'features', 'how_to_use')

