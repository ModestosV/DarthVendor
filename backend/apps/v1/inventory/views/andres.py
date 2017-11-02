from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.v1.inventory.models.Desktop import Desktop
from backend.apps.v1.inventory.models.Laptop import Laptop
from backend.apps.v1.inventory.models.MonitorDisplay import MonitorDisplay
from backend.apps.v1.inventory.models.Store import Store
from backend.apps.v1.inventory.models.Tablet import Tablet


from backend.apps.v1.inventory.mappers.ItemSpecMapper import ItemSpecMapper

store = Store()


class AndresView(APIView):

    def get(self, request):
        itemspec = Desktop("AndMOdel5", "Andres",3,3,"cd",3,"","And"
                          ,"",3,"","",8,9,"",2,3,4)
        ItemSpecMapper.insert(itemspec)
        
        return Response()
 
    