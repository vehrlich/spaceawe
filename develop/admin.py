from django.contrib import admin

from develop.models import Mooc, Module, DidacticCourse, DidacticCourseDisclaimer


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class DidacticCourseInline(admin.TabularInline):
    model = DidacticCourse
    extra = 0


class DidacticCourseDisclaimerInline(admin.TabularInline):
    model = DidacticCourseDisclaimer
    extra = 0


class MoocAdmin(admin.ModelAdmin):

    inlines = [
        ModuleInline,
    ]


class ModuleAdmin(admin.ModelAdmin):
    pass


class DidacticCourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class DidacticCourseDisclaimerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mooc, MoocAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(DidacticCourse, DidacticCourseAdmin)
admin.site.register(DidacticCourseDisclaimer, DidacticCourseDisclaimerAdmin)

