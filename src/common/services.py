
def get_all_objects(model):
    return model.objects.all()


def get_object_data(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except Exception as error:
        return None


def create_object(model, **kwargs):
    return model.objects.create(**kwargs)

