from django.contrib import admin
from .models import EngineRegistry, InboundConnection

@admin.register(EngineRegistry)
class EngineRegistryAdmin(admin.ModelAdmin):
    list_display = ('system_name', 'performance_score', 'display_as_flagship', 'registered_on')
    list_filter = ('display_as_flagship', 'core_tech_stack')
    search_fields = ('system_name', 'core_tech_stack')

@admin.register(InboundConnection)
class InboundConnectionAdmin(admin.ModelAdmin):
    list_display = ('sender_identity', 'sender_email', 'logged_at')
    readonly_fields = ('sender_identity', 'sender_email', 'transmitted_payload', 'logged_at')