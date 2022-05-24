from shapely import wkb
from geoalchemy2.elements import WKBElement


def transform_wkb_element_to_xy(wkb_element: WKBElement):
    wkb_data = wkb.loads(bytes(wkb_element.data))

    return wkb_data.x, wkb_data.y
