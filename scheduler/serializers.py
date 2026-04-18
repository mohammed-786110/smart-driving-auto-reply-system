from rest_framework.serializers import ModelSerializer
from .models import Contact

# is serilizer ko property ke ssath saath city kaa deta bhi milega to isko double mehnat krni he
# apna calc krna hi he id mang rkhi he iski but city ka bhi kaam krna he

class ContactSerializer(ModelSerializer):
    

    class Meta:
        model = Contact
        fields = '__all__'