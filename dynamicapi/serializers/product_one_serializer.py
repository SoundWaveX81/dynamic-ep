from rest_framework import serializers

class ProductOneSerializer(serializers.Serializer):
    char_1 = serializers.CharField()
    int_1 = serializers.IntegerField()

    class Meta:
        fields = '__all__'