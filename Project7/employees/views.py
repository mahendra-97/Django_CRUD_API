from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.views import View
from .models import Employee


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeAPI(View):
    def get(self, request, employee_id=None):
        try:
            if employee_id:
                employee = Employee.objects.get(id=employee_id)
                data = {
                    'id': employee.id,
                    'name': employee.name,
                    'phone': employee.phone,
                    'email': employee.email,
                    'department': employee.department,
                }
            else:
                employees = Employee.objects.all()
                data = [{'id': emp.id, 'name': emp.name, 'phone': emp.phone} for emp in employees]

            return JsonResponse({'data': data})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request):
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            department = request.POST.get('department')
            validate_email(['email'])

            employee = Employee.objects.create(name=name, phone=phone, email=email, department=department)

            return JsonResponse({'id': employee.id, 'success': 'Employee created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, employee_id):
        try:
            ename = request.POST.get('name')
            ephone = request.POST.get('phone')
            eemail = request.POST.get('email')
            edepartment = request.POST.get('department')

            is_employee_exist = Employee.objects.filter(id=employee_id).count()

            if is_employee_exist > 0:
                Employee.objects.filter(id=employee_id).update(name = ename, phone = ephone, email = eemail, department = edepartment)
                return JsonResponse({'success': 'Employee updated successfully'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def patch(self, request, employee_id):
        try:
            pass
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()

            return JsonResponse({'success': 'Employee deleted successfully'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


