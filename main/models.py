from django.db import models

class EngineRegistry(models.Model):
    """
    Stores metadata for development projects and AI subsystems.
    Helps render the dynamic Cyberpunk Bento Grid components.
    """
    system_name = models.CharField(max_length=120, verbose_name="Project Title")
    brief_description = models.TextField(verbose_name="System Overview")
    core_tech_stack = models.CharField(max_length=250, verbose_name="Technologies Used")
    performance_score = models.IntegerField(default=85, verbose_name="AI Optimization Score")
    repository_source = models.URLField(blank=True, null=True, verbose_name="GitHub Link")
    deployment_live = models.URLField(blank=True, null=True, verbose_name="Live Production URL")
    display_as_flagship = models.BooleanField(default=False, verbose_name="Feature on Main Hero Grid")
    registered_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Engine Registries"

    def __str__(self):
        return f"{self.system_name} | Target Core: {self.performance_score}%"

class InboundConnection(models.Model):
    """
    Captures secure contact logs from the portfolio dashboard.
    """
    sender_identity = models.CharField(max_length=100, verbose_name="Client Name")
    sender_email = models.EmailField(verbose_name="Contact Email")
    transmitted_payload = models.TextField(verbose_name="Message Body")
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Secure Ping from {self.sender_identity} - {self.logged_at.strftime('%Y-%m-%d')}"