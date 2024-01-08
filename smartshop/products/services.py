def get_product_photo(instance, file):
    return f'product/photo/{instance.id}/{file}'


def get_attachment_photo(instance, file):
    return f'product/photo/{instance.id}/attachments/{file}'


def get_product_video(instance, file):
    return f'product/video/{instance.id}/{file}'
