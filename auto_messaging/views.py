
from scheduler.models import Contact, UserState
from .services import generate_reply





def handle_incoming_message(user, sender):

    state, _ = UserState.objects.get_or_create(user=user)

    # If not driving >> no reply
    if not state.is_driving:
        return {
            "reply_sent": False,
            "reason": "User not driving"
        }

    #  Find contact
    contact = Contact.objects.filter(
        user=user,
        name=sender,
        auto_reply_enabled=True
    ).first()

    if contact:
        reply = generate_reply(contact.relation,sender)

        return {
            "reply_sent": True,
            "to": sender,
            "relation": contact.relation,
            "message": reply
        }

    #  Unknown number
    return {
        "reply_sent": False,
        "message": "Will respond later."
    }


# ONLY MESSAGE TO CUSTOMIZED IMPORTANT CONTACTS WILL BE REPLIED AUTOMATICALLY.
# THIS CAN BE CUSTOMIZED IN SETTINGS. CONTACTS CAN BE ADDED IN CONTACTS SECTION IN SETTINGS.
# RELATION CAN BE SET TO FAMILY, FRIEND, BOSS, EMERGENCY OR OTHERS. REPLY WILL BE GENERATED ACCORDING TO RELATION.
# This is not proper that an unknow person is sending message and auto reply is being sent. SO ONLY REPLY TO CUSTOMIZED CONTACTS WILL BE SENT AUTOMATICALLY.
