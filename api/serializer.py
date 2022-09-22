from importlib.metadata import requires
from rest_framework import serializers


# 爆風電卓リクエストのシリアライザー
class BlastRequestSerializer(serializers.Serializer):
    exp_weight = serializers.FloatField(required=True)
    exp_er = serializers.FloatField(required=True)
    add_tnt = serializers.FloatField(required=True)
    meas_points = serializers.CharField(required=True)

    def validate_meas_points(self, value):
        for str in value.split(','):
            try:
                float(str)
            except ValueError:
                raise serializers.ValidationError('数字をカンマ区切りで入力してください。')
        return value
