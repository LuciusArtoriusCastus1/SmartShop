from django import forms

from products.models import Products, Attachments, Rating, Reviews


class AddLaptop(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
                'name',
                'made_in',
                'photo',
                'video',
                'price',
                'screen_diagonal',
                'weight',
                'manufacture_year',
                'color',
                'amount',
                'description',
                'laptop_brand',
                'laptop_processor',
                'laptop_ram',
                'laptop_descrete_grafics_card',
                'laptop_operating_system',
                'laptop_sssd_capacity',
                'laptop_video_card_memory_capacity',
                'laptop_screentype',
                'laptop_processor_cores',
                'laptop_videocard_type',
                'laptop_drive_type',
                'laptop_ram_type',
                'laptop_resolution',
                'laptop_battery_capacity',
                'laptop_screen_refresh_rate',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'made_in': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'video': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'manufacture_year': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'color': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_brand': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_processor': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_ram': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_descrete_grafics_card': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_operating_system': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_sssd_capacity': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_video_card_memory_capacity': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_screentype': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_processor_cores': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_videocard_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_drive_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_ram_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_resolution': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_battery_capacity': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_screen_refresh_rate': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class AddTablet(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
                'name',
                'made_in',
                'photo',
                'video',
                'price',
                'screen_diagonal',
                'weight',
                'manufacture_year',
                'color',
                'amount',
                'description',
                'number_of_sim_cards',
                'tablet_brand',
                'tablet_ram',
                'tablet_built_in_memory',
                'tablet_wireless_capabilities',
                'tablet_operating_system',
                'tablet_matrix_type',
                'tablet_features',
                'tablet_screen_resolution',
                'tablet_processor_cores',
                'tablet_processor',
                'tablet_main_camera',
                'tablet_front_camera',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'made_in': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'video': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'manufacture_year': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'color': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'number_of_sim_cards': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_brand': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_ram': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_built_in_memory': forms.Select({'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_wireless_capabilities': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_operating_system': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_matrix_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_features': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_screen_resolution': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_processor_cores': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_processor': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_main_camera': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_front_camera': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class AddPhone(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
                'name',
                'made_in',
                'photo',
                'video',
                'price',
                'screen_diagonal',
                'weight',
                'manufacture_year',
                'color',
                'amount',
                'description',
                'number_of_sim_cards',
                'phone_brand',
                'phone_ram',
                'phone_built_in_memory',
                'phone_memory_capacity',
                'phone_tireless_technologies',
                'phone_main_camera_mp',
                'phone_main_camera_features',
                'phone_front_camera_mp',
                'phone_processor_name',
                'phone_display_resolution',
                'phone_matrix_type',
                'phone_screen_refresh_rate',
                'phone_operating_system',
                'phone_equipment',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'made_in': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'video': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'manufacture_year': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'color': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'number_of_sim_cards': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_brand': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_ram': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_built_in_memory': forms.Select({'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_memory_capacity': forms.Select({'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_tireless_technologies': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_main_camera_mp': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_main_camera_features': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_front_camera_mp': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_processor_name': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_display_resolution': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_matrix_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_screen_refresh_rate': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_operating_system': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_equipment': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class UpdateTablet(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
                'name',
                'made_in',
                'photo',
                'video',
                'price',
                'discount',
                'screen_diagonal',
                'weight',
                'manufacture_year',
                'color',
                'amount',
                'description',
                'number_of_sim_cards',
                'tablet_brand',
                'tablet_ram',
                'tablet_built_in_memory',
                'tablet_wireless_capabilities',
                'tablet_operating_system',
                'tablet_matrix_type',
                'tablet_features',
                'tablet_screen_resolution',
                'tablet_processor_cores',
                'tablet_processor',
                'tablet_main_camera',
                'tablet_front_camera',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'made_in': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'video': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'discount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'manufacture_year': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'color': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'number_of_sim_cards': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_brand': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_ram': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_built_in_memory': forms.Select({'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_wireless_capabilities': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_operating_system': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_matrix_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_features': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_screen_resolution': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_processor_cores': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_processor': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_main_camera': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'tablet_front_camera': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class UpdateLaptop(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            'name',
            'made_in',
            'photo',
            'video',
            'price',
            'screen_diagonal',
            'weight',
            'manufacture_year',
            'color',
            'amount',
            'description',
            'laptop_brand',
            'laptop_processor',
            'laptop_ram',
            'laptop_descrete_grafics_card',
            'laptop_operating_system',
            'laptop_sssd_capacity',
            'laptop_video_card_memory_capacity',
            'laptop_screentype',
            'laptop_processor_cores',
            'laptop_videocard_type',
            'laptop_drive_type',
            'laptop_ram_type',
            'laptop_resolution',
            'laptop_battery_capacity',
            'laptop_screen_refresh_rate',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'made_in': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'video': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'discount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'manufacture_year': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'color': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_brand': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_processor': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_ram': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_descrete_grafics_card': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_operating_system': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_sssd_capacity': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_video_card_memory_capacity': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_screentype': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_processor_cores': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_videocard_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_drive_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_ram_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_resolution': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_battery_capacity': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'laptop_screen_refresh_rate': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class UpdatePhone(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
                'name',
                'made_in',
                'photo',
                'video',
                'price',
                'discount',
                'screen_diagonal',
                'weight',
                'manufacture_year',
                'color',
                'amount',
                'description',
                'number_of_sim_cards',
                'phone_brand',
                'phone_ram',
                'phone_built_in_memory',
                'phone_memory_capacity',
                'phone_tireless_technologies',
                'phone_main_camera_mp',
                'phone_main_camera_features',
                'phone_front_camera_mp',
                'phone_processor_name',
                'phone_display_resolution',
                'phone_matrix_type',
                'phone_screen_refresh_rate',
                'phone_operating_system',
                'phone_equipment',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'made_in': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'video': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'discount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'screen_diagonal': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'manufacture_year': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'color': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'number_of_sim_cards': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_brand': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_ram': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_built_in_memory': forms.Select({'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_memory_capacity': forms.Select({'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_tireless_technologies': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_main_camera_mp': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_main_camera_features': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_front_camera_mp': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_processor_name': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_display_resolution': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_matrix_type': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_screen_refresh_rate': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_operating_system': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_equipment': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class AddAttachmentsForm(forms.Form):
    photo = MultipleFileField()

    class Meta:
        model = Attachments
        fields = ('photo',)


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rate',)

        widgets = {
            'rate': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('text',)

        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }
