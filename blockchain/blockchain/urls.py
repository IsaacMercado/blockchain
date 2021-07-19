from django.urls import path

from . import views


urlpatterns = [
    path('get_chain/', views.GetChainAPIView.as_view(), name="get_chain"),
    path('mine_block/', views.MineBlockAPIView.as_view(), name="mine_block"),
    path('add_transaction/', views.AddTransactionAPIView.as_view(), name="add_transaction"),
    path('is_valid/', views.IsValidAPIView.as_view(), name="is_valid"),
    path('connect_node/', views.ConnectNodeAPIView.as_view(), name="connect_node"),
    path('replace_chain/', views.ReplaceChainAPIView.as_view(), name="replace_chain"),
]
