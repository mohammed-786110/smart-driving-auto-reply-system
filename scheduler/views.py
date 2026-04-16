# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact

@api_view(['POST'])
def add_contact(request):
    user = request.user
    
    name = request.data.get('name')
    phone = request.data.get('phone')
    relation = request.data.get('relation')

    # 🔹 Validation
    if not name or not phone:
        return Response({"error": "Name and phone required"}, status=400)

    # 🔹 Save
    contact = Contact.objects.create(
        user=user,
        name=name,
        phone=phone,
        relation=relation
    )

    return Response({
        "message": "Contact added successfully",
        "contact_id": contact.id
    }, status=201)
    
from .models import UserState



# DRIVING MODE API:

@api_view(['POST'])
def toggle_driving(request):
    user = request.user

    # Get or create state
    state, created = UserState.objects.get_or_create(user=user)

    # Toggle
    state.is_driving = not state.is_driving
    state.save()

    return Response({
        "is_driving": state.is_driving,
        "message": "Driving mode updated"
    })
