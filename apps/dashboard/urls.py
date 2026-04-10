from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [

    # =========================
    # 🏠 MAIN DASHBOARD
    # =========================
    path('', views.dashboard_home, name='home'),

    # AI Dashboard
    path('ai/', views.ai_dashboard, name='ai_dashboard'),

    # Profiling Hub
    path('hub/', views.profiling_hub, name='profiling_hub'),

    # =========================
    # 🌳 CAREER TREE
    # =========================
    path('career-tree/', views.career_tree_view, name='career_tree'),

    # =========================
    # 🌟 CAREER ROADMAP
    # =========================
    path('career-roadmap/', views.career_roadmap_page, name='career_roadmap'),
    path('api/career-roadmap/', views.career_roadmap_api, name='career_roadmap_api'),
    path('career-roadmap/api/', views.get_roadmap_api, name='get_roadmap_api'),

    # =========================
    # 🤖 AI CHATBOT (IMPORTANT)
    # =========================
    path('career-chat/', views.career_chat, name='career_chat'),
    path('chat/', views.chatbot_page, name='chatbot_page'),  # ✅ NEW PAGE

    # =========================
    # ⚡ APIs
    # =========================
    path('career/api/details/', views.career_details_api, name='career_details'),
    path('career/api/children/', views.get_children_api, name='career_children'),

    # =========================
    # 📄 EXPORT
    # =========================
    path('export/', views.export_career_report, name='export_pdf'),

    # =========================
    # 📝 ASSESSMENTS (FIXED)
    # =========================
    path('assessments/', views.assessments_view, name='assessments'),
]