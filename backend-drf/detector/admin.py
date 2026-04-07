

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from .models import EmailScan


# 🔹 Inline: show user scans inside User page
class EmailScanInline(admin.TabularInline):
    model = EmailScan
    extra = 0
    readonly_fields = ['email_text', 'prediction', 'confidence', 'created_at']
    can_delete = False


# 🔹 Custom User Admin (MAIN PART)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [EmailScanInline]

    def total_scans(self, obj):
        return obj.emailscan_set.count()

    def phishing_count(self, obj):
        return obj.emailscan_set.filter(prediction="Phishing").count()

    def safe_count(self, obj):
        return obj.emailscan_set.filter(prediction="Safe").count()

    list_display = ['username', 'email', 'total_scans', 'phishing_count', 'safe_count']


# 🔹 Register EmailScan separately (optional but useful)
@admin.register(EmailScan)
class EmailScanAdmin(admin.ModelAdmin):
    list_display = ['user', 'prediction', 'confidence', 'created_at']
    list_filter = ['prediction', 'created_at']
    search_fields = ['user__username', 'email_text']


# 🔹 Replace default User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)