from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EngineRegistry, InboundConnection

def render_portfolio_dashboard(request):
    """
    Renders the production-grade cyberpunk portfolio dashboard with
    live metrics logging and flash notification triggers.
    """
    if request.method == "POST":
        client_identity = request.POST.get('client_identity')
        client_mail = request.POST.get('client_mail')
        secure_message = request.POST.get('secure_message')
        
        if client_identity and client_mail and secure_message:
            InboundConnection.objects.create(
                sender_identity=client_identity,
                sender_email=client_mail,
                transmitted_payload=secure_message
            )
            # Professional feedback trigger
            messages.success(request, "Transmission Successful. Secure route established.")
            return redirect('portfolio_root')
        else:
            messages.error(request, "Payload corrupt. Verification failed.")

    # Core data fetching
    registered_subsystems = EngineRegistry.objects.all().order_by('-registered_on')
    
    # Advanced portfolio matrix metrics mapping
    system_capabilities = [
        {"name": "Python/Django Stack", "level": 94},
        {"name": "REST API Architecture", "level": 88},
        {"name": "NLP / LLM Integration", "level": 85},
        {"name": "Database Optimisation", "level": 80}
    ]
    
    context = {
        'subsystems': registered_subsystems,
        'capabilities': system_capabilities
    }
    return render(request, 'index.html', context)