

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            superuser = User.objects.create_superuser(
                username=env('SUPER_USER_NAME', default="abcd"),
                email=env('SUPER_USER_EMAIL', default="abc@gmail.com"),
                password=env('SUPER_USER_PASSWORD', default="abc"))
            superuser.save()
        except IntegrityError:
            print(f"Super User with username {env('SUPER_USER_NAME')} is already exit!")
        except Exception as e:
            print(e)
        else:
            print('Admin accounts can only be initialized if no Accounts exist')