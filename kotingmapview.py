from kivy_garden.mapview import MapView
from kivy.clock import Clock

class KotingMapView(MapView):

    getting_markets_timer = None

    def start_getting_markets_in_fov(self):
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)
    
    def get_markets_in_fov(self, *args):
        print(self.get_bbox())
        print("AAAAAAAAAHHHHHH atests afdklakldflka ")
        #aaahh