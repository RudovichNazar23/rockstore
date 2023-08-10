
def get_all_objects(model):
    return model.objects.all()


def get_object_data(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except Exception as error:
        return None


def get_queryset(model, **kwargs):
    return model.objects.filter(**kwargs)


def check_is_anonymous_user(user):
    return user.is_anonymous


def check_object_is_none(obj):
    return obj is None


def create_object(model, **kwargs):
    return model.objects.create(**kwargs)

