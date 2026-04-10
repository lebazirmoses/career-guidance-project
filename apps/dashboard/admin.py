# apps/dashboard/admin.py
from django.contrib import admin
from .models import CareerNode, Career

# =========================================================
# 🔹 INLINE CHILDREN DISPLAY
# =========================================================
class CareerNodeInline(admin.TabularInline):
    model = CareerNode
    fk_name = 'parent'          # child nodes link to parent
    extra = 0                   # don't show extra empty rows
    readonly_fields = ('is_generated',)  # show generated flag
    fields = ('name', 'stage', 'is_generated', 'description')


# =========================================================
# 🔹 CAREER NODE ADMIN
# =========================================================
@admin.register(CareerNode)
class CareerNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage', 'parent', 'is_generated')
    list_filter = ('stage', 'is_generated')
    search_fields = ('name',)
    inlines = [CareerNodeInline]
    ordering = ('stage', 'name')


# =========================================================
# 🔹 CAREER ADMIN
# =========================================================
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_logic', 'required_creativity', 'required_social', 'required_verbal')
    search_fields = ('name',)