from faceverifier.models import ApplicationUser, ClockIn

class ClockInService:
    def save_clockin(self, profile_picture, status, insert_method, user_id):
        
        if user_id is None:
            ClockIn.objects.create(
                status=status,
                insert_method=insert_method,
                foto_sended=profile_picture
            )
            return
        
        user = ApplicationUser.objects.filter(id=user_id).first()
        
        if not user:
            raise ValueError("Usuário com ID fornecido não encontrado")
        
        ClockIn.objects.create(
            user_name=user.name,
            user_email=user.email,
            user_id=user.id,
            status=status,
            insert_method=insert_method,
            foto_sended=profile_picture
        )
