from rest_framework import serializers

class ProductTwoSerializer(serializers.Serializer):
    char_2 = serializers.CharField()
    int_2 = serializers.IntegerField()

    class Meta:
        fields = '__all__'